---
type: Control
title: "Safe work resumption"
description: "Reconcile ownership, current state, and remaining obligations before interrupted work resumes."
status: draft
family: workflow-and-coordination
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Previously cited: Ownership, execution and recovery (unavailable at pinned revision)"
  - id: templates-work-item
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md
    title: "Previously cited: Work-item template (unavailable at pinned revision)"
---

# Safe work resumption

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement authored for this catalog. The earlier draft cited semantic_search sources that returned HTTP 404 at their pinned revisions when checked on 2026-09-29; their contents could not be reviewed and are not asserted as support.[^policies-execution][^templates-work-item] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply after interruption, context loss, cancellation, or transfer to another actor.

## Requirement

Preserve a durable record of accepted scope, authority, ownership, revisions, unfinished changes, checks, external effects, limits, and next action. Before a successor mutates shared state, confirm prior writers have stopped or cannot write, reconcile the record with actual local and remote state, and reopen invalidated checks. Missing essential scope or authority blocks dependent resumption.

## Implementation

1. Use the project's existing record and follow [restart and handoff records](../restart-and-handoff-records.md); retain sensitive evidence through protected references.
2. Stop or fence predecessor processes and descendants; a lease timestamp, branch, or written generation is insufficient proof.
3. Inspect current files, processes, destination state, and grants before accepting the handoff.
4. When a packet is missing, reconstruct from the original request and observable state after safe stop; mark unrecoverable inputs unknown. Preserve cancellation as cancellation.

Mechanism: technical restrictions and observed execution checks, supported by an owned procedure.

## Expected outcome and assessment

Expected outcome: resumption preserves work and obligations without overlapping writers or invented authority.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A stopped predecessor leaves a complete packet | The successor reconciles current state and resumes within remaining scope and limits. |
| The predecessor can still mutate the shared target | Successor mutation is withheld until exclusive ownership is established. |
| A packet is missing or contradicts actual state | The successor reconstructs only supported facts; essential unknowns block mutation. |
| The user cancels affected work | Owned execution stops safely and unfinished work is preserved without a completion claim. |

- **Pass:** Each case preserves unrelated work and cumulative limits, and mutations occur only after ownership and scope are established.
- **Fail:** A stale writer overlaps, a summary overrides contradictory reality, or missing authority is invented.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Checkpoint, predecessor-stop/access evidence, state comparison, successor acceptance, and preserved obligations.

## Dependencies and limitations

This control checks whether actual state permits work to resume. [Durable work handoff](durable-work-handoff.md) governs maintaining and transferring the record before interruption; [exclusive mutation ownership](exclusive-mutation-ownership.md) enforces the writer boundary. A maintained record alone cannot establish that a predecessor has stopped.

Requires process or access visibility. Use [reconcile before retry](reconcile-before-retry.md) for uncertain effects and [bounded execution](bounded-execution.md) for limits. A record supports recovery but is not an enforcement mechanism or scheduler.

[^policies-execution]: Previously cited as [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md); the exact pinned URL returned HTTP 404 on 2026-09-29 and was not reviewed.
[^templates-work-item]: Previously cited as [Work-item template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md); the exact pinned URL returned HTTP 404 on 2026-09-29 and was not reviewed.
