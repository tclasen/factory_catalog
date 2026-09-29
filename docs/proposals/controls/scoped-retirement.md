---
type: Control
title: "Scoped retirement"
description: "Verify authorized retirement while preserving shared assets and retention obligations."
status: draft
family: information-protection
sources:
  - id: workflows-operations
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md
    title: "Operations, maintenance and retirement"
  - id: policies-governance
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md
    title: "Scope, authority and security"
---

# Scoped retirement

[Adoption](../../../catalog/adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^workflows-operations][^policies-governance] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when removing services, credentials, data, or infrastructure, including backups and offline copies.

## Requirement

Before irreversible retirement, establish exact owned resources, actual deletion authority, dependencies, retention/consent obligations, and required recovery/evidence preservation. Execute only the authorized scope and verify disposition. Shared or unrelated assets must remain intact; unresolved offline copies remain explicit obligations rather than a completed deletion claim.

## Implementation

1. Inventory resource identities, owners, dependents, retained obligations, and every relevant copy or credential path.
2. Resolve conflicts between deletion, retention, and recovery requirements with their authorized owners.
3. Choose a reversible preparation where possible, then perform only authorized actions with protected records.
4. Verify target removal and shared-resource preservation; track pending copies and residual access until their required disposition is observed.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: retirement removes the intended resources and accurately reports retained or outstanding obligations.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| An authorized isolated resource has no unmet retention dependency | Its removal and required evidence preservation are verified. |
| The proposed target includes a shared asset or lacks deletion authority | That part of the operation is withheld. |
| An offline copy remains pending | The report retains the open obligation and does not claim complete deletion. |

- **Pass:** Observed disposition matches authorized scope, shared assets are preserved, and all pending obligations remain visible.
- **Fail:** Unrelated assets are removed, retention is violated, or unverified copies disappear from the completion report.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Resource/copy inventory, owner authorization, obligation resolution, action records, and post-action inspection.

## Dependencies and limitations

Requires complete-enough discovery and observable disposition. Use [bounded external action](../../../catalog/controls/bounded-external-action.md); its authority check does not itself establish retention correctness. Assess destructive cases only on authorized disposable fixtures.

[^workflows-operations]: [Operations, maintenance and retirement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md).
[^policies-governance]: [Scope, authority and security](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md).
