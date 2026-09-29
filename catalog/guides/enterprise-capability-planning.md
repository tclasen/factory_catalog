---
type: Guide
title: "Plan enterprise capabilities with traceable architecture decisions"
description: "Connect objectives, capability gaps, activities, owners, and outcome evidence for organizational change."
status: draft
sources:
  - id: c220
    resource: https://publications.opengroup.org/c220
    title: "The TOGAF® Standard, 10th Edition"
  - id: c260
    resource: https://publications.opengroup.org/c260
    title: "ArchiMate® 4 Specification"
  - id: c143
    resource: https://publications.opengroup.org/c143
    title: "The Exploration & Mining Business Capability Reference Map"
---

# Plan enterprise capabilities with traceable architecture decisions

[Research map](../open-group-standards-opportunities.md) · [Ontology](../ontology.md)

## Source and applicability

TOGAF provides architecture method/content/governance guidance; ArchiMate supplies a language for modeling relationships; EMMM demonstrates industry-specific capability references.[^c220][^c260][^c143] The procedure below is a catalog adaptation for organizational planning, including public services, research operations, procurement, and mining. It does not assert a TOGAF or ArchiMate conformance mapping.

## Procedure

1. Name the beneficiary, observable outcome, planning horizon, constraints, and accountable decision owner. State whether the work recommends a change or can authorize it.
2. Describe the present ability to deliver that outcome. Separate a capability (what the organization can do) from an activity (work it performs), team, tool, and funded initiative. Record evidence rather than assigning an unexplained maturity score.
3. Identify the desired ability and the measured gap. Use [capability investment alignment](../controls/capability-investment-alignment.md) to assess the connection between each candidate investment and the gap it is expected to reduce; document dependencies and contrary evidence.
4. Apply [architecture decision traceability](../controls/architecture-decision-traceability.md) to material choices. Record rejected options and unresolved assumptions, including a do-nothing option where meaningful.
5. Define an observation plan using [outcome verification](../controls/outcome-verification.md). Delivery of a model or system is an artifact milestone; improved organizational performance requires separate measurement.
6. Review after changes to the objective, operating constraints, source model, or material assumptions. Reopen the decision if the trace no longer supports it.

## Embedded capability record

| Field | Required local decision |
|---|---|
| Capability and scope | Local name, definition, organizational boundary; external model/edition and mapping rationale if used |
| Outcome | Beneficiary, target, observation period, baseline evidence |
| Current/target condition | Observations, uncertainty, proposed improvement, gap |
| Activities and artifacts | Which work changes and what evidence it produces |
| Accountable owner | Who maintains the record; who may authorize investment |
| Options and dependencies | Cost/effort assumptions, sequencing, alternatives, unresolved constraints |
| Decision and assessment | Decision revision, supporting sources, outcome test, reassessment trigger |

For a record connecting capabilities to service stages, actors, and shared information, use [Map capabilities, value, and information](capability-value-information-mapping.md). These are embedded records under the existing ontology. A capability model can organize activities and outcomes without declaring every external term a new catalog type. If importing ArchiMate, pin the language edition and document mappings explicitly: Version 4 changes elements compared with 3.2.[^c260] Test the mappings with [semantic mapping validation](../controls/semantic-mapping-validation.md).

## Example and review

A city permit service proposes a document triage capability. The goal is fewer returned incomplete applications within one quarter, with no reduction in accessibility or required review. Proposed artifacts include an intake checklist and exception queue. An agent may draft mappings and analyze public metrics; only the designated official may approve procedural changes.

Reviewers should be able to trace each initiative to a measured gap and owner, and each decision to its supporting revision. An orphan initiative or a claimed outcome with no observation plan requires revision. This guide supplies no evidence that the example improves service performance. The [mining planning example](../factories/mining-investment-planning.md) illustrates a second application.

[^c220]: The Open Group, The TOGAF® Standard, 10th Edition; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c260]: The Open Group, ArchiMate® 4 Specification; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c143]: The Open Group, The Exploration & Mining Business Capability Reference Map; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
