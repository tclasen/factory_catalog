#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Regression tests for catalog validation; run directly with uv on PATH."""

from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import review_catalog as reviewer
import check_catalog as checker

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
        shutil.copyfile(REPOSITORY / "LICENSE", self.root.parent / "LICENSE")
        self.control = self.root / "controls/bounded-external-action.md"

    def append(self, text):
        self.control.write_text(self.control.read_text() + "\n" + text, encoding="utf-8")

    def errors(self):
        return validator.validate(self.root)[0]

    def test_examples_do_not_require_contributor_taxonomy(self):
        self.assertFalse((self.root / "work-types.md").exists())
        self.assertFalse((self.root.parent / "docs").exists())
        example = self.root / "factories/learning.md"
        text = example.read_text()
        example.write_text(re.sub(r"activities: .*", 'activities: ["assess a new community mediation exercise"]', text))
        self.assertEqual(self.errors(), [])
        output = self.root.parent / "standalone"
        builder.build(self.root, output)
        self.assertEqual(validator.validate(output, require_index_coverage=True)[0], [])
        self.assertFalse((output / "work-types.md").exists())
        self.assertFalse((output / "research").exists())

    def test_example_activity_descriptions_are_required(self):
        example = self.root / "factories/learning.md"
        original = example.read_text()
        for value in ('[]', '[""]', '[42]', '"teaching"', 'null'):
            with self.subTest(value=value):
                example.write_text(re.sub(r"activities: .*", "activities: " + value, original))
                self.assertTrue(any("activities must" in e for e in self.errors()))
        example.write_text(original.replace("activities:", "work_types:"))
        self.assertTrue(any("replace work_types" in e for e in self.errors()))
        example.write_text(original.replace("../controls/outcome-verification.md", "../adoption.md"))
        self.assertTrue(any("selection does not reference a Control" in e for e in self.errors()))

    def test_duplicate_yaml_keys(self):
        for field in ("family: bogus\n", "sources:\n  - resource: a\n    resource: b\n"):
            with self.subTest(field=field):
                original = self.control.read_text()
                self.control.write_text(original.replace("---\n", "---\n" + field, 1))
                self.assertTrue(any("duplicate YAML key" in error for error in self.errors()))
                self.control.write_text(original)

    def source_errors(self, sources, body=""):
        doc = validator.Document(self.control, body, {"sources": sources}, True)
        return validator.validate_sources(self.root, doc, {})

    def test_source_records(self):
        for sources, message in (({}, "sources must"), (["bad"], "mapping"),
                                 ([{}], "resource"), ([{"resource": "x", "id": 2}], "id must"),
                                 ([{"resource": "x", "id": "a"}] * 2, "duplicate source")):
            with self.subTest(sources=sources):
                self.assertTrue(any(message in error for error in self.source_errors(sources)))
        self.assertEqual(self.source_errors([{"resource": "all queries in project X"},
                                             {"resource": "https://example.com/a"}]), [])

    def test_local_source_integrity(self):
        self.assertEqual(self.source_errors([{"resource": "../adoption.md"}]), [])
        for resource in ("../missing-research.md", "../../README.md"):
            self.assertTrue(any("out-of-bundle link" in error for error in
                                self.source_errors([{"resource": resource}])))

    def test_keyed_footnotes(self):
        sources = [{"id": "research", "resource": "https://example.com"}]
        body = "Claim.[^research]\n\n[^research]: Evidence."
        self.assertEqual(self.source_errors(sources, body), [])
        self.assertTrue(any("undefined footnote" in error for error in self.source_errors(sources, "Claim.[^research]")))
        self.assertTrue(any("no matching source" in error for error in self.source_errors([], body)))
        self.assertTrue(any("duplicate footnote" in error for error in
                            self.source_errors(sources, body + "\n\n[^research]: Again.")))
        self.assertEqual(self.source_errors([], "`[^missing]`\n\n```md\n[^missing]\n\n[^missing]: Example\n```"), [])

    def test_parsed_heading_anchors(self):
        body = "```md\n## Phantom\n```\n\nReal heading\n------------\n\n## A *formatted* `heading`\n## Repeat\n## Repeat\n## Repeat-1\n"
        self.assertEqual(validator.extract_heading_anchors(body),
                         ["real-heading", "a-formatted-heading", "repeat", "repeat-1", "repeat-1-1"])
        self.append("[Phantom](#phantom)\n\n```md\n## Phantom\n```")
        self.assertTrue(any("missing heading" in error for error in self.errors()))

    def test_distribution_integrity(self):
        output = self.root.parent / "distribution"
        builder.build(self.root, output)
        self.assertEqual(builder.validate_distribution(self.root, output), [])
        (output / "LICENSE").unlink()
        index = output / "index.md"
        index.write_text(index.read_text().replace("(controls/bounded-external-action.md)", "(controls/outcome-verification.md)"))
        listing = output / "controls/index.md"
        listing.write_text(listing.read_text().replace("[status:", "[maturity:"))
        errors = builder.validate_distribution(self.root, output)
        for message in ("LICENSE", "family navigation", "show status"):
            self.assertTrue(any(message in error for error in errors), errors)

    def test_review_is_advisory_and_remote_lookup_is_optional(self):
        self.append("Pending proposal https://github.com/tclasen/factory_catalog/pull/99999")
        with patch.object(reviewer.subprocess, "run") as run:
            findings = reviewer.review(self.root)
            run.assert_not_called()
        self.assertTrue(any("live state not checked" in finding for finding in findings))
        with patch.object(reviewer.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, '{"state":"closed","merged_at":"2026-01-01"}')):
            self.assertTrue(any("state merged" in finding for finding in reviewer.review(self.root, github=True)))
        with patch.object(reviewer.subprocess, "run", side_effect=OSError("offline")):
            self.assertTrue(any("unavailable" in finding for finding in reviewer.review(self.root, github=True)))
        # The warning test must not depend on defects remaining in production content.
        shutil.copyfile(self.control, self.control.with_name("overlapping-fixture.md"))
        self.assertTrue(any("overlapping controls" in finding for finding in reviewer.review(self.root)))

    def test_missing_repository_license_blocks_build(self):
        (self.root.parent / "LICENSE").unlink()
        with self.assertRaisesRegex(ValueError, "LICENSE"):
            builder.build(self.root, self.root.parent / "unlicensed")

    def test_absent_status_defaults_to_stable(self):
        self.control.write_text(re.sub(r"^status:.*\n", "", self.control.read_text(), flags=re.MULTILINE))
        output = self.root.parent / "default-status"
        builder.build(self.root, output)
        listing = output / "controls/index.md"
        self.assertIn("[status: stable;", next(line for line in listing.read_text().splitlines()
                                             if "](bounded-external-action.md)" in line))
        listing.write_text(listing.read_text().replace("[status: stable;", "[status: unspecified;"))
        self.assertTrue(any("show status" in error for error in builder.validate_distribution(self.root, output)))

    def test_generated_links_encode_filenames(self):
        directory = self.root / "guides" / "space # % (é)"
        directory.mkdir(parents=True)
        name = "guide # % (é).md"
        (directory / name).write_text(
            "---\ntype: Guide\ntitle: Guide\ndescription: Example\n---\n# Guide\n"
        )
        shutil.copyfile(self.control, self.control.with_name(name))
        output = self.root.parent / "encoded-links"
        builder.build(self.root, output)
        self.assertEqual(validator.validate(output, require_index_coverage=True)[0], [])
        self.assertEqual(builder.validate_distribution(self.root, output), [])
        listing = output / "controls/index.md"
        self.assertIn("guide%20%23%20%25%20%28%C3%A9%29.md", listing.read_text())
        listing.write_text("\n".join(line for line in listing.read_text().splitlines()
                                   if "guide%20" not in line) + "\n")
        self.assertTrue(any("unlisted entry" in error for error in
                            validator.validate(output, require_index_coverage=True)[0]))

    def test_review_reports_invalid_selection_without_traceback(self):
        example = self.root / "factories/research.md"
        example.write_text(re.sub(r"control_selections:\n(?:[ \t].*\n)+", "control_selections: null\n",
                                  example.read_text()))
        result = subprocess.run([sys.executable, str(REPOSITORY / "scripts/review_catalog.py"), str(self.root)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing control selections", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_whitespace_in_clean_checkout_and_staged_changes(self):
        repo = self.root.parent / "git-fixture"
        repo.mkdir()

        def git(*args):
            return subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=repo,
                                  check=True, capture_output=True, text=True)

        git("init")
        document = repo / "document.md"
        document.write_text("bad trailing space \n")
        git("add", ".")
        git("-c", "commit.gpgsign=false", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
            "commit", "-m", "Whitespace fixture")
        self.assertEqual(git("status", "--porcelain").stdout, "")
        self.assertNotEqual(checker.check_whitespace(repo), 0)
        document.write_text("clean\n")
        git("add", ".")
        self.assertEqual(checker.check_whitespace(repo), 0)
        document.write_text("staged error \n")
        git("add", ".")
        document.write_text("clean\n")
        self.assertNotEqual(checker.check_whitespace(repo), 0)

    def test_check_command_propagates_failure(self):
        with patch.object(sys, "argv", ["check_catalog.py"]), patch.object(
            checker.subprocess, "run", return_value=subprocess.CompletedProcess([], 7)
        ) as run:
            self.assertEqual(checker.main(), 7)
            self.assertEqual(run.call_count, 1)
        with patch.object(sys, "argv", ["check_catalog.py"]), patch.object(
            checker.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)
        ), patch.object(checker, "check_whitespace", return_value=2):
            self.assertEqual(checker.main(), 2)

    def test_current_catalog(self):
        self.assertEqual(self.errors(), [])

    def test_version_change_needs_only_one_source_edit(self):
        baseline = self.snapshot(self.root)
        version = self.root / "VERSION"
        version.write_text("v2.3.4-rc.1+test.7\n")
        self.assertEqual(self.errors(), [])
        output = self.root.parent / "version-build"
        builder.build(self.root, output)
        self.assertEqual({path for path, data in self.snapshot(self.root).items()
                          if baseline.get(path) != data}, {Path("VERSION")})
        self.assertEqual((output / "VERSION").read_bytes(), version.read_bytes())
        self.assertEqual((output / self.control.relative_to(self.root)).read_bytes(),
                         self.control.read_bytes())
        for replacement in ("v9.0.0\n", None):
            if replacement is None:
                (output / "VERSION").unlink()
            else:
                (output / "VERSION").write_text(replacement)
            self.assertTrue(any("VERSION" in error for error in
                                builder.validate_distribution(self.root, output)))

    def test_invalid_or_missing_bundle_version(self):
        version = self.root / "VERSION"
        for value in ("", "v01.2.3\n", "v1.2\n", "v1.2.3\nv2.0.0\n",
                      "v1.2.3-01\n", "v1.2.3+\n", " v1.2.3\n"):
            with self.subTest(value=value):
                version.write_text(value)
                self.assertTrue(any("VERSION:" in error for error in self.errors()))
        version.unlink()
        self.assertTrue(any("VERSION: cannot read" in error for error in self.errors()))

    def test_reject_duplicate_bundle_metadata_and_summary_headers(self):
        original = self.control.read_text()
        self.control.write_text(original.replace("---\n", "---\ncatalog_version: v9.0.0\n", 1))
        self.assertTrue(any("catalog_version belongs only" in error for error in self.errors()))
        self.control.write_text(original)
        self.append("```md\n**Identity:** `example`\n```")
        self.assertEqual(self.errors(), [])
        self.append("**Identity:** `controls/stale-name` · **Family:** `stale-family`")
        self.assertTrue(any("do not repeat summary headers" in error for error in self.errors()))

    def test_family_change_needs_no_body_summary_update(self):
        original = self.control.read_text()
        self.control.write_text(re.sub(r"^family:.*$", "family: quality-and-validation",
                                       original, flags=re.MULTILINE))
        self.assertEqual(self.errors(), [])
        output = self.root.parent / "family-build"
        builder.build(self.root, output)
        listing = (output / "controls/index.md").read_text()
        entry = next(line for line in listing.splitlines() if "](bounded-external-action.md)" in line)
        self.assertIn("family: quality-and-validation", entry)

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
            '---\n\n# A guide\n\nNew guidance.\n'
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
