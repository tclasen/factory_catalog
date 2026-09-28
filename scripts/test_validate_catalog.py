#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0"]
# ///
"""Regression tests for catalog validation; run directly with uv on PATH."""

from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import validate_catalog as validator
import build_catalog as builder


REPOSITORY = Path(__file__).resolve().parent.parent
HEADINGS = (
    "Purpose and applicability", "Requirement", "Implementation",
    "Expected outcome and assessment", "Dependencies and limitations",
)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve() / "catalog"
        shutil.copytree(REPOSITORY / "catalog", self.root)
        self.control = self.root / "controls/bounded-external-action.md"

    def append(self, text):
        self.control.write_text(self.control.read_text() + "\n" + text, encoding="utf-8")

    def errors(self):
        return validator.validate(self.root)[0]

    def test_current_catalog(self):
        self.assertEqual(self.errors(), [])

    def test_missing_inline_link(self):
        self.append("[Missing](missing.md)")
        self.assertTrue(any("missing.md" in error for error in self.errors()))

    def test_missing_reference_link_forms(self):
        for link in ("[Missing][ref]", "[ref][]", "[ref]"):
            with self.subTest(link=link):
                self.assertEqual(validator.extract_links(link + "\n\n[ref]: missing.md"), ["missing.md"])
        self.append("[Missing][ref]\n\n[ref]: missing.md")
        self.assertTrue(any("missing.md" in error for error in self.errors()))

    def test_valid_reference_link_with_title(self):
        self.append('[Other][other]\n\n[other]: outcome-verification.md "Other control"')
        self.assertEqual(self.errors(), [])

    def test_code_examples_are_not_links(self):
        self.append('`[Example](missing.md)`\n\n~~~md\n[Example](missing.md)\n~~~\n\n```md\n[Example][ref]\n\n[ref]: missing.md\n```')
        self.assertEqual(self.errors(), [])

    def test_image_destination(self):
        self.append("![Missing image](missing.png)")
        self.assertTrue(any("missing.png" in error for error in self.errors()))

    def test_missing_anchor(self):
        self.append("[Missing](outcome-verification.md#missing)")
        self.assertTrue(any("missing heading" in error for error in self.errors()))

    def test_link_outside_bundle(self):
        self.append("[Outside](../../README.md)")
        self.assertTrue(any("out-of-bundle" in error for error in self.errors()))

    def test_empty_control_sections(self):
        for content in ("", "<!-- TODO -->", "### Placeholder"):
            with self.subTest(content=content):
                body = "\n\n".join(f"## {heading}\n{content}" for heading in HEADINGS)
                doc = validator.Document(self.control, body, {"family": "test"}, True)
                self.assertEqual(len(validator.validate_control(doc, ["test"])), 5)

    def test_headings_in_code_are_not_sections(self):
        body = "```md\n" + "\n".join(f"## {heading}" for heading in HEADINGS) + "\n```"
        doc = validator.Document(self.control, body, {"family": "test"}, True)
        self.assertTrue(all("missing section" in error for error in validator.validate_control(doc, ["test"])))

    def test_populated_sections_with_subheadings(self):
        body = "\n\n".join(f"## {heading}\n### Detail\nUseful text." for heading in HEADINGS)
        doc = validator.Document(self.control, body, {"family": "test"}, True)
        self.assertEqual(validator.validate_control(doc, ["test"]), [])

    def test_invalid_yaml(self):
        self.control.write_text("---\ntype: [\n---\n", encoding="utf-8")
        self.assertTrue(any("invalid YAML" in error for error in self.errors()))

    def test_unknown_family(self):
        text = self.control.read_text()
        self.control.write_text(re.sub(r"^family:.*$", "family: nonexistent", text, flags=re.MULTILINE))
        self.assertTrue(any("unknown family" in error for error in self.errors()))

    def test_unlisted_concept(self):
        shutil.copyfile(self.control, self.control.with_name("unlisted.md"))
        self.assertEqual(self.errors(), [])
        output = self.root.parent / "coverage-build"
        builder.build(self.root, output)
        index = output / "controls/index.md"
        index.write_text("\n".join(line for line in index.read_text().splitlines()
                                   if "](unlisted.md)" not in line) + "\n")
        errors, _ = validator.validate(output, require_index_coverage=True)
        self.assertTrue(any("unlisted entry unlisted.md" in error for error in errors))

    def test_missing_entry_point(self):
        (self.root / "index.md").unlink()
        self.assertTrue(any("missing bundle entry point" in error for error in self.errors()))

    def snapshot(self, root):
        return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}

    def test_build_is_deterministic_and_does_not_edit_source(self):
        before = self.snapshot(self.root)
        first, second = self.root.parent / "first", self.root.parent / "second"
        builder.build(self.root, first)
        builder.build(self.root, second)
        self.assertEqual(self.snapshot(self.root), before)
        self.assertEqual(self.snapshot(first), self.snapshot(second))
        self.assertEqual(validator.validate(first, require_index_coverage=True)[0], [])
        self.assertEqual((first / "controls/bounded-external-action.md").read_bytes(), self.control.read_bytes())

    def test_independent_additions_combine_without_shared_edits(self):
        baseline = self.snapshot(self.root)
        additions = {}
        for name in ("agent-alpha", "agent-beta"):
            branch = self.root.parent / name
            shutil.copytree(self.root, branch)
            control = branch / f"controls/{name}.md"
            shutil.copyfile(self.control, control)
            self.assertEqual(validator.validate(branch)[0], [])
            builder.build(branch, self.root.parent / f"{name}-build")
            changed = {path: data for path, data in self.snapshot(branch).items() if baseline.get(path) != data}
            self.assertEqual(set(changed), {Path(f"controls/{name}.md")})
            self.assertFalse(set(additions) & set(changed))
            additions.update(changed)
        for path, data in additions.items():
            (self.root / path).write_bytes(data)
        combined = self.root.parent / "combined"
        builder.build(self.root, combined)
        index = (combined / "controls/index.md").read_text()
        for path in additions:
            self.assertIn(f"]({path.name})", index)
        self.assertEqual(validator.validate(combined, require_index_coverage=True)[0], [])

    def test_new_nested_concepts_need_no_source_indexes(self):
        directory = self.root / "guides/nested"
        directory.mkdir(parents=True)
        (directory / "new-guide.md").write_text(
            '---\ntype: Guide\ntitle: "A [guide]"\ndescription: "Use *examples*."\n'
            'catalog_version: v0.1.0\n---\n\n# A guide\n\nNew guidance.\n'
        )
        self.assertEqual(self.errors(), [])
        output = self.root.parent / "nested-build"
        builder.build(self.root, output)
        for path in ("index.md", "guides/index.md", "guides/nested/index.md"):
            self.assertTrue((output / path).is_file())
        self.assertIn(r"A \[guide\]", (output / "guides/nested/index.md").read_text())
        self.assertEqual(validator.validate(output, require_index_coverage=True)[0], [])

    def test_build_rejects_invalid_source_and_unsafe_output(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            builder.build(self.root, self.root / "output")
        with self.assertRaisesRegex(ValueError, "overlap"):
            builder.build(self.root, self.root.parent)
        output = self.root.parent / "existing"
        output.mkdir()
        with self.assertRaisesRegex(ValueError, "already exists"):
            builder.build(self.root, output)
        self.append("[Broken](missing.md)")
        with self.assertRaisesRegex(ValueError, "missing.md"):
            builder.build(self.root, self.root.parent / "invalid")
        self.assertFalse((self.root.parent / "invalid").exists())

    def test_build_cli_and_strict_index_validation(self):
        shutil.copyfile(self.control, self.control.with_name("unlisted.md"))
        command = [sys.executable, str(REPOSITORY / "scripts/validate_catalog.py"), str(self.root)]
        result = subprocess.run(command + ["--require-index-coverage"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing directory index", result.stderr)
        output = self.root.parent / "cli-build"
        command = [sys.executable, str(REPOSITORY / "scripts/build_catalog.py"),
                   "--source", str(self.root), "--output", str(output)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS:", result.stdout)
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)

    def test_cli_exit_codes_and_diagnostics(self):
        command = [sys.executable, str(REPOSITORY / "scripts/validate_catalog.py"), str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS:", result.stdout)
        self.append("[Missing][ref]\n\n[ref]: missing.md")
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("controls/bounded-external-action.md:", result.stderr)
        self.assertNotIn("PASS:", result.stdout)


if __name__ == "__main__":
    unittest.main()
