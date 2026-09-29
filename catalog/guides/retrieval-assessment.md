---
type: Guide
title: "Assess extraction and retrieval"
description: "Separate extraction accuracy, retrieval coverage, uncertainty, and correction durability."
status: draft
sources:
  - id: evaluation
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/product/search-evaluation.md
    title: "Search evaluation specification"
  - id: publication
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/adr/0004-local-storage-and-revision-publication.md
    title: "Revision publication decision"
---

# Assess extraction and retrieval

[Adoption](../adoption.md) · [Retrieval coverage qualification](../controls/retrieval-coverage-qualification.md)

## Procedure

Use for systems that extract claims, index them, and retrieve evidence for users. The source evaluation and revision-publication designs inform this proposed procedure; source tests were not executed.[^evaluation][^publication]

1. Pin sources, extraction pipeline, corpus, index, query set, and judges. Define the intended population and required outcomes before testing.
2. Evaluate retrieval first against a reviewed reference corpus, then against extracted data on the same queries. Attribute wrong facts to extraction even if retrieval correctly finds them. Report failures by stage and relevant subset.
3. Keep related documents, entities, paraphrases, or clips together when splitting development and acceptance data. Freeze thresholds; once acceptance cases guide tuning, obtain independent acceptance evidence before claiming generalization.
4. Include difficult negatives, missing modalities, contradictory and unjudged items, unknown entities, and no-match queries. Preserve supported, contradicted, ambiguous, and unjudged evidence states through presentation. Model agreement is not independent ground truth; missing annotations do not make a negative label.
5. Evaluate useful answers and justified abstention separately. Apply [retrieval coverage qualification](../controls/retrieval-coverage-qualification.md) before exhaustive or absence claims, and [evidence traceability](../controls/evidence-traceability.md) to entities, joins, and final claims.
6. For updates, capture a consistent result revision, preserve authoritative corrections outside disposable views, and test interruption before and after activation. Use [data-preserving migration](../controls/data-preserving-migration.md) and [independent restoration](../controls/independent-restoration.md).

## Fixtures and disposition

| Fixture | Required observation |
|---|---|
| Wrong extraction retrieved correctly | Extraction failure stays visible; search success cannot qualify the fact |
| Unjudged item or conflicting source | Evidence remains unknown or disputed; it cannot silently count as correct ground truth |
| No reviewed match and useful valid queries | Appropriate abstention and useful retrieval both meet predeclared criteria; refusing everything fails |
| Missing page or source partition | Exhaustive claim is narrowed or withheld |
| Correction, rebuild, interrupted activation, restore | Results use a consistent revision; accepted corrections survive; missing data is an error rather than a valid empty answer |

Retain corpus and pipeline identities, split assignments, judgments and disagreements, expected/returned sets, all stage results, correction digests, recovery observations, evaluator, and time. Fail the procedure for misclassified known errors, hidden omissions, mixed revisions, or lost corrections; insufficient ground truth is inconclusive. A pass requires both valid cases and adverse fixtures to meet their declared observations. A small pilot supports only its tested scope.

[^evaluation]: Pinned semantic_search search evaluation specification.
[^publication]: Pinned semantic_search revision-publication decision; its architecture is an example, and its stated crash-consistency and scale limits remain unverified.
