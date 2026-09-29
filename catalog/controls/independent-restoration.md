---
type: Control
title: "Independent restoration"
description: "Demonstrate restoration from the claimed backup while preserving acknowledged changes and deletion obligations."
status: draft
family: reliability-and-recovery
sources:
  - id: workflows-operations
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md
    title: "Operations, maintenance and retirement"
---

# Independent restoration

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^workflows-operations] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when a factory relies on backups to recover durable data or service state.

## Requirement

Define required recovery inputs, targets, and acknowledged changes before testing. Restore from the claimed backup location without relying on surviving primary data or caches. Verify restored integrity and replay or otherwise preserve required corrections and deletion obligations. Missing required history blocks activation; the existence of backup files is insufficient evidence.

## Implementation

1. Inventory required data, configuration, correction/deletion history, backup identity, access controls, and recovery objectives.
2. Use an authorized isolated target and make primary originals/caches unavailable to the restore procedure.
3. Perform restoration from the claimed source and check content identities, integrity, and required later changes.
4. Measure against the recovery targets and retain failures; activate only within authority after required invariants pass.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: the backup supports the declared recovery objective without undoing acknowledged obligations.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A complete independent backup and required subsequent history are available | Restoration meets declared integrity, data, and recovery targets. |
| Local originals are unavailable and the backup lacks required content | The drill fails visibly rather than borrowing primary data. |
| Correction or deletion history needed for current state is missing | Activation is withheld. |
| Backup data predates an acknowledged correction or deletion | Recovered state honors it through verified replay or another recorded mechanism. |

- **Pass:** The positive restoration meets its targets and all missing-data/history cases block activation.
- **Fail:** Primary caches mask an incomplete backup, stale user state is exposed, or backup existence is called proven recovery.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Backup/source identities, isolated restore setup, procedure, timings, integrity checks, replay history, and activation disposition.

## Dependencies and limitations

Requires access to independent recovery inputs and defined targets; testing does not authorize deletion of primary data. Complements [verified service recovery](verified-service-recovery.md). Protection and retention of backups remain separate obligations.

[^workflows-operations]: [Operations, maintenance and retirement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md).
