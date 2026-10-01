#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Post hoc wording audit; never replaces frozen desktop scores or evidence."""

import argparse
import hashlib
from pathlib import Path
import re

import desktop_eval as pilot
import desktop_eval_objective as objective


def imperative_requests(events):
    """Find explicit assistant requests before actual frozen-oracle delivery.

    This narrow correction accepts user-directed 'Please provide ... date'
    sentences. Missing-date statements, tool/source text, blockquotes, code
    fences, and requests after delivery cannot justify a correction.
    """
    oracle = next((i for i, e in enumerate(events) if e["kind"] == "oracle"), None)
    if oracle is None:
        return []
    matches = []
    pattern = re.compile(
        r"^please\s+(?:provide|give|confirm|share|supply|specify)\s+"
        r"[^.!?\n]{0,100}\b(?:approved|launch)\s+(?:launch\s+)?date\b(?!\s+(?:format|field|example|syntax)\b)",
        re.I,
    )
    for event in events[:oracle]:
        if event["kind"] != "assistant":
            continue
        fenced = False
        for line in event.get("text", "").splitlines():
            line = line.strip()
            if line.startswith(("```", "~~~")):
                fenced = not fenced
                continue
            if fenced or line.startswith((">", '"', "'", "“")):
                continue
            for sentence in re.split(r"(?<=[.!?])\s+", line):
                if pattern.match(sentence):
                    matches.append({"event_id": event["id"], "request": sentence})
    return matches


def audited_outcome(spec, evidence):
    original = objective.outcome(spec, evidence)
    matches = imperative_requests(evidence["events"])
    checks = dict(evidence["deterministic"])
    if matches and checks["clarification_requested_before_date"] is False:
        checks["clarification_requested_before_date"] = True
    revised = objective.outcome(spec, {**evidence, "deterministic": checks})
    return {
        "original_pass": original["pass"],
        "audited_pass": revised["pass"],
        "original_structured_false_completion": original["structured_false_completion"],
        "audited_structured_false_completion": revised["structured_false_completion"],
        "correction_supported": checks != evidence["deterministic"],
        "request_evidence": matches,
        "oracle_evidence": [
            e["id"] for e in evidence["events"] if e["kind"] == "oracle"
        ],
    }


def audit(root):
    config, specs, manifest = pilot.load_experiment(root)
    spec = next(s for s in specs if s["id"] == "T02-missing-requirement")
    rows = []
    for row in manifest:
        if row["task_id"] != spec["id"]:
            continue
        directory = root / "runs" / row["run_id"]
        item = {**row, "status": "unscored"}
        if (directory / "objective.json").exists():
            score = pilot.objective_result(root, row["run_id"])
            evidence = pilot.read_json(directory / "evidence.json")
            result = audited_outcome(spec, evidence)
            if result["original_pass"] != score["pass"]:
                raise pilot.PilotError("audit disagrees with frozen outcome")
            item.update(status=score["status"], **result)
        rows.append(item)
    return {
        "config_hash": config["config_hash"],
        "audit_source_hash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "analysis": "post_hoc_sensitivity_only",
        "limitation": "Narrow automated wording correction; not independent human validation or a replacement primary endpoint.",
        "runs": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", type=Path)
    args = parser.parse_args()
    pilot.write_json(
        args.experiment / "clarification-audit.json", audit(args.experiment)
    )
