#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Objective benchmark endpoint, inference, and durable execution regressions."""

import base64
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import desktop_eval as pilot
import desktop_eval_objective as obj
from desktop_eval_evidence import EvidenceError, snapshot
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

    def test_permitted_binary_auxiliary_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload = bytes(range(256))
            (root / "scratch").mkdir()
            (root / "adoption").mkdir()
            (root / "scratch" / "compiled.pyc").write_bytes(payload)
            (root / "adoption" / "record.bin").write_bytes(payload)
            (root / "output.txt").write_text("Text remains text")
            with self.assertRaises(EvidenceError):
                snapshot(root)
            result = snapshot(root, binary_auxiliary=True)
            self.assertEqual(result["output.txt"], "Text remains text")
            for name in ("scratch/compiled.pyc", "adoption/record.bin"):
                self.assertEqual(result[name]["encoding"], "base64")
                self.assertEqual(base64.b64decode(result[name]["content"]), payload)
            (root / "output.bin").write_bytes(payload)
            with self.assertRaises(EvidenceError):
                snapshot(root, binary_auxiliary=True)

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

    def test_luna_replay_preserves_original_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp) / "original"
            pilot.prepare(original, "HEAD", "synthetic", True)
            _, _, old = pilot.load_experiment(original)
            keys = ("task_id", "condition_id", "repetition", "block", "order")
            for model in ("gpt-5.6-luna", "gpt-6-luna"):
                root = Path(tmp) / model
                config = pilot.prepare(
                    root, "HEAD", "synthetic", True, model, "xhigh", 81
                )
                _, _, rows = pilot.load_experiment(root)
                self.assertEqual(len(rows), 243)
                self.assertEqual(config["planned_looks"], [81])
                self.assertEqual(config["task_limit"], 243)
                self.assertEqual(config["reasoning_effort"], "xhigh")
                self.assertEqual(
                    [{k: r[k] for k in keys} for r in rows],
                    [{k: r[k] for k in keys} for r in old[:243]],
                )
                self.assertTrue(all(r["model_id"] == model for r in rows))
                self.assertTrue(
                    set(r["run_id"] for r in rows).isdisjoint(r["run_id"] for r in old)
                )
                with self.assertRaises(pilot.PilotError):
                    pilot.objective_report(root, look=64)
                rows[0]["model_id"] = pilot.MODEL
                pilot.write_json(root / "manifest.json", rows)
                with self.assertRaises(pilot.PilotError):
                    pilot.load_experiment(root)
            for count in (0, 129, True):
                with self.assertRaises(pilot.PilotError):
                    pilot.prepare(
                        Path(tmp) / "bad",
                        "HEAD",
                        "synthetic",
                        True,
                        replay_blocks=count,
                    )

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
        self.check_reporting(False)

    def test_fixed_replay_reporting_and_no_early_stop(self):
        self.check_reporting(True)

    def check_reporting(self, replay):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "experiment"
            config = pilot.prepare(
                root,
                "HEAD",
                "synthetic",
                True,
                "gpt-6-luna",
                "xhigh",
                81 if replay else None,
            )
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
            for row in rows[: 243 if replay else 192]:
                run = row["run_id"]
                spec = next(s for s in specs if s["id"] == row["task_id"])
                if row["order"] == 193:
                    self.assertEqual(
                        pilot.objective_report(root)["decision"], "await_planned_look"
                    )
                    pilot.reserve(root, run, "task")
                    events = pilot.ledger(root, config)
                else:
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
            self.assertEqual(report["selected_look"], 81 if replay else 64)
            self.assertEqual(report["scored"], 243 if replay else 192)
            self.assertEqual(
                report["conditions"]["catalog-full"]["passed"], 81 if replay else 64
            )
            if replay:
                with self.assertRaises(pilot.PilotError):
                    pilot.reserve(root, rows[-1]["run_id"], "task")
            else:
                with self.assertRaisesRegex(pilot.PilotError, "planned stopping gate"):
                    pilot.reserve(root, rows[192]["run_id"], "task")


if __name__ == "__main__":
    unittest.main()
