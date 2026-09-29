---
type: Risk Scenario
title: "Poisoned memory influences later work"
description: "Adversary-controlled content is persisted as a preference, instruction, or summary and later reused."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: AML.T0080.000
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L3932
    title: "AML.T0080.000: Memory"
  - id: AML.CS0040
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L8518
    title: "AML.CS0040: Hacking ChatGPT's Memories with Prompt Injection"
  - id: AML.M0031
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6794
    title: "AML.M0031: Memory Hardening"
---

# Poisoned memory influences later work

[ATLAS assessment guide](../atlas-threat-assessment.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Identity:** `risks/poisoned-persistent-memory` · **Catalog:** v0.1.0

## Cause and enabling conditions

A supplier-comparison worker saves a preference embedded in a shared document. A new session applies that preference without consulting the original task owner. Automatic summaries and checkpoints can carry the same contamination.

## Threatened outcomes and affected parties

Persistent artifacts and fair, accurate comparisons are threatened. Decision owners, users sharing state, and evaluated suppliers may be affected.

## Candidate controls

- [Persistent memory admission](../controls/persistent-memory-admission.md) addresses this scenario by the following mechanism: mediates durable writes and retains origin.
- [Persistent state recovery](../controls/persistent-state-recovery.md) addresses this scenario by the following mechanism: quarantines and removes admitted contamination from dependent state.
- [Outcome verification](../controls/outcome-verification.md) addresses this scenario by the following mechanism: checks intended comparison outcomes without proving memory integrity.

These are applicability candidates, not adoption or effectiveness claims. The local factory owner records applicability, scope, assumptions, an assessment owner, and a reassessment trigger using the [adoption procedure](../adoption.md).

## Assessment example

Attempt to save a hostile fixture preference through retrieval and automatic summarization; compare with an authorized preference update. Inspect state and begin a fresh session. In a separate recovery fixture, seed contamination directly, then inspect restored memory and derived summaries. Retain revision lineage and fresh-session observations.

Evaluate each selected control using its own criteria. A forbidden effect is a failure; missing observations are inconclusive. This is a hypothetical fixture, with no local implementation or assessment asserted.

## Limits and reassessment

Admission can accept false content from an authorized writer. Restoring memory cannot undo decisions already made. Reassess when memory stores, sharing boundaries, or summarization processes change.

## Source basis

This scenario is a catalog interpretation informed by AML.T0080.000[^AML.T0080.000], AML.CS0040[^AML.CS0040], AML.M0031[^AML.M0031]. Source case studies illustrate reported conditions, not current vendor vulnerability status or local attack probability.

[^AML.T0080.000]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.CS0040]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.M0031]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
