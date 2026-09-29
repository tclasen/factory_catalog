---
type: Control
title: "Reconciliation before retry"
description: "Determine an uncertain external effect before repeating its mutation."
catalog_version: "v0.1.0"
status: draft
family: reliability-and-recovery
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
---

# Reconciliation before retry

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

**Identity:** `controls/reconciliation-before-retry` · **Catalog:** v0.1.0 · **Family:** `reliability-and-recovery`

Draft requirement adapted from the source factory policies.[^policies-execution][^policies-delivery] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when a commit, publication, installation, transaction, or other mutation returns ambiguously or loses its response.

## Requirement

Record intended effect, target, operation identity where available, and expected result before consequential execution. After an ambiguous response, inspect authoritative destination state before repeating the mutation. If the effect is present, verify it without duplication; if absent, retry only within authority and limits; if unresolved, keep the mutation blocked.

## Implementation

1. Choose an operation identifier or destination query that can distinguish the intended effect from unrelated work.
2. Persist intent and observations in the current work record, excluding secrets.
3. Reconcile actual destination state and concurrent changes before deciding present, absent, conflicting, or unknown.
4. Use supported idempotency mechanisms where available and retain attempt history across recovery.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: lost responses do not cause duplicate effects or unsupported success claims.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| The mutation succeeds but its response is lost | Read-back identifies the intended effect; no duplicate mutation is sent. |
| The destination confirms the effect did not occur | An authorized bounded retry can proceed and its result is verified. |
| The destination cannot distinguish absence from an unknown effect | Another mutation is withheld and the missing evidence is recorded. |

- **Pass:** All cases take the specified path and the observed destination contains no unintended duplicate effect.
- **Fail:** A timeout is treated as automatic failure or success, or unresolved effects are blindly repeated.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Intent/operation identifiers, response failure, destination observations, retry decision, and effect count.

## Dependencies and limitations

Requires a trustworthy destination query or idempotency facility. Where neither exists, uncertainty may remain blocked. [Bounded external action](bounded-external-action.md) governs permission; [bounded execution](bounded-execution.md) governs attempts.

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md).
