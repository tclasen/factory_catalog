# Parallel OKF authoring

## Decision

Keep independently maintained knowledge in concept files at their existing paths. Treat checked-in indexes as curated navigation, and derive complete indexes in an untracked distribution copy. Use Git and PR history for ongoing change records. Preserve existing log entries and entry-point paths.

The owner's request is to remove merge conflicts caused by routine OKF maintenance when agents submit independent PRs. Previously every addition required editing its directory index, and changes accumulated under the same date in the shared log. These edits created conflicts even when the underlying concepts were independent.

## Format and implementation

The pinned OKF 0.2 specification permits generated indexes (§8), makes indexes and logs optional (§§3, 9), and defines concept identity by path (§2). No format upgrade or domain-schema change is needed.

- `catalog/` remains the authored bundle. Its indexes are curated entry points rather than exhaustive inventories. File scanning is authoritative for source discovery.
- `scripts/build_catalog.py` copies the bundle, preserves index prose, and appends sorted listings from concept metadata. It generates missing indexes at intermediate directory levels and validates the complete output.
- `build/` is ignored. A build without `--output` uses a temporary directory. Retained output requires a new destination so a build cannot overwrite authored work or preserve stale files from an earlier build.
- Source validation still checks structure, metadata, links, and control content. Exhaustive index coverage is required for generated distributions with `--require-index-coverage`.
- `catalog/log.md` retains earlier entries. PR descriptions hold change rationale, version impact, and validation evidence; Git records content history. A plain archive does not include the full Git/PR history.

This avoids a generated-file commit after every content PR, a new shared manifest, or merge drivers that silently combine conflicting prose. CI builds from the tree being checked with read-only repository permissions.

## Compatibility and limits

Existing concept identities, control requirements, source URLs, and reserved entry-point paths are preserved. Intended version impact is patch for tooling and workflow; the v0.1.0 baseline hold remains in force. No release is approved by this decision.

Source consumers that assumed an exhaustive index must scan concept files or use the generated bundle. Curated links still require maintenance when their target is deliberately moved or removed. Changes to the same concept, taxonomy, schema, or navigation design still need coordination. Parallel branches must be checked again against the combined tree before merge, including semantic review of relationships and dependencies.

Regression coverage checks that two additions can each touch only their own file and both appear in the combined generated index. It also checks nested discovery, deterministic builds, source preservation, rejected unsafe destinations, and continued rejection of invalid source content.

## Evidence from open PRs

On 2026-09-28, inspection of [PR #8](https://github.com/tclasen/factory_catalog/pull/8), [PR #10](https://github.com/tclasen/factory_catalog/pull/10), and [PR #11](https://github.com/tclasen/factory_catalog/pull/11) confirmed that all three edit `catalog/index.md` and `catalog/log.md`. Local Git merge-tree checks against `origin/main` reported log conflicts for all three and an index conflict for #10. #11 also adds an entry to the factory index. These are independent additions forced through common navigation and history files.

The diffs also expose optional reciprocal-link edits: #8 appends related guidance to all three controls, and #10 adds guide pointers to adoption, control families, and the research example. New guidance should own its outgoing relationships. Existing targets should change only when their substantive content needs revision.

To migrate an already-open PR after this workflow lands, update its branch against the default branch, retain its new concepts and substantive edits, and drop obsolete inventory/log additions. Move any unique decision or provenance text out of discarded log entries into the concept or PR description. Review each reciprocal-link edit separately; retain it only if it contributes a necessary substantive change. Then run source validation, the generated-bundle check, and regression tests. Merely merging this workflow does not resolve conflicts already present in other branches.
