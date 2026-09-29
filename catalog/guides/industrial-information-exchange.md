---
type: Guide
title: "Plan industrial information exchange and integration evidence"
description: "Connect industry reference models to versioned interfaces, data meanings, and bounded integration assessments."
status: draft
sources:
  - id: c230
    resource: https://publications.opengroup.org/c230
    title: "O-PAS™ Standard, 2nd Edition"
  - id: c268
    resource: https://publications.opengroup.org/c268
    title: "The OSDU® Data Platform Standard, Version 1.0"
  - id: c224
    resource: https://publications.opengroup.org/c224
    title: "The Open Group Commercial Aviation Reference Architecture Standard"
  - id: c232
    resource: https://publications.opengroup.org/c232
    title: "FACE® Technical Standard, Edition 3.2"
  - id: c239
    resource: https://publications.opengroup.org/c239
    title: "Technical Standard for SOSA® Reference Architecture, Edition 1.1"
---

# Plan industrial information exchange and integration evidence

[Research map](../open-group-standards-opportunities.md) · [Ontology](../ontology.md)

## Sources and applicability

O-PAS describes process automation interfaces and platforms; OSDU describes a data-platform reference architecture; Commercial Aviation provides an industry architecture; FACE and SOSA address portable components and modular sensor systems.[^c230][^c268][^c224][^c232][^c239] These scopes suggest reusable integration questions. Their profiles are not interchangeable, and public summaries do not establish detailed conformance requirements.

Use this guide for engineering information exchange, supplier handoffs, asset information, and planning integration trials. Physical-system deployment requires its own engineering and safety approvals.

## Procedure and records

1. State the operational outcome and bounded exchange: sender, receiver, information, timing, environment, and failure consequence. Identify the engineering owner and permitted test environment.
2. Record the selected standard edition, parts, corrigenda, optional profile, vendor implementation, and local configuration. For O-PAS, a reference to “2nd Edition” alone omits part-level details and applicable corrections.[^c230]
3. Build an interface record with identifiers, schema revision, field meanings, units, coordinate/reference systems where relevant, time basis, access rules, quality flags, and missing-data behavior.
4. Apply [semantic mapping validation](../controls/semantic-mapping-validation.md) and [measurement basis validation](../controls/measurement-basis-validation.md). Schema acceptance establishes structure only; demonstrate that both sides interpret the information consistently.
5. Plan an isolated trial with a positive exchange, unsupported version, unknown identifier, missing field, unit mismatch, delayed/duplicate message, and loss of connection as applicable. Predeclare acceptable effects and recovery behavior with the engineering owner.
6. Use [interoperability acceptance](../controls/interoperability-acceptance.md) to assess the combined exchange boundary, including participating parties, receiving responsibilities, and failure handling, alongside the mapping and measurement checks above. Preserve the exact configuration, fixtures, observations, discrepancies, and owner disposition. A passing exchange is scoped to tested endpoints and profiles; broader interoperability needs additional evidence.

## Graph relationships

An exchange activity consumes a source artifact and produces a target artifact. Its mapping record explains the transformation; an assessment evaluates that mapping and implementation using retained fixtures. A source reference model supplies vocabulary, while a local owner supplies applicability and authority. Use [supplier assurance records](supplier-assurance-records.md) for components and [architecture decisions](../controls/architecture-decision-traceability.md) for material profile choices.

## Non-software example and limits

A mining planning team exchanges equipment energy measurements with a consultant. The planned trial checks kWh versus MWh, local time versus UTC, duplicate meter intervals, and ownership of corrected readings. No trial authorizes changing a plant controller. Retain access restrictions for asset and supplier data.

Unreviewed standards clauses, calibration, functional safety, cybersecurity, real-time behavior, environmental suitability, and certification remain separate gaps. A vendor declaration or architectural fit is insufficient evidence for these properties. All trials here are proposed; none were run.

[^c230]: The Open Group, O-PAS™ Standard, 2nd Edition; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c268]: The Open Group, The OSDU® Data Platform Standard, Version 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c224]: The Open Group, The Open Group Commercial Aviation Reference Architecture Standard; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c232]: The Open Group, FACE® Technical Standard, Edition 3.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c239]: The Open Group, Technical Standard for SOSA® Reference Architecture, Edition 1.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
