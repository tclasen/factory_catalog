---
type: Control
title: "Risk estimate transparency"
description: "Make the assumptions, uncertainty, and decision sensitivity of risk estimates inspectable."
catalog_version: "v0.1.0"
status: draft
family: quality-and-validation
sources:
  - id: g180
    resource: https://publications.opengroup.org/g180
    title: "Open FAIR Risk Analysis Process Guide, Version 1.1"
  - id: g21a
    resource: https://publications.opengroup.org/g21a
    title: "Open FAIR Risk Analysis Example Guide"
  - id: g262
    resource: https://publications.opengroup.org/g262
    title: "The Mathematics of the Open FAIR Methodology, Version 1.1"
---

# Risk estimate transparency

[Adoption](../adoption.md) · [Control families](../control-families.md)

**Identity:** `controls/risk-estimate-transparency` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

## Purpose and applicability

Address unjustified precision or incomparable risk estimates used to rank actions. Apply when risk analysis informs a policy, resource allocation, supplier choice, or service design. Use qualitative descriptions where credible quantitative inputs are unavailable, with the uncertainty visible to the decision owner.

## Requirement

Before a risk estimate is used for a decision, record the scenario, affected parties and assets, time horizon, units, input provenance, uncertainty, model or method revision, dependencies, and decision threshold. Separate observations, expert estimates, and assumptions. Compare options on compatible scopes and test whether plausible input changes alter the preferred action. Report unresolved uncertainty and obtain an explicit disposition from the decision owner.

## Implementation

1. Describe cause, enabling condition, unwanted outcome, and affected parties using the existing [ontology](../ontology.md). Set a decision question before calculating.
2. Record each input’s origin, coverage, units, and uncertainty. Explain how ranges or probabilities were elicited; do not convert ordinal labels into probabilities without justification.
3. Retain the calculation or rubric, model version, dependence assumptions, and any random seed or run settings needed for reproduction. Check unit and time consistency.
4. Compare the current arrangement and alternatives. Test plausible extremes and correlated events; explain any double counting or exclusions.
5. Present the result and sensitivity to the decision owner. Record whether to act, gather evidence, run a bounded experiment, or defer; assign a review trigger.

Mechanism: documented analysis and a review gate. An automated calculation checks only the supplied model and inputs.

## Expected outcome and assessment

Expected outcome: every decision using a scoped risk estimate can inspect its basis and conditions under which the recommendation changes.

Reproduce one analysis. Test a supported estimate, a comparison mixing annual and monthly exposure, and a case where a plausible input change reverses the ranking.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the supported estimate is reproducible within a predeclared tolerance; the time mismatch blocks comparison until repaired; the reversal is disclosed and receives an explicit decision disposition.
- **Fail:** an unsupported point estimate is treated as certain, incompatible quantities are ranked without adjustment, or sensitivity that changes the decision is concealed.
- **Inconclusive:** input evidence, method, or decision records are unavailable.
- **Evidence:** scenario, input table, model or rubric revision, reproduction result, sensitivity results, reviewer, and decision disposition.

## Dependencies and limitations

Requires a competent analyst, inspectable evidence, and a decision owner. Model precision does not establish predictive accuracy. Some harms cannot be responsibly reduced to money; keep such constraints explicit. [Evidence traceability](evidence-traceability.md) supports input review. This does not implement or certify the Open FAIR methodology. Preserve adoption references using [adoption](../adoption.md).

## Source basis

G180 addresses applying Open FAIR risk analysis; G21A describes qualitative and quantitative comparisons and a business case using calibrated estimates; G262 introduces mathematics for constructing and checking models.[^g180][^g21a][^g262] The generic decision procedure above is the catalog’s proposal, not an extraction of the gated methodology.

[^g180]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g21a]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g262]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
