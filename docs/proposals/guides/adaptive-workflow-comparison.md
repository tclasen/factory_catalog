---
type: Guide
title: "Compare learning and delegated workflows"
description: "Measure task ordering, retained learning, delegation overhead, and total accepted-work cost."
status: draft
sources:
  - id: ap-evals
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/verification/multi-run-shuffled-order-evaluation.md
    title: "Agent Patterns: Multi-run shuffled-order evaluation"
  - id: ap-delegation
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/patterns/agent-design/delegation-threshold-calibration.md
    title: "Agent Patterns: Delegation threshold calibration"
---

# Compare learning and delegated workflows

[Adoption](../../../catalog/adoption.md) · [Process experiment records](../../../catalog/process-experiment-records.md)

## Learning across tasks

Use [measured process improvement](../../../catalog/controls/measured-process-improvement.md) and [agent evaluation coverage](agent-evaluation-coverage.md) when retained experience changes later performance. Reset initial memory between independent replicates; preserve intentional learning within a stream. Compare fixed-memory and updating-memory conditions with recorded initial state, task order, model, tools, criteria, and repetitions. Test plausible alternative orders; preserve required production ordering when shuffling would invalidate the task. Retain failures and variation, not just the best run.[^ap-evals]

A gain that reverses under an applicable order cannot support an unconditional improvement claim. Missing comparable observations are inconclusive. Test the decision procedure with a supported bounded improvement, a reversal, and an omitted failing run; withholding the misleading claims and retaining the supported claim is the expected result.

## Delegation economics

Use [task configuration selection](../controls/task-configuration-selection.md) to compare direct execution, one agent, and delegated agents on one independent task set and one tightly coupled set. Hold outcome criteria and accounting boundaries constant. Record preparation, duplicate context/retrieval, synthesis, review, repairs, retries, compression reacquisition, elapsed time, and billed usage. State whether ceilings or realized spend are matched.[^ap-delegation]

Recommend an arrangement only within its observed task class and authority. More actors or fewer prompt tokens are not measures of accepted-work value. A faster configuration that fails required acceptance must not win on speed alone; unknown cost remains unknown. Retain decisions to keep, revise, or reject configurations alongside all results.

## Evidence and limits

Keep task/order/initial-state identities, resource counters, outcomes, reviewer effort, configuration revisions, comparison plan, evaluator, and time. The procedure fails if it hides a failed invariant, task-order reversal, or cost outside its declared boundary. It is inconclusive without the required comparable observations. These are proposed adaptations of Agent Patterns guidance, not reproduced performance findings. Assess the selected controls against their complete criteria.

[^ap-evals]: Agent Patterns, multi-run shuffled-order evaluation; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^ap-delegation]: Agent Patterns, delegation threshold calibration, pinned revision.
