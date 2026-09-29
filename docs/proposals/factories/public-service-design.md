---
type: Factory Example
title: "Public service design factory"
description: "A fictional team produces and evaluates a cross-agency service design grounded in resident needs."
status: draft
sources:
  - id: g236
    resource: https://publications.opengroup.org/g236
    title: "GovStack Ecosystem Reference Architecture"
example: true
domain: "Public administration"
activities: ["elicit stakeholder concerns", "map service activities", "compare service options", "review acceptance evidence"]
control_selections:
  - control: ../controls/stakeholder-concern-validation.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/capability-investment-alignment.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/value-stream-stage-acceptance.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/information-meaning-agreement.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/interoperability-acceptance.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Public service design factory

**Fictional design; proposed implementations; no operational assessments performed.**

[Ontology](../../../catalog/ontology.md) · [Adoption](../../../catalog/adoption.md)

## Factory profile

| Field | Proposed design |
|---|---|
| Purpose / owner | Produce a reviewable design for a municipal assistance referral service; service design lead owns the work |
| Beneficiaries | Residents and staff who need understandable referral status across participating agencies |
| Inputs → outputs | Authorized interviews, service policies, aggregate case observations → concern map, service stages, information agreement, option comparison, pilot assessment plan |
| Intended outcome | In a separately authorized pilot, participants can identify the next responsible office and unresolved steps in at least 90% of 20 fictional referral cases; accessibility findings remain explicit |
| Actors | Researchers gather evidence; an analyst or AI assistant organizes approved material; agency representatives review; a service owner decides readiness |
| Workflow | Discover concerns → map abilities and stages → agree meanings → compare options → review a simulated exchange → approve or return the design |
| Autonomy | Assistant may classify and draft; stops at personal-data access, unresolved policy conflict, or missing stakeholder representation |
| Authority | Research and drafting only within approved resources; no benefit eligibility decisions, agency commitments, resident messaging, or production-system changes |
| Context | Cross-agency responsibilities, differing terms and service rules, accessibility needs; use fictional records in tests |

The broader digital-government opportunity is motivated by G236’s description of architecture and reusable building blocks.[^g236] The workflow and thresholds are illustrative catalog choices, not GovStack requirements.

## Activities and relationships

The factory **performs** discovery, planning, specification, and assurance activities. Researchers **produce** a concern map; agency representatives **consume** it to review requirements. The analyst **produces** the stage map and exchange definition. These activities **contribute to** the intended resident-understanding outcome; an attractive blueprint alone does not establish that outcome.

Apply the [mapping procedure](../guides/capability-value-information-mapping.md) before choosing a technology. Keep “can coordinate referrals” separate from “purchased a case-management system”.

## Control selections and rationale

| Risk or objective | Selected control and proposed mechanism |
|---|---|
| Residents unable to participate are treated as agreeing | [Stakeholder concern validation](../controls/stakeholder-concern-validation.md): engagement owner records participation, representation limits, and unresolved concerns |
| A tool purchase is justified without an observed service gap | [Capability investment alignment](../controls/capability-investment-alignment.md): service owner reviews gap evidence and a current-arrangement alternative |
| Agency A closes a case when agency B has not accepted it | [Value stream stage acceptance](../controls/value-stream-stage-acceptance.md): distinct sent, accepted, rejected, and pending states with owners |
| “Eligible” has incompatible meanings across agencies | [Information meaning agreement](../controls/information-meaning-agreement.md): stewards agree definitions and prohibited inferences |
| Technical exchange works but no party owns failed referrals | [Interoperability acceptance](../controls/interoperability-acceptance.md): jointly reviewed simulated cases and failure responsibilities |
| A draft misstates policy or interview findings | [Evidence traceability](../../../catalog/controls/evidence-traceability.md): researcher checks material claims against authorized evidence |
| Design delivery is mistaken for a useful service | [Outcome verification](../../../catalog/controls/outcome-verification.md): a later pilot tests understanding against predeclared criteria |

## Assessment plan

Design lead runs each selected control’s positive and negative fixtures on fictional cases and retains revisions, expected and observed dispositions, reviewer, and limits. Include an absent resident group, an incompatible status definition, and a referral whose receiving agency is unavailable. No case may silently disappear or imply stakeholder agreement without evidence.

The pilot owner separately recruits suitable participants under an approved engagement process and observes the stated task. If fewer than 18 of 20 cases meet the criterion, report the outcome unmet; if observations are unavailable, report it unverified. This tiny illustrative pilot cannot establish population-wide effectiveness or equitable access.

## Remaining gaps and reassessment

A deployed service also needs applicable privacy, accessibility, retention, appeal, security, and operational controls. Local policy and authorized domain review determine eligibility rules; this design does not supply them. Reassess on changed agencies, populations, data access, terminology, or external-action capability.

All selections remain proposed and not assessed. Before implementation, record the exact source commit and URL for each selected control through [adoption](../../../catalog/adoption.md). The service owner owns applicability review and local adaptations.

[^g236]: G236, GovStack Ecosystem Reference Architecture; public product description accessed 2026-09-29 UTC; full guide not reviewed.
