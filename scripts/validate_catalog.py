#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0"]
# ///
"""Validate this catalog against pinned OKF 0.2 and repository conventions.

Link integrity, index coverage, and domain fields are repository checks, not OKF
conformance requirements. This is not a general-purpose OKF validator.
"""

import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
import sys
from typing import Any

import yaml
from markdown_it import MarkdownIt


MARKDOWN = MarkdownIt("commonmark")


@dataclass(frozen=True)
class Document:
    path: Path
    body: str
    metadata: dict[str, Any]
    has_frontmatter: bool


def qualify_errors(root: Path, path: Path, errors: list[str]) -> list[str]:
    """Attach a bundle-relative filename to each diagnostic."""
    return [f"{path.relative_to(root)}: {error}" for error in errors]


def validate_document_structure(root: Path, document: Document) -> list[str]:
    """Check reserved filenames and common concept metadata."""
    errors = []
    path, data = document.path, document.metadata
    if path.name == "index.md":
        if path == root / "index.md":
            if data != {"okf_version": "0.2"}:
                errors.append('root index must declare only okf_version: "0.2"')
        elif document.has_frontmatter:
            errors.append("nested index cannot contain frontmatter")
    elif path.name == "log.md":
        if document.has_frontmatter:
            errors.append("log cannot contain frontmatter")
        for heading in re.findall(r"^## (.+)$", document.body, re.MULTILINE):
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", heading):
                    raise ValueError("invalid date")
                date.fromisoformat(heading)
            except ValueError:
                errors.append(f"invalid log date {heading}")
    else:
        for key in ("type", "title", "description"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(f"missing non-empty {key}")
        if data.get("catalog_version") != "v0.1.0":
            errors.append("catalog_version must be v0.1.0 during baseline hold")
        if "status" in data and data["status"] not in ("draft", "stable", "deprecated"):
            errors.append("invalid OKF lifecycle status")
    return errors


def load_documents(root: Path) -> tuple[dict[Path, Document], list[str]]:
    """Read UTF-8 documents, parse safe YAML, and check their structure."""
    documents = {}
    errors = []
    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            errors.extend(qualify_errors(root, path, [f"cannot read UTF-8: {exc}"]))
            continue
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
        data = {}
        if frontmatter:
            try:
                data = yaml.safe_load(frontmatter[1])
                if not isinstance(data, dict):
                    raise ValueError("frontmatter must be a mapping")
            except (yaml.YAMLError, ValueError) as exc:
                errors.extend(qualify_errors(root, path, [f"invalid YAML: {exc}"]))
                continue
        body = text[frontmatter.end():] if frontmatter else text
        document = Document(path, body, data, frontmatter is not None)
        documents[path] = document
        errors.extend(qualify_errors(root, path, validate_document_structure(root, document)))
    if root / "index.md" not in documents:
        errors.append("index.md: missing bundle entry point")
    return documents, errors


def resolve_reference(root: Path, path: Path, target: str) -> Path:
    """Resolve an OKF bundle-relative or document-relative reference."""
    local = root / target.lstrip("/") if target.startswith("/") else path.parent / target
    return local.resolve()


def extract_links(body: str) -> list[str]:
    """Find navigation links, excluding literal examples in fenced blocks."""
    links = []

    def visit(tokens):
        for token in tokens:
            attribute = {"link_open": "href", "image": "src"}.get(token.type)
            if attribute:
                target = token.attrGet(attribute)
                if target is not None:
                    links.append(target)
            if token.children:
                visit(token.children)

    visit(MARKDOWN.parse(body))
    return links


def extract_heading_anchors(body: str) -> list[str]:
    return [
        re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        for heading in re.findall(r"^#{1,6}\s+(.+)$", body, re.MULTILINE)
    ]


def validate_links(
    root: Path, documents: dict[Path, Document], links: dict[Path, list[str]],
) -> list[str]:
    """Check local navigation destinations and heading anchors."""
    errors = []
    for path, targets in links.items():
        for target in targets:
            if re.match(r"[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue
            file, separator, anchor = target.partition("#")
            dest = resolve_reference(root, path, file) if file else path
            if not dest.is_relative_to(root) or not dest.exists():
                errors.extend(qualify_errors(root, path, [f"missing or out-of-bundle link {target}"]))
                continue
            if separator:
                destination = documents.get(dest)
                headings = extract_heading_anchors(destination.body if destination else "")
                if anchor not in headings:
                    errors.extend(qualify_errors(root, path, [f"missing heading {target}"]))
    return errors


def validate_index_coverage(
    root: Path, documents: dict[Path, Document], links: dict[Path, list[str]],
) -> list[str]:
    """Require each directory index to list its documents and subdirectories."""
    errors = []
    for directory in sorted({path.parent for path in documents}):
        index = directory / "index.md"
        if index not in documents:
            errors.extend(qualify_errors(root, index, ["missing directory index"]))
            continue
        targets = [
            resolve_reference(root, index, link.partition("#")[0])
            for link in links.get(index, [])
        ]
        for child in sorted(directory.iterdir()):
            if child.name == "index.md":
                continue
            expected = child / "index.md" if child.is_dir() else child
            if expected.suffix != ".md":
                continue
            if expected not in targets and not (child.is_dir() and child in targets):
                errors.extend(qualify_errors(root, index, [f"unlisted entry {child.name}"]))
    return errors


def extract_vocabulary(document: Document | None) -> list[str]:
    """Read the value column of a catalog taxonomy table."""
    body = document.body if document else ""
    return re.findall(r"^\|[^|]+\| `([^`]+)` \|", body, re.MULTILINE)


def validate_control(document: Document, families: list[str]) -> list[str]:
    errors = []
    if document.metadata.get("family") not in families:
        errors.append("unknown family")
    tokens = MARKDOWN.parse(document.body)
    sections = {}
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.tag != "h2":
            continue
        heading = tokens[index + 1].content
        end = next((
            pos for pos in range(index + 3, len(tokens))
            if tokens[pos].type == "heading_open" and tokens[pos].tag in ("h1", "h2")
        ), len(tokens))
        # Subheadings and HTML comments alone do not constitute section content.
        sections[heading] = any(
            tokens[pos].content.strip()
            and tokens[pos].type in ("inline", "fence", "code_block")
            and tokens[pos - 1].type != "heading_open"
            for pos in range(index + 3, end)
        )
    for heading in (
        "Purpose and applicability", "Requirement", "Implementation",
        "Expected outcome and assessment", "Dependencies and limitations",
    ):
        if heading not in sections:
            errors.append(f"missing section {heading}")
        elif not sections[heading]:
            errors.append(f"empty section {heading}")
    return errors


def validate_control_selection(
    root: Path, path: Path, selection: Any, documents: dict[Path, Document],
) -> list[str]:
    if not isinstance(selection, dict) or not isinstance(selection.get("control"), str):
        return ["invalid control selection"]
    errors = []
    dest = resolve_reference(root, path, selection["control"])
    control = documents.get(dest)
    if control is None or control.metadata.get("type") != "Control":
        errors.append(f"selection does not reference a Control: {selection['control']}")
    for key, values in {
        "applicability": ("applicable", "not-applicable", "undetermined"),
        "implementation_state": ("not-planned", "proposed", "implemented", "retired"),
        "assessment_result": ("not-assessed", "pass", "fail", "inconclusive"),
    }.items():
        if selection.get(key) not in values:
            errors.append(f"invalid {key}")
    return errors


def validate_factory_example(
    root: Path, document: Document, work_types: list[str], documents: dict[Path, Document],
) -> list[str]:
    errors = []
    data = document.metadata
    if data.get("example") is not True:
        errors.append("example must be true")
    if not isinstance(data.get("domain"), str) or not data["domain"].strip():
        errors.append("missing domain")
    types = data.get("work_types")
    if not isinstance(types, list) or not types or any(item not in work_types for item in types):
        errors.append("missing or unknown work types")
    selections = data.get("control_selections")
    if not isinstance(selections, list) or not selections:
        errors.append("missing control selections")
        return errors
    for selection in selections:
        errors.extend(validate_control_selection(root, document.path, selection, documents))
    return errors


def validate_domain_metadata(root: Path, documents: dict[Path, Document]) -> list[str]:
    """Apply catalog-specific checks without rejecting unknown OKF types."""
    errors = []
    families = extract_vocabulary(documents.get(root / "control-families.md"))
    work_types = extract_vocabulary(documents.get(root / "work-types.md"))
    for path, document in documents.items():
        if document.metadata.get("type") == "Control":
            findings = validate_control(document, families)
        elif document.metadata.get("type") == "Factory Example":
            findings = validate_factory_example(root, document, work_types, documents)
        else:
            continue
        errors.extend(qualify_errors(root, path, findings))
    return errors


def validate(root: Path, *, require_index_coverage: bool = False) -> tuple[list[str], int]:
    """Run validation phases in diagnostic order."""
    documents, errors = load_documents(root)
    links = {path: extract_links(document.body) for path, document in documents.items()}
    errors.extend(validate_links(root, documents, links))
    if require_index_coverage:
        errors.extend(validate_index_coverage(root, documents, links))
    errors.extend(validate_domain_metadata(root, documents))
    return errors, len(documents)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "catalog", nargs="?", type=Path,
        default=Path(__file__).resolve().parent.parent / "catalog",
    )
    parser.add_argument("--require-index-coverage", action="store_true",
                        help="require exhaustive indexes in a generated bundle")
    args = parser.parse_args()
    errors, count = validate(args.catalog.resolve(), require_index_coverage=args.require_index_coverage)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    coverage = ", and index coverage" if args.require_index_coverage else ""
    print(f"PASS: {count} Markdown files; OKF structure, catalog metadata, local links{coverage}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
