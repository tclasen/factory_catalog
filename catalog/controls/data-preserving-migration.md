---
type: Control
title: "Data-preserving migration"
description: "Verify compatibility, concurrent writes, and recovery before changing durable data or active interfaces."
catalog_version: "v0.1.0"
status: stable
family: change-and-dependencies
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/migrations.md
    title: "Software Factory: Data-preserving migration basis"
---

# Data-preserving migration

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

**Identity:** `controls/data-preserving-migration` · **Catalog:** v0.1.0 · **Family:** `change-and-dependencies`

## Purpose and applicability

Apply when changing durable data representations or interfaces with active consumers. Prevent cutover, backfill, or rollback from losing acknowledged data or silently breaking consumers.

## Requirement

Before mutation, identify semantic invariants, authoritative representations, affected consumers, coexistence requirements, cutover criteria, and recovery limits. Verify representative transitions, interruption, and concurrent writes before exposure. Remove old representations only after authorized removal conditions are satisfied. Recovery must preserve acknowledged changes and applicable deletion/retention obligations; an old snapshot is not automatically a safe rollback.

## Implementation

1. Assign data and cutover owners; inspect contracts, migration history, consumers, and meaning that cannot be inferred mechanically.
2. Define the compatibility window and accepted invariants. Use expand, backfill, verify/cutover, and contract stages where appropriate, or justify an alternative.
3. Bound batches, resource use, locks, and retries. Use durable progress markers and conflict handling so stale backfill cannot overwrite newer writes.
4. Reconcile rejected records and changes made during migration. Compare semantic values and relationships as well as counts.
5. Rehearse supported recovery, identify irreversible points and forward-repair options, then check current authority, destination, evidence, and monitoring before production action.

## Expected outcome and assessment

Expected outcome: the declared migration preserves acknowledged information and supported consumer behavior, or blocks unsafe cutover.

Use synthetic or authorized sanitized fixtures with known invariants. Exercise old/new readers and writers, interrupted/resumed backfill, duplicate batches, a concurrent update, invalid records, and recovery after a new-version write. Test attempted early removal of an old interface.

- **Pass:** supported consumers and semantic invariants hold; no newer acknowledged value is overwritten; retries converge without duplication; rejected records are accounted for; unsafe rollback and premature removal are blocked.
- **Fail:** data is silently dropped or altered, supported consumers lose their required contract, or recovery discards acknowledged changes. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** representative data, consumer behavior, or recovery effects cannot be inspected.
- **Evidence:** contract/invariant revisions, fixture identities, stage observations, reconciliation totals, concurrent-write traces, recovery results, cutover/removal decisions, owners and times.

## Dependencies and limitations

Requires maintained migration tooling with verified transaction and resume semantics. Use [assessment evidence validity](assessment-evidence-validity.md), [reconcile before retry](reconcile-before-retry.md), and [bounded external action](bounded-external-action.md). Representative tests do not establish production capacity or every domain interpretation. Any untested load or irreversible recovery limitation must remain explicit.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/migrations.md).
