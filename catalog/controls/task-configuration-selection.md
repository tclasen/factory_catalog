---
type: Control
title: "Task configuration selection"
description: "Select model and reasoning settings using task requirements and credible cost-quality evidence."
catalog_version: "v0.1.0"
status: draft
family: workflow-and-coordination
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
---

# Task configuration selection

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

**Identity:** `controls/task-configuration-selection` · **Catalog:** v0.1.0 · **Family:** `workflow-and-coordination`

Draft requirement adapted from the source factory policies.[^policies-execution] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when an agent or operator can choose among model/reasoning configurations for an assignment.

## Requirement

Filter supported configurations by acceptance, security, tool/context needs, deadlines, consent, and resource limits. Compare feasible alternatives using credible task-relevant evidence for quality, reliability, total delivery cost, and latency. Record the selected configuration, alternatives, evidence date, tradeoff, and uncertainty. Do not claim measured savings from an unmeasured rationale or weaken acceptance to fit a cheaper option.

## Implementation

1. Inspect actual available controls and choices at assignment time; identify inherited defaults when settings cannot be changed.
2. Include likely retries, review, and repair in cost/latency reasoning. Reject an option clearly worse on every relevant dimension than a feasible alternative.
3. When evidence is sparse, make a provisional choice and state what is unknown; no benchmark campaign is implied.
4. Verify the result and reconsider settings when failures or new evidence warrant it, preserving existing limits and provider permissions.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: configuration choices are justified for the assignment and their uncertainty is visible.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| Two feasible alternatives have comparable task evidence | The choice reflects declared quality/cost/latency priorities. |
| One option is demonstrably no better, more costly, and slower | It is rejected unless a documented missing constraint changes feasibility. |
| Settings or reliable cost data are unavailable | The limitation is disclosed; defaults are not represented as proven optimization. |
| A cheaper configuration fails required acceptance | Acceptance remains unchanged and diagnosis precedes bounded reselection. |

- **Pass:** Each selection has a supported rationale and the cases preserve constraints, uncertainty, and acceptance.
- **Fail:** Unsupported savings or a proven optimum are claimed, required constraints are ignored, or acceptance is weakened.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Available configurations, task constraints, dated comparison sources, selected settings, rationale, and observed results.

## Dependencies and limitations

Requires trustworthy comparable evidence where available; model rankings and prices change. This control does not prescribe a model or grant authority to override runtime settings. Use [bounded execution](bounded-execution.md) for resource ceilings.

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
