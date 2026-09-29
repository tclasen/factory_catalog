#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
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
from urllib.parse import unquote
import unicodedata

import yaml
from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin


MARKDOWN = MarkdownIt("commonmark").use(
    footnote_plugin, inline=False, move_to_end=False, always_match_refs=True,
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous mappings, including nested metadata mappings."""

    def construct_mapping(self, node, deep=False):
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in keys:
                    raise ValueError(f"duplicate YAML key {key!r}")
                keys.add(key)
            except TypeError as exc:
                raise ValueError("YAML mapping keys must be scalar") from exc
        return super().construct_mapping(node, deep=deep)



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
        if "catalog_version" in data:
            errors.append("catalog_version belongs only in bundle VERSION, not concept metadata")
        if any(token.type == "inline" and
               re.match(r"\*\*(?:Identity|Catalog|Family):\*\*", token.content)
               for token in MARKDOWN.parse(document.body)):
            errors.append("derive identity, catalog version, and family; do not repeat summary headers")
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
                data = yaml.load(frontmatter[1], Loader=UniqueKeyLoader)
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
    """Derive heading IDs from parsed Markdown, with GitHub duplicate suffixes."""
    def plain(tokens):
        return "".join(
            plain(token.children) if token.children else
            token.content if token.type in ("text", "code_inline") else
            " " if token.type in ("softbreak", "hardbreak") else ""
            for token in tokens
        )

    anchors = []
    tokens = MARKDOWN.parse(body)
    for pos, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        text = plain(tokens[pos + 1].children or []).lower()
        slug = "".join(c for c in text if c in "-_ " or
                       unicodedata.category(c)[0] not in "PSCZ").replace(" ", "-")
        anchor, suffix = slug, 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{slug}-{suffix}"
        anchors.append(anchor)
    return anchors


def validate_sources(root: Path, document: Document, documents: dict[Path, Document]) -> list[str]:
    """Check source records and keyed attribution, ignoring literal code examples."""
    errors, ids, local = [], set(), []
    sources = document.metadata.get("sources", [])
    if not isinstance(sources, list):
        return ["sources must be a list"]
    for source in sources:
        if not isinstance(source, dict):
            errors.append("source must be a mapping")
            continue
        resource = source.get("resource")
        if not isinstance(resource, str) or not resource.strip():
            errors.append("source requires non-empty resource")
        elif not re.match(r"[a-z][a-z0-9+.-]*:", resource, re.I) and (
            resource.startswith(("./", "../", "/")) or
            (not re.search(r"\s", resource) and ("/" in resource or "." in resource))
        ):
            local.append(resource)
        if "id" in source:
            label = source["id"]
            if not isinstance(label, str) or not label.strip():
                errors.append("source id must be a non-empty string")
            elif label in ids:
                errors.append(f"duplicate source id {label}")
            else:
                ids.add(label)
    definitions, references = [], []

    def visit(tokens):
        for token in tokens:
            if token.type == "footnote_reference_open":
                definitions.append(token.meta["label"])
            elif token.type == "footnote_ref":
                references.append(token.meta["label"])
            if token.children:
                visit(token.children)

    visit(MARKDOWN.parse(document.body))
    for label in sorted(set(definitions + references)):
        if label not in ids:
            errors.append(f"footnote {label} has no matching source id")
        if label in references and label not in definitions:
            errors.append(f"undefined footnote {label}")
        if definitions.count(label) > 1:
            errors.append(f"duplicate footnote definition {label}")
    errors.extend(validate_links(root, documents, {document.path: local}))
    return errors


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
            file, anchor = unquote(file), unquote(anchor)
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
            resolve_reference(root, index, unquote(link.partition("#")[0]))
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
    root: Path, document: Document, documents: dict[Path, Document],
) -> list[str]:
    errors = []
    data = document.metadata
    if data.get("example") is not True:
        errors.append("example must be true")
    if not isinstance(data.get("domain"), str) or not data["domain"].strip():
        errors.append("missing domain")
    activities = data.get("activities")
    if (not isinstance(activities, list) or not activities
            or any(not isinstance(item, str) or not item.strip() for item in activities)):
        errors.append("activities must be a non-empty list of non-empty descriptions")
    if "work_types" in data:
        errors.append("replace work_types taxonomy references with free-text activities")
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
    for path, document in documents.items():
        if document.metadata.get("type") == "Control":
            findings = validate_control(document, families)
        elif document.metadata.get("type") == "Factory Example":
            findings = validate_factory_example(root, document, documents)
        else:
            continue
        errors.extend(qualify_errors(root, path, findings))
    return errors


def validate_version(root: Path) -> list[str]:
    """Check the single bundle version without tying validation to a release."""
    try:
        value = (root / "VERSION").read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"VERSION: cannot read bundle version: {exc}"]
    number = r"(?:0|[1-9][0-9]*)"
    identifier = rf"(?:{number}|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    semver = (rf"v{number}\.{number}\.{number}"
              rf"(?:-{identifier}(?:\.{identifier})*)?"
              r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?\n?")
    if not re.fullmatch(semver, value):
        return ["VERSION: expected one vMAJOR.MINOR.PATCH value with optional SemVer suffixes"]
    return []


def validate(root: Path, *, require_index_coverage: bool = False) -> tuple[list[str], int]:
    """Run validation phases in diagnostic order."""
    documents, errors = load_documents(root)
    errors.extend(validate_version(root))
    links = {path: extract_links(document.body) for path, document in documents.items()}
    errors.extend(validate_links(root, documents, links))
    if require_index_coverage:
        errors.extend(validate_index_coverage(root, documents, links))
    errors.extend(validate_domain_metadata(root, documents))
    for path, document in documents.items():
        errors.extend(qualify_errors(root, path, validate_sources(root, document, documents)))
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
