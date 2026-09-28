---
type: Factory Example
title: "Workplace learning factory"
description: "A learning workflow that separates lesson delivery from improved ability."
catalog_version: "v0.1.0"
status: stable
example: true
domain: "Workplace learning"
work_types: ["design-and-specification", "content-and-media-production", "translation-and-adaptation", "teaching-and-capability-development", "evaluation-and-assurance"]
control_selections:
  - control: ../controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Example: workplace learning factory

[Factory examples](index.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Fictional design case; proposed implementations; no assessments performed.**

## Factory profile

| Field | Design |
|---|---|
| Why / owner | Help staff recognize phishing; training owner is accountable for instructional quality |
| Domain / work types | Workplace learning; design, content production, adaptation, teaching, evaluation |
| Inputs → artifacts | Approved policy and learner needs → lesson, practice exercises, assessment, feedback |
| Outcome | Learners improve their ability to identify suspicious messages and choose the appropriate response |
| Measure | Illustrative pilot criterion: mean score improves by at least 20 percentage points on a comparable unseen assessment after seven days; report participation and missing observations separately |
| Actors | Curriculum author, tutor agent, human facilitator, assessment reviewer |
| Workflow | Needs assessment → lesson design → factual review → tutoring → unseen assessment → follow-up |
| Autonomy | Tutor adapts exercises within approved material; escalates policy ambiguities and learner distress |
| Authority | Deliver content in the assigned learning session; no email campaigns, employment decisions, or modification of personnel records |
| Context | Learner identities and performance are sensitive; scope is a voluntary pilot; no real malicious attachments or live phishing campaign |

## Control selections

| Scenario or objective | Control | Applicability / proposed implementation |
|---|---|---|
| Incorrect policy advice enters a lesson | [Evidence traceability](../controls/evidence-traceability.md) | Applicable: policy owner checks material claims against approved policy revisions |
| Lesson completion is reported as improved ability | [Outcome verification](../controls/outcome-verification.md) | Applicable: retain baseline and follow-up results, use unseen items, disclose missing data and proxy limitations |
| Tutor publishes to the wrong learner session | [Bounded external action](../controls/bounded-external-action.md) | Applicable: enforce session-scoped standing grants for delivery; no new human approval for each authorized response |

The threshold is a review fixture, not a general learning standard. The training owner must justify a real criterion. A score change measures assessment performance; it does not prove fewer real incidents or that training caused the change.

## Assessment plan and evidence

For outcome verification, use three synthetic cases: course complete but improvement below criterion; no follow-up observations; criterion met with complete records. Expected reports are respectively unmet, unverified, and met. Inspect the definition and timing of criteria and the treatment of missing observations. Test cross-session delivery denial separately.

Retain criterion versions, sanitized score records, participation counts, rubric, assessor review, delivery test records, and follow-up actions. Keep individual performance access restricted and specify retention before collecting real data.

All implementations are **proposed** and assessments **not assessed**. The learner outcome is **unverified**.

## Remaining gaps and reassessment

Privacy, accessibility, fairness of assessment, consent or applicable organizational obligations, and escalation need further design. Employment use, minors, new data sharing, or different learner groups trigger review by the training owner before expansion.

## Selection and adoption

The selections above link to controls in this bundle revision. They describe a fictional design, not actual adoption or passing evidence. Before implementing a selection, follow the [adoption procedure](../adoption.md) to pin its control identity, catalog version, and exact source URL. The profile owner also owns applicability decisions; the reassessment triggers above apply to those decisions.
