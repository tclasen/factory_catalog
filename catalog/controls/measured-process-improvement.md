---
type: Control
title: "Measured process improvement"
description: "Base adoption of a process change on declared comparisons that retain quality, failures, and operating costs."
status: stable
family: monitoring-and-improvement
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/measurement.md
    title: "Software Factory: Measured process improvement basis"
---

# Measured process improvement

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when a claimed improvement in workflow, model, tool, or instructions is used to justify adoption. Explicit authorized corrections can take effect immediately; this control applies to claims of measured benefit and decisions based on them.

## Requirement

Before observing comparative results, record the decision, hypothesis, baseline/treatment, representative tasks, fixed acceptance criteria, resource limits, and keep/revise/revert conditions. Retain unsuccessful and blocked tasks, quality regressions, human effort, and available resource measurements. Record unavailable telemetry as unknown. Adopt only within the evidence's scope and existing authority; do not claim causation or general benefit beyond the comparison design.

## Implementation

1. Use the [process experiment record](../process-experiment-records.md) and nominate a decision owner.
2. Select comparable task classes and pin relevant model/tool/instruction identities. Record ordering, prior exposure, and concurrent changes.
3. Keep outcome criteria constant. Predeclare repetitions and stopping conditions proportionate to the decision; use the same accounting boundaries across treatments.
4. Collect outcomes, defects, elapsed time, review/repair effort, and available costs including retries and evaluation. Retain variation and contrary observations.
5. Apply the decision conditions; record authorized adoption scope, reversal method, and reconsideration trigger. Preserve rejected alternatives and their reasons.

## Expected outcome and assessment

Expected outcome: process decisions reflect accepted outcomes and costs, and speed cannot conceal degraded required quality.

Audit a complete comparison against its predeclared plan. Exercise decision fixtures for faster execution with a severe regression, missing cost telemetry, a supported improvement, and insufficient comparable observations. These synthetic cases test reporting and disposition, not real productivity.

- **Pass:** the regression does not justify adoption on speed alone; missing values stay unknown; supported benefit is limited to tested conditions; insufficient evidence yields revision, deferral, or an explicitly bounded experimental decision without a proven-benefit claim.
- **Fail:** failed tasks disappear, criteria are silently relaxed, unknown measurements become zero, or adoption claims exceed evidence or authority. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** the original plan or material observations cannot be inspected.
- **Evidence:** dated plan, task cohort, identities, all outcomes, resource measurements, deviations, decision rationale, owner and reversal/review conditions.

## Dependencies and limitations

Use [outcome verification](outcome-verification.md) for success criteria and [evidence traceability](evidence-traceability.md) for supporting claims. [Cumulative execution limits](cumulative-execution-limits.md) bounds the experiment. Small or uncontrolled comparisons support limited conclusions; document size and agent-reported reads do not measure tokens or latency. Project findings require new applicability analysis before becoming shared rules.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/measurement.md).
