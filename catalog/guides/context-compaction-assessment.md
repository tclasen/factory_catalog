---
type: Guide
title: "Assess context preservation"
description: "Test that compression preserves constraints, corrections, unresolved effects, and the ability to resume work."
status: draft
sources:
  - id: ap-retention
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/per-type-retention-under-compaction.md
    title: "Agent Patterns: Per-type retention under compaction"
  - id: ap-reacquisition
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/reacquisition-cost-measurement.md
    title: "Agent Patterns: Reacquisition cost"
---

# Assess context preservation

[Adoption](../adoption.md) · [Restart and handoff records](../restart-and-handoff-records.md) · [Task tracking](durable-task-tracking.md)

## Procedure

Use when a continuing workflow compresses or replaces its context. Apply [durable work handoff](../controls/durable-work-handoff.md), [safe work resumption](../controls/safe-work-resumption.md), and [required guidance selection](../controls/required-guidance-selection.md). Agent Patterns' retention and reacquisition guidance informs these proposed fixtures.[^ap-retention][^ap-reacquisition]

1. Inventory authoritative scope, grants, acceptance criteria, source references, late corrections, completed work, remaining obligations, resource totals, and unresolved external effects before compression.
2. Store authoritative records outside the summary. Mark summaries as derived artifacts with source revisions. Recover canonical material before dependent action when a summary is insufficient; recheck current grants and state.
3. Compare an uncompressed run with repeated compression on the same task and criteria. For any task that can create external or irreversible effects, run each comparison in an isolated, resettable fixture with synthetic data or mock destinations that cannot reach production. Verify the fixture is reset between runs. Include a late correction, unresolved external effect, omitted constraint, and completed action that must not be repeated; represent external effects in the fixture rather than repeating live mutations.
4. Inspect the next decisions and observed fixture effects. Test absent canonical records: dependent work must stop with a recovery condition while independent authorized work may proceed. Assess production behavior separately, and only under applicable authority with a predeclared method that avoids duplicating effects.
5. Retain all runs, preserved/missing items, reacquisition calls, review effort, latency, and total cost. Report performance changes only under [measured process improvement](../controls/measured-process-improvement.md).

## Assessment

The procedure passes when valid work still completes, required constraints survive or are reacquired before use, limits persist, and uncertain effects are reconciled before retries. A prohibited effect, repeated completed mutation, forgotten correction, or false completion fails. Missing records or unobservable effects make the affected finding inconclusive.

Retain pre/post summaries, protected canonical references, configuration identities, action traces, measurements, evaluator, time, and dispositions. A good summary cannot substitute for [external authority enforcement](../controls/bounded-external-action.md); important historical events may still be needed for audit and recovery.

[^ap-retention]: Agent Patterns, per-type retention under compaction; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^ap-reacquisition]: Agent Patterns, reacquisition-cost measurement, pinned revision.
