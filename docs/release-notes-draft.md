# First stable major release — notes to finalize

Unpublished preparation. The baseline, version change, and publication remain
subject to explicit owner decisions. Replace unresolved statements with
candidate-bound evidence before using these notes in a GitHub Release.

## Supported use

The catalog supports humans, humans working with agents, and programs selecting,
implementing, and assessing individually applicable controls. It is distributed
as Markdown with YAML frontmatter, pinned to OKF 0.2, with generated navigation,
VERSION, and the unchanged project license. Reference and copied adoption retain
full source provenance and local adaptations.

The [consumer contract](../catalog/consumer-contract.md) covers published paths,
identities, requirements, assessment meanings, metadata, and structured records.
After the first stable major release, incompatible changes require a major
version; compatible additions require a minor version; clarifications preserving
implementations and assessments require a patch.

## Migration from pre-v1

Compare the exact previously adopted commit with the approved release, including
selected controls, dependencies, schema, and local adaptations. Preserve old
adoption records and reassess affected implementations. Do not infer compatibility
from pre-v1 version labels. The repository's current candidate is a held-version
readiness build from commit `7a91dad1a8e1850d8e8baa436532696f5f1f79b2` and is not
an approved baseline.

Observed pre-v1 changes relevant to the candidate:

- Compared with main `e01f0e70604ffa8d97a9ab3f4a6fc581603d9298`, eighty-eight
  draft concepts were moved out of `catalog/` into
  `docs/proposals/`. They are preserved in the source repository but are not in
  the distributed candidate. Consumers who adopted one of these drafts by its
  former bundle path should retain the old pinned commit, copied content, and
  adoption record, then compare against the [#48 disposition checklist](https://github.com/tclasen/factory_catalog/issues/48).
  Make a deliberate defer, adapt, or replacement decision; if recovering a
  proposal, review it at the exact candidate commit. A stable concept is not an
  automatic substitute, and the old path or draft semantics are not supported.
- The earlier PR #67 already retired the duplicate
  `catalog/guides/factory-work-record.md` path before that comparison revision;
  its consolidation rationale is recorded in the PR. Consumers referencing
  that pre-v1 path should inspect the current adoption guidance and compare
  their local procedure before updating.
- The candidate has 49 stable catalog concept documents. PR #68 also removed
  optional links to deferred drafts from stable guidance and repaired affected
  repository references. PR #69 corrected two stable controls' descriptions of
  private source access; the private source content is not part of their support
  basis.

## Compatibility classification for the held candidate

The comparison point `e01f0e70604ffa8d97a9ab3f4a6fc581603d9298` is a pre-v1
source revision, not a stable release. The exact comparison with held candidate
`7a91dad1a8e1850d8e8baa436532696f5f1f79b2` removes 88 catalog paths and modifies
six stable files. The 88 draft concepts remain in `docs/proposals/` and are not
included in the candidate bundle. If removal or movement of a published concept
path occurred after v1.0, the consumer contract classifies it as a major change.
These removals occurred before the first stable baseline, when compatibility is
not promised; v1.0.0 would establish the initial contract at the owner-selected
baseline rather than claim compatibility with the pre-v1 paths.

Four stable files remove optional links to deferred drafts:
`catalog/factories/learning.md`, `catalog/factories/software-delivery.md`,
`catalog/factory-implementation-tradeoffs.md`, and
`catalog/guides/durable-task-tracking.md`. Their instructions remain
self-contained. Two controls, `catalog/controls/assessment-evidence-validity.md`
and `catalog/controls/reconcile-before-retry.md`, clarify that private source
contents are not relied on as support; their requirements and assessment
criteria are unchanged. The duplicate factory work-record guide was retired
before the comparison revision. These changes do not establish an earlier
published catalog version; pre-v1 adopters should follow the exact-commit
migration guidance above.

These are observed pre-v1 tree changes, not a promise that any earlier commit
was compatible or published. As of 2026-09-29, the repository has no release
tags or GitHub Releases; a prior adopter may still have used an exact checkout.
The release issue must bind the final migration summary to the owner-selected
baseline and exact release commit, list any further moved, removed, consolidated,
deferred, or meaningfully revised concepts, and carry accepted limitations.

## Evidence and limitations to carry into publication

Evidence records: [catalog dispositions and content review](https://github.com/tclasen/factory_catalog/issues/48),
[candidate adoption exercises](https://github.com/tclasen/factory_catalog/issues/49),
and [qualification and package verification](https://github.com/tclasen/factory_catalog/issues/50).

For held candidate `7a91dad1a8e1850d8e8baa436532696f5f1f79b2`, the programmatic
consumer found 49 concepts and resolved 12 structured selections to stable
controls. The agent-only venue scenario found A too small for 14 people and B
conditional on supported Tuesday availability; it did not claim a booking or
meeting outcome. Both are candidate-bound machine/scenario evidence only.

At publication, link these records with the final checks, source commit, archive
checksum, and immutable release assets. State known source-access restrictions
and unresolved limitations. No human walkthroughs were performed for this
release; human usability has not been empirically validated. The programmatic
and agent-only exercises support machine-consumer and scenario review only.
The absence of human evidence and other known limitations must be visible in the
baseline decision and final release notes. The agent simulation does not
establish every control's operational effectiveness, exhaustive domain coverage,
or fitness for every deployment.

## Unresolved publication fields

- Owner-approved baseline and version; final integrated source commit.
- Final included concept dispositions are recorded in #48; the held-candidate
  pre-v1 migration classification is recorded above and in #50. Bind both to the
  owner-approved baseline and final release commit.
- Held-candidate archive SHA-256 is
  `ca95706bf4f79ad35effed132b38128889caa6da5cadabe1a9c7872d63604c4b`; it is a
  readiness artifact, not an approved baseline or release asset. Rebuild against
  the approved final commit after the VERSION PR is integrated.
- Candidate-bound programmatic consumer evidence and autonomous agent-only task
  simulation; repeat affected procedures if the selected candidate changes.
- Explicit acknowledgement that no human usability sessions were performed and
  human usability remains unvalidated.
- Known limitations accepted for that candidate.
- Final artifact verification and release URL.
