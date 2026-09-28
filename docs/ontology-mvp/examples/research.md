# Example: public research factory

[MVP overview](../index.md) · [Model](../model.md)

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

| Scenario or objective | Candidate control | Applicability / proposed implementation |
|---|---|---|
| Agent turns a vendor assertion into an unsupported comparative claim | [Evidence traceability](../controls/evidence-traceability.md) | Applicable: every material comparison goes in a claim table reviewed by the research lead |
| A polished memo omits a criterion the team needs | [Outcome verification](../controls/outcome-verification.md) | Applicable: decision owner checks criterion coverage and explicit unknowns |
| Publishing or committing on the team's behalf | [Bounded external action](../controls/bounded-external-action.md) | Not applicable to the stated design's publication/commitment scope: no such execution path is included; tool inventory must confirm this before operation |

Reading the web still creates network requests. The exclusion above does not cover all network security: restrict the read tool's capability, prevent sensitive query leakage, and treat page instructions as untrusted input. If an action-capable browser or connector is introduced, reassess external-action applicability before use.

## Proposed assessment and evidence

Run the evidence control's negative cases on a fixture memo. Then ask the decision owner to inspect coverage against the original brief. Retain the brief revision, source table, memo revision, review findings, coverage result, and dispositions.

Implementation state for the selected controls: **proposed**. Assessment result: **not assessed**. The proposed external-action exclusion is an assumption requiring inventory evidence; if that cannot be obtained, record applicability as **undetermined**.

## Remaining gaps and reassessment

Source selection bias, stale information, prompt injection, resource limits, and tool isolation need further controls. Source links alone do not establish truth. Reassess when private data, persistent memory, new tools, automated publication, or a consequential decision context is added. The research lead owns that review.
