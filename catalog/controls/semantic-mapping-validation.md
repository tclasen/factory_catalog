---
type: Control
title: "Semantic mapping validation"
description: "Verify that information exchanged between models preserves its intended meaning."
status: draft
family: knowledge-and-evidence
sources:
  - id: c223
    resource: https://publications.opengroup.org/c223
    title: "O-DEF™, the Open Data Element Framework, Version 3.0"
  - id: c231
    resource: https://publications.opengroup.org/c231
    title: "Open Universal Domain Description Language (Open UDDL), Edition 1.1"
---

# Semantic mapping validation

[Adoption](../adoption.md) · [Research map](../open-group-standards-opportunities.md)

## Purpose and applicability

Prevent a syntactically valid translation from silently changing meaning. Apply when a factory maps fields, categories, model elements, identifiers, or reference data between organizations, schemas, or standards. O-DEF supports common vocabulary/classification, while Open UDDL describes formal data modeling; this control is a catalog adaptation, not their conformance test.[^c223][^c231]

This control assesses the semantic relationship between source and target meanings. [Context translation contracts](context-translation-contracts.md) addresses the surrounding handoff agreement, ownership, and accepted revisions. [Data semantic interoperability](data-semantic-interoperability.md) applies to cross-product results, where join cardinality and population reconciliation need assessment beyond the field mapping.

## Requirement

Before accepting an information mapping, identify the source and target definitions and revisions, transformation rules, scope, and owner. State whether each material mapping is equivalent, narrower, broader, lossy, or unresolved, with rationale. A competent reviewer must test meaning with representative and boundary cases and confirm that unmapped, ambiguous, or lossy values are rejected or visibly qualified before downstream reliance. Matching names or valid schemas alone must not establish equivalence.

## Implementation

1. Declare the exchange's intended use and material fields. [Domain identity and values](domain-identity-and-values.md) explains identity and equality rules that help distinguish an identifier mapping from a value conversion. Retain source/target vocabulary definitions, versions, identifiers, units, cardinality, null semantics, and relevant reference conditions.
2. Build an explicit mapping table with transformation, semantic relationship, evidence, known loss, owner, and reassessment trigger.
3. Include representative, boundary, unknown, and conflicting values. Test inverse/round-trip behavior where reversibility is claimed; where loss is intentional, test its disclosure and permitted use.
4. Have source and target domain expertise review the intended meaning. Check all material fields, including fields omitted from the mapping table.
5. Withhold acceptance for unresolved material meaning. Reassess when either model, vocabulary, method, or intended use changes.

Mechanism: fixtures and review tied to exchange acceptance. [Industrial information exchange](../guides/industrial-information-exchange.md) provides application context; [measurement basis validation](measurement-basis-validation.md) adds quantitative checks.

## Expected outcome and assessment

Expected outcome: the accepted exchange preserves all meaning needed for its declared use and exposes any approved information loss.

Inspect a declared mapping revision. Test identical labels with different definitions, source null incorrectly converted to zero, an unknown enumeration silently assigned a default, and a many-to-one mapping falsely described as reversible. Include an equivalent mapping and an authorized, disclosed lossy mapping as positive cases.

- **Pass:** every material field has reviewed meaning and tested behavior; all negative cases block or correct the mapping before use; both positive cases preserve the declared semantics and qualifications.
- **Fail:** unsupported equivalence, undisclosed loss, or unresolved material meaning reaches accepted output.
- **Inconclusive:** source/target definitions, test observations, or domain review cannot be inspected.
- **Evidence:** definitions and mapping revisions, field coverage, reviewer identities, fixtures/results, loss qualifications, acceptance decisions, change triggers.

## Dependencies and limitations

Requires access to definitions and qualified reviewers on both sides of the exchange. Semantic validity does not establish privacy, authority, availability, or fitness for an untested use. Automated schema checks support only part of the requirement. This draft defines an assessment but claims no executed implementation or O-DEF/Open UDDL conformance.

[^c223]: The Open Group, O-DEF™, the Open Data Element Framework, Version 3.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c231]: The Open Group, Open Universal Domain Description Language (Open UDDL), Edition 1.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
