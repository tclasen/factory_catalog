---
type: Control
title: "Durable work handoff"
description: "Preserve enough current intent and state for another session to resume work correctly."
status: stable
family: workflow-and-coordination
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/durable-resumption.md
    title: "Software Factory: Durable work handoff basis"
---

# Durable work handoff

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when interruption, session boundaries, or a change of owner could lose consequential state. Preserve the next safe action and unfinished obligations without requiring an orchestration service for ordinary work.

## Requirement

Maintain an accessible, versioned record of accepted intent, owner, relevant revisions, observations, uncertain effects, authority references, cumulative limits, blockers, and next action. Save intent before consequential effects and observations afterward. On resumption, reconcile the record with current instructions, cancellation, ownership, actual local and external state, and evidence validity before mutation. Explicitly handle incompatible record formats and unknown state.

## Implementation

1. Use the existing project record and the [restart and handoff guide](../restart-and-handoff-records.md); assign its owner and permitted readers. The [task-tracking procedure](../guides/durable-task-tracking.md) shows how to keep remaining obligations discoverable across several deliveries.
2. Record unrelated edits and outstanding writers/processes that must be preserved. Store references to authority, never credential values.
3. Use atomic record replacement where supported; state the crash-loss window and which observations may be missing after failure.
4. Preserve operation identity and intent before effects. Record observed completion separately from remaining acceptance or delivery duties.
5. At resume, verify fresh ownership and authority, reconcile effects, invalidate stale evidence, and choose the next unfinished action. Migrate an incompatible record through a validated procedure or stop dependent work.

## Expected outcome and assessment

Expected outcome: a new session can resume without inventing permission, losing limits, duplicating effects, or discarding unrelated work.

Give a fresh reader only the durable record and authorized source systems. Test interruption before submission and after an effect but before recording its response. Also change instructions, cancel work, introduce unrelated edits, invalidate evidence, and provide an incompatible record format.

- **Pass:** the reader identifies current intent, owner, remaining duties and allowance; preserves unrelated work; reconciles uncertain effects; respects current restrictions; blocks unreadable or unresolved state.
- **Fail:** resumption acts on stale authority, omits a required obligation, resets limits, repeats an unresolved effect, or overwrites unrelated work. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** necessary records or source state cannot be inspected to determine the resumed behavior.
- **Evidence:** checkpoints before/after interruption, record versions, reconciliation observations, reader decisions, preserved-file comparisons, and operation history.

## Dependencies and limitations

Use [reconcile before retry](reconcile-before-retry.md), [assessment evidence validity](assessment-evidence-validity.md), and [cumulative execution limits](cumulative-execution-limits.md) for their separate requirements. Concurrent handoff also needs [exclusive mutation ownership](exclusive-mutation-ownership.md). A saved file does not restart an agent or enforce a write boundary.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/durable-resumption.md).
