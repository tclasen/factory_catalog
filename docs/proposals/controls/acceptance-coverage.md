---
type: Control
title: "Acceptance coverage"
description: "Account for every required criterion before claiming acceptance."
status: draft
family: quality-and-validation
sources:
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
---

# Acceptance coverage

[Adoption](../../../catalog/adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^policies-verification] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply to a work item or milestone with several checks, layers, or required user outcomes.

## Requirement

Before implementation, map accepted criteria to applicable checks at component and user/operator levels. Before acceptance, reconcile the required inventory with actual results on the final candidate. A required failure, unavailable check, or missing result prevents the affected acceptance claim. Every not-applicable disposition needs criterion-specific justification.

## Implementation

1. List required criteria and planned checks; include normal, boundary, denied, failure, and recovery cases where relevant.
2. Inspect the mapping in both directions: uncovered criteria and checks with no stated purpose.
3. Run the applicable checks and report covered/required counts, failures, unrun cases, and exclusions.
4. Review the final candidate separately from production. Use independent review where required or justified within available authority; disclose reviewer limitations.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: partial success cannot conceal missing required acceptance evidence.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| Every applicable criterion has current passing evidence | Acceptance is eligible within that declared scope. |
| One required test is missing, skipped without justification, or failed | The affected acceptance remains open despite other passes. |
| A mock or screenshot is offered for required deployed behavior | The evidence gap is explicit and deployment acceptance is withheld. |

- **Pass:** The complete declared inventory is reconciled, and missing or insufficient evidence blocks each affected claim.
- **Fail:** An aggregate success conceals a required gap, or unavailable infrastructure is reclassified as inapplicable.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Criteria/check mapping, final candidate identity, all result dispositions, coverage counts, and review findings.

## Dependencies and limitations

Requires [accepted work definition](accepted-work-definition.md) and [assessment evidence validity](../../../catalog/controls/assessment-evidence-validity.md). This checks completeness against declared criteria; use [outcome verification](../../../catalog/controls/outcome-verification.md) to judge whether those criteria demonstrate the intended benefit.

[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
