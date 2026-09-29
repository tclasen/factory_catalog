---
type: Control
title: "Risk estimate assumptions"
description: "Make quantitative risk estimates reproducible and expose uncertainty that can change the decision."
catalog_version: "v0.1.0"
status: draft
family: quality-and-validation
sources:
  - id: c250
    resource: https://publications.opengroup.org/c250
    title: "Risk Analysis (O-RA), Version 2.1"
  - id: c251
    resource: https://publications.opengroup.org/c251
    title: "Risk Taxonomy (O-RT), Version 3.1"
---

# Risk estimate assumptions

**Identity:** `controls/risk-estimate-assumptions` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

[Adoption](../adoption.md) · [Research map](../open-group-standards-opportunities.md)

## Purpose and applicability

Prevent precise-looking risk estimates from concealing unsupported inputs, incompatible scopes, or uncertain treatment effects. Apply when a quantitative estimate informs a consequential choice. Qualitative-only work can be excluded with recorded rationale, but ordinal ratings must not be presented as measured quantities. Open FAIR's analysis/taxonomy separation motivates this independently authored catalog requirement.[^c250][^c251]

## Requirement

Before accepting an estimate, record the scenario, affected parties, time horizon, units, input evidence, assumptions, uncertainty, calculation method/version, and exclusions. A competent reviewer must reproduce the result within a predeclared tolerance, check for incompatible units and overlapping consequences, and inspect how material assumptions affect the decision. Unsupported inputs and unverified control effects must remain explicit estimates or unknowns. Missing material evidence must prevent presentation as a validated result.

## Implementation

1. Declare the decision, baseline and alternatives, estimation scope, and responsible analyst/reviewer before calculation.
2. Separate measurements, elicited estimates, and assumptions. Retain ranges/distributions and their rationale; do not turn “unknown” into zero.
3. Pin data, model/code/spreadsheet revision, parameters, and relevant random seed/sampling settings. Define units, horizon, dependence assumptions, and aggregation rules.
4. Reproduce calculations and vary each decision-sensitive assumption over its justified range. If the preferred option changes, disclose the change and the evidence needed to resolve it.
5. Label results by what the method supports. Record owner disposition of uncertainty and triggers for recalculation. Keep risk acceptance authority separate from model review.

Mechanism: analytical review plus reproducible computation. [Risk decision records](../guides/risk-analysis-decision-records.md) provide context. [Evidence traceability](evidence-traceability.md) supports the inputs; a plausible model explanation alone is not an independent reproduction.

## Expected outcome and assessment

Expected outcome: the assessed estimate can be reproduced and no material unsupported assumption is hidden from its decision maker.

Review a declared estimate and reproduce it using retained inputs. Test fixtures with a yearly/monthly mismatch, a missing material input, duplicated loss counted twice, and a claimed control reduction with no evidence. Include a supported estimate with disclosed uncertainty as a positive case.

- **Pass:** the scoped record meets the requirement; reproduction is within the predeclared tolerance; all negative cases are rejected or corrected before acceptance; the positive case is accepted with its uncertainty intact.
- **Fail:** reproduction fails, material assumptions are hidden, incompatible/duplicated quantities remain, or an unsupported treatment effect is presented as observed.
- **Inconclusive:** necessary inputs, model, competence evidence, or observations cannot be inspected.
- **Evidence:** scenario and model revisions, input provenance, tolerance, reproduction result, sensitivity results, reviewer identity, fixture outcomes, decision packet and dispositions.

## Dependencies and limitations

Requires an appropriate model and competent reviewer. Passing demonstrates analytical discipline within the assessed scope; it does not validate future event rates or guarantee a better decision. Non-security use needs domain validation. The requirement is not a complete Open FAIR method, and no implementation has passed it as part of this contribution.

[^c250]: The Open Group, Risk Analysis (O-RA), Version 2.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c251]: The Open Group, Risk Taxonomy (O-RT), Version 3.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
