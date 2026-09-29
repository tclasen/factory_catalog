---
type: Control
title: "Instruction change control"
description: "Update canonical instructions from observed evidence without silently changing authority or acceptance."
status: draft
family: monitoring-and-improvement
sources:
  - id: policies-instructions
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/instructions.md
    title: "Durable instructions and improvement"
---

# Instruction change control

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

Draft requirement adapted from the source factory policies.[^policies-instructions] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply to durable user corrections, process defects, and proposed changes to agent guidance.

## Requirement

Record material observations and their source, distinguish explicit direction from inferred preference or uncertain cause, and update the canonical rule within authorized scope. Reconcile conflicting guidance and affected examples. Changes expanding authority or budgets or reducing acceptance/security require the applicable owner decision before adoption. Verify the change proportionately and define when to review, revise, or remove it.

## Implementation

1. Find the rule’s authoritative home; keep generic guidance separate from project grants, incidents, and temporary constraints.
2. Record the observed problem, likely cause, smallest useful change, expected benefit/tradeoff, verification scenario, and review trigger.
3. Apply authorized corrections and simplifications; keep proposals distinct from operative rules when authority is missing.
4. Check affected references and scenarios, then use later relevant work to assess benefit. Prefer removing duplication over adding procedures.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: durable guidance reflects authorized corrections and evaluated improvements.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| An explicit correction conflicts with existing guidance | The canonical rule and affected references are reconciled in the authorized task. |
| A repeated failure suggests an uncertain cause | The cause remains a hypothesis with a bounded proposal and review signal. |
| A proposed rule would expand spending or weaken acceptance | It remains unadopted until the appropriate decision is recorded. |
| An adopted process change produces no expected benefit | Its review trigger leads to revision, removal, or a supported retention decision. |

- **Pass:** All cases preserve rule ownership, evidence, authorization, and a review disposition.
- **Fail:** A hypothesis becomes a permanent grant, contradictory instructions remain operative, or self-modification excuses a failed gate.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Observation/source, prior and revised rule, authorization where needed, affected references, check results, and review trigger/disposition.

## Dependencies and limitations

Requires discoverable rule ownership. Use [planning consistency](planning-consistency.md) for wider propagation and [outcome verification](outcome-verification.md) for benefit claims. No background monitoring or extra project is authorized.

[^policies-instructions]: [Durable instructions and improvement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/instructions.md).
