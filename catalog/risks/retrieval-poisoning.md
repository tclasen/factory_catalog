---
type: Risk Scenario
title: "Retrieval poisoning corrupts a decision"
description: "An adversary inserts or changes indexed content that later appears relevant to a legitimate query."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: AML.T0070
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L3650
    title: "AML.T0070: RAG Poisoning"
  - id: AML.M0025
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6673
    title: "AML.M0025: Maintain AI Dataset Provenance"
---

# Retrieval poisoning corrupts a decision

[ATLAS assessment guide](../atlas-threat-assessment.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Identity:** `risks/retrieval-poisoning` · **Catalog:** v0.1.0

## Cause and enabling conditions

A contract factory retrieves an altered policy as authority for an obsolete approval rule. Ingestion access, stale caches, or missing source review allow the altered revision to influence the output.

## Threatened outcomes and affected parties

Corpus integrity, factual claims, and authorized contracting outcomes are threatened. Reviewers, signatories, and counterparties may be affected.

## Candidate controls

- [Retrieval corpus integrity](../controls/retrieval-corpus-integrity.md) addresses this scenario by the following mechanism: controls admission, revisions, reader scopes, and withdrawals.
- [Evidence traceability](../controls/evidence-traceability.md) addresses this scenario by the following mechanism: checks whether cited material supports the output in context.
- [Persistent state recovery](../controls/persistent-state-recovery.md) addresses this scenario by the following mechanism: restores affected indexes and derived state.

These are applicability candidates, not adoption or effectiveness claims. The local factory owner records applicability, scope, assumptions, an assessment owner, and a reassessment trigger using the [adoption procedure](../adoption.md).

## Assessment example

Try an unauthorized policy replacement, retrieve an approved revision, then withdraw a cached document and query while rebuilding. Include a memo whose reachable citation contradicts its claim. Retain ingestion decisions, retrieved revisions, cache observations, and review disposition. Unauthorized/withdrawn content must not be served and the contradictory claim must be withheld.

Evaluate each selected control using its own criteria. A forbidden effect is a failure; missing observations are inconclusive. This is a hypothetical fixture, with no local implementation or assessment asserted.

## Limits and reassessment

Authorized sources can themselves be deceptive. Provenance does not establish source truth or research completeness. Reassess when indexing, cache behavior, corpus writers, or reader permissions change.

## Source basis

This scenario is a catalog interpretation informed by AML.T0070[^AML.T0070], AML.M0025[^AML.M0025]. Source case studies illustrate reported conditions, not current vendor vulnerability status or local attack probability.

[^AML.T0070]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.M0025]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
