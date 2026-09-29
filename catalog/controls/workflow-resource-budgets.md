---
type: Control
title: "Workflow resource budgets"
description: "Enforce aggregate resource limits across a job, its retries, and delegated work."
status: stable
family: reliability-and-recovery
sources:
  - id: AML.M0036
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L7016
    title: "AML.M0036: Limit AI Workload Resource Consumption"
  - id: AML.T0034.002
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L2302
    title: "AML.T0034.002: Agentic Resource Consumption"
---

# Workflow resource budgets

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Limit resource exhaustion and unbounded spending. Apply to jobs that invoke models, tools, retries, or child work. Limits must match the resources the workflow can consume; absence of financial billing does not eliminate time, memory, or capacity risk.

## Requirement

Before a job starts, assign enforceable limits and an accountable owner for relevant cost, time, compute, token, tool-call, concurrency, retry, and delegation resources. Count the entire job tree against shared limits. Prevent admission of work that would exceed a limit, or reserve a conservative maximum including in-flight work. Termination must stop new work and handle already-running work within the declared bound. The job cannot raise its own limits.

## Implementation

1. Identify all billable and capacity-consuming operations, measurement delays, cancellation behavior, and worst-case in-flight consumption.
2. Set limits, reservations, a stopping policy, and a safe disposition for partial artifacts before execution. Route increases to an authorized owner.
3. Use a shared budget ledger or equivalent atomic enforcement across children and retries. Propagate remaining limits without granting each child the full parent budget.
4. Record usage and denials, cancel or drain in-flight work as specified, and prevent resumed jobs from resetting consumption unintentionally.

## Expected outcome and assessment

Expected outcome: total measured or conservatively reserved use stays within the declared job limits.

Run a normal bounded task, repeated failures with retries, recursive delegation, concurrent children racing for the final allocation, and resume after interruption. Attempt a job-authored limit increase. Measure child and in-flight consumption after the stop signal.

**Pass:** the positive task succeeds, every stress case stays within its predeclared limit, and further work cannot bypass the stop. **Fail:** excess use, uncounted child work, unauthorized increases, or rejection of the within-budget positive case. **Inconclusive:** consumption or in-flight exposure cannot be bounded.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires reliable metering or conservative reservations and cancellation/admission mechanisms. Query rate limits alone do not bound one expensive job. [Outcome verification](outcome-verification.md) separately determines whether the bounded work was useful.

Addresses [delegated resource exhaustion](../risks/delegated-resource-exhaustion.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0036[^AML.M0036], AML.T0034.002[^AML.T0034.002]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0036]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0034.002]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
