---
type: Control
title: "Evidence validity"
description: "Use assessment evidence only while its relevant inputs and scope remain applicable."
catalog_version: "v0.1.0"
status: draft
family: knowledge-and-evidence
sources:
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
---

# Evidence validity

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

**Identity:** `controls/evidence-validity` · **Catalog:** v0.1.0 · **Family:** `knowledge-and-evidence`

Draft requirement adapted from the source factory policies.[^policies-verification][^policies-execution] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply whenever previous checks or reviews are reused to accept, integrate, publish, or resume work.

## Requirement

Bind evidence to the assessed artifact or tree, criteria, dependencies, configuration, fixtures, tools, and relevant environment. Check those identities before relying on the result. Changed inputs invalidate affected evidence; unaffected evidence may be reused only with a recorded impact rationale. Keep failed attempts and gaps visible.

## Implementation

1. Record commands or review methods, input identities, results, and protected evidence locations.
2. For uncommitted changes, retain a tree or patch digest covering the assessed content.
3. Compare current inputs at the consuming decision, including after integration or installation.
4. Rerun invalidated checks and preserve historical results under their original identities.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: acceptance relies on evidence applicable to the actual candidate and context.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| Current candidate and all relevant inputs match | Complete passing evidence may be reused. |
| A dependency, criterion, or configuration changes | Affected passes are invalidated before acceptance. |
| An unrelated prose edit leaves assessed behavior unchanged | Reuse is allowed only with an explicit impact rationale. |

- **Pass:** Every reused result has matching inputs or justified unaffected scope, and relevant changes prevent reuse in the test cases.
- **Fail:** Stale or differently scoped evidence supports acceptance, or failed attempts are concealed.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Candidate/input identities, original results, comparison record, reuse rationale, and replacement results.

## Dependencies and limitations

Requires reliable input identification and access to observations. Complements [evidence traceability](evidence-traceability.md): applicability does not establish authenticity, source truth, or complete test coverage.

[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
