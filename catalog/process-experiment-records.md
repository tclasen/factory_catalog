---
type: Guide
title: "Process experiment records"
description: "Plan and record a bounded comparison before adopting a claimed process improvement."
status: stable
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/assets/templates/process-experiment.md
    title: "Software Factory: Process experiment records basis"
---

# Process experiment records

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## Use

Support [measured process improvement](controls/measured-process-improvement.md) using existing work records and telemetry. Use a comparison when benefit is uncertain; an explicit authorized correction need not wait for an experiment. Keep project-specific observations and permissions in the owner project.

## Suggested record

| Field | Content |
|---|---|
| Decision | Owner, problem/opportunity, observation sources, competing explanations, and adoption scope |
| Hypothesis | Proposed change, expected benefit, smallest alternative including simplification, and assumptions |
| Comparison | Baseline and treatment revisions; task cohort and selection; model, tool, host and instruction identities; ordering and prior exposure |
| Acceptance | Fixed outcome criteria, mandatory quality/safety gates, measurement definitions, repetitions, stop conditions, and keep/revise/revert thresholds declared before results |
| Budget | Total attempt/time/cost bounds, accounting boundaries including setup, retrieval, review and retries, and owner authority |
| Observations | Every attempted task, failures/blockers, accepted outcomes, defects/severity, review and repair effort, elapsed time, available usage/cost, and unknown telemetry |
| Interpretation | Per-task variation, missing observations, sample limits, confounders and deviations; distinguish observation from inference |
| Decision and follow-up | Keep, revise, revert, or defer with rationale; authorized adoption, reversal method, canonical owner, and review/removal trigger |

## Procedure

1. Establish the baseline and criterion revisions before inspecting treatment outcomes. Select tasks representative of the decision and record exclusions.
2. Compare conditions consistently. When several variables change, report the combined intervention and limit causal attribution.
3. Preserve failed and blocked work; report unavailable cost or timing as unknown. File sizes and reported reads are not measured token use.
4. Apply [outcome verification](controls/outcome-verification.md) to benefit claims and [evidence traceability](controls/evidence-traceability.md) to their support. Use [cumulative execution limits](controls/cumulative-execution-limits.md) across the whole experiment.
5. Decide using the predeclared criteria. If they legitimately change, version the change and treat affected comparisons as a new evaluation.
6. Record the adoption or reversal action within existing authority. Retain rejected alternatives and reconsider only with new evidence or changed conditions.

## Illustrative decision

A proposed review shortcut reduces elapsed time but misses a mandatory access-control defect. The result fails the fixed quality gate, so speed alone does not justify adoption. Retain both observations and choose revision or reversion. If cost was not observable, leave it unknown rather than claiming savings.

## Review the record

Check that another reviewer can recover the original plan, every attempted task, actual observations, and the decision rationale. A small uncontrolled trial supports a limited local decision; it does not establish a universal productivity improvement or authorize changes to a shared process.

## Source and scope

Adapted from the pinned Software Factory procedure.[^software-factory] The tables are suggested local record fields, not new required OKF frontmatter. Store actual records with their owning project and appropriate access and retention controls. A populated record is not evidence that its claimed observations are true. No operational assessment is asserted here.

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/assets/templates/process-experiment.md).
