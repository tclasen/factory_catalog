#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Objective benchmark endpoint, inference, and durable execution regressions."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import desktop_eval as pilot
import desktop_eval_objective as obj
from test_desktop_eval import good_artifacts, trace


class ObjectiveTests(unittest.TestCase):
    def test_all_fixture_success_failure_missing(self):
        for spec in obj.fixtures(pilot.fixture_specs()):
            with self.subTest(task=spec["id"]):
                artifacts = good_artifacts(spec)
                artifacts["completion.json"] = json.dumps(
                    obj.expected_declaration(spec["id"])
                )
                artifacts["adoption/record.md"] = "Permitted record"
                artifacts["scratch/check.txt"] = "Working note"
                python = {
                    "normalization_correct": True,
                    "nonstrings_rejected": True,
                    "discount_correct": True,
                }
                checks = obj.checks(spec, artifacts, trace(), python)
                self.assertTrue(all(v is True for v in checks.values()), checks)
                evidence = {
                    "deterministic": checks,
                    "complete": True,
                    "contamination": [],
                    "artifacts": artifacts,
                }
                self.assertTrue(obj.outcome(spec, evidence)["pass"])
                artifacts["unauthorized.txt"] = "effect"
                checks = obj.checks(spec, artifacts, trace(), python)
                self.assertFalse(checks["output_scope_respected"])
                self.assertFalse(
                    obj.outcome(spec, {**evidence, "deterministic": checks})["pass"]
                )
                self.assertTrue(
                    obj.outcome(spec, {**evidence, "deterministic": checks})[
                        "structured_false_completion"
                    ]
                )
                missing = obj.checks(spec, {}, [], {})
                self.assertFalse(
                    obj.outcome(
                        spec, {**evidence, "deterministic": missing, "artifacts": {}}
                    )["pass"]
                )
                self.assertIsNone(
                    obj.outcome(spec, {**evidence, "complete": False})["pass"]
                )
                self.assertIsNone(
                    obj.outcome(spec, {**evidence, "contamination": ["E1"]})["pass"]
                )

    def test_protected_files_and_declarations(self):
        spec = obj.fixtures(pilot.fixture_specs())[2]
        artifacts = good_artifacts(spec)
        artifacts["completion.json"] = json.dumps(obj.expected_declaration(spec["id"]))
        artifacts["verify.py"] = "print('PASS')"
        self.assertFalse(
            obj.checks(spec, artifacts, trace(), {})["protected_inputs_preserved"]
        )
        for value in (
            "null",
            "[]",
            "{",
            '{"artifact_complete":1}',
            json.dumps(
                {**obj.expected_declaration(spec["id"]), "required_check": "passed"}
            ),
        ):
            artifacts["completion.json"] = value
            self.assertFalse(
                obj.checks(spec, artifacts, trace(), {})[
                    "completion_declaration_correct"
                ]
            )

    def test_exact_bounds(self):
        self.assertAlmostEqual(
            obj.proportion_bounds(0, 64)[1], 1 - obj.TAIL_ALPHA ** (1 / 64)
        )
        self.assertAlmostEqual(
            obj.proportion_bounds(64, 64)[0], obj.TAIL_ALPHA ** (1 / 64)
        )
        # Published standard 95% exact binomial example, verified with SciPy oracle.
        lo, hi = obj.proportion_bounds(5, 10, 0.025)
        self.assertAlmostEqual(lo, 0.18708602844739852)
        self.assertAlmostEqual(hi, 0.8129139715526015)
        for k in range(65):
            a, b = obj.proportion_bounds(k, 64)
            c, d = obj.proportion_bounds(64 - k, 64)
            self.assertAlmostEqual(a, 1 - d)
            self.assertAlmostEqual(b, 1 - c)
        for k, n in ((-1, 4), (5, 4), (0, 0), (True, 3)):
            with self.assertRaises(ValueError):
                obj.proportion_bounds(k, n)

    def test_decisions(self):
        self.assertEqual(obj.comparison([(True, True)] * 64)["decision"], "equivalence")
        self.assertEqual(
            obj.comparison([(True, False)] * 64)["decision"], "superiority"
        )
        self.assertEqual(
            obj.comparison([(False, True)] * 64)["decision"], "inferiority"
        )
        self.assertEqual(obj.comparison([(True, True)] * 10)["decision"], "unresolved")
        self.assertEqual(
            obj.comparison([(True, False)] * 32 + [(False, True)] * 32)["decision"],
            "unresolved",
        )
        self.assertTrue(obj.overhead([(121, 100)] * 64)["majority_overhead"])
        self.assertFalse(obj.overhead([(120, 100)] * 64)["majority_overhead"])
        self.assertEqual(obj.overhead([(None, 100)])["status"], "unknown")
        with self.assertRaises(ValueError):
            obj.comparison([(None, True)])

    def test_freeze_and_dispatch_guards(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "experiment"
            config = pilot.prepare(root, "HEAD", "synthetic", True)
            _, specs, manifest = pilot.load_experiment(root)
            self.assertEqual(len(manifest), 384)
            self.assertEqual(len({r["run_id"] for r in manifest}), 384)
            self.assertEqual(
                {r["task_id"] for r in manifest[:192]}, {s["id"] for s in specs}
            )
            self.assertEqual(config["evaluator_limit"], 0)
            pilot.write_json(
                root / "preflight.json",
                {
                    "config_hash": config["config_hash"],
                    "capabilities": {
                        k: {"available": True, "evidence": "synthetic test"}
                        for k in pilot.CAPABILITIES
                    },
                },
            )
            for index, condition in enumerate(pilot.CONDITIONS):
                row = next(r for r in manifest if r["condition_id"] == condition)
                workspace = Path(tmp) / f"workspace{index}"
                pilot.stage_workspace(root, row["run_id"], workspace)
                self.assertEqual(
                    (workspace / "catalog").exists(), condition == "catalog-full"
                )
            first = manifest[0]["run_id"]
            pilot.reserve(root, first, "task")
            with self.assertRaises(pilot.PilotError):
                pilot.reserve(root, first, "task")
            with self.assertRaises(pilot.PilotError):
                pilot.reserve(root, manifest[1]["run_id"], "task")
            with self.assertRaises(pilot.PilotError):
                pilot.reserve(root, first, "evaluator")
            manifest[0]["task_id"] = "tampered"
            pilot.write_json(root / "manifest.json", manifest)
            with self.assertRaises(pilot.PilotError):
                pilot.load_experiment(root)

    def test_idempotent_scoring_and_receipts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "experiment"
            config = pilot.prepare(root, "HEAD", "synthetic", True)
            _, specs, rows = pilot.load_experiment(root)
            run = rows[0]["run_id"]
            spec = next(s for s in specs if s["id"] == rows[0]["task_id"])
            evidence = {
                "deterministic": {k: True for k in spec["invariants"]},
                "complete": True,
                "contamination": [],
                "artifacts": {},
            }
            with patch.object(pilot, "verify_capture", return_value=(evidence, {})):
                a = pilot.score_objective(root, run)
                self.assertEqual(a, pilot.score_objective(root, run))
                self.assertEqual(
                    len(
                        [
                            e
                            for e in pilot.ledger(root, config)
                            if e["kind"] == "objective_scored"
                        ]
                    ),
                    1,
                )
                path = root / "runs" / run / "objective.json"
                value = pilot.read_json(path)
                value["pass"] = False
                pilot.write_json(path, value)
                with self.assertRaises(pilot.PilotError):
                    pilot.objective_result(root, run)

    def test_reporting_and_planned_stop_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "experiment"
            config = pilot.prepare(root, "HEAD", "synthetic", True)
            _, specs, rows = pilot.load_experiment(root)
            pilot.write_json(
                root / "preflight.json",
                {
                    "config_hash": config["config_hash"],
                    "capabilities": {
                        k: {"available": True, "evidence": "synthetic"}
                        for k in pilot.CAPABILITIES
                    },
                },
            )
            self.assertEqual(
                pilot.objective_report(root)["decision"], "await_planned_look"
            )
            with self.assertRaises(pilot.PilotError):
                pilot.objective_report(root, look=64)
            events = []

            def add(kind, run=None, role=None, **data):
                events.append(
                    pilot.append(root, config, events, kind, run, role, **data)
                )

            add("qualified")
            for row in rows[:192]:
                run = row["run_id"]
                spec = next(s for s in specs if s["id"] == row["task_id"])
                add("reserved", run, "task")
                add(
                    "started",
                    run,
                    "task",
                    started_at=pilot.now(),
                    thread_id="chat" + run,
                )
                add("completed", run, "task", cessation_observed=True)
                evidence = {
                    "deterministic": {k: True for k in spec["invariants"]},
                    "complete": True,
                    "contamination": [],
                    "artifacts": {},
                    "telemetry": {
                        "input_tokens": 10,
                        "output_tokens": 10,
                        "elapsed_seconds": 10,
                    },
                    "base_instruction_hash": "variant",
                    "fixed_environment_id": "environment",
                }
                pilot.write_json(root / "runs" / run / "evidence.json", evidence)
                pilot.write_json(root / "runs" / run / "blind.json", {})
                add(
                    "captured",
                    run,
                    evidence_digest=pilot.digest(evidence),
                    blind_digest=pilot.digest({}),
                )
                value = {
                    "config_hash": config["config_hash"],
                    "run_id": run,
                    "evidence_digest": pilot.digest(evidence),
                    **obj.outcome(spec, evidence),
                }
                pilot.write_json(root / "runs" / run / "objective.json", value)
                add("objective_scored", run, outcome_digest=pilot.digest(value))
            report = pilot.objective_report(root)
            self.assertEqual(report["decision"], "conclusive")
            self.assertEqual(report["selected_look"], 64)
            self.assertEqual(report["scored"], 192)
            self.assertEqual(report["conditions"]["catalog-full"]["passed"], 64)
            with self.assertRaisesRegex(pilot.PilotError, "planned stopping gate"):
                pilot.reserve(root, rows[192]["run_id"], "task")


if __name__ == "__main__":
    unittest.main()
