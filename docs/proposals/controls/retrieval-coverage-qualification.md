---
type: Control
title: "Retrieval coverage qualification"
description: "Bound completeness claims by the corpus, accessible scope, and observed retrieval coverage."
status: draft
family: knowledge-and-evidence
sources:
  - id: ap-listing
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/exhaustive-retrieval-for-listing-questions.md
    title: "Agent Patterns: Exhaustive retrieval for listing questions"
  - id: ap-sufficiency
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/retrieval-sufficiency-gate.md
    title: "Agent Patterns: Retrieval sufficiency gate"
---

# Retrieval coverage qualification

[Adoption](../../../catalog/adoption.md) · [Retrieval assessment](../guides/retrieval-assessment.md)

## Purpose and applicability

Apply when a search result supports a list, an absence claim, or a decision that depends on finding all relevant material. Prevent a ranked or truncated result from being treated as an exhaustive inventory. Applies to human research and automated retrieval.

## Requirement

Before retrieval, record the question, corpus revision or observation time, permitted scope, required answer coverage, and stopping criteria. A completeness claim requires evidence that the declared scope was enumerated and its matching rule applied, or an explicitly qualified estimate with its method and uncertainty. Missing partitions, exhausted budgets, unresolved matching, or incomplete pagination must narrow or withhold the claim. An empty result or repeated search without new hits is insufficient by itself.

## Implementation

1. Name the research owner and define what counts as a relevant item, including exclusions and duplicates.
2. Prefer an authoritative inventory or structured enumeration for exhaustive questions. Record filters, page tokens, scope restrictions, withdrawals, and a consistent snapshot where available.
3. Reconcile returned identities with an independent expected set or coverage signal. For semantic retrieval, use judged samples and state the limits of estimated recall.
4. Publish the result with its scope and omissions. Escalate unresolved coverage where the decision requires completeness; do not expand access to fill a gap without authority.

## Expected outcome and assessment

Expected outcome: complete authorized retrieval can support a bounded completeness claim; partial results cannot silently support one.

Use a known corpus containing matches beyond the first page, duplicates, a withdrawn item, and an inaccessible partition. Test complete enumeration, truncated pagination, exhausted budget, unknown matching, and a genuinely empty authorized scope.

- **Pass:** the complete fixture yields exactly the expected eligible set; duplicates and withdrawals are handled; each incomplete or uncertain case is qualified or withheld; the valid empty result is reported only with scope evidence.
- **Fail:** any known omission supports an unqualified complete/absent claim, excluded data is disclosed, or the valid complete case is incorrectly rejected.
- **Inconclusive:** the expected set, snapshot, or retrieval observations cannot be established.
- **Evidence:** corpus/query revisions, expected and returned identities, page/partition coverage, budget disposition, omissions, evaluator, time, and final claims.

## Dependencies and limitations

[Corpus integrity](../../../catalog/controls/retrieval-corpus-integrity.md) governs admitted sources; [evidence traceability](../../../catalog/controls/evidence-traceability.md) checks support for claims. Neither guarantees retrieval completeness. This control requires observable enumeration or a defensible estimation method; it cannot establish coverage of inaccessible or unknown sources, nor correctness of synthesis.

Adapted from Agent Patterns' retrieval guidance, CC BY 4.0.[^ap-listing][^ap-sufficiency] Requirements and fixtures are catalog proposals, not operational results.

[^ap-listing]: Agent Patterns, pinned exhaustive-retrieval guidance; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^ap-sufficiency]: Agent Patterns, pinned retrieval-sufficiency guidance.
