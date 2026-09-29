---
type: Control
title: "Planning consistency"
description: "Reconcile affected requirements, plans, and checks when scope or assumptions change."
status: draft
family: change-and-dependencies
sources:
  - id: policies-planning
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md
    title: "Requirements and planning"
---

# Planning consistency

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

Draft requirement adapted from the source factory policies.[^policies-planning] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when accepted scope, criteria, architecture, or material assumptions change across related documents or activities.

## Requirement

Before dependent work resumes, inventory the current planning set, propagate the change to affected requirements, interfaces, checks, and operating plans, and record why other items are unaffected. Resolve contradictions and invalidate assessments that relied on superseded criteria. Preserve prior evidence with its original scope.

## Implementation

1. Name the change owner and identify the canonical requirement and all relevant plans, including release and recovery where applicable.
2. Inspect dependencies in both directions; update affected documents and test expectations together.
3. Record each relevant item as updated or unaffected with a reason. Resolve disagreement through the owner of the requirement.
4. Mark invalidated evidence and obtain fresh checks under [assessment evidence validity](assessment-evidence-validity.md).

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: dependent work uses consistent accepted requirements and expectations.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A change has a limited, documented impact | Affected artifacts agree and unaffected items have supported reasons. |
| An interface changes but its contract test and operating plan retain the old assumption | The contradiction is found and dependent acceptance is withheld. |
| An acceptance threshold changes after an earlier pass | The earlier result remains scoped to its old criteria; a new claim needs current evidence. |

- **Pass:** No unresolved material contradiction remains in the declared planning set, and all cases handle affected evidence correctly.
- **Fail:** A known contradiction reaches dependent implementation or an old pass is relabeled against new criteria.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Change request, planning inventory, impact dispositions, updated revisions, and invalidated/replacement evidence.

## Dependencies and limitations

Requires discoverable canonical plans and competent impact review. A complete-looking inventory cannot prove every dependency was found. Connect to [accepted work definition](accepted-work-definition.md).

[^policies-planning]: [Requirements and planning](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md).
