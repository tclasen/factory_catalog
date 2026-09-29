#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3", "markdown-it-py==4.0.0", "mdit-py-plugins==0.5.0"]
# ///
"""Check release candidates and package/verify exact committed catalog revisions.

This tool never approves, tags, or publishes a release. Semantic compatibility,
source support, and actual adoption usability remain review gates.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import build_catalog as builder
import validate_catalog as validator

REPOSITORY = Path(__file__).resolve().parent.parent
TOOLS = ("release_catalog.py", "build_catalog.py", "validate_catalog.py")


def release_errors(source: Path) -> list[str]:
    source = source.resolve()
    errors, _ = validator.validate(source)
    documents, _ = validator.load_documents(source)
    for path, doc in documents.items():
        if (
            path.name not in ("index.md", "log.md")
            and doc.metadata.get("status", "stable") != "stable"
        ):
            errors.append(
                f"{path.relative_to(source)}: release requires stable lifecycle status"
            )
    for name in (
        "ontology.md",
        "adoption.md",
        "consumer-contract.md",
        "control-families.md",
    ):
        if source / name not in documents:
            errors.append(f"{name}: missing consumer entry contract")
    return errors


def compare(baseline: Path, candidate: Path) -> tuple[list[str], list[str]]:
    """Detect structural breaks; prose changes always need a semantic decision."""
    baseline, candidate = baseline.resolve(), candidate.resolve()
    for root in (baseline, candidate):
        errors, _ = validator.validate(root)
        if errors:
            raise ValueError("\n".join(errors))
    before, _ = validator.load_documents(baseline)
    after, _ = validator.load_documents(candidate)
    breaking, review = [], []
    for path, old in before.items():
        if path.name in ("index.md", "log.md"):
            continue
        identity = path.relative_to(baseline)
        new = after.get(candidate / identity)
        if new is None:
            breaking.append(f"{identity}: removed published identity")
            continue
        for key in ("type", "family"):
            if old.metadata.get(key) != new.metadata.get(key):
                # Conservative: classification changes may be compatible after review.
                review.append(
                    f"{identity}: changed {key}; review meaning and consumers"
                )
                if key == "type":
                    breaking.append(f"{identity}: changed document type")
        if old.body != new.body:
            review.append(
                f"{identity}: changed prose; review requirements, assessments, and record schema"
            )
        if old.metadata.get("control_selections") != new.metadata.get(
            "control_selections"
        ):
            review.append(
                f"{identity}: changed selection records; review states and meaning"
            )
        other_keys = (set(old.metadata) | set(new.metadata)) - {
            "type",
            "family",
            "control_selections",
        }
        for key in sorted(other_keys):
            if old.metadata.get(key) != new.metadata.get(key):
                review.append(
                    f"{identity}: changed metadata {key}; review consumer impact"
                )
    old_families = set(
        validator.extract_vocabulary(before.get(baseline / "control-families.md"))
    )
    new_families = set(
        validator.extract_vocabulary(after.get(candidate / "control-families.md"))
    )
    for family in sorted(old_families - new_families):
        breaking.append(f"removed family value: {family}")
    return breaking, review


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError(result.stderr.decode(errors="replace").strip())
    return result.stdout


def snapshot(repository: Path, revision: str, destination: Path) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("revision must be a full 40-character commit SHA")
    actual = (
        git(repository, "rev-parse", "--verify", revision + "^{commit}")
        .decode()
        .strip()
    )
    if actual != revision:
        raise ValueError("revision must identify the commit itself")
    for entry in git(
        repository, "ls-tree", "-rz", revision, "--", "catalog", "LICENSE", "scripts"
    ).split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        mode, kind, blob = metadata.split()
        path = raw_path.decode("utf-8")
        if kind != b"blob" or mode not in (b"100644", b"100755"):
            raise ValueError(f"unsupported source entry: {path}")
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(git(repository, "cat-file", "blob", blob.decode()))
    for name in TOOLS:
        expected = destination / "scripts" / name
        if (
            not expected.is_file()
            or expected.read_bytes() != (REPOSITORY / "scripts" / name).read_bytes()
        ):
            raise ValueError(
                f"run packaging tooling from the requested commit: scripts/{name}"
            )


def archive_bundle(bundle: Path, archive: Path) -> None:
    """Stable ordering, paths, permissions, timestamps, and uncompressed bytes."""
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_STORED) as output:
        for path in sorted(bundle.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"symlink is not a release file: {path}")
            if not path.is_file():
                continue
            entry = zipfile.ZipInfo(
                "catalog/" + path.relative_to(bundle).as_posix(), (1980, 1, 1, 0, 0, 0)
            )
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            output.writestr(entry, path.read_bytes())


def build_revision(
    repository: Path, revision: str, temporary: Path
) -> tuple[Path, str]:
    checkout = temporary / "source"
    checkout.mkdir()
    snapshot(repository, revision, checkout)
    source = checkout / "catalog"
    errors = release_errors(source)
    if errors:
        raise ValueError("\n".join(errors))
    bundle = temporary / "bundle"
    builder.build(source, bundle)
    return bundle, (source / "VERSION").read_text().strip()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package(repository: Path, revision: str, output: Path) -> Path:
    if output.exists():
        raise ValueError("output directory already exists; choose a new directory")
    with tempfile.TemporaryDirectory() as name:
        bundle, version = build_revision(repository, revision, Path(name).resolve())
        archive_name = f"factory-catalog-{version}-{revision[:12]}.zip"
        archive = Path(name) / archive_name
        archive_bundle(bundle, archive)
        manifest = {
            "format": 1,
            "source_commit": revision,
            "catalog_version": version,
            "archive": archive_name,
            "sha256": digest(archive),
        }
        output.mkdir(parents=True)
        (output / archive_name).write_bytes(archive.read_bytes())
        manifest_path = output / "manifest.json"
        manifest_path.write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        (output / "SHA256SUMS").write_text(
            f"{manifest['sha256']}  {archive_name}\n{digest(manifest_path)}  manifest.json\n",
            encoding="utf-8",
        )
    return manifest_path


def verify(repository: Path, manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    keys = {"format", "source_commit", "catalog_version", "archive", "sha256"}
    if (
        not isinstance(manifest, dict)
        or set(manifest) != keys
        or manifest["format"] != 1
    ):
        raise ValueError("invalid or incomplete provenance manifest")
    if not all(isinstance(manifest[k], str) for k in keys - {"format"}):
        raise ValueError("manifest provenance fields must be strings")
    archive_name = manifest["archive"]
    if not re.fullmatch(r"[A-Za-z0-9.+_-]+\.zip", archive_name):
        raise ValueError("archive must be a local ZIP filename")
    archive = manifest_path.parent / archive_name
    if digest(archive) != manifest["sha256"]:
        raise ValueError("archive checksum mismatch")
    expected_sums = (
        f"{digest(archive)}  {archive_name}\n{digest(manifest_path)}  manifest.json\n"
    )
    if (manifest_path.parent / "SHA256SUMS").read_text() != expected_sums:
        raise ValueError("SHA256SUMS mismatch")
    with tempfile.TemporaryDirectory() as name:
        temporary = Path(name).resolve()
        bundle, version = build_revision(
            repository, manifest["source_commit"], temporary
        )
        if version != manifest["catalog_version"]:
            raise ValueError("manifest version does not match source revision")
        rebuilt = temporary / "expected.zip"
        archive_bundle(bundle, rebuilt)
        if archive.read_bytes() != rebuilt.read_bytes():
            raise ValueError("archive does not match complete rebuilt source revision")
        # Extract only after exact comparison to our generated, confined archive.
        extracted = temporary / "extracted"
        with zipfile.ZipFile(archive) as package_file:
            package_file.extractall(extracted)
        errors, _ = validator.validate(
            extracted / "catalog", require_index_coverage=True
        )
        errors.extend(
            builder.validate_distribution(
                temporary / "source/catalog", extracted / "catalog"
            )
        )
        if errors:
            raise ValueError("\n".join(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser(
        "check", help="check a stable-only candidate, without release approval"
    )
    check.add_argument("--source", type=Path, default=REPOSITORY / "catalog")
    comparison = commands.add_parser(
        "compare", help="flag compatibility changes for review"
    )
    comparison.add_argument("--baseline", type=Path, required=True)
    comparison.add_argument("--source", type=Path, default=REPOSITORY / "catalog")
    packing = commands.add_parser(
        "package", help="package an exact committed candidate"
    )
    packing.add_argument("--revision", required=True)
    packing.add_argument("--output", type=Path, required=True)
    verification = commands.add_parser(
        "verify", help="rebuild and compare a package using local Git history"
    )
    verification.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "check":
            errors = release_errors(args.source)
            if errors:
                raise ValueError("\n".join(errors))
            print(
                "PASS: stable-only release structure; content and adoption review still required."
            )
        elif args.command == "compare":
            breaking, review = compare(args.baseline, args.source)
            for line in breaking:
                print("BREAKING: " + line)
            for line in review:
                print("REVIEW: " + line)
            if breaking or review:
                print(
                    "Compatibility decision required; no semantic compatibility pass is asserted."
                )
                return 1
            print(
                "PASS: no detected structural or body changes; review additional metadata and release scope."
            )
        elif args.command == "package":
            manifest = package(REPOSITORY, args.revision, args.output.resolve())
            verify(REPOSITORY, manifest)
            print(
                f"PASS: packaged and verified {manifest}; release remains unapproved."
            )
        else:
            verify(REPOSITORY, args.manifest.resolve())
            print(
                "PASS: archive, provenance, complete source correspondence, and extracted navigation."
            )
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
