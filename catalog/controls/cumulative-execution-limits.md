---
type: Control
title: "Cumulative execution limits"
description: "Preserve and enforce applicable resource allowances across retries, restarts, and handoffs."
catalog_version: "v0.1.0"
status: stable
family: reliability-and-recovery
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/execution.md
    title: "Software Factory: Cumulative execution limits basis"
---

# Cumulative execution limits

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

**Identity:** `controls/cumulative-execution-limits` · **Catalog:** v0.1.0 · **Family:** `reliability-and-recovery`

## Purpose and applicability

Apply when work has attempt, time, spending, or other resource limits. Prevent interruption or delegation from silently granting a fresh allowance. This control preserves actual limits; it does not invent quotas for every task.

## Requirement

Associate applicable limits and cumulative usage with a durable task identity. Before starting work that consumes an allowance, determine and reserve enough remaining capacity, or use an enforceable bound that prevents overrun. Carry usage across attempts, resumed sessions, redeliveries, and delegated work. Stop when exhausted or when uncertain usage prevents establishing a safe remaining allowance. Only an authorized owner may revise limits, with the prior usage retained.

## Implementation

1. Record issuer, scope, units, limit, and accounting semantics: for example wall-clock deadline versus active runtime, and what counts as an attempt.
2. Choose a durable ledger or maintained host budget facility. Account for outstanding reservations as well as completed consumption.
3. Charge or reserve before dispatch where necessary. With concurrent consumers, use atomic reservations or serialize dispatch.
4. On failure or lost telemetry, reconcile usage or conservatively retain the reservation. Release it only with evidence that consumption did not occur.
5. Carry the ledger reference in the [restart record](../restart-and-handoff-records.md). Escalate exhaustion with actual usage and the smallest needed decision.

## Expected outcome and assessment

Expected outcome: authorized work can proceed within its allowance, and no retry or handoff resets the budget.

Use declared synthetic limits. Test normal consumption, exact exhaustion, restart near exhaustion, duplicate event delivery, delegated consumption, unknown usage after a timeout, and an authorized limit increase. Where concurrency exists, race two reservations against the final available unit.

- **Pass:** usage and reservations remain cumulative; only affordable work starts; uncertainty cannot create extra capacity; concurrent claims cannot overdraw; authorized increases preserve history.
- **Fail:** a restart resets usage, dispatch exceeds a required bound, unknown usage becomes zero without evidence, or a worker expands its own allowance. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** accounting or actual consumption cannot establish whether the bound held.
- **Evidence:** limit/grant revisions, ledger entries, reservations, dispatch/stop decisions, observed consumption, and interruption/concurrency traces.

## Dependencies and limitations

Needs reliable accounting and enforcement suited to the resource. Unbounded external costs cannot be strictly limited by instructions alone; use provider caps or bounded operations and disclose remaining exposure. [Bounded external action](bounded-external-action.md) governs spending authority. [Reconcile before retry](reconcile-before-retry.md) addresses effects, which may differ from billed attempts. Atomic reservations are a catalog implementation refinement of the source's cumulative-limit rule.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/execution.md).
