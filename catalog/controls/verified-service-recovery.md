---
type: Control
title: "Verified service recovery"
description: "Verify actual service and data recovery within incident authority."
status: draft
family: reliability-and-recovery
sources:
  - id: workflows-operations
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md
    title: "Operations, maintenance and retirement"
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
---

# Verified service recovery

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

The requirement and assessment below are catalog-proposed synthesis. The cited source files were unavailable at their pinned revision when checked, so their contents have not been verified and this is not a substantiated adaptation claim.[^workflows-operations][^policies-delivery]

## Purpose and applicability

Apply to an authorized running service after a health failure, incident, or failed activation.

## Requirement

Confirm impact, contain within existing authority, and select a bounded repair or compatible rollback. Before activation, establish that acknowledged user changes and consent obligations will be preserved. Verify real health and required data invariants after recovery. Observation gaps remain unknown until fresh evidence exists; recovery does not turn a failed feature into delivered work.

## Implementation

1. Record the affected service/artifact, observed impact, incident owner, authority, recovery targets, and limits.
2. Inspect active state before action; reconcile ambiguous activation through [reconcile before retry](reconcile-before-retry.md).
3. Assess code/data compatibility and later acknowledged changes before rollback; stop when safe recovery cannot be established.
4. Check real service behavior and data after repair; retain the failed candidate and remaining corrective work in the work record.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: recovery restores verified service without silently losing acknowledged state.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| An authorized repair restores required health and data invariants | Recovery is reported with fresh observations. |
| A proposed rollback would discard newer acknowledged changes | Activation is withheld until a compatible recovery path exists. |
| An observer was stopped during an incident | The gap is reported as unknown; fresh checks are required before a recovery claim. |
| The service restarts but a required journey still fails | Recovery remains incomplete. |

- **Pass:** All cases honor authority and data invariants, and recovery claims have current functional evidence.
- **Fail:** Restart alone is called recovery, acknowledged state is lost, or incident urgency expands authority.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Incident observations, action grant, active/candidate identities, compatibility assessment, data checks, and post-recovery health results.

## Dependencies and limitations

Requires observable health, defined invariants, and a safe isolated assessment target. Backup restoration is outside this control’s boundary; [independent restoration](independent-restoration.md) is a separate draft proposal, not a required stable dependency. Simulated recovery cannot qualify the production environment.

[^workflows-operations]: [Operations, maintenance and retirement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md), cited at commit `70cfad0de635197f36f14e5276dec145483c5128`. This exact path returned HTTP 404 on 2026-09-29; the source content and its relationship to this proposal remain unverified.
[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md), cited at commit `70cfad0de635197f36f14e5276dec145483c5128`. This exact path returned HTTP 404 on 2026-09-29; the source content and its relationship to this proposal remain unverified.
