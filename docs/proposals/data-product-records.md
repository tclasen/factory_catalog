---
type: Guide
title: "Data product records"
description: "Describe products, contracts, distribution interfaces, and assessments without changing the catalog schema."
status: draft
tags: [data-mesh, data-stewardship]
sources:
  - id: dcat
    resource: https://www.w3.org/TR/vocab-dcat-3/
    title: "Data Catalog Vocabulary (DCAT), Version 3"
  - id: lineage
    resource: https://openlineage.io/docs/spec/object-model/
    title: "OpenLineage Object Model"
  - id: odcs
    resource: https://bitol-io.github.io/open-data-contract-standard/latest/
    title: "Open Data Contract Standard"
---

# Data product records

[Data product design](guides/data-product-design.md) · [Ontology](../../catalog/ontology.md)

## Purpose and representation

Use this guide to prepare an inspectable product record. A product is a maintained service commitment around data; the catalog can express its actors, artifacts, activities, outcomes, grants, implementations, and assessments using the existing ontology. This guide adds no `Data Product` document type or mandatory metadata extension.

DCAT supplies distinctions between datasets, distributions, and services.[^dcat] OpenLineage supplies runtime observations about jobs and datasets.[^lineage] ODCS offers a concrete contract format.[^odcs] Use these as linked external specifications when needed; none substitutes for the pinned OKF bundle format.

## Minimum local record

| Field | Record |
|---|---|
| Identity and scope | Stable product identity, domain boundary, intended consumers and use |
| Accountability | Owner, steward, support route, accepted responsibilities, capacity, review trigger |
| Inputs and outputs | Artifact identities, exact revisions or time windows, sensitivity, provenance |
| Meaning | Grain, keys, units, definitions, population, time basis, known ambiguity |
| Contract | Exact contract revision, consumer acceptance, checks, exceptions |
| Distribution | Each table, file, stream, report, or API; its version and access procedure |
| Authority | Grant references, issuer, actor, purpose/action, scope, validity, restrictions |
| Service | Agreed objectives, observations, observation coverage, incident route |
| Dependencies | Input and consumer links; whether declared or observed; coverage gaps |
| Lifecycle | Change notice, compatibility decision, correction, retirement, retention disposition |
| Assessment | Target revision, method, evaluator, time, pass/fail criteria, result, evidence |
| Adoption | Control identity, catalog version, exact commit URL, local adaptations |

Do not put sensitive records, access credentials, or restricted metadata into a public knowledge bundle. Store protected evidence in its authorized system and record an appropriately restricted reference. Missing evidence remains unknown to readers who cannot inspect it.

## Proposed graph edges

Name the relationship in prose around each relative Markdown link:

- An activity **consumes** an input artifact and **produces** a product revision.
- An owner **is accountable for** the product's declared support and outcomes.
- A product record **references** its contract and distribution descriptions.
- A transformation record **derives output from** identified inputs; distinguish a planned transformation from an observed run.
- A consumer activity **depends on** a product revision for a stated purpose.
- An assessment **evaluates** a local control implementation using retained evidence.

These are explanatory relationships within a record, not additions to the shared ontology. Generic OKF readers see document links; they must not infer permission, successful assessment, or semantic equality from a link.

## Worked record fragment

Fictional product: monthly regional water observations. The monitoring team owns source observations, the laboratory owns assay results, and the regional analysis team owns the combined indicator. Its grain is one station and calendar month; missing assays remain missing, and units are explicit. Consumers receive a dated CSV snapshot and a readable report linked to the same product revision.

A correction to a station identifier changes the mapping revision and triggers downstream reconciliation. A recorded successful processing run does not prove that the laboratory method or the mapping is correct. Retain separate evidence for the source, transformation, and accepted use.

The [regional water example](factories/regional-water-evidence.md) supplies roles, activities, control selections, and a proposed assessment plan. No real organization or successful implementation is asserted.

## Record review

Ask a reviewer unfamiliar with the producing team to locate the owner, interpret one value including its time and unit, identify an authorized access route, trace a result to inputs, and explain what happens after a correction. Mark missing information and disputed meaning explicitly. Then execute the selected controls' assessment procedures; this record review alone is not their passing evidence.

Keep small objects embedded in a record. Propose a separate concept type only when independent reuse or lifecycle warrants it and after a schema design decision under the contribution workflow. An actual OKF attested computation additionally needs its runtime, sanctioned computation, executor, receipt requirements, and deterministic attester; this guide does not create one.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^dcat]: [Data Catalog Vocabulary (DCAT), Version 3](https://www.w3.org/TR/vocab-dcat-3/).
[^lineage]: [OpenLineage Object Model](https://openlineage.io/docs/spec/object-model/).
[^odcs]: [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/).
