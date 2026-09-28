#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Validate this catalog against pinned OKF 0.2 and repository conventions.

Link integrity, index coverage, and domain fields are repository checks, not OKF
conformance requirements. This is not a general-purpose OKF validator.
"""

import argparse
from datetime import date
from pathlib import Path
import re
import sys

import yaml


def validate(root: Path) -> tuple[list[str], int]:
    errors = []
    documents = {}
    metadata = {}

    def fail(path: Path, message: str) -> None:
        errors.append(f"{path.relative_to(root)}: {message}")

    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            fail(path, f"cannot read UTF-8: {exc}")
            continue
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
        data = {}
        if frontmatter:
            try:
                data = yaml.safe_load(frontmatter[1])
                if not isinstance(data, dict):
                    raise ValueError("frontmatter must be a mapping")
            except (yaml.YAMLError, ValueError) as exc:
                fail(path, f"invalid YAML: {exc}")
                continue
        body = text[frontmatter.end():] if frontmatter else text
        documents[path] = body
        metadata[path] = data
        if path.name == "index.md":
            if path == root / "index.md":
                if data != {"okf_version": "0.2"}:
                    fail(path, 'root index must declare only okf_version: "0.2"')
            elif frontmatter:
                fail(path, "nested index cannot contain frontmatter")
        elif path.name == "log.md":
            if frontmatter:
                fail(path, "log cannot contain frontmatter")
            for heading in re.findall(r"^## (.+)$", body, re.MULTILINE):
                try:
                    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", heading):
                        raise ValueError("invalid date")
                    date.fromisoformat(heading)
                except ValueError:
                    fail(path, f"invalid log date {heading}")
        else:
            for key in ("type", "title", "description"):
                if not isinstance(data.get(key), str) or not data[key].strip():
                    fail(path, f"missing non-empty {key}")
            if data.get("catalog_version") != "v0.1.0":
                fail(path, "catalog_version must be v0.1.0 during baseline hold")
            if "status" in data and data["status"] not in ("draft", "stable", "deprecated"):
                fail(path, "invalid OKF lifecycle status")

    if root / "index.md" not in documents:
        errors.append("index.md: missing bundle entry point")

    def resolve(path: Path, target: str) -> Path:
        local = root / target.lstrip("/") if target.startswith("/") else path.parent / target
        return local.resolve()

    links = {}
    for path, body in documents.items():
        # Fenced examples contain literal sample references, not navigation links.
        prose = re.sub(r"^```.*?^```[^\n]*$", "", body, flags=re.MULTILINE | re.DOTALL)
        links[path] = re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", prose)
        for target in links[path]:
            if re.match(r"[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue
            file, separator, anchor = target.partition("#")
            dest = resolve(path, file) if file else path
            if not dest.is_relative_to(root) or not dest.exists():
                fail(path, f"missing or out-of-bundle link {target}")
                continue
            if separator:
                headings = [
                    re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
                    for heading in re.findall(r"^#{1,6}\s+(.+)$", documents.get(dest, ""), re.MULTILINE)
                ]
                if anchor not in headings:
                    fail(path, f"missing heading {target}")

    for directory in sorted({path.parent for path in documents}):
        index = directory / "index.md"
        if index not in documents:
            fail(index, "missing directory index")
            continue
        targets = [resolve(index, link.partition("#")[0]) for link in links.get(index, [])]
        for child in sorted(directory.iterdir()):
            if child.name == "index.md":
                continue
            expected = child / "index.md" if child.is_dir() else child
            if expected.suffix != ".md":
                continue
            if expected not in targets and not (child.is_dir() and child in targets):
                fail(index, f"unlisted entry {child.name}")

    def vocabulary(filename: str) -> list[str]:
        return re.findall(r"^\|[^|]+\| `([^`]+)` \|", documents.get(root / filename, ""), re.MULTILINE)

    families = vocabulary("control-families.md")
    work_types = vocabulary("work-types.md")
    for path, data in metadata.items():
        if data.get("type") == "Control":
            if data.get("family") not in families:
                fail(path, "unknown family")
            for heading in (
                "Purpose and applicability", "Requirement", "Implementation",
                "Expected outcome and assessment", "Dependencies and limitations",
            ):
                if f"## {heading}\n" not in documents[path]:
                    fail(path, f"missing section {heading}")
        elif data.get("type") == "Factory Example":
            if data.get("example") is not True:
                fail(path, "example must be true")
            if not isinstance(data.get("domain"), str) or not data["domain"].strip():
                fail(path, "missing domain")
            types = data.get("work_types")
            if not isinstance(types, list) or not types or any(item not in work_types for item in types):
                fail(path, "missing or unknown work types")
            selections = data.get("control_selections")
            if not isinstance(selections, list) or not selections:
                fail(path, "missing control selections")
                continue
            for selection in selections:
                if not isinstance(selection, dict) or not isinstance(selection.get("control"), str):
                    fail(path, "invalid control selection")
                    continue
                dest = resolve(path, selection["control"])
                if metadata.get(dest, {}).get("type") != "Control":
                    fail(path, f"selection does not reference a Control: {selection['control']}")
                for key, values in {
                    "applicability": ("applicable", "not-applicable", "undetermined"),
                    "implementation_state": ("not-planned", "proposed", "implemented", "retired"),
                    "assessment_result": ("not-assessed", "pass", "fail", "inconclusive"),
                }.items():
                    if selection.get(key) not in values:
                        fail(path, f"invalid {key}")

    return errors, len(documents)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent / "catalog")
    args = parser.parse_args()
    errors, count = validate(args.catalog.resolve())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {count} Markdown files; OKF structure, catalog metadata, local links, and index coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
