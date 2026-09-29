---
type: Control
title: "Cancellation enforcement"
description: "Stop new effects after cancellation and reconcile in-flight work without reopening cancelled intent."
status: stable
family: workflow-and-coordination
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/queued-events.md
    title: "Software Factory: Cancellation enforcement basis"
---

# Cancellation enforcement

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when queued, recurring, delegated, or asynchronous work may outlive the user's current intent. Prevent delayed events or stale workers from restarting cancelled activity.

## Requirement

Persist cancellation in authoritative task state and enforce it before dispatch and at each controllable consequential effect boundary. Reject delayed callbacks and stale generations that would reopen cancelled work. On cancellation, stop new effects and reconcile those already in flight; report their actual outcome without claiming they were undone. Renewed work requires explicit authorized intent with a new generation. Cancellation does not itself authorize destructive compensation.

## Implementation

1. Assign cancellation authority and define task identity, generation, terminal states, and the point beyond which an effect cannot be withdrawn.
2. Couple cancellation/state revision checks to dispatch or mutation using an atomic guard or host-enforced equivalent; close the check-then-act race where controllable.
3. Revoke or fence workers and cancel queued deliveries as supported. Ensure redelivery cannot reset state or allowances.
4. Inventory in-flight operations at cancellation; query authoritative results and record remaining observation or recovery duties.
5. Preserve terminal cancellation while attaching late evidence. A cancellation request after recorded completion must not erase completion or imply reversal; record the request and any remaining duties. Require a new authorized generation before new effects.

## Expected outcome and assessment

Expected outcome: cancellation prevents new controllable effects, and late results update evidence without reviving the cancelled task.

Test cancellation before dispatch, between claim and effect, during an already submitted effect, after completion, and before a stale worker returns. Deliver duplicate callbacks and a new explicitly authorized generation. Observe effect initiation at the actual boundary.

- **Pass:** cancelled work initiates no new effects after the cancellation boundary; in-flight results are reconciled honestly; duplicate/stale callbacks preserve terminal state; cancellation after completion does not rewrite observed effects; an authorized new generation can run without reviving old events.
- **Fail:** a cancelled generation starts a new effect, cancellation is silently reversed, or unverified rollback is reported as having undone an effect. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** boundary ordering or in-flight outcomes cannot be established; record remaining reconciliation duties.
- **Evidence:** cancellation issuer/time, task generations and revisions, dispatch/effect traces, stale-event decisions, final state, and unresolved operation records.

## Dependencies and limitations

Depends on [exclusive mutation ownership](exclusive-mutation-ownership.md) where workers compete and [reconcile before retry](reconcile-before-retry.md) for ambiguous effects. An already accepted external operation may be irreversible. Document that boundary explicitly; a cooperative prompt stop alone does not enforce cancellation across independent workers or tools.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/queued-events.md).
