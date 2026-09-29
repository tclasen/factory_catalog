---
type: Guide
title: "Record risk analyses for inspectable decisions"
description: "Separate scenarios, estimates, uncertainty, control assumptions, and authority to accept risk."
status: draft
sources:
  - id: c250
    resource: https://publications.opengroup.org/c250
    title: "Risk Analysis (O-RA), Version 2.1"
  - id: c251
    resource: https://publications.opengroup.org/c251
    title: "Risk Taxonomy (O-RT), Version 3.1"
  - id: g21a
    resource: https://publications.opengroup.org/g21a
    title: "Open FAIR™ Risk Analysis Example Guide"
---

# Record risk analyses for inspectable decisions

[Research map](../open-group-standards-opportunities.md) · [Ontology](../ontology.md)

## Source and boundary

Open FAIR pairs a risk analysis standard with a risk taxonomy for information-security risk.[^c250][^c251] Its example guide describes qualitative/quantitative comparison and calibrated estimates.[^g21a] This catalog procedure is inspired by that separation. It is not a complete Open FAIR method or a validated model. Applying it to procurement delay, operational disruption, or environmental decisions requires a domain owner to validate the scenario and loss model.

## Build the decision record

1. State the decision, alternatives, scope, horizon, affected parties, and authorized decision maker. Describe a cause acting through a condition to produce a specific loss; avoid a bare label such as “supplier risk”.
2. Separate observed incidents, estimates, and assumptions. Define exposure units, event counting rules, loss categories, and whether consequences overlap.
3. Apply [risk estimate assumptions](../controls/risk-estimate-assumptions.md). Preserve input ranges/distributions, sources, calculation revision, and sensitivity analysis. An ordinal high/medium/low label is not a measured probability.
4. Compare alternatives on a common horizon and basis. Explain which mechanism might change event occurrence or consequence and what evidence supports that assumption. Selecting a control is not evidence of its effect.
5. Use [risk estimate transparency](../controls/risk-estimate-transparency.md) for the decision-facing comparison and disposition. Present uncertainty and missing evidence to the decision owner. Record the owner's decision separately from the analyst's estimate and separately from any [authority grant](../controls/bounded-external-action.md).
6. Set reassessment triggers: new incident data, altered exposure, changed supplier, control failure, or revised decision horizon.

## Record shape and graph links

| Record | Contents and relationship |
|---|---|
| Scenario | Cause, condition, artifact/outcome threatened, affected parties |
| Estimate | Units, horizon, method/version, assumptions, evidence, uncertainty, exclusions |
| Treatment option | Selected control revision or other response; proposed causal effect and evidence gap |
| Decision | Authorized owner, selected option, conditions, accepted uncertainty, review date |
| Assessment | Target implementation and revision, observed effects, method, evidence, pass/fail/inconclusive |

Use [evidence traceability](../controls/evidence-traceability.md) for cited inputs. A loss estimate is an analytical artifact, not an assessment pass. An assessment can inform a new estimate without granting permission to accept risk.

## Synthetic illustration

Suppose a procurement team estimates two delivery interruptions per year and 10–30 staff-hours of rework per interruption. Under a deliberately simple fixed-frequency model, expected annual rework lies between 20 and 60 hours. These are invented inputs, not observed rates, a probability interval, or an Open FAIR implementation. Show the independence and linearity assumptions; clustered interruptions, capacity constraints, and overlapping rework can invalidate the calculation.

Before a real decision, test a changed horizon, overlapping loss categories, a missing source, and a treatment option with no effectiveness evidence. The estimate must expose or reject these issues under [risk estimate assumptions](../controls/risk-estimate-assumptions.md). Monetary valuation, safety judgments, and formal risk acceptance require their own authorized expertise. No operational risk analysis was executed for this guide.

[^c250]: The Open Group, Risk Analysis (O-RA), Version 2.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c251]: The Open Group, Risk Taxonomy (O-RT), Version 3.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^g21a]: The Open Group, Open FAIR™ Risk Analysis Example Guide; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
