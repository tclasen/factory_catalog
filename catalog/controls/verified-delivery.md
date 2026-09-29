---
type: Control
title: "Verified delivery"
description: "Verify the agreed destination and completion stages before reporting delivery."
status: draft
family: release-and-external-action
sources:
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
---

# Verified delivery

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

Draft requirement adapted from the source factory policies.[^policies-delivery][^policies-verification] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when work must be integrated, published, installed, or otherwise delivered beyond a local candidate.

## Requirement

Define applicable completion stages and destination before delivery. Verify the final candidate locally, follow the authorized integration/review process, independently confirm destination identity, and check required remote or installed behavior. Report partial delivery whenever a required stage is incomplete. A changed artifact or configuration reopens affected qualification.

## Implementation

1. Bind local acceptance, integration target, remote destination, deployment conditions, and recovery prerequisites to the work item.
2. Review the staged change and preserve unrelated work; follow the host signing and branch rules.
3. Confirm the actual revision/artifact at the destination and inspect required remote checks and installed behavior.
4. Record stage results and justified inapplicability. Use [reconcile before retry](reconcile-before-retry.md) for ambiguous publication responses.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: delivery claims match the verified content and actual destination state.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| The assessed candidate reaches its agreed destination and required checks pass | Delivery is reported with candidate and destination evidence. |
| Push succeeds but a required remote check fails or installation is absent | Only completed stages are reported; full delivery remains open. |
| The installed artifact differs from the qualified candidate | Qualification is reopened before delivery can pass. |
| The agreed task ends at a reviewed PR or local document | Only those authorized stages are required; no merge or deployment is invented. |

- **Pass:** Every applicable stage has supporting observations for the same candidate and all incomplete cases remain partial.
- **Fail:** Local success or upload alone is called complete, substituted content inherits a pass, or delivery exceeds authority.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Agreed stage contract, local results, integration/publication receipts, independent destination inspection, and installed checks when applicable.

## Dependencies and limitations

Requires [bounded external action](bounded-external-action.md), [assessment evidence validity](assessment-evidence-validity.md), and observable destinations. This generalizes the source main-integration rule to the adopter’s authorized endpoint; the host’s merge and release authorizations remain binding. Delivery does not establish downstream benefit.

For artifact comparison at the destination, [qualified artifact promotion](qualified-artifact-promotion.md) describes immutable identities, complete file comparisons, and packaging changes. Verified delivery covers the agreed completion stages, including required remote checks and installed behavior.

[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md).
[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
