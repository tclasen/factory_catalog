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

[Adoption](../../../catalog/adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

The requirement and assessment below are catalog-proposed synthesis. The cited source files were unavailable at their pinned revision when checked, so their contents have not been verified and this is not a substantiated adaptation claim.[^policies-delivery][^policies-verification]

## Purpose and applicability

Apply when work must be integrated, published, installed, or otherwise delivered beyond a local candidate.

## Requirement

Define applicable completion stages and destination before delivery. Verify the final candidate locally, follow the authorized integration/review process, independently confirm destination identity, and check required remote or installed behavior. Report partial delivery whenever a required stage is incomplete. A changed artifact or configuration reopens affected qualification.

## Implementation

1. Bind local acceptance, integration target, remote destination, deployment conditions, and recovery prerequisites to the work item.
2. Review the staged change and preserve unrelated work; follow the host signing and branch rules.
3. Confirm the actual revision/artifact at the destination and inspect required remote checks and installed behavior.
4. Record stage results and justified inapplicability. Use [reconcile before retry](../../../catalog/controls/reconcile-before-retry.md) for ambiguous publication responses.

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

Requires [bounded external action](../../../catalog/controls/bounded-external-action.md), [assessment evidence validity](../../../catalog/controls/assessment-evidence-validity.md), and observable destinations. The proposed requirement applies to the adopter’s authorized endpoint; the host’s merge and release authorizations remain binding. The cited source rule could not be checked. Delivery does not establish downstream benefit.

For artifact comparison at the destination, [qualified artifact promotion](../../../catalog/controls/qualified-artifact-promotion.md) describes immutable identities, complete file comparisons, and packaging changes. Verified delivery covers the agreed completion stages, including required remote checks and installed behavior.

[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md), cited at commit `70cfad0de635197f36f14e5276dec145483c5128`. This exact path returned HTTP 404 on 2026-09-29; the source content and its relationship to this proposal remain unverified.
[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md), cited at commit `70cfad0de635197f36f14e5276dec145483c5128`. This exact path returned HTTP 404 on 2026-09-29; the source content and its relationship to this proposal remain unverified.
