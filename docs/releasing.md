# Qualify and publish a catalog release

[Contribution policy](../CONTRIBUTING.md#4-classify-the-version-impact) governs
baseline approval, signing, review, merge, and publication. This procedure creates
reviewable artifacts; running a command does not grant release authority.

## Readiness evidence

Use the release issue and PRs as the work record. Review every concept, including
already-stable ones, for adopter usefulness, distinct meaning, complete and
assessable requirements, supported claims, and usable dependencies. Record a
retain, revise, consolidate, or defer disposition with its reason. Review edits
before promoting lifecycle status; never bulk-refresh verification timestamps.

Keep unfinished proposals under `docs/proposals/`, preserving source attribution
and repairing links. No released concept may depend on deferred material. The
release bundle must contain only stable concepts; ordinary source validation
continues to permit drafts. A source marked stable still needs release review.

Use the [consumer contract](../catalog/consumer-contract.md) to review compatibility.
Automation checks structural compatibility and reports normative text changes for
review; it cannot decide whether two requirements mean the same thing.

Use the [candidate adoption exercises](release-walkthroughs.md) and
[draft release notes](release-notes-draft.md). Record candidate-bound evidence
from a programmatic consumer and an autonomous agent-only task simulation.
Together they should cover by-reference and copied adoption, cross-control
dependencies, missing evidence, failed criteria, unavailable dependencies, and
interrupted handoff. These exercises support a scoped assessment of machine
consumption and scenario execution; they do not establish empirical human
usability or control effectiveness. Live human adoption sessions are not a 1.0
release gate. State clearly when they were not performed, and do not describe
human usability as validated.

## Check and package

Stage new files and run `./scripts/check_catalog.py --github` and `git diff --check`.
Review all advisory findings and changed external sources. Then run:

```sh
./scripts/release_catalog.py check
./scripts/release_catalog.py compare --baseline /path/to/previous/catalog
```

The comparison command requires a previous stable release for later releases;
there is no published compatibility baseline for the first major release.
Its structural findings block acceptance until given the proper version impact;
changed prose still requires review. Record semantic decisions in the PR.

After signed commit publication, package that exact full commit SHA:

```sh
./scripts/release_catalog.py package --revision FULL_COMMIT_SHA --output build/release-candidate
./scripts/release_catalog.py verify build/release-candidate/manifest.json
```

Use a new output directory. Packaging reads committed content and tooling at the
specified revision, includes generated indexes and the unchanged VERSION and
LICENSE, and writes a deterministic ZIP, an external provenance manifest, and
SHA256SUMS. Verification rebuilds from the stated commit and compares the complete
archive before validating extracted navigation. A candidate may still carry the
held pre-v1 version; never describe it as a published major release.

The manifest is distribution provenance, not a concept-discovery API. It binds
source SHA, catalog version, archive filename, and SHA-256. Keep it with the bundle.
No release command publishes, changes VERSION, creates tags, or approves a gate.

## Owner decision and publication

Present the reviewed content, compatibility contract, walkthrough evidence,
checks, archive identity, known limitations, migration effects, and release notes
to the owner. Obtain explicit approval of the selected baseline and VERSION
change. Publish that version change through a tested, signed PR. Merge requires
its own authorization and current review/check verification.

After authorized integration, rerun required checks and packaging against the
final integrated commit. Any relevant change invalidates affected earlier evidence.
Obtain release publication authorization identifying the final version and commit;
confirm the version tag and release do not already exist. Create the tag and
GitHub Release at that exact commit and upload the ZIP, manifest, and SHA256SUMS.
Never overwrite published tags or assets. On an ambiguous response, inspect the
remote tag, release, and assets before retrying.

Download the published assets into a fresh directory, run verification, and
confirm the remote tag resolves to the approved commit. Retain the release URL,
checksums, checks, signature evidence, and any remaining limitations in the issue.
Do not close readiness merely because an archive built successfully.
