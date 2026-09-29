#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Run the same blocking checks and advisory scan locally and in CI."""

import argparse
from pathlib import Path
import subprocess
import sys


def check_whitespace(root: Path) -> int:
    """Check the tracked working tree, including errors already committed in CI."""
    empty_tree = subprocess.run(["git", "hash-object", "-w", "-t", "tree", "--stdin"],
                                input="", capture_output=True, text=True, cwd=root)
    if empty_tree.returncode:
        print(empty_tree.stderr, file=sys.stderr, end="")
        return empty_tree.returncode
    commands = [
        # These pinned upstream files contain whitespace that must be preserved.
        ["git", "diff", "--check", empty_tree.stdout.strip(), "--", ".",
         ":(exclude)vendor/okf/SPEC.md", ":(exclude)vendor/okf/LICENSE.md"],
        ["git", "diff", "--check"],
        ["git", "diff", "--cached", "--check"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=root)
        if result.returncode:
            return result.returncode
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github", action="store_true", help="also check live PR states (requires gh authentication)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    commands = [[sys.executable, str(root / "scripts" / name)] for name in (
        "test_validate_catalog.py", "validate_catalog.py", "build_catalog.py",
        "check_guidance_links.py", "review_catalog.py",
    )]
    if args.github:
        commands[-1].append("--github")
    for command in commands:
        result = subprocess.run(command, cwd=root)
        if result.returncode:
            return result.returncode
    result = check_whitespace(root)
    if result:
        return result
    print("PASS: all blocking catalog checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
