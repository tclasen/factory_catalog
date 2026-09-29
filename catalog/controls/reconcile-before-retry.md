---
type: Control
title: "Reconcile before retry"
description: "Resolve uncertain external effects before repeating a consequential operation."
catalog_version: "v0.1.0"
status: stable
family: reliability-and-recovery
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/tool-contracts.md
    title: "Software Factory: Reconcile before retry basis"
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
---

# Reconcile before retry

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

**Identity:** `controls/reconcile-before-retry` · **Catalog:** v0.1.0 · **Family:** `reliability-and-recovery`

## Purpose and applicability

Apply to consequential writes whose response may be lost, delayed, partial, or ambiguous. Prevent duplicate messages, payments, publications, or state changes after an uncertain response.

## Requirement

Before submitting an operation, retain its target, intended effect, and stable operation identity where supported. If the outcome becomes uncertain, query authoritative recipient state before any repeated mutation. Distinguish observed completion, known absence of effect, and unresolved uncertainty. Retry only when reconciliation establishes a safe path under the recipient's documented semantics and current authority; otherwise block the dependent mutation and escalate. Do not change operation identity to evade duplicate detection.

## Implementation

1. Inventory mutation paths and the recipient's status lookup, idempotency scope, expiry, and partial-success semantics. Record limitations.
2. Persist intent before submission and observations afterward using a [restart and handoff record](../restart-and-handoff-records.md).
3. After timeout or interruption, query using the original identity. Distinguish the intended effect from concurrent or conflicting work; a matching count alone is insufficient. For bulk actions, reconcile each component that may have succeeded.
4. If complete, continue outstanding verification without repeating the effect. If known not applied, retry within current grants and remaining limits. If unknown, retain the block.
5. Use recipient-supported idempotent replay only when its semantics and identity retention resolve the duplicate risk; a local assumption is insufficient.

## Expected outcome and assessment

Expected outcome: uncertain responses produce no duplicate effect and no unsupported completion claim.

In an authorized observable fixture, test a valid write, known pre-write failure, lost response after success, partial bulk completion, a concurrent conflicting write, delayed status visibility, and unavailable status lookup. Include an expired or mismatched idempotency key where that mechanism is used. Inspect recipient state rather than only request logs.

- **Pass:** valid work completes; safe retries complete only the missing effects; completed effects are not repeated; unresolved cases remain blocked with evidence and an owner.
- **Fail:** any duplicate effect, unsafe replay, or completion claim unsupported by recipient state. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** recipient effects or relevant identity semantics cannot be observed.
- **Evidence:** operation/target identities, sanitized requests, recipient observations and times, attempt history, per-component disposition, and remaining verification.

## Dependencies and limitations

Depends on trustworthy recipient observations and adequate operation identity. [Bounded external action](bounded-external-action.md) still governs permission; [cumulative execution limits](cumulative-execution-limits.md) governs retries. [Exclusive mutation ownership](exclusive-mutation-ownership.md) addresses competing writers. Reconciliation cannot guarantee exactly-once behavior from a provider that supplies no suitable guarantees.

## Source and adoption

This catalog requirement combines Software Factory guidance[^software-factory] with the semantic_search policies.[^policies-execution][^policies-delivery] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/tool-contracts.md).

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md).
