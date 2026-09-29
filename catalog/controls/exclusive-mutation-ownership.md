---
type: Control
title: "Exclusive mutation ownership"
description: "Prevent conflicting or stale workers from mutating the same protected resource."
status: stable
family: workflow-and-coordination
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/queued-events.md
    title: "Software Factory: Exclusive mutation ownership basis"
---

# Exclusive mutation ownership

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when concurrent workers, retries, or delayed events can modify shared state. The protected resource may be a task record, file, database object, or external operation. Independent work on non-overlapping resources need not be serialized.

## Requirement

Define the mutation scope and enforce current ownership at its write boundary. Ownership transfer must prevent prior owners and stale attempts from writing. A preliminary read or expired lease alone must not authorize a later write. Use atomic revision checks, fencing tokens, or a demonstrated equivalent; serialize work when safe concurrent enforcement is unavailable.

## Implementation

1. Inventory shared mutation surfaces, processes, identities, and bypass paths, including services shared by separate worktrees.
2. Record authoritative owner, task generation, state revision, and lease if used. Claim ownership atomically against the expected state.
3. Make the receiving write boundary reject stale ownership/revisions. An advisory lease with no receiving enforcement is insufficient.
4. Before reassignment, revoke or fence old writers; preserve their unresolved effects for reconciliation.
5. Record accepted and rejected writes and the ownership transitions that explain them.

## Expected outcome and assessment

Expected outcome: only the current authorized owner can mutate a protected scope, and transfer cannot leave two effective writers.

Test a normal claim/write, simultaneous claims, a delayed write after lease expiry, a former worker returning after reassignment, and a bypass through an alternate tool. For serialized fallback, demonstrate the former writer has lost effective write access before replacement begins.

- **Pass:** current-owner writes succeed; conflicting and stale writes are rejected at the mutation boundary; no lost update or duplicate protected effect occurs in the tested interleavings.
- **Fail:** two owners can mutate the protected scope, a stale writer succeeds, or transfer relies solely on cooperative cessation when enforcement is required. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** a writer path or receiving boundary cannot be observed.
- **Evidence:** scope/path inventory, ownership and state revisions, enforcement configuration, interleaving traces, rejected/accepted operations, and final resource state.

## Dependencies and limitations

Requires an authoritative store and a write boundary able to enforce ownership, or effective serialization. [Bounded external action](bounded-external-action.md) governs grants; ownership never expands them. Use [reconcile before retry](reconcile-before-retry.md) for uncertain effects and [cancellation enforcement](cancellation-enforcement.md) for cancelled intent. Filesystem checkout isolation alone does not isolate credentials, ports, or services.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/queued-events.md).
