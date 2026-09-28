---
type: Factory Example
title: "Software delivery factory"
description: "A report-export workflow connecting acceptance, artifact identity, authorized delivery, and interruption recovery."
catalog_version: "v0.1.0"
status: stable
example: true
domain: "Internal reporting software"
work_types: ["design-and-specification", "software-and-computational-development", "evaluation-and-assurance", "monitoring-and-operational-response"]
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
sources:
  - id: lessons
    resource: ../software-factory-learnings.md
    title: "Lessons from Software Factory"
---

# Example: software delivery factory

[Factory examples](./) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Fictional design case; proposed implementations; no assessments performed.** This applies the [source-backed lessons](../software-factory-learnings.md) to an invented reporting service. Its roles, thresholds, and infrastructure are illustrative local choices, not facts about the source repository.[^lessons]

## Factory profile

| Field | Design |
|---|---|
| Why / owner | Help analysts export an approved report without manually copying rows; product owner owns acceptance and follow-up |
| Inputs → artifacts | Accepted criteria, existing service, approved synthetic data → code change, tests, candidate package, evidence record, release record |
| Outcome | Intended analysts can select the right report, export it, and open the correct contents without assistance |
| Measure | In an authorized pilot within five working days of deployment, three designated analysts each complete the agreed task on synthetic data without assistance or content mismatch; this small sample supports only the pilot claim |
| Artifact acceptance | Export contains all and only authorized rows, with agreed columns and encoding; empty/error cases are usable; denied requests reveal no report data |
| Actors | Product owner sets intent and criteria; implementing agent changes code; reviewer checks claims and acceptance; release operator owns deployment; service owner owns observation and recovery |
| Workflow | Define one usable export slice → implement → review and verify candidate → authorized integration → promote package → observe pilot → retain evidence and next decision |
| Autonomy | Agent chooses implementation within accepted scope; stops dependent work at missing required evidence, unclear writer ownership, invalid authority, or unresolved external effects |
| Authority | Workspace edits and configured checks are permitted; integration and deployment follow separate recorded grants and repository/service gates; no implied production, spending, user-data collection, or delegation grant |
| Context | Existing authenticated service and release pipeline; potentially sensitive real reports; synthetic test data; no new runtime or additional agent required |

The implementing agent **performs** development that **produces** a candidate artifact. The factory **seeks** the analyst outcome. The evaluator **uses** revision-bound evidence to assess acceptance; the release operator acts under a distinct authority grant. Pilot participation and data use must be authorized before observation begins.

## Risk scenarios and control selections

All three selections are applicable, proposed, and not assessed. Before real implementation, create the [adoption record](../adoption.md#record-the-adoption) with each control's identity, catalog v0.1.0, exact catalog commit, and pinned source URL. Resolve cross-control references against that same revision.

| Scenario | Control / owner | Proposed implementation and reassessment trigger |
|---|---|---|
| A release report claims tests passed for a different candidate or conceals a blocked check | [Evidence traceability](../controls/evidence-traceability.md) / reviewer | Map material claims to candidate, configuration, commands, observations, reviewer, and gaps; reopen affected claims when their inputs change |
| A valid test result is treated as permission to deploy, or a different package is sent under an action-specific approval | [Bounded external action](../controls/bounded-external-action.md) / release operator | Pipeline and credential boundaries enforce actor, action, target, limits, validity, and any approval binding; inventory alternate paths and reassess after credential, actor, or destination changes |
| A correct file is counted as proof that analysts can complete their task | [Outcome verification](../controls/outcome-verification.md) / product owner | Declare pilot criteria first, retain artifact acceptance separately, record unmet or unobserved outcomes, and assign rework/follow-up; reassess if task, users, criteria, or observation period changes |

## Evidence and assessment plan

Retain candidate and configuration identities, criteria revision, fixture identities, check outputs, claim review, authority records without secrets, destination package identity, and pilot observations with access limits. Mark blocked and unrun checks in those records; assessment results use the catalog's separate vocabulary.

Run each selected control's complete assessment before claiming it passes:

- **Evidence traceability:** inspect all material claims; in a separate fixture, seed a fabricated citation, contradictory source, and unsupported claim omitted from the claim table. Acceptance must be withheld for each.
- **Bounded external action:** in an observable test environment, exercise valid and invalid grants, revocation, wrong actor/action/target/limits, changed action-specific approval payload, and alternate execution paths. Denied actions must produce no external effect.
- **Outcome verification:** use declared cases for met, unmet, and missing pilot evidence. Completed code with an unsuccessful pilot must be reported as an unmet outcome; when pilot observations are absent, the outcome must remain unverified with follow-up.

These are assessment plans. A passed structural check on this example cannot establish any operational result.

## Interruption and completion

Before deployment, record the candidate, destination, operation identifier where available, expected state, remaining limits, and outstanding checks. If the response is lost, mark the effect unknown and inspect authoritative destination state before retrying. Preserve historical attempts. If state cannot be reconciled, keep delivery blocked and escalate to the service owner. Recovery must preserve newer acknowledged data and stay within its own authority.

Completion requires applicable integration and delivery gates plus destination verification. If the pilot is pending, report software delivery and outcome observation separately and leave the observation obligation with its owner. A later candidate or configuration change invalidates the affected evidence.

## Coverage gaps

The three controls do not fully specify evaluator protection, verifier qualification, artifact promotion, duplicate prevention, safe rollback, or information protection. The mechanisms above illustrate local design needs; they are not additional catalog controls. Record these gaps before adoption and use the [candidate-control discussion](../software-factory-learnings.md#candidate-controls-for-discussion) to prioritize reusable definitions. Enforced boundary tests and representative operational evidence are still needed.

[^lessons]: [Lessons from Software Factory](../software-factory-learnings.md), with pinned upstream sources and evidence limits.
