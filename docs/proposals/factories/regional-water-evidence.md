---
type: Factory Example
title: "Regional water evidence network"
description: "A fictional data mesh application connecting field observations, laboratory results, and regional planning evidence."
status: draft
tags: [data-mesh, scientific-research, public-services]
example: true
domain: "Environmental research and regional planning"
activities: ["publish producer observations", "reconcile units and coverage", "combine authorized data products", "assess regional evidence"]
control_selections:
  - control: ../controls/data-product-accountability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-product-contract.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-semantic-interoperability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-product-discovery.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-product-service-objectives.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/federated-data-policy-enforcement.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-lineage-impact.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/data-contract-evolution.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Example: regional water evidence network

[Data product design](../guides/data-product-design.md) · [Product records](../data-product-records.md) · [Adoption](../../../catalog/adoption.md)

**Fictional design; all implementations proposed; no assessments performed.** This example supports environmental analysis. It does not authorize public health decisions or establish scientific or regulatory adequacy.

## Purpose, ownership, and outcome

A regional planning consortium needs monthly evidence about observation coverage and trends. Its research director owns the overall workflow and acceptance; domain leads own their products. The intended outcome is that an analyst can identify usable evidence, reproduce a reviewed comparison, and explain missing observations without private assistance from the producing teams.

For a proposed four-week pilot, assess five representative analyst tasks selected before testing. All five must identify the source revision, unit, observation period, and missing-data limits correctly, and reproduce the reviewed reference result within its predeclared tolerance. Record completion time against the existing workflow. These are fictional pilot criteria, not measured benefits or universal targets.

## Domains and products

| Domain / accountable owner | Product and activity | Inputs → outputs / interface |
|---|---|---|
| Field monitoring / monitoring lead | Collect and curate station observations | Instrument readings and calibration records → dated observations and quality flags in a versioned file |
| Laboratory / laboratory lead | Review assays | Sample identifiers, assay method, results → approved assay release with units and detection limits |
| Regional analysis / research director | Reconcile and interpret | Two producer releases and approved station mapping → monthly analytical table and evidence memo |
| Shared services / platform lead | Maintain discovery and authorized delivery | Product descriptions, contracts, grants → searchable metadata and controlled download routes |

The analytical product has its own owner. It does not transfer responsibility for every downstream inference to the laboratory. Each domain chooses its internal workflow within the shared interface and policy agreements.

## Activities, authority, and constraints

1. Domain staff review source observations and approve product releases.
2. An analysis assistant reads authorized releases and drafts a reconciliation report. It may choose queries within its assigned scope, but stops on unknown units, ambiguous identifiers, missing grants, or exhausted processing limits.
3. A domain specialist resolves mapping and scientific interpretation questions. The assistant cannot silently impute absent assays or change approved mappings.
4. The research director assesses the evidence memo and authorized use. A separately authorized publisher releases only the approved public aggregate.

The consortium's designated access authority issues scoped grants for actors, datasets, purposes, and expiry. Field and laboratory leads exercise only delegated access decisions. Exact locations and restricted observations remain in protected storage; public metadata and aggregates undergo separate disclosure review. Read permission does not authorize redistribution. The platform owner supplies enforcement and records, while domain owners retain stewardship responsibilities.

## Control selections and proposed implementations

The research director owns applicability decisions for the whole workflow; product owners implement their respective requirements. All controls listed in frontmatter are applicable because the design publishes maintained products across domain boundaries.

| Risk or need | Control and proposed implementation / owner |
|---|---|
| An absent producer leaves questions unanswered | [Accountability](../controls/data-product-accountability.md): accepted support responsibilities and successor / domain leads |
| Files omit meaning or delivery commitments | [Contract](../controls/data-product-contract.md): grain, units, sample identifiers, methods, limitations, and revision / producer and consumer leads |
| A many-to-many join inflates observations | [Semantic interoperability](../controls/data-semantic-interoperability.md): approved station/sample mapping and count reconciliation / analysis lead |
| Consumers find an obsolete release | [Discovery](../controls/data-product-discovery.md): distinguish product identity and dated distributions / platform lead |
| A successful job serves old observations | [Service objectives](../controls/data-product-service-objectives.md): measure source-to-publication delay and missing observations / producer leads |
| One download route ignores restrictions | [Federated policy enforcement](../controls/federated-data-policy-enforcement.md): shared route inventory and denial tests / access authority and platform lead |
| A correction has unknown downstream effects | [Lineage and impact](../controls/data-lineage-impact.md): bind input, mapping, and output revisions, including exported reports / analysis lead |
| A method or unit changes without notice | [Contract evolution](../controls/data-contract-evolution.md): review, consumer notice, transition, and safe withdrawal / laboratory lead |
| A memo overstates findings | [Evidence traceability](../../../catalog/controls/evidence-traceability.md): review material claims and source limits / scientific reviewer |
| Products are available but unusable | [Outcome verification](../../../catalog/controls/outcome-verification.md): five predefined analyst tasks / research director |
| A draft or restricted observation is published | [Bounded external action](../../../catalog/controls/bounded-external-action.md): separate publication grant tied to approved revision and destination / publisher |

## Proposed assessment and evidence

Use a synthetic fixture with two stations, two laboratory releases, a changed station mapping, a restricted record, and an expected combined result reviewed by a specialist. Retain inputs, contracts, grants, mapping revision, procedure revision, actual outputs, timestamps, and reviewer decisions.

Run a valid journey from discovery through authorized analysis. Then inject a duplicate key, a unit change that preserves numeric types, an old observation in a newly processed file, missing lineage for a manual export, an expired exception, and an unresolved consumer at retirement. Execute the complete procedures of the corresponding selected controls; these six cases are an integration supplement, not a substitute for their required cases. Assess existing evidence, outcome, and action controls using their own procedures as well.

Expected integration behavior: valid data reaches the authorized analyst; invalid combinations are withheld; missing monitoring and lineage remain visible; denied access produces no disclosure; unresolved retirement triggers an authorized decision. Failure of any required case prevents full readiness. Missing evidence makes the affected finding inconclusive.

No fixture has been executed. Current assessment result for every selection is **not-assessed**. Document review or catalog validation cannot change that result.

## Gaps, reassessment, and adoption

Scientific sampling bias, calibration adequacy, spatial comparability, causal interpretation, re-identification, records obligations, and emergency response need additional domain review. The proposed controls are not a complete scientific assurance or information-protection program.

Reassess on new laboratories, methods, geographic coverage, public access routes, AI tools, or intended decisions. The research director owns this review. Before implementation, pin every selected control's identity, catalog version, and exact commit URL under the [adoption procedure](../../../catalog/adoption.md#record-the-adoption); the links above describe proposed selection only.
