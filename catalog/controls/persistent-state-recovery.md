---
type: Control
title: "Persistent state recovery"
description: "Quarantine contaminated state and restore a declared clean revision across dependent stores."
status: stable
family: reliability-and-recovery
sources:
  - id: AML.M0031
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6794
    title: "AML.M0031: Memory Hardening"
---

# Persistent state recovery

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Restore usable state after contamination or unauthorized changes. Apply when a factory retains memory, summaries, retrieval indexes, caches, or checkpoints that can affect later work. Select independently from admission controls: prevention and restoration require different evidence.

## Requirement

Maintain a recovery procedure with an owner, recovery point and time objectives, protected recovery material, and a map of dependent state. On suspected contamination, prevent further use or propagation of affected state, preserve restricted incident evidence, and restore or rebuild from a justified clean revision. Resume only after validating active and derived state and recording unrecoverable work or data loss.

## Implementation

1. Inventory dependencies among memories, summaries, corpus entries, indexes, caches, and checkpoints; identify writers that can reintroduce contamination.
2. Define how a clean revision is selected, protected, and tested, including a rebuild option if no trusted snapshot exists.
3. Quiesce affected writers, quarantine active copies, and restore or rebuild all dependent state. Keep quarantined evidence outside normal retrieval.
4. Validate a fresh session and resumed jobs before reopening access. Record elapsed recovery, data loss, exceptions, and any missed recovery objective.

## Expected outcome and assessment

Expected outcome: the recovered factory can perform legitimate work without consuming the seeded contamination, within declared recovery objectives.

Seed a synthetic malicious preference and a derived summary/cache entry. Recover to the declared clean point while testing a concurrent writer or queued update. Open a fresh session, resume a checkpoint, and run a normal task. Also exercise the case where the proposed snapshot is itself contaminated.

**Pass:** contaminated state is inaccessible in tested active paths, legitimate work succeeds, unsafe snapshots are rejected, and recovery meets the declared time/data-loss criteria. **Fail:** contamination returns, validation is bypassed, an objective is missed, or normal work fails. **Inconclusive:** clean-state justification or dependent-store observations are unavailable.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires trustworthy recovery material, dependency lineage, and authority to stop writers. A rollback cannot undo information already disclosed or external actions already completed. [Persistent memory admission](persistent-memory-admission.md) and [retrieval corpus integrity](retrieval-corpus-integrity.md) reduce reinfection paths.

Addresses [poisoned persistent memory](../risks/poisoned-persistent-memory.md) and [retrieval poisoning](../risks/retrieval-poisoning.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0031[^AML.M0031]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0031]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
