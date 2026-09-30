#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Analyze Factory Catalog evaluation results with the Python standard library."""

from __future__ import annotations
import argparse
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path

SCORE_FIELDS = (
    "artifact_correctness",
    "process_correctness",
    "recovery",
    "calibration",
    "efficiency",
)
TELEMETRY_FIELDS = (
    "input_tokens",
    "output_tokens",
    "tool_calls",
    "elapsed_seconds",
    "human_review_minutes",
    "human_rework_minutes",
    "cost_usd",
)


def validate(r, path, line):
    def fail(message):
        raise SystemExit(f"{path}:{line}: {message}")

    if not isinstance(r, dict):
        fail("record must be an object")
    req = (
        "run_id",
        "task_id",
        "condition_id",
        "model_id",
        "repetition",
        "scores",
        "mandatory_invariants",
        "silent_error",
        "failure_modes",
    )
    missing = [key for key in req if key not in r]
    if missing:
        fail(f"missing fields: {', '.join(missing)}")
    for key in ("run_id", "task_id", "condition_id", "model_id"):
        if not isinstance(r[key], str) or not r[key]:
            fail(f"{key} must be a nonempty string")
    if type(r["repetition"]) is not int or r["repetition"] < 1:
        fail("repetition must be a positive integer")
    if not isinstance(r["scores"], dict) or set(r["scores"]) != set(SCORE_FIELDS):
        fail("scores must contain exactly the five rubric dimensions")
    for field in SCORE_FIELDS:
        value = r["scores"][field]
        if type(value) is not int or not 0 <= value <= 4:
            fail(f"scores.{field} must be integer 0..4")
    inv = r["mandatory_invariants"]
    if not isinstance(inv, dict) or any(
        value is not None and type(value) is not bool for value in inv.values()
    ):
        fail("invalid mandatory_invariants")
    if type(r["silent_error"]) is not bool:
        fail("silent_error must be boolean")
    modes = r["failure_modes"]
    if not isinstance(modes, list) or any(not isinstance(x, str) for x in modes):
        fail("failure_modes must be an array of strings")
    if len(modes) != len(set(modes)):
        fail("failure_modes must be unique")
    for field in (
        "catalog_commit",
        "fixture_revision",
        "environment_id",
        "evaluator_id",
        "notes",
    ):
        if r.get(field) is not None and not isinstance(r[field], str):
            fail(f"{field} must be a string or null")
    if (
        r.get("evaluator_blinded") is not None
        and type(r["evaluator_blinded"]) is not bool
    ):
        fail("evaluator_blinded must be boolean or null")
    telemetry = r.get("telemetry", {})
    if not isinstance(telemetry, dict) or set(telemetry) - set(TELEMETRY_FIELDS):
        fail("invalid telemetry fields")
    for field, value in telemetry.items():
        if value is None:
            continue
        types = (int,) if field in TELEMETRY_FIELDS[:3] else (int, float)
        if type(value) not in types or not math.isfinite(value) or value < 0:
            fail(
                f"telemetry.{field} must be a finite nonnegative number of the required type"
            )


def load(path):
    rows = []
    seen_ids, seen_cells = set(), set()
    with path.open(encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: invalid JSON: {e}") from e
            validate(r, path, n)
            cell = (r["task_id"], r["model_id"], r["repetition"], r["condition_id"])
            if r["run_id"] in seen_ids or cell in seen_cells:
                raise SystemExit(f"{path}:{n}: duplicate run_id or experimental cell")
            seen_ids.add(r["run_id"])
            seen_cells.add(cell)
            rows.append(r)
    return rows


def passed(r):
    inv = r["mandatory_invariants"]
    return (
        bool(inv)
        and all(v is True for v in inv.values())
        and r["scores"]["artifact_correctness"] >= 3
        and r["scores"]["process_correctness"] >= 3
        and r["scores"]["calibration"] >= 3
    )


def mean(xs):
    xs = list(xs)
    return statistics.fmean(xs) if xs else None


def fmt(x):
    return "unknown" if x is None else f"{x:.3f}"


def ci(xs, seed, samples=4000):
    if not xs:
        return None
    if len(xs) == 1:
        return (xs[0], xs[0])
    rng = random.Random(seed)
    n = len(xs)
    vals = sorted(
        statistics.fmean(xs[rng.randrange(n)] for _ in range(n)) for _ in range(samples)
    )
    return vals[int(0.025 * (samples - 1))], vals[int(0.975 * (samples - 1))]


def summary(rows):
    tele = {}
    for f in TELEMETRY_FIELDS:
        vals = [r.get("telemetry", {}).get(f) for r in rows]
        tele[f] = mean(
            v for v in vals if isinstance(v, (int, float)) and not isinstance(v, bool)
        )
    return {
        "n": len(rows),
        "pass_rate": mean(1.0 if passed(r) else 0.0 for r in rows),
        "silent_error_rate": mean(1.0 if r["silent_error"] else 0.0 for r in rows),
        "scores": {f: mean(r["scores"][f] for r in rows) for f in SCORE_FIELDS},
        "telemetry": tele,
    }


def deltas(rows, treatment, baseline="bare"):
    groups = defaultdict(dict)
    for r in rows:
        groups[(r["task_id"], r["model_id"], r["repetition"])][r["condition_id"]] = r
    pd, sd = [], []
    matched = 0
    for g in groups.values():
        if baseline not in g or treatment not in g:
            continue
        b, t = g[baseline], g[treatment]
        for field in ("fixture_revision", "environment_id", "catalog_commit"):
            if b.get(field) != t.get(field):
                raise SystemExit(
                    f"incompatible matched pair {b['run_id']}/{t['run_id']}: {field}"
                )
        if set(b["mandatory_invariants"]) != set(t["mandatory_invariants"]):
            raise SystemExit(
                "incompatible matched pair: mandatory invariant names differ"
            )
        matched += 1
        pd.append((1.0 if passed(t) else 0.0) - (1.0 if passed(b) else 0.0))
        sd.append(
            (1.0 if t["silent_error"] else 0.0) - (1.0 if b["silent_error"] else 0.0)
        )
    seed = sum(map(ord, treatment))
    return matched, mean(pd), ci(pd, seed), mean(sd), ci(sd, seed + 1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("results", type=Path)
    a = p.parse_args()
    rows = load(a.results)
    if not rows:
        raise SystemExit("no result records")
    by = defaultdict(list)
    for r in rows:
        by[r["condition_id"]].append(r)
    print("# Condition summary")
    print(
        "condition\tn\tpass_rate\tsilent_error\tartifact\tprocess\trecovery\tcalibration\tefficiency"
    )
    for c in sorted(by):
        s = summary(by[c])
        print(
            "\t".join(
                [
                    c,
                    str(s["n"]),
                    fmt(s["pass_rate"]),
                    fmt(s["silent_error_rate"]),
                    *(fmt(s["scores"][f]) for f in SCORE_FIELDS),
                ]
            )
        )
    if "bare" in by:
        print("\n# Matched deltas versus bare")
        for c in sorted(x for x in by if x != "bare"):
            n, pd, pci, sd, sci = deltas(rows, c)
            pct = "unknown" if pci is None else f"[{pci[0]:.3f}, {pci[1]:.3f}]"
            sct = "unknown" if sci is None else f"[{sci[0]:.3f}, {sci[1]:.3f}]"
            print(
                f"{c}: matched={n} pass_delta={fmt(pd)} ci95={pct} silent_error_delta={fmt(sd)} ci95={sct}"
            )
    print("\n# By model")
    bm = defaultdict(lambda: defaultdict(list))
    for r in rows:
        bm[r["model_id"]][r["condition_id"]].append(r)
    for m in sorted(bm):
        print(
            m
            + ": "
            + " | ".join(
                f"{c}:n={summary(bm[m][c])['n']},pass={fmt(summary(bm[m][c])['pass_rate'])},silent={fmt(summary(bm[m][c])['silent_error_rate'])}"
                for c in sorted(bm[m])
            )
        )
    print("\n# Available telemetry (mean; observed/total)")
    for c in sorted(by):
        values = summary(by[c])["telemetry"]
        for field in TELEMETRY_FIELDS:
            observed = sum(r.get("telemetry", {}).get(field) is not None for r in by[c])
            print(f"{c} {field}: {fmt(values[field])}; {observed}/{len(by[c])}")
    print("\n# Failure modes")
    counts = defaultdict(Counter)
    for r in rows:
        counts[r["condition_id"]].update(r.get("failure_modes", []))
    for c in sorted(counts):
        print(
            c
            + ": "
            + (", ".join(f"{k}={v}" for k, v in counts[c].most_common()) or "none")
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
