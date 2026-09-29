---
type: Control
title: "Isolated parallel work"
description: "Isolate concurrent edits and verify the combined result under one integration owner."
status: draft
family: workflow-and-coordination
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
---

# Isolated parallel work

[Adoption](../../../catalog/adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^policies-execution] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when several actors contribute concurrently to shared work. Read-only contributions may share source access.

## Requirement

Give each editing actor an explicit scope, separate checkout and branch from a recorded base, and reserved shared resources. Serialize overlapping edits and shared mutations under a named owner. Accept contributions from their actual diff and evidence, then recheck affected behavior on the integrated candidate. If edit isolation is unavailable, use one writer.

## Implementation

1. Before delegation, verify authority, available slots, limits, and useful independent work. Do not duplicate work merely to occupy slots.
2. Provide bounded packets covering objective, criteria, instructions, inputs, allowed surfaces, base, limits, and forbidden effects.
3. Reserve shared files, services, ports, databases, caches, and integration targets; a worktree isolates only part of the environment.
4. Have one integrator inspect returned changes, preserve unrelated work, resolve conflicts, and run affected checks before delivery.

Mechanism: technical restrictions and observed execution checks, supported by an owned procedure.

## Expected outcome and assessment

Expected outcome: concurrent contributions preserve each other’s work and meet acceptance after integration.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| Two independent edits use separate recorded-base checkouts | Both are preserved and the combined candidate receives relevant checks. |
| Assignments overlap on a file or shared service | Reservation or serial execution prevents simultaneous conflicting mutations. |
| Both branches pass separately but their combination fails | Integration remains unaccepted until repaired and rechecked. |
| Only a shared mutable checkout is available | One owner edits; other assignments remain read-only. |

- **Pass:** All contributions and unrelated work are preserved, shared mutations have one owner, and combined failures block delivery.
- **Fail:** Workers share uncontrolled edit surfaces, a contribution is accepted from a summary alone, or branch passes substitute for integrated checks.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Assignments, base/checkouts, resource reservations, returned diffs/results, integration diff, and combined checks.

## Dependencies and limitations

Requires authorized delegation and actual isolation. Use [safe work resumption](safe-work-resumption.md) for ownership transfers and [bounded execution](bounded-execution.md) for shared allowances. Isolation of files does not isolate credentials or processes.

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
