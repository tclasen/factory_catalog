#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Emit advisory content findings; these require human interpretation."""

import argparse
from difflib import SequenceMatcher
from itertools import combinations
import json
from pathlib import Path
import re
import subprocess
import sys

import validate_catalog as validator


def review(root: Path, *, github: bool = False) -> list[str]:
    errors, _ = validator.validate(root)
    if errors:
        raise ValueError("\n".join(errors))
    documents, _ = validator.load_documents(root)
    warnings = []
    controls = [doc for doc in documents.values() if doc.metadata.get("type") == "Control"]
    for left, right in combinations(controls, 2):
        if left.metadata.get("family") != right.metadata.get("family"):
            continue
        title_a, title_b = left.metadata["title"].lower(), right.metadata["title"].lower()
        if SequenceMatcher(None, title_a, title_b).ratio() >= 0.75:
            warnings.append(f"Possible overlapping controls: {left.path.relative_to(root)} and "
                            f"{right.path.relative_to(root)}; compare requirements and applicability.")
    drafts = sum(doc.metadata.get("status") == "draft" for doc in controls)
    if drafts and "ready to use" in documents[root / "index.md"].body.lower():
        warnings.append(f"index.md: blanket readiness wording with {drafts} draft controls; review the claim.")
    cache = {}
    for path, doc in documents.items():
        if doc.metadata.get("type") == "Factory Example":
            states = {item.get("implementation_state") for item in doc.metadata.get("control_selections", [])
                      if isinstance(item, dict)}
            if re.search(r"(?:selected controls:|all implementations are)\s*\*\*proposed\*\*", doc.body, re.I) and states - {"proposed"}:
                warnings.append(f"{path.relative_to(root)}: blanket proposed-state wording differs from selection metadata.")
        # Paragraph context keeps historical mentions advisory, never a hard failure.
        for paragraph in doc.body.split("\n\n"):
            if not re.search(r"\b(pending|propos\w*|coordinat\w*)\b", paragraph, re.I):
                continue
            for number in sorted(set(re.findall(r"https://github.com/tclasen/factory_catalog/pull/(\d+)", paragraph))):
                if not github:
                    warnings.append(f"{path.relative_to(root)}: review proposal/pending wording for PR #{number}; live state not checked (use --github).")
                    continue
                if number not in cache:
                    try:
                        result = subprocess.run(
                            ["gh", "api", f"repos/tclasen/factory_catalog/pulls/{number}"],
                            check=True, capture_output=True, text=True, timeout=20,
                        )
                        data = json.loads(result.stdout)
                        cache[number] = "merged" if data.get("merged_at") else data["state"]
                    except (OSError, subprocess.SubprocessError, ValueError, KeyError):
                        cache[number] = "unavailable"
                state = cache[number]
                if state != "open":
                    warnings.append(f"{path.relative_to(root)}: PR #{number} state {state}; review proposal/pending wording."
                                    if state != "unavailable" else
                                    f"PR #{number}: live state unavailable; check manually.")
    return sorted(set(warnings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github", action="store_true", help="query referenced PRs using read-only gh api calls")
    parser.add_argument("catalog", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent / "catalog")
    args = parser.parse_args()
    try:
        warnings = review(args.catalog.resolve(), github=args.github)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    for warning in warnings:
        print("REVIEW: " + " ".join(warning.split()))
    print(f"Review scan: {len(warnings)} advisory findings; semantic correctness still requires human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
