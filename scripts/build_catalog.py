#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Build and validate complete OKF indexes without modifying source files.

With no arguments, check a temporary build. Use --output with a new directory
to retain a browsable bundle. Existing output directories are never overwritten.
"""

import argparse
from pathlib import Path
import re
import shutil
import sys
import tempfile

import validate_catalog as validator


def markdown_text(value: str) -> str:
    """Render metadata as plain text, even when it contains Markdown syntax."""
    return re.sub(r"([\\`*_{}\[\]()#+.!<>|~-])", r"\\\1", " ".join(value.split()))


def validate_distribution(source: Path, destination: Path) -> list[str]:
    """Check packaging and generated control discovery independently of the writer."""
    errors = []
    license_path = source.parent / "LICENSE"
    bundled = destination / "LICENSE"
    if not bundled.is_file() or bundled.read_bytes() != license_path.read_bytes():
        errors.append("generated bundle must include the unchanged repository LICENSE")
    documents, _ = validator.load_documents(source)
    index = (destination / "index.md").read_text(encoding="utf-8")
    section = index.partition("## Controls by family\n")[2]
    targets = validator.extract_links(section)
    groups = {}
    listings = {}
    for path, document in documents.items():
        if document.metadata.get("type") != "Control":
            continue
        target = path.relative_to(source).as_posix()
        family = document.metadata["family"]
        if family not in groups:
            group = section.partition(f"### {family}\n")[2].split("\n### ")[0]
            groups[family] = validator.extract_links(group)
        if targets.count(target) != 1 or target not in groups[family]:
            errors.append(f"family navigation must list {target} exactly once under {family}")
        if path.parent not in listings:
            listings[path.parent] = (destination / path.parent.relative_to(source) / "index.md").read_text()
        listing = listings[path.parent]
        entry = next((line for line in listing.splitlines() if f"]({path.name})" in line), "")
        status = document.metadata.get("status", "unspecified")
        if f"[status: {status}; family: {family}]" not in entry:
            errors.append(f"generated entry must show status and family for {target}")
    return errors


def build(source: Path, destination: Path) -> int:
    source, destination = source.resolve(), destination.resolve()
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        raise ValueError("output and source directories must not overlap")
    if destination.exists():
        raise ValueError(f"output already exists; choose a new directory: {destination}")
    errors, _ = validator.validate(source)
    if errors:
        raise ValueError("\n".join(errors))
    license_path = source.parent / "LICENSE"
    if not license_path.is_file():
        raise ValueError("source repository must supply LICENSE beside the catalog directory")
    shutil.copytree(source, destination)
    shutil.copyfile(license_path, destination / "LICENSE")
    documents, _ = validator.load_documents(destination)
    # Include intermediate directories even when only descendants hold concepts.
    directories = {destination}
    for path in documents:
        directories.update(parent for parent in path.parents if parent.is_relative_to(destination))
    for directory in sorted(directories):
        index = directory / "index.md"
        preface = index.read_text(encoding="utf-8").rstrip() if index.exists() else (
            f"# {markdown_text(directory.name)}"
        )
        entries = []
        for child in sorted(directory.iterdir()):
            if child.name == "index.md":
                continue
            if child.is_dir() and child in directories:
                entries.append(f"- [{markdown_text(child.name)}]({child.name}/index.md)")
            elif child in documents:
                document = documents[child]
                title = document.metadata.get("title", child.stem)
                description = document.metadata.get("description", "")
                suffix = f" — {markdown_text(description)}" if description else ""
                if document.metadata.get("type") == "Control":
                    suffix += (f" [status: {document.metadata.get('status', 'unspecified')}; "
                               f"family: {document.metadata['family']}]")
                entries.append(f"- [{markdown_text(title)}]({child.name}){suffix}")
        index.write_text(preface + "\n\n## Directory contents\n\n" + "\n".join(entries) + "\n", encoding="utf-8")
    root_index = destination / "index.md"
    family_lines = ["", "## Controls by family", ""]
    families = validator.extract_vocabulary(documents.get(destination / "control-families.md"))
    for family in families:
        family_lines.extend([f"### {family}", ""])
        for path, document in sorted(documents.items()):
            if document.metadata.get("type") == "Control" and document.metadata.get("family") == family:
                family_lines.append(f"- [{markdown_text(document.metadata['title'])}]"
                                    f"({path.relative_to(destination).as_posix()})")
        family_lines.append("")
    root_index.write_text(root_index.read_text() + "\n".join(family_lines), encoding="utf-8")
    errors, count = validator.validate(destination, require_index_coverage=True)
    errors.extend(validate_distribution(source, destination))
    if errors:
        raise ValueError("\n".join(errors))
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parent.parent / "catalog")
    parser.add_argument("--output", type=Path, help="new directory for the generated bundle")
    args = parser.parse_args()
    try:
        if args.output:
            count = build(args.source, args.output)
        else:
            with tempfile.TemporaryDirectory() as temporary:
                count = build(args.source, Path(temporary) / "catalog")
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"PASS: generated bundle; {count} Markdown files; complete indexes and catalog validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
