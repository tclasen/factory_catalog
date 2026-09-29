#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Exercise release rejection paths, consumer changes, and provenance binding."""

import json
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

import release_catalog as release
import validate_catalog as validator


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.repo = self.root / "repository"
        self.source = self.repo / "catalog"
        shutil.copytree(release.REPOSITORY / "catalog", self.source)
        shutil.copyfile(release.REPOSITORY / "LICENSE", self.repo / "LICENSE")
        # Synthetic stable candidate tests release mechanics, never content maturity.
        for path in self.source.rglob("*.md"):
            path.write_text(path.read_text().replace("status: draft", "status: stable"))
        (self.repo / "scripts").mkdir()
        for name in release.TOOLS:
            shutil.copyfile(
                release.REPOSITORY / "scripts" / name, self.repo / "scripts" / name
            )
        self.control = self.source / "controls/bounded-external-action.md"

    def commit(self):
        for args in (
            ("init", "-q"),
            ("add", "."),
            (
                "-c",
                "user.name=Fixture",
                "-c",
                "user.email=fixture@example.invalid",
                "-c",
                "commit.gpgsign=false",
                "-c",
                "core.hooksPath=/dev/null",
                "commit",
                "-qm",
                "isolated synthetic test fixture",
            ),
        ):
            subprocess.run(
                ["git", "-C", str(self.repo), *args], check=True, capture_output=True
            )
        return release.git(self.repo, "rev-parse", "HEAD").decode().strip()

    def package(self):
        return release.package(self.repo, self.commit(), self.root / "release")

    def rewrite_sums(self, manifest):
        data = json.loads(manifest.read_text())
        archive = manifest.parent / data["archive"]
        data["sha256"] = release.digest(archive)
        manifest.write_text(json.dumps(data, indent=2) + "\n")
        (manifest.parent / "SHA256SUMS").write_text(
            f"{release.digest(archive)}  {archive.name}\n{release.digest(manifest)}  manifest.json\n"
        )

    def test_drafts_allowed_for_authoring_but_not_release(self):
        self.control.write_text(
            self.control.read_text().replace("status: stable", "status: draft")
        )
        self.assertEqual(validator.validate(self.source)[0], [])
        self.assertTrue(
            any(
                "release requires stable" in e
                for e in release.release_errors(self.source)
            )
        )

    def test_missing_optional_status_and_unknown_metadata_are_valid(self):
        self.control.write_text(
            self.control.read_text().replace(
                "status: stable\n", "x-consumer-note: optional\n"
            )
        )
        self.assertEqual(release.release_errors(self.source), [])

    def test_malformed_metadata_and_missing_dependency_block_release(self):
        original = self.control.read_text()
        self.control.write_text(original.replace("---\n", "---\ntype: Duplicate\n", 1))
        self.assertTrue(
            any("duplicate YAML" in e for e in release.release_errors(self.source))
        )
        self.control.write_text(original + "\n[required dependency](missing.md)\n")
        self.assertTrue(
            any("missing.md" in e for e in release.release_errors(self.source))
        )

    def test_invalid_selection_state_blocks_release(self):
        example = self.source / "factories/learning.md"
        example.write_text(
            example.read_text().replace(
                "assessment_result: not-assessed",
                "assessment_result: unknown-new-state",
            )
        )
        self.assertTrue(
            any(
                "invalid assessment_result" in e
                for e in release.release_errors(self.source)
            )
        )

    def test_missing_source_provenance_blocks_release(self):
        self.control.write_text(
            self.control.read_text().replace(
                "---\n", "---\nsources:\n  - id: absent\n", 1
            )
        )
        self.assertTrue(
            any("resource" in e for e in release.release_errors(self.source))
        )

    def test_compatible_addition_and_incompatible_identity_type_changes(self):
        baseline = self.root / "baseline"
        shutil.copytree(self.source, baseline)
        extra = self.source / "extra.md"
        extra.write_text(
            "---\ntype: Future Concept\ntitle: Extra\ndescription: Optional addition\n---\n\n# Extra\n"
        )
        self.assertEqual(release.compare(baseline, self.source), ([], []))
        shutil.copyfile(extra, baseline / "extra.md")
        extra.unlink()
        self.assertTrue(
            any(
                "removed published" in e
                for e in release.compare(baseline, self.source)[0]
            )
        )
        extra.write_text(
            (baseline / "extra.md")
            .read_text()
            .replace("Future Concept", "Changed Concept")
        )
        self.assertTrue(
            any(
                "changed document type" in e
                for e in release.compare(baseline, self.source)[0]
            )
        )

    def test_changed_record_schema_requires_semantic_review(self):
        baseline = self.root / "baseline"
        shutil.copytree(self.source, baseline)
        ontology = self.source / "ontology.md"
        ontology.write_text(
            ontology.read_text() + "\nA proposed mandatory record field.\n"
        )
        breaking, review = release.compare(baseline, self.source)
        self.assertEqual(breaking, [])
        self.assertTrue(any("ontology.md" in e for e in review))

    def test_exact_commit_roundtrip_and_deterministic_build(self):
        revision = self.commit()
        first = release.package(self.repo, revision, self.root / "first")
        second = release.package(self.repo, revision, self.root / "second")
        release.verify(self.repo, first)
        release.verify(self.repo, second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        manifest = json.loads(first.read_text())
        self.assertEqual(
            (first.parent / manifest["archive"]).read_bytes(),
            (second.parent / manifest["archive"]).read_bytes(),
        )
        with self.assertRaisesRegex(ValueError, "already exists"):
            release.package(self.repo, revision, first.parent)

    def test_working_tree_changes_cannot_enter_committed_archive(self):
        revision = self.commit()
        self.control.write_text("uncommitted invalid replacement")
        (self.source / "untracked.txt").write_text("must not be included")
        manifest = release.package(self.repo, revision, self.root / "release")
        release.verify(self.repo, manifest)
        data = json.loads(manifest.read_text())
        with zipfile.ZipFile(manifest.parent / data["archive"]) as archive:
            self.assertNotIn("catalog/untracked.txt", archive.namelist())
            self.assertNotIn(
                b"uncommitted",
                archive.read("catalog/controls/bounded-external-action.md"),
            )

    def test_missing_or_forged_provenance_is_rejected(self):
        manifest = self.package()
        original = json.loads(manifest.read_text())
        data = dict(original)
        del data["source_commit"]
        manifest.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "provenance"):
            release.verify(self.repo, manifest)
        data = dict(original, catalog_version="v9.9.9")
        manifest.write_text(json.dumps(data))
        self.rewrite_sums(manifest)
        with self.assertRaisesRegex(ValueError, "version does not match"):
            release.verify(self.repo, manifest)

    def test_tampered_archive_fails_even_with_recomputed_checksums(self):
        manifest = self.package()
        data = json.loads(manifest.read_text())
        archive_path = manifest.parent / data["archive"]
        original = archive_path.read_bytes()
        for mutation in ("extra", "missing", "changed"):
            with self.subTest(mutation=mutation):
                archive_path.write_bytes(original)
                with zipfile.ZipFile(archive_path) as archive:
                    entries = [
                        (info, archive.read(info)) for info in archive.infolist()
                    ]
                with zipfile.ZipFile(archive_path, "w") as archive:
                    for info, content in entries:
                        if info.filename == "catalog/LICENSE":
                            if mutation == "missing":
                                continue
                            if mutation == "changed":
                                content += b"tampered"
                        archive.writestr(info, content)
                    if mutation == "extra":
                        archive.writestr("catalog/extra.txt", "unqualified")
                self.rewrite_sums(manifest)
                with self.assertRaisesRegex(ValueError, "complete rebuilt source"):
                    release.verify(self.repo, manifest)

    def test_moving_ref_and_mismatched_tooling_are_rejected(self):
        revision = self.commit()
        with self.assertRaisesRegex(ValueError, "full 40-character"):
            release.package(self.repo, "HEAD", self.root / "release")
        script = self.repo / "scripts/build_catalog.py"
        script.write_text(script.read_text() + "\n# changed build behavior\n")
        revision = self.commit()
        with self.assertRaisesRegex(ValueError, "tooling from the requested commit"):
            release.package(self.repo, revision, self.root / "release")


if __name__ == "__main__":
    unittest.main()
