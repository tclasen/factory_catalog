---
type: Factory Example
title: "Public research factory"
description: "A public-source research workflow with claim review and explicit unknowns."
status: stable
example: true
domain: "Product research"
activities: ["collect comparison evidence", "review material claims", "resolve contradictions", "deliver a research memo"]
control_selections:
  - control: ../controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/bounded-external-action.md
    applicability: undetermined
    implementation_state: not-planned
    assessment_result: not-assessed
  - control: ../controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Example: public research factory

[Factory examples](./) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Fictional design case; proposed implementations; no assessments performed.**

## Factory profile

| Field | Design |
|---|---|
| Why / owner | Help a product team compare three options; research lead owns scope and acceptance |
| Domain / activities | Product research; research and discovery, analysis and diagnosis, content production, evaluation |
| Inputs → artifacts | Approved question and public sources → evidence table and comparison memo |
| Outcome | Decision owner can compare all three options against the agreed criteria and identify unresolved questions |
| Measure | Before accepting the memo, decision owner confirms every criterion has a supported comparison or an explicit unknown; this is usability, not proof of a better decision |
| Actors | Research agent gathers and drafts; research lead reviews evidence; decision owner assesses usefulness |
| Workflow | Clarify question → retrieve → compare → draft → source review → owner acceptance |
| Autonomy | Agent chooses searches and drafts within scope; stops at missing access, budget limit, or unresolved material source conflict |
| Authority | Read public sources and write the draft workspace; no sending, publishing, purchasing, or installing tools |
| Context | Public input data; untrusted web content; no private connectors or persistent shared memory; a bounded run with an agreed budget |

## Risk scenarios and control selections

| Scenario or objective | Control | Applicability / proposed implementation |
|---|---|---|
| Agent turns a vendor assertion into an unsupported comparative claim | [Evidence traceability](../controls/evidence-traceability.md) | Applicable: every material comparison goes in a claim table reviewed by the research lead |
| A polished memo omits a criterion the team needs | [Outcome verification](../controls/outcome-verification.md) | Applicable: decision owner checks criterion coverage and explicit unknowns |
| Publishing or committing on the team's behalf | [Bounded external action](../controls/bounded-external-action.md) | Undetermined: the fictional design intends to exclude these actions, but no tool-path inventory is supplied to establish that exclusion |

Reading the web still creates network requests. The stated exclusion concerns publishing and commitment actions, not all network security: restrict the read tool's capability, prevent sensitive query leakage, and treat page instructions as untrusted input. The bounded external-action applicability remains undetermined until an inventory confirms whether any tool or alternate path can perform those actions. Reassess when tools or permissions change.

## Assessment plan and evidence

Run the evidence control's negative cases on a fixture memo. Then ask the decision owner to inspect coverage against the original brief. Retain the brief revision, source table, memo revision, review findings, coverage result, and dispositions.

Evidence traceability and outcome verification have implementation state **proposed**. Bounded external action is **not-planned**, with applicability **undetermined** because no tool-path inventory is provided. All three selections have assessment result **not-assessed**.

## Remaining gaps and reassessment

Source selection bias, stale information, prompt injection, resource limits, and tool isolation need further controls. Source links alone do not establish truth. Reassess when private data, persistent memory, new tools, automated publication, or a consequential decision context is added. The research lead owns that review.

## Selection and adoption

The selections above link to controls in this bundle revision. They describe a fictional design, not actual adoption or passing evidence. Before implementing a selection, follow the [adoption procedure](../adoption.md) to pin its control identity, catalog version, and exact source URL. The profile owner also owns applicability decisions; the reassessment triggers above apply to those decisions.
