#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Prepare a randomized Factory Catalog evaluation manifest without invoking a model."""

from __future__ import annotations
import argparse
import hashlib
import json
import random
from pathlib import Path


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def stable_run_id(
    task_id: str, condition_id: str, model_id: str, repetition: int, seed: int
) -> str:
    raw = f"{task_id}\0{condition_id}\0{model_id}\0{repetition}\0{seed}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--tasks", type=Path, default=Path("evals/tasks.json"))
    p.add_argument("--conditions", type=Path, default=Path("evals/conditions.json"))
    p.add_argument("--model", action="append", dest="models", required=True)
    p.add_argument("--repetitions", type=int, default=3)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--include-optional", action="store_true")
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    if a.repetitions < 1:
        p.error("--repetitions must be >= 1")
    if len(set(a.models)) != len(a.models):
        p.error("duplicate model id")
    tasks, conditions = load_json(a.tasks), load_json(a.conditions)
    if not tasks or not conditions:
        p.error("tasks and conditions must be nonempty")
    if not a.include_optional:
        conditions = [c for c in conditions if not c.get("optional", False)]
    if len({t["id"] for t in tasks}) != len(tasks):
        raise SystemExit("duplicate task id")
    if len({c["id"] for c in conditions}) != len(conditions):
        raise SystemExit("duplicate condition id")
    runs = []
    for model in a.models:
        for task in tasks:
            for rep in range(1, a.repetitions + 1):
                for condition in conditions:
                    if condition["id"] == "expert-task-prompt" and not task.get(
                        "expert_prompt"
                    ):
                        continue
                    runs.append(
                        {
                            "run_id": stable_run_id(
                                task["id"], condition["id"], model, rep, a.seed
                            ),
                            "task_id": task["id"],
                            "stratum": task.get("stratum"),
                            "category": task.get("category"),
                            "condition_id": condition["id"],
                            "model_id": model,
                            "repetition": rep,
                            "seed": a.seed,
                        }
                    )
    random.Random(a.seed).shuffle(runs)
    for i, r in enumerate(runs, 1):
        r["order"] = i
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open("w", encoding="utf-8") as f:
        for r in runs:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    print(f"wrote {len(runs)} runs to {a.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
