---
type: Factory Example
title: "Public research factory"
description: "A public-source research workflow with claim review and explicit unknowns."
catalog_version: "v0.1.0"
status: stable
example: true
domain: "Product research"
work_types: ["research-and-discovery", "analysis-and-diagnosis", "content-and-media-production", "evaluation-and-assurance"]
control_selections:
  - control: ../controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/bounded-external-action.md
    applicability: not-applicable
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
| Domain / work types | Product research; research and discovery, analysis and diagnosis, content production, evaluation |
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
| Publishing or committing on the team's behalf | [Bounded external action](../controls/bounded-external-action.md) | Not applicable to the stated design's publication/commitment scope: no such execution path is included; tool inventory must confirm this before operation |

Reading the web still creates network requests. The exclusion above does not cover all network security: restrict the read tool's capability, prevent sensitive query leakage, and treat page instructions as untrusted input. If an action-capable browser or connector is introduced, reassess external-action applicability before use.

## Assessment plan and evidence

Run the evidence control's negative cases on a fixture memo. Then ask the decision owner to inspect coverage against the original brief. Retain the brief revision, source table, memo revision, review findings, coverage result, and dispositions.

Evidence traceability and outcome verification have implementation state **proposed**. Bounded external action is **not-planned** because the stated design excludes its execution paths. All three selections have assessment result **not-assessed**. The proposed external-action exclusion is an assumption requiring inventory evidence; if that cannot be obtained, record applicability as **undetermined**.

## Source intake extension

Proposed application of the [classwork source-intake learning](../classwork-learnings.md#1-resolve-the-source-before-integrating-its-claims): before drafting, the research agent records each source's exact revision or access time, relevant passage, and whether the comparison is directly supported or inferred. The research lead records whether new evidence confirms, qualifies, or conflicts with the existing comparison. Keep unresolved conflicts visible to the decision owner.

Add a fixture with two source editions that disagree on one product capability. Expected behavior: identify the edition used, retain both observations and their context, and qualify the comparison until the conflict is resolved. Silent edition mixing or an unsupported definitive recommendation fails this proposed check. Retain the intake table, draft revision, and reviewer disposition. This fixture has not been run.

## Remaining gaps and reassessment

Source selection bias, stale information, prompt injection, resource limits, and tool isolation need further controls. Source links alone do not establish truth. Reassess when private data, persistent memory, new tools, automated publication, or a consequential decision context is added. The research lead owns that review.

## Selection and adoption

The selections above link to controls in this bundle revision. They describe a fictional design, not actual adoption or passing evidence. Before implementing a selection, follow the [adoption procedure](../adoption.md) to pin its control identity, catalog version, and exact source URL. The profile owner also owns applicability decisions; the reassessment triggers above apply to those decisions.
