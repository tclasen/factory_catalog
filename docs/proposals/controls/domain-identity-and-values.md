---
type: Control
title: "Domain identity and values"
description: "Distinguish continuing identities from equal values before matching or combining records."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: knowledge-and-evidence
sources:
  - id: tactical
    resource: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design
    title: "Use tactical DDD to design microservices, Microsoft"
---

# Domain identity and values

[Adoption](../../../catalog/adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent incorrect merges, splits, substitutions, or comparisons. Apply to case records, participants, artifacts, measurements, and other objects whose identity or equality affects a decision. Tactical DDD distinguishes continuing entities from value objects defined by their attributes.[^tactical] The procedure below extends that distinction to knowledge records.

## Requirement

Define identity and equality rules for material objects in the adopted context. Preserve a continuing identity through permitted attribute changes. Compare values using their full meaning, including required units and context. Resolve ambiguous matches before a dependent merge or decision, or report them explicitly as unresolved.

## Implementation

1. For each object kind, decide whether the workflow needs continuity over time or only an interchangeable value. The answer may differ across contexts.
2. For continuing identities, record the issuing namespace, identifier, lifecycle, and rules for correction, merge, and split. A shared label or matching name is insufficient by itself.
3. For values, specify required attributes, units, scale, precision, and equality rule. Replace revised values while retaining provenance needed for earlier decisions.
4. Define [cross-context mappings](context-translation-contracts.md) explicitly; preserve original identifiers and uncertainty. Do not expose sensitive identifiers merely to make joins convenient.
5. Review downstream effects of corrections. Connect retained evidence through [evidence traceability](../../../catalog/controls/evidence-traceability.md).

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: the declared sample contains no silently conflated identities or semantically incompatible value comparisons.

Test two different people with the same name; one person's name change; two equal values; two values with equal numerals but different units; and an ambiguous external identifier. Use fictional records, such as two research participants named Alex and measurements of 5 minutes versus 5 hours.

- **Pass:** distinct identities stay distinct; the name change preserves continuity; equal values compare equal; incompatible units require explicit conversion or rejection; the ambiguous identifier stays unresolved until reviewed.
- **Fail:** a required distinction disappears, an unsupported identity link is accepted, or a required case is omitted.
- **Inconclusive:** authoritative identity or unit information is unavailable for assessing a decision.
- **Evidence:** object definitions, namespaces, equality rules, case inputs and results, mapping revisions, reviewer decisions, and correction impact records.

## Dependencies and limitations

Requires domain-specific identity evidence and an owner for corrections. It does not establish real-world identity from a generated identifier, nor authorize joining personal records. Model status, source uncertainty, and access restrictions remain attached to records. This is proposed guidance with no assessed implementation.

[^tactical]: [Use tactical DDD to design microservices, Microsoft](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design).
