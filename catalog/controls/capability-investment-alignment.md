---
type: Control
title: "Capability investment alignment"
description: "Tie proposed investments to a defined business ability, an observed gap, and a measurable beneficiary outcome."
status: draft
family: purpose-and-accountability
sources:
  - id: g211
    resource: https://publications.opengroup.org/g211
    title: "TOGAF Series Guide: Business Capabilities, Version 2"
  - id: g233
    resource: https://publications.opengroup.org/g233
    title: "TOGAF Series Guide: Business Capability Planning"
---

# Capability investment alignment

[Adoption](../adoption.md) · [Control families](../control-families.md)

## Purpose and applicability

Address investment in tools, staffing, or training that has no demonstrated connection to the ability an organization needs. Apply to portfolio proposals, public service improvements, education programs, procurement, and factory redesign. Routine work under an already approved investment can reference its current assessment.

## Requirement

Before approving an investment recommendation, name the business ability it should improve, its beneficiary, current and target performance, evidence for the gap, accountable owner, affected activities, and alternatives. Distinguish the ability from a product or department. Preserve unknowns and dependencies; a proposal with an unsubstantiated gap must be returned for investigation or explicitly presented as an experiment with a bounded budget and success criteria.

## Implementation

1. Name an investment owner and a reviewer who can question the business case. Describe the ability without requiring a particular supplier or implementation.
2. Record observations of current performance, their period and coverage, and the target outcome. Label estimates and assumptions.
3. Map the ability to the people, activities, information, and resources needed to exercise it. Record shared dependencies and competing demands.
4. Compare at least the proposed change and retaining the current arrangement, including costs, capacity, benefits, and disbenefits. Include a nontechnical alternative when credible.
5. Retain the recommendation, decision rationale, funding limits, and follow-up date. Check benefit claims using [outcome verification](outcome-verification.md).

Mechanism: a human investment review supported by a versioned capability and proposal record. A completed map alone does not enforce the decision gate.

## Expected outcome and assessment

Expected outcome: every recommendation in the declared portfolio scope traces to an evidenced gap or a clearly bounded experiment.

Inspect a declared proposal set and reproduce the reviewer’s disposition. Exercise three fixtures: a purchase justified only by a product name; a training proposal with observed demand and a measurable target; and a proposal dependent on staff capacity already allocated elsewhere.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the first is returned or reframed as an experiment; the second is eligible for a reasoned decision; the third exposes the capacity conflict and withholds an unconditional recommendation until resolved. Every inspected record meets the requirement.
- **Fail:** an unsupported benefit or unresolved critical dependency is represented as established readiness, or a required record is omitted.
- **Inconclusive:** evidence needed to evaluate the records cannot be inspected.
- **Evidence:** proposal revision, gap observations, dependency map, alternatives, reviewer dispositions, and follow-up owner/date.

## Dependencies and limitations

Requires an owner able to change priorities and access to performance evidence. This supports the planning outcome; it does not establish return on investment or authorize spending. Use [bounded external action](bounded-external-action.md) for purchases and commitments. The [mapping guide](../guides/capability-value-information-mapping.md) supplies a reusable record. Preserve exact revisions through [adoption](../adoption.md).

## Source basis

G211 describes capability maps linked to other business viewpoints; G233 addresses introducing and refining capability planning.[^g211][^g233] The requirement, decision gate, and fixtures above are this catalog’s proposed synthesis from public descriptions, not quoted TOGAF requirements or a conformity assessment.

[^g211]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g233]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
