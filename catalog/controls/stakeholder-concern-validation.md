---
type: Control
title: "Stakeholder concern validation"
description: "Check that a proposed service or change addresses affected parties and preserves unresolved concerns."
status: draft
family: intake-and-work-definition
sources:
  - id: g176
    resource: https://publications.opengroup.org/g176
    title: "TOGAF Series Guide: Business Scenarios"
  - id: g206
    resource: https://publications.opengroup.org/g206
    title: "TOGAF Series Guide: Organization Mapping"
  - id: i121
    resource: https://publications.opengroup.org/i121
    title: "A Handbook for the Consensus Decision-Making Process"
---

# Stakeholder concern validation

[Adoption](../adoption.md) · [Control families](../control-families.md)

## Purpose and applicability

Address plans that reflect a sponsor’s preferences while omitting the needs or burdens of affected parties. Apply to policy design, public services, organizational change, education programs, and cross-team factory design. Scale engagement to consequences and identify groups whose direct participation is unavailable.

## Requirement

Before approving a service design or change recommendation, identify affected parties, the scenarios they face, their desired outcomes and constraints, and how those concerns influence requirements and acceptance criteria. Record engagement evidence, representation limits, conflicting concerns, and a decision owner’s disposition. Silence, nonresponse, and AI-generated personas must not be recorded as stakeholder agreement.

## Implementation

1. Identify beneficiaries, operators, contributors, excluded populations, and parties that bear costs or risks. Assign an engagement owner.
2. Gather concerns through a suitable accessible process. Record who participated, what they were asked, and which views are inferred or unrepresented; protect sensitive contributions.
3. Build scenarios linking actors, conditions, work, artifacts, and outcomes. Trace each material concern to a requirement, an explicit scope exclusion, or an unresolved issue.
4. Review scenarios with participants or clearly identified representatives. Keep disagreement and representation limits visible rather than compressing them into a false consensus.
5. Obtain the authorized decision owner’s disposition and conditions for proceeding. Reopen engagement when the service, population, or consequence changes.

Mechanism: facilitated review with a versioned concern-to-decision record. Participation does not confer authority to approve the proposal.

## Expected outcome and assessment

Expected outcome: every material concern identified in the assessment scope has a traceable disposition, and claims of agreement match the engagement evidence.

Inspect a proposed change and independently check its affected-party list against the operating context. Test documented agreement, a material objection, and an absent group represented only by a generated persona.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** agreement is attributed only to actual participants; the objection remains visible with an authorized disposition; the absent group is marked unrepresented and the decision records that limit and required follow-up.
- **Fail:** an omitted material concern is found without disposition, dissent is rewritten as agreement, or a persona/nonresponse is treated as consent.
- **Inconclusive:** engagement or decision records cannot be inspected sufficiently.
- **Evidence:** affected-party scope, engagement method and records, scenarios, concern mappings, representation limits, and decision disposition.

## Dependencies and limitations

Requires appropriate engagement methods and a decision owner. A well-documented process can still exclude people or produce a poor decision; assess the resulting outcome separately. This does not replace consent or legally required consultation. [Outcome verification](outcome-verification.md) evaluates results; [bounded external action](bounded-external-action.md) governs commitments. Pin adoption through [adoption](../adoption.md).

## Source basis

G176 connects business scenarios to requirements; G206 identifies organizational participants; I121 provides consensus-process guidance for Open Group working bodies.[^g176][^g206][^i121] Applying these themes to broader stakeholder review is the catalog’s synthesis, not a claim that the handbook governs other organizations.

[^g176]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g206]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^i121]: Public product description refreshed November 2025, accessed 2026-09-29 UTC; full handbook not reviewed.
