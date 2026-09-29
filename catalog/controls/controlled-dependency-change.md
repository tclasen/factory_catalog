---
type: Control
title: "Controlled dependency change"
description: "Qualify changed tools, models, dependencies, and configuration before relying on them."
catalog_version: "v0.1.0"
status: draft
family: change-and-dependencies
sources:
  - id: workflows-operations
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md
    title: "Operations, maintenance and retirement"
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
---

# Controlled dependency change

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

**Identity:** `controls/controlled-dependency-change` · **Catalog:** v0.1.0 · **Family:** `change-and-dependencies`

Draft requirement adapted from the source factory policies.[^workflows-operations][^policies-verification] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply to changes in dependencies, model versions, tools, or configuration that can affect behavior, security, or acceptance.

## Requirement

Identify and pin accepted inputs; assess provenance, security, compatibility, requirements, and recovery implications before activation. Obtain fresh evidence for affected behavior and configuration. Preserve consent and acceptance criteria unless changed through their authorized decision process. Reopen relevant exceptions when tools or rules change.

## Implementation

1. Record old/new identities, change purpose, accountable owner, and relevant source/security information.
2. Use [planning consistency](planning-consistency.md) and [evidence validity](evidence-validity.md) to identify invalidated assumptions and checks.
3. Test affected behavior, including compatibility and safe recovery where state changes are possible.
4. Activate through [verified delivery](verified-delivery.md); retain the recovery route and any justified exceptions.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: changed dependencies and settings receive qualification appropriate to their effects.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A pinned update meets applicable behavioral and compatibility criteria | Authorized activation uses the qualified inputs. |
| A model or configuration change violates a required outcome | Acceptance is withheld; thresholds are not silently relaxed. |
| New tooling invalidates an old diagnostic exception | The exception is reviewed before the new configuration is accepted. |
| The update would send data to a new provider | Processing waits for valid destination authority. |

- **Pass:** All affected inputs and checks are accounted for and the cases prevent unqualified or unauthorized changes.
- **Fail:** Unpinned/substituted inputs inherit an old pass, consent changes silently, or a known compatibility failure reaches acceptance.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Old/new identities, provenance review, impact map, fresh checks, exception dispositions, and activation/recovery record.

## Dependencies and limitations

Requires inspectable dependency identities and meaningful behavioral checks. Use [approved data processing](approved-data-processing.md) for destination limits. Pinning enables reproducibility but does not itself establish trustworthiness.

[^workflows-operations]: [Operations, maintenance and retirement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md).
[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
