#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
from __future__ import annotations
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def mod(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    assert s and s.loader
    sys.modules[name] = m
    s.loader.exec_module(m)
    return m


def test_ids():
    tasks = json.loads((ROOT / "evals/tasks.json").read_text())
    conditions = json.loads((ROOT / "evals/conditions.json").read_text())
    assert len(tasks) == 25 and len({t["id"] for t in tasks}) == 25
    assert len({c["id"] for c in conditions}) == len(conditions)
    assert {
        "bare",
        "minimal",
        "catalog-full",
        "catalog-controls-only",
        "catalog-procedure-only",
    } <= {c["id"] for c in conditions}
    for t in tasks:
        assert (
            t["mandatory_invariants"]
            and t["failure_modes"]
            and t["stratum"] in {"simple", "medium", "long"}
        )


def test_manifest():
    script = ROOT / "scripts/prepare_eval_runs.py"
    with tempfile.TemporaryDirectory() as td:
        a, b = Path(td) / "a", Path(td) / "b"
        base = [
            str(script),
            "--tasks",
            str(ROOT / "evals/tasks.json"),
            "--conditions",
            str(ROOT / "evals/conditions.json"),
            "--model",
            "m1",
            "--repetitions",
            "3",
            "--seed",
            "7",
        ]
        subprocess.run(
            base + ["--output", str(a)], check=True, capture_output=True, text=True
        )
        subprocess.run(
            base + ["--output", str(b)], check=True, capture_output=True, text=True
        )
        assert a.read_text() == b.read_text()
        rows = [json.loads(x) for x in a.read_text().splitlines()]
        assert len(rows) == 25 * 5 * 3 and len({r["run_id"] for r in rows}) == len(rows)


def test_analysis():
    m = mod(ROOT / "scripts/analyze_evals.py", "ae")
    b = {
        "run_id": "b",
        "task_id": "T",
        "condition_id": "bare",
        "model_id": "m",
        "repetition": 1,
        "scores": {
            "artifact_correctness": 2,
            "process_correctness": 3,
            "recovery": 2,
            "calibration": 3,
            "efficiency": 3,
        },
        "mandatory_invariants": {"x": True},
        "silent_error": True,
        "failure_modes": ["premature_success"],
    }
    t = json.loads(json.dumps(b))
    t.update(
        {
            "run_id": "t",
            "condition_id": "catalog-full",
            "silent_error": False,
            "failure_modes": [],
        }
    )
    t["scores"]["artifact_correctness"] = 4
    assert not m.passed(b) and m.passed(t)
    n, pd, _, sd, _ = m.deltas([b, t], "catalog-full")
    assert n == 1 and pd == 1.0 and sd == -1.0
    t["mandatory_invariants"]["x"] = None
    assert not m.passed(t)


def example_record():
    return {
        "run_id": "b",
        "task_id": "T",
        "condition_id": "bare",
        "model_id": "m",
        "repetition": 1,
        "scores": {
            f: 3
            for f in (
                "artifact_correctness",
                "process_correctness",
                "recovery",
                "calibration",
                "efficiency",
            )
        },
        "mandatory_invariants": {"x": True},
        "silent_error": False,
        "failure_modes": [],
    }


def rejects(action):
    try:
        action()
    except SystemExit:
        return
    raise AssertionError("invalid input was accepted")


def test_record_validation():
    m = mod(ROOT / "scripts/analyze_evals.py", "validation")
    good = example_record()
    m.validate(good, "fixture", 1)
    for field, value in (
        ("scores", []),
        ("repetition", True),
        ("repetition", 0),
        ("run_id", ""),
        ("failure_modes", "oops"),
        ("failure_modes", ["x", "x"]),
        ("mandatory_invariants", {"x": 1}),
        ("silent_error", 1),
        ("telemetry", None),
        ("telemetry", {"input_tokens": 1.5}),
        ("telemetry", {"cost_usd": -1}),
        ("telemetry", {"cost_usd": float("nan")}),
        ("telemetry", {"cost_usd": float("inf")}),
    ):
        bad = dict(good, **{field: value})
        rejects(lambda: m.validate(bad, "fixture", 1))
    rejects(lambda: m.validate([], "fixture", 1))
    for invariants in ({}, {"x": None}, {"x": False}):
        assert not m.passed(dict(good, mandatory_invariants=invariants))
    assert m.summary([good])["telemetry"]["cost_usd"] is None


def test_duplicate_results_and_pair_mismatch():
    m = mod(ROOT / "scripts/analyze_evals.py", "duplicates")
    baseline = example_record()
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "results.jsonl"
        for duplicate in (baseline, dict(baseline, run_id="other")):
            path.write_text(json.dumps(baseline) + "\n" + json.dumps(duplicate) + "\n")
            rejects(lambda: m.load(path))
    treatment = dict(baseline, run_id="t", condition_id="catalog-full")
    for field in ("fixture_revision", "environment_id", "catalog_commit"):
        changed = dict(treatment, **{field: "different"})
        rejects(lambda: m.deltas([baseline, changed], "catalog-full"))
    rejects(
        lambda: m.deltas(
            [baseline, dict(treatment, mandatory_invariants={"y": True})],
            "catalog-full",
        )
    )
    assert m.deltas([baseline], "catalog-full")[0] == 0
    assert m.ci([0, 1, -1], 7) == m.ci([0, 1, -1], 7)


def test_cli_telemetry_and_duplicate_models():
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "results.jsonl"
        path.write_text(json.dumps(example_record()) + "\n")
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/analyze_evals.py"), str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        assert "bare cost_usd: unknown; 0/1" in result.stdout
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/prepare_eval_runs.py"),
                "--model",
                "m",
                "--model",
                "m",
                "--seed",
                "1",
                "--output",
                str(Path(td) / "manifest"),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0 and "duplicate model id" in result.stderr


def main():
    ts = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    for t in ts:
        t()
        print("PASS", t.__name__)
    print(f"{len(ts)} tests passed")


if __name__ == "__main__":
    main()
