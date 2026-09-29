---
type: Control
title: "Data contract evolution"
description: "Protect consumers when product meaning, interfaces, or availability change."
status: draft
tags: [data-mesh, data-stewardship]
family: change-and-dependencies
sources:
  - id: dcat
    resource: https://www.w3.org/TR/vocab-dcat-3/
    title: "Data Catalog Vocabulary (DCAT), Version 3"
---

# Data contract evolution

[Adoption](../adoption.md) · [Data product design](../guides/data-product-design.md)

## Purpose and applicability

Apply to changes in shared data meaning, schema, refresh expectations, access interfaces, or retirement. DCAT supports relationships between resource versions.[^dcat]

## Requirement

Before activating a material product change, compare old and new contracts, identify affected consumers, and record a transition decision, notice period, validation evidence, and recovery or withdrawal plan. Preserve access to the agreed revision for the agreed transition period where authorized. Retire only after consumer dispositions and retention obligations are resolved.

## Implementation

1. Classify changes using consumer expectations. A renamed field, new unit, changed population, or slower delivery can break a use even if a schema checker passes.
2. Use [lineage and impact assessment](data-lineage-impact.md) to identify dependencies and gaps. Obtain affected consumer acceptance or an authorized explicit disruption decision.
3. Test old and new consumers against versioned fixtures. Document coexistence, translation, rollback, and any irreversible effects. Do not keep prohibited data merely to enable rollback.
4. Update [discovery records](data-product-discovery.md), deadlines, support, and access paths together. Record disposition of downstream copies, caches, and exports at retirement.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Consumers can identify the version in use, and transitions meet declared compatibility, notice, and recovery criteria.

Exercise a compatible change and a numeric-unit change that preserves the schema. Then rehearse retirement with one unresolved consumer and recovery after a failed activation. The meaning change must trigger transition review, and unresolved retirement must be withheld pending an authorized disposition.

- **Pass:** the scoped implementation meets the requirement, and all four cases follow the approved transition rules, versions remain distinguishable, and recovery or safe withdrawal meets its target.
- **Fail:** a requirement is violated; in particular, a breaking change bypasses review, retirement silently strands a consumer, or recovery mixes incompatible revisions.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** old and new contracts, consumer inventory, approvals and notices, fixture results, activated versions, and recovery observations.

## Dependencies and limitations

Requires [contracts](data-product-contract.md) and [ownership](data-product-accountability.md). Data retention, legal holds, and deletion decisions require appropriate local authority. Recovery can require recomputation rather than restoring an old service. Use [controlled dependency change](controlled-dependency-change.md) for implementation dependencies and [scoped retirement](scoped-retirement.md) for actual resource and copy disposition; this control adds consumer contract transitions. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^dcat]: [Data Catalog Vocabulary (DCAT), Version 3](https://www.w3.org/TR/vocab-dcat-3/).
