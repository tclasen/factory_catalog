---
type: Control
title: "Data product discovery"
description: "Keep product descriptions findable and consistent with the interfaces consumers can use."
catalog_version: "v0.1.0"
status: draft
tags: [data-mesh, data-stewardship]
family: knowledge-and-evidence
sources:
  - id: dcat
    resource: https://www.w3.org/TR/vocab-dcat-3/
    title: "Data Catalog Vocabulary (DCAT), Version 3"
---

# Data product discovery

[Adoption](../adoption.md) · [Data mesh research](../data-mesh-architectures.md)

**Identity:** `controls/data-product-discovery` · **Catalog:** v0.1.0 · **Family:** `knowledge-and-evidence`

## Purpose and applicability

Apply when users discover shared datasets, reports, evidence packages, or analytical services through a catalog. DCAT distinguishes a dataset from its distributions and access services.[^dcat]

## Requirement

Each in-scope shared product must have a discoverable record with a persistent identity, purpose, owner, current contract, lifecycle state, freshness information, and access procedure. Link each supported distribution to that identity and its revision. Reconcile the catalog against the actual publication inventory; do not expose restricted metadata to unauthorized audiences.

## Implementation

1. Declare the publication inventory and allowed metadata audiences. Include uncataloged products in reconciliation instead of using the catalog as its own completeness baseline.
2. Link [contracts](data-product-contract.md), support contacts, distributions, and superseding versions. Mark unavailable products and explain the authorized route for questions.
3. Ask a representative consumer to locate a product, judge suitability, and request access using only the record. Set an acceptable completion time before the trial.
4. Check record freshness after releases, moves, and retirements. Test metadata permissions separately from data permissions.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Every product in the assessed inventory can be found and correctly distinguished from obsolete or inaccessible distributions by the intended audience.

Reconcile the full declared inventory and perform the consumer trial. In an isolated synthetic fixture, introduce an omitted product, stale endpoint, and metadata record marked restricted but configured for the wrong audience. Detect all three and correct or quarantine them before publication.

- **Pass:** the scoped implementation meets the requirement, and inventory reconciliation is complete, the consumer trial meets its target, and all injected defects are detected and contained.
- **Fail:** a requirement is violated; in particular, an inventory product is missing without explanation, stale information misdirects the trial, or restricted metadata is disclosed.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** inventory and catalog snapshots, audience permissions, trial timing, endpoint observations, and reconciliation dispositions.

## Dependencies and limitations

Requires ownership and an authoritative inventory. Discovery does not grant access. Search ranking and catalog completeness are different assessments. Pair with [bounded external action](bounded-external-action.md) for authorized sharing. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^dcat]: [Data Catalog Vocabulary (DCAT), Version 3](https://www.w3.org/TR/vocab-dcat-3/).
