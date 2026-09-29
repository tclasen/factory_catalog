---
type: Control
title: "Bounded execution"
description: "Keep attempts, time, resource use, and concurrency within the work item’s limits."
status: draft
family: reliability-and-recovery
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
---

# Bounded execution

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^policies-execution] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply to sustained agent work, retries, delegated work, and expensive validation.

## Requirement

Before sustained work, record a coherent task boundary and applicable time, resource, attempt, and concurrency limits. Account for all participating processes and descendants. Preserve consumption across retries, repairs, and handoffs; relabeling unfinished work cannot reset a limit. Stop unchanged failure loops and checkpoint before exceeding the applicable allowance.

## Implementation

1. Use explicit grants and host limits; record which resource measurements are available and which are unknown.
2. Reserve time for verification and safe cleanup; set a progress reassessment point appropriate to the task.
3. Track cumulative attempts, launches, and expensive checks in the existing work record. Diagnose repeated failures before another bounded attempt.
4. At a limit, stop new incurring work and preserve state and the decision needed to continue. Do not schedule future work without authority.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: work stops or changes approach within its limits without concealing unfinished obligations.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A task completes within its allowance | Actual usage or its stated proxy and completion evidence are retained. |
| The task restarts or delegates after consuming most of its allowance | Successors inherit remaining limits; descendants count toward the shared total. |
| An unchanged failure repeats or the allowance is exhausted | New incurring attempts stop and a checkpoint records remaining work. |

- **Pass:** All cases preserve cumulative accounting and no observed operation exceeds the declared limits.
- **Fail:** Restart, task renaming, or delegation resets consumption, or known exhaustion triggers further incurring work.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Task boundary, grants/limits, attempt and resource records, progress decisions, and final checkpoint.

## Dependencies and limitations

This control defines the work boundary and stopping procedure. [Cumulative execution limits](cumulative-execution-limits.md) specifies durable accounting across attempts, while [workflow resource budgets](workflow-resource-budgets.md) requires enforcement across the job tree. Select the applicable scopes and reuse evidence where it satisfies each assessment.

Requires observable usage or conservative time/launch proxies. Account-wide counters cannot establish task cost by themselves. Use [safe work resumption](safe-work-resumption.md); limits do not excuse a false completion claim.

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
