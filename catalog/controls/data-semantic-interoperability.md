---
type: Control
title: "Data semantic interoperability"
description: "Validate shared meanings and joins before combining data products."
catalog_version: "v0.1.0"
status: draft
tags: [data-mesh, data-stewardship]
family: quality-and-validation
sources:
  - id: fair
    resource: https://www.nature.com/articles/sdata201618
    title: "The FAIR Guiding Principles for scientific data management and stewardship"
---

# Data semantic interoperability

[Adoption](../adoption.md) · [Data mesh research](../data-mesh-architectures.md)

**Identity:** `controls/data-semantic-interoperability` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

## Purpose and applicability

Apply when combining products, comparing indicators, or exchanging data across domains. FAIR calls for shared knowledge representation, qualified references, and domain standards.[^fair]

## Requirement

Before accepting a cross-product result, document and test mappings for identifiers, record-grain, units, time, populations, and term meanings. Name the owners approving each mapping and its valid scope. Unresolved ambiguity or a failed mapping must block the affected result or be visibly excluded with its effect stated.

## Implementation

1. List the products and revisions being combined. Define the business question and the expected join cardinality, matched population, and allowed losses or duplicates before running the join.
2. Document local meanings and explicit transformations. Keep incompatible definitions distinct; a common field name does not establish equivalence.
3. Construct reference cases including legitimate unmatched records, duplicate identifiers, missing values, differing time zones, and unit conversions. Have domain specialists establish expected results.
4. Reassess mappings when definitions or reference data change. Show excluded records and uncertainty with the result.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: An accepted combination preserves the declared meaning and meets predeclared reconciliation limits.

Combine two synthetic products with reviewed expected totals and record counts. Run a valid mapping, then inject a duplicate join key, a unit mismatch, and a changed population definition. Verify the valid result and detect each invalid result before acceptance.

- **Pass:** the scoped implementation meets the requirement, and valid results match reviewed expectations and each injected semantic defect blocks or explicitly excludes the affected result as declared.
- **Fail:** a requirement is violated; in particular, an undetected defect changes an accepted result, or thresholds are changed after observing failures.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** product versions, approved mappings, expected and actual counts and totals, excluded rows, reviewer decisions, and fixture results.

## Dependencies and limitations

Requires domain expertise and [contracts](data-product-contract.md). Links express relationships, not equivalence. [Evidence traceability](evidence-traceability.md) supports mapping justification; syntactic compatibility alone cannot assess meaning. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^fair]: [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618).
