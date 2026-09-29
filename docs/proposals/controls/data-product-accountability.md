---
type: Control
title: "Data product accountability"
description: "Assign sustained responsibility for data products used across organizational boundaries."
status: draft
tags: [data-mesh, data-stewardship]
family: purpose-and-accountability
sources:
  - id: principles
    resource: https://martinfowler.com/articles/data-mesh-principles.html
    title: "Data Mesh Principles and Logical Architecture"
---

# Data product accountability

[Adoption](../../../catalog/adoption.md) · [Data product design](../guides/data-product-design.md)

## Purpose and applicability

Apply when another team relies on a dataset, report, evidence collection, or analytical service. An internal disposable analysis may be excluded with a recorded rationale. Domain ownership is one of the original data mesh principles.[^principles]

## Requirement

Before offering a product for shared use, record an accountable owner, operating steward, consumer purpose, funded support capacity, escalation route, and successor or retirement procedure. The owner must accept responsibility for quality, access decisions within granted authority, changes, and consumer communication throughout the declared service period.

## Implementation

1. Describe the business boundary and intended consumers. Split ownership when terms such as customer or case have different meanings; name an owner for each derived product.
2. Record the support schedule, response target, maintenance allocation, and escalation decision maker. Distinguish accountability from permission to read, disclose, or change data.
3. Have the named owner accept the record and verify that the support route reaches a person or staffed function. Reassess at reorganizations and budget changes.
4. Rehearse a transfer: keep responsibility with the outgoing owner until an authorized successor accepts it, or suspend the shared service with consumer notice.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Every assessed product has accepted and resourced ownership, and support requests reach the responsible function within its declared target.

Assess all products in a declared portfolio and service period. Send a permitted support request and rehearse an owner departure in an isolated scenario. Introduce an unaccepted owner assignment and an unstaffed contact; both must prevent readiness approval.

- **Pass:** the scoped implementation meets the requirement, and all ownership records are accepted, capacity is identified, the support request meets its target, and both negative cases withhold readiness.
- **Fail:** a requirement is violated; in particular, a product is approved with unaccepted or unsupported ownership, or an unresolved transfer leaves it represented as supported.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** portfolio revision, owner acceptance, capacity decision, support timestamps, transfer rehearsal, and readiness decisions.

## Dependencies and limitations

Requires management support and explicit authority. Use [decision rights and accountability](decision-rights-and-accountability.md) for activity authority and intervention; this control adds product support capacity and continuity commitments. A title or funding entry alone does not establish competence. Pair with [data product service objectives](data-product-service-objectives.md) and [outcome verification](../../../catalog/controls/outcome-verification.md). Adopt using the exact source revision under the [adoption procedure](../../../catalog/adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^principles]: [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html).
