#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Check local Markdown links in root guidance, docs/, and factory/."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from validate_catalog import extract_heading_anchors, extract_links


def read_body(path: Path) -> str:
    """Exclude YAML metadata without imposing the catalog's document schema."""
    text = path.read_text(encoding="utf-8")
    return re.sub(r"\A---\n.*?\n---(?:\n|\Z)", "", text, count=1, flags=re.DOTALL)


def validate(root: Path) -> tuple[list[str], int]:
    root = root.resolve()
    sources = sorted(set(root.glob("*.md")) | {
        path for directory in ("docs", "factory")
        for path in (root / directory).rglob("*.md")
    })
    errors = []
    anchors = {}
    for source in sources:
        label = source.relative_to(root)
        try:
            if not source.resolve().is_relative_to(root):
                raise ValueError("source resolves outside repository")
            targets = extract_links(read_body(source))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{label}: cannot read guidance: {exc}")
            continue
        for target in targets:
            try:
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                file = unquote(url.path)
                destination = (
                    root / file.lstrip("/") if file.startswith("/")
                    else source.parent / file if file else source
                ).resolve()
                if not destination.is_relative_to(root) or not destination.exists():
                    errors.append(f"{label}: missing or out-of-repository link {target}")
                    continue
                # Non-Markdown fragments (e.g. PDF pages) have different semantics.
                if url.fragment and destination.suffix.lower() == ".md":
                    if destination not in anchors:
                        anchors[destination] = extract_heading_anchors(read_body(destination))
                    if unquote(url.fragment) not in anchors[destination]:
                        errors.append(f"{label}: missing heading {target}")
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"{label}: cannot check link {target}: {exc}")
    return errors, len(sources)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    errors, count = validate(args.repository)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: local links and Markdown heading anchors in {count} guidance files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
