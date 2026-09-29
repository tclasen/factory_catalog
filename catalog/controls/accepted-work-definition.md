---
type: Control
title: "Accepted work definition"
description: "Record accepted scope and observable criteria before starting dependent work."
status: draft
family: intake-and-work-definition
sources:
  - id: policies-planning
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md
    title: "Requirements and planning"
  - id: policies-governance
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md
    title: "Scope, authority and security"
---

# Accepted work definition

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^policies-planning][^policies-governance] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when a request, defect, or proposal becomes implementation work. Prevent accidental scope expansion and changes justified only by existing behavior.

## Requirement

Before dependent implementation, record the request source, intended outcome, accepted scope, exclusions, dependencies, accountable owner, and observable acceptance criteria. Link the work to that record. Resolve consequential ambiguity with the authorized decision owner; unknown inputs block only dependent work. A document describing future operations does not authorize executing them.

## Implementation

1. Inspect the request, existing requirements, current state, and actual grants; reuse known facts.
2. Write one concise canonical record with a stable local identity and criteria that can be observed. Link duplicate requests to it.
3. Map planned changes and checks to accepted criteria. Classify new ideas as proposals until accepted within authority.
4. On scope changes, update the record and invoke [planning consistency](planning-consistency.md) before dependent work.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: every implemented change has an accepted purpose and testable boundary.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A bounded accepted correction with complete criteria | The mapped correction proceeds within the recorded scope. |
| A documentation request mentions deployment | Only the requested documentation is produced; deployment remains outside scope. |
| A change needs an unresolved owner decision | Dependent implementation waits; the missing decision and any independent work are explicit. |

- **Pass:** All changes in the declared review set map to accepted criteria and all three cases respect their scope.
- **Fail:** Any implementation exceeds scope, relies on invented acceptance, or silently assumes a consequential unknown.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Request, dated accepted record, change-to-criterion mapping, scenario observations, and unresolved decisions.

## Dependencies and limitations

Requires an identifiable decision owner and inspectable scope. This records work authority but does not enforce external permissions; use [bounded external action](bounded-external-action.md). Criteria quality still needs [outcome verification](outcome-verification.md).

[^policies-planning]: [Requirements and planning](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md).
[^policies-governance]: [Scope, authority and security](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md).
