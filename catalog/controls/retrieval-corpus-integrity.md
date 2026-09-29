---
type: Control
title: "Retrieval corpus integrity"
description: "Authorize corpus changes and keep retrieval aligned with admitted document revisions and withdrawals."
status: stable
family: knowledge-and-evidence
sources:
  - id: AML.M0025
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6673
    title: "AML.M0025: Maintain AI Dataset Provenance"
  - id: AML.T0070
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L3650
    title: "AML.T0070: RAG Poisoning"
---

# Retrieval corpus integrity

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Prevent unauthorized corpus changes from becoming trusted context. Apply to indexed sources, retrieval stores, embeddings, and caches used to support decisions. Public sources still need an explicit intake policy; being readable does not make them authoritative.

## Requirement

Admit corpus entries under a recorded source and access policy, preserving origin, revision, admission decision, and reader scope. Authorize modifications and withdrawals and propagate them to derived indexes and caches before those versions are served again. Quarantine unresolved integrity or scope changes. Keep a record of changes sufficient to identify affected retrieval outputs.

## Implementation

1. Assign corpus ownership and inventory source stores, ingestion paths, indexes, caches, and access filters.
2. Define permitted sources and writers, document identities, integrity checks, reader scopes, and admission criteria. Separate source identity from claims of truth.
3. Version ingestion and index builds; mediate writes and use a deny/tombstone mechanism while removal or rebuilding is incomplete.
4. Record document-to-index lineage and test that withdrawal, permission reduction, and replacement affect every serving path.

## Expected outcome and assessment

Expected outcome: retrieval serves only admitted revisions to authorized readers and stops serving withdrawn content.

Index a permitted document and retrieve it in the positive case. Attempt an unauthorized replacement and cross-tenant query. Withdraw a previously cached document, reduce a reader permission, and query while reindexing is pending. Verify recorded lineage for returned passages.

**Pass:** positive retrieval works with provenance; unauthorized revisions and readers are denied; withdrawn content cannot be served from any tested cache/index. **Fail:** stale forbidden content is served, lineage is missing, or permitted retrieval fails. **Inconclusive:** a serving path or derived index cannot be observed.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires authenticated ingestion and retrieval identities plus control over serving paths. Authorized documents can be false or malicious. [Evidence traceability](evidence-traceability.md) checks claims; [persistent state recovery](persistent-state-recovery.md) repairs contamination. This control does not certify semantic truth.

Addresses [retrieval poisoning corrupting decisions](../risks/retrieval-poisoning.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0025[^AML.M0025], AML.T0070[^AML.T0070]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0025]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0070]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
