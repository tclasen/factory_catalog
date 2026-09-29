---
type: Control
title: "Measurement basis validation"
description: "Check units, boundaries, periods, and conversion methods before measurements are combined or reported."
catalog_version: "v0.1.0"
status: draft
family: quality-and-validation
sources:
  - id: c267
    resource: https://publications.opengroup.org/c267
    title: "The Open Footprint® Standard, Edition 1.0"
  - id: v244
    resource: https://publications.opengroup.org/v244
    title: "Energistics Unit of Measure (UOM) Standard v1.0.1"
---

# Measurement basis validation

**Identity:** `controls/measurement-basis-validation` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

[Adoption](../adoption.md) · [Research map](../open-group-standards-opportunities.md)

## Purpose and applicability

Prevent aggregation of quantities that look comparable but use different units, boundaries, periods, or methods. Apply to environmental reporting, energy analysis, industrial measurements, and derived physical metrics. Open Footprint's environmental data model and Energistics' unit dictionary motivate this catalog proposal.[^c267][^v244]

## Requirement

Before accepting a reported quantity, retain its origin, measured or estimated status, unit, time period, scope/boundary, and calculation or conversion basis. Declare which dimensions determine comparability. A designated reviewer must verify that all material inputs are compatible with the target basis, that transformations preserve their meaning, and that overlapping observations are not counted twice. Missing basis information must block aggregation or be reported as an explicit coverage gap; it must not silently become zero.

## Implementation

1. Define the output boundary, period, quantity, unit, and permitted estimation rules before collecting inputs. Assign an owner and reviewer with domain competence.
2. For each input, retain identity, source revision, measured/estimated flag, uncertainty where known, period, boundary, and method. Preserve original values alongside normalized values.
3. Pin conversion factors, methods, and reference conditions. Check dimensional compatibility and time alignment. Distinguish a unit conversion from a model-based calculation such as applying an emissions factor.
4. Detect repeated or overlapping records; document allocation/exclusion decisions. Reconcile included/excluded inputs to the declared population and expose incomplete coverage.
5. Have the reviewer independently recalculate the aggregate within a predeclared tolerance and resolve discrepancies before acceptance. Reassess after input corrections, method/factor revisions, or changed boundaries.

Mechanism: data validation and calculation checks plus domain review. [Semantic mapping validation](semantic-mapping-validation.md) covers meaning across fields; [evidence traceability](evidence-traceability.md) covers the source support. An accepted schema cannot establish a valid measurement basis.

## Expected outcome and assessment

Expected outcome: all material quantities in the accepted revision share a defensible target basis or have explicit exclusions/coverage gaps, with reproducible transformations.

Assess all material inputs and conversions for one output revision. Use fixtures with a missing unit, kWh presented as MWh without conversion, overlapping meter intervals, incompatible reporting periods, and a missing reading encoded as zero. Include a correct unit conversion and an explicitly disclosed coverage gap as positive cases.

- **Pass:** the scoped record meets the requirement, recomputation is within tolerance, every negative case blocks or corrects the affected aggregation, and positive cases preserve the correct value and limitation.
- **Fail:** an incompatible/duplicate quantity enters the accepted total, a missing reading silently becomes zero, or a material transformation cannot be reproduced.
- **Inconclusive:** underlying data, factors, or reviewer observations cannot be inspected.
- **Evidence:** population/boundary definition, original and normalized records, factors/method revisions, exclusions, recomputation/tolerance, reviewer, fixture results, final disposition.

## Dependencies and limitations

Requires calibrated/fit-for-purpose sources, suitable domain methods, and enforcement of acceptance findings. Correct arithmetic cannot establish sensor accuracy, environmental accounting compliance, or completeness of undisclosed upstream data. The [environmental reporting example](../factories/environmental-reporting.md) proposes an application. No operational assessment or external-standard conformance is asserted.

[^c267]: The Open Group, The Open Footprint® Standard, Edition 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^v244]: The Open Group, Energistics Unit of Measure (UOM) Standard v1.0.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
