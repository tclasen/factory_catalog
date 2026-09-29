---
type: Guide
title: "Use The Open Group standards to extend the knowledge-work graph"
description: "A research map of enterprise, environmental, industrial, risk, and interoperability standards with scoped catalog opportunities."
status: draft
sources:
  - id: c202
    resource: https://publications.opengroup.org/c202
    title: "O-DEF, the Open Data Element Framework, Version 2.0"
  - id: c220
    resource: https://publications.opengroup.org/c220
    title: "The TOGAF® Standard, 10th Edition"
  - id: c260
    resource: https://publications.opengroup.org/c260
    title: "ArchiMate® 4 Specification"
  - id: c250
    resource: https://publications.opengroup.org/c250
    title: "Risk Analysis (O-RA), Version 2.1"
  - id: c251
    resource: https://publications.opengroup.org/c251
    title: "Risk Taxonomy (O-RT), Version 3.1"
  - id: c267
    resource: https://publications.opengroup.org/c267
    title: "The Open Footprint® Standard, Edition 1.0"
  - id: c143
    resource: https://publications.opengroup.org/c143
    title: "The Exploration & Mining Business Capability Reference Map"
  - id: c135
    resource: https://publications.opengroup.org/c135
    title: "The Exploration & Mining Business Reference Model"
  - id: c230
    resource: https://publications.opengroup.org/c230
    title: "O-PAS™ Standard, 2nd Edition"
  - id: c268
    resource: https://publications.opengroup.org/c268
    title: "The OSDU® Data Platform Standard, Version 1.0"
  - id: c163
    resource: https://publications.opengroup.org/c163
    title: "Open Data Element Framework (O-DEF), Version 1.0"
  - id: c225-1
    resource: https://publications.opengroup.org/c225-1
    title: "Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 1: Requirements and Recommendations, Version 1.2"
  - id: c225-2
    resource: https://publications.opengroup.org/c225-2
    title: "Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 2: Assessment Procedures for the O-TTPS, Version 1.2"
  - id: c224
    resource: https://publications.opengroup.org/c224
    title: "The Open Group Commercial Aviation Reference Architecture Standard"
  - id: c239
    resource: https://publications.opengroup.org/c239
    title: "Technical Standard for SOSA® Reference Architecture, Edition 1.1"
  - id: c232
    resource: https://publications.opengroup.org/c232
    title: "FACE® Technical Standard, Edition 3.2"
  - id: c231
    resource: https://publications.opengroup.org/c231
    title: "Open Universal Domain Description Language (Open UDDL), Edition 1.1"
  - id: c262
    resource: https://publications.opengroup.org/c262
    title: "Open Agile Architecture™ Standard, Version 2.0"
  - id: c196
    resource: https://publications.opengroup.org/c196
    title: "Digital Practitioner Body of Knowledge™ Standard"
  - id: c247
    resource: https://publications.opengroup.org/c247
    title: "Zero Trust Commandments"
  - id: c246
    resource: https://publications.opengroup.org/c246
    title: "Security Principles for Architecture"
  - id: v244
    resource: https://publications.opengroup.org/v244
    title: "Energistics Unit of Measure (UOM) Standard v1.0.1"
  - id: p161
    resource: https://publications.opengroup.org/p161
    title: "Open Business Architecture (O-BA) – Part I"
  - id: p171
    resource: https://publications.opengroup.org/p171
    title: "Open Business Architecture (O-BA) – Part II"
  - id: c24a
    resource: https://publications.opengroup.org/c24a
    title: "The Open Group IT4IT™ Standard, Version 3.0.1: A Reference Architecture for Managing Digital"
  - id: c223
    resource: https://publications.opengroup.org/c223
    title: "O-DEF™, the Open Data Element Framework, Version 3.0"
  - id: g180
    resource: https://publications.opengroup.org/g180
    title: "Open FAIR™ Risk Analysis Process Guide, Version 1.1"
  - id: g21a
    resource: https://publications.opengroup.org/g21a
    title: "Open FAIR™ Risk Analysis Example Guide"
  - id: s182
    resource: https://publications.opengroup.org/s182
    title: "Healthcare Enterprise Reference Architecture (HERA) (Expired Snapshot)"
  - id: s260
    resource: https://publications.opengroup.org/s260
    title: "Open Digital Transformation Architecture™ for Government (Snapshot)"
  - id: c243
    resource: https://publications.opengroup.org/c243
    title: "The Open Group Base Specifications, Issue 8"
---

# Use The Open Group standards to extend the knowledge-work graph

[Ontology](ontology.md) · [Adoption](adoption.md) · [Work types](work-types.md)

## Research scope and evidence limits

The [standards collection](https://publications.opengroup.org/standards) spans architecture, digital management, industry reference models, information exchange, security, and operating-system interfaces. Research on **2026-09-28** inspected the collection, the first listing page in 20 relevant subject categories, and 31 individual publication pages, following supersession notices and selected related guides. This is a broad opportunity survey, not an exhaustive review of every publication or every category page. Category counts include editions, translations, licenses, snapshots, and supporting artifacts; they are not counts of distinct adopted standards.

The evidence below is the publisher's public descriptions and edition/status metadata. Attempts to read TOGAF and Open FAIR online text reached sign-in; licensed documents, schemas, and model downloads were not obtained or reviewed. No claim below establishes clause-level coverage, certification, deployed effectiveness, or permission to redistribute source content. The procedures and tests in the linked nodes are **catalog proposals**, inferred from source scope and local needs. They are not quotations or requirements attributed to the standards.

Public descriptions can lag releases. For example, the semantic-interoperability category lists O-DEF 1.0; its publication page points to 2.0, which points to 3.0. Follow the publication's supersession chain and corrigenda rather than choosing the first search result. O-DEF 3.0 notes an April 2026 correction even though its publication-date field remains May 2022.[^c163][^c202][^c223]

## Source findings and opportunities

Edition labels below identify the inspected source, not a promise that it remains the latest edition. Recheck before adoption.

| Subject and inspected source | Supported finding | Graph opportunity and disposition |
|---|---|---|
| TOGAF 10th Edition, C220; May 2025 corrigendum applied | Separates fundamental architecture content from configuration guidance, including development method, content, capability, and governance.[^c220] | Add [enterprise capability planning](guides/enterprise-capability-planning.md) and [architecture decision traceability](controls/architecture-decision-traceability.md). Useful to strategy, public administration, contracts, and operational redesign. |
| ArchiMate 4, C260, April 2026 | A modeling language for architecture relationships; changes from 3.2 include merged behavior elements and removal of some concepts.[^c260] | Use explicit, versioned model mappings in the enterprise guide. Do not silently equate an ArchiMate element with a catalog concept. |
| Open Business Architecture Parts I/II, P161/P171 | Publisher metadata labels both as preliminary specifications; their focus is enterprise transformation and business architecture practice.[^p161][^p171] | Useful supporting perspective for capability planning; do not call them a finalized replacement ontology. |
| Open Agile Architecture 2.0, C262, April 2026 | Architecture guidance for agility at scale, including experience, products, operations, and technical systems.[^c262] | Connect capability changes to a learning question and outcome review. A separate agile control would overlap generic outcome verification without more specific evidence. |
| IT4IT 3.0.1, C24A | A reference architecture spanning digital-product investment through end-of-life; incorporates the 3.0 corrigendum.[^c24a] | Candidate product lifecycle guide linking portfolio decision → product owner → operating evidence → retirement. Defer a separate node until mapped against existing delivery/implementation guidance. |
| DPBoK, C196, corrigendum applied January 2020 | Organizes digital practice into individual, team, team-of-teams, and enduring-enterprise contexts.[^c196] | Candidate learning/capability assessment guide; use context to select governance depth, without treating the contexts as universal maturity scores. |
| Open FAIR O-RA 2.1 / O-RT 3.1, C250/C251 | Companion standards address information-security risk analysis and its taxonomy.[^c250][^c251] | Add [risk decision records](guides/risk-analysis-decision-records.md) and [risk estimate assumptions](controls/risk-estimate-assumptions.md). Transfer to other domains requires explicit validation. |
| Open FAIR process/example guides, G180/G21A | Supporting guidance includes a qualitative/quantitative comparison and calibrated estimates for a business case.[^g180][^g21a] | Useful next reading for analysts; these older guides do not by themselves prove alignment with every 2025 revision. |
| Open Footprint 1.0, C267, April 2026 | Environmental-impact data standard with general data-model requirements, an element dictionary, and associated JSON schemas.[^c267] | Add [environmental reporting example](factories/environmental-reporting.md), measurement-basis control, and semantic mapping control. Schema exchange and environmental-method validity are separate questions. |
| Energistics UOM 1.0.1, V244 | Unit dictionary resources support consistent exchange and conversion, with XML and JSON resources.[^v244] | Support [measurement basis validation](controls/measurement-basis-validation.md). Apply to physical quantities in mining, emissions, and engineering. |
| O-DEF 3.0, C223, April 2026 correction | Common vocabulary, classification method, and federated index with plugins help identify data meaning.[^c223] | Add [semantic mapping validation](controls/semantic-mapping-validation.md). Vocabulary similarity alone is insufficient evidence of equivalent meaning. |
| Open UDDL 1.1, C231 | Formal data modeling for describing, querying, and communicating information.[^c231] | Candidate formal-model mapping guide; retain source/target model versions and test fixtures before claiming interoperability. |
| OSDU Data Platform 1.0, C268, April 2026 | Technology-independent platform reference architecture and application standards support portability and data integration.[^c268] | Connect to [industrial information exchange](guides/industrial-information-exchange.md); retain identifiers, units, access rules, and actual platform-version evidence. |
| EMMM capability map C143 and business reference model C135 | Reference capabilities and model definitions describe exploration/mining organizations.[^c143][^c135] | Add [mining investment planning example](factories/mining-investment-planning.md). Capability gaps and investment decisions belong in the graph alongside software work. |
| Commercial Aviation reference architecture C224 | Industry taxonomy and architecture descriptions support enterprise transformation; an associated model is available.[^c224] | Apply enterprise planning and industrial exchange guides to airline operations and supplier coordination. Operational/airworthiness assurance needs separate evidence. |
| O-PAS 2nd Edition C230 | Includes security, connectivity, system management, information/exchange models, and physical platform parts; specified parts were corrected in August 2024.[^c230] | Industrial exchange guide proposes a profile/version matrix and bounded integration trials. Do not infer plant safety or live-update readiness from architecture alignment. |
| FACE 3.2 C232; SOSA 1.1 C239 | FACE addresses portable software architecture; SOSA covers modular sensor systems across hardware/software interfaces.[^c232][^c239] | Candidate interface/profile conformance evidence nodes. Keep software portability, physical integration, and system safety assessments distinct. |
| O-TTPS 1.2, C225-1/C225-2 | Part 1 covers COTS ICT supply-chain integrity across the lifecycle; Part 2 supplies assessment procedures for Part 1 requirements.[^c225-1][^c225-2] | Add [supplier assurance records](guides/supplier-assurance-records.md), spanning procurement through disposal. Formal assessments must use the actual licensed requirements. |
| Security Principles C246; Zero Trust Commandments C247 | Architecture-level security principles and requirements for Zero Trust frameworks.[^c246][^c247] | Candidate architecture review guide; assess the existing [bounded external action](controls/bounded-external-action.md), [execution isolation](controls/execution-isolation.md), and [sensitive data egress](controls/sensitive-data-egress.md) controls before proposing another access or disclosure requirement. |
| Base Specifications Issue 8, C243 | Covers definitions, interfaces, shell/utilities, and rationale; technically identical to POSIX.1-2024.[^c243] | Lower priority here: implementation portability evidence can link to this source without importing its APIs into the knowledge-work ontology. |
| HERA S182; government architecture S260 | HERA is explicitly obsolete/expired. Government architecture is a snapshot valid through March 31, 2027.[^s182][^s260] | HERA is a research lead only. Government service-design guidance is promising, but any dedicated node must preserve provisional status and the expiry date. |

## Selection and graph design

Use the existing **Guide**, **Control**, and **Factory Example** types. No schema, family, or shared inventory change is needed. Each new path is its identity. Small capability, mapping, measurement, supplier, and risk records remain embedded in guides/examples until independent ownership or reuse justifies splitting them. These record templates do not introduce mandatory frontmatter fields.

Prioritize additions by reuse beyond software, a distinct uncovered decision, accessible supporting evidence, and an observable assessment. This yields four independently selectable controls and six application guides/examples linked from this research node. The controls address decision lineage, quantitative assumptions, measurement basis, and semantic meaning. Existing [evidence traceability](controls/evidence-traceability.md), [outcome verification](controls/outcome-verification.md), and [bounded external action](controls/bounded-external-action.md) supply complementary requirements.

Graph edges have named meaning in surrounding prose: a guide proposes an implementation; a control addresses a stated risk; an example selects a control with a separate assessment state. Source references express derivation, not adoption. Architecture views do not confer authority, supplier certificates do not establish every product's integrity, and a measured quantity does not establish the validity of the decision made from it.

## Research gaps and next decisions

1. Have domain reviewers inspect the proposed controls and mappings before real adoption. All new nodes remain draft and all example implementations are proposed/not-assessed.
2. Obtain authorized access to selected full editions, corrections, schemas, and certification rules. Add clause-level mappings only after reviewing them; do not infer requirements from marketing descriptions.
3. For formal integration, choose one concrete interchange profile and retain schema versions and conversion fixtures. Do not claim implementation compatibility from this survey.
4. Validate non-security use of the risk guide, environmental calculation methods, and industrial safety boundaries with competent domain owners.
5. Recheck sources when adopting, when a linked edition changes, and before relying on time-limited snapshots. Preserve source access dates separately from publication dates.

Adopt a catalog control only with its identity, catalog version, and [exact-commit source reference](adoption.md#record-the-adoption). This research does not approve a release baseline or certify compliance with any external standard.

[^c220]: The Open Group, The TOGAF® Standard, 10th Edition; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c260]: The Open Group, ArchiMate® 4 Specification; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c250]: The Open Group, Risk Analysis (O-RA), Version 2.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c251]: The Open Group, Risk Taxonomy (O-RT), Version 3.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c267]: The Open Group, The Open Footprint® Standard, Edition 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c143]: The Open Group, The Exploration & Mining Business Capability Reference Map; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c135]: The Open Group, The Exploration & Mining Business Reference Model; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c230]: The Open Group, O-PAS™ Standard, 2nd Edition; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c268]: The Open Group, The OSDU® Data Platform Standard, Version 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c163]: The Open Group, Open Data Element Framework (O-DEF), Version 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c225-1]: The Open Group, Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 1: Requirements and Recommendations, Version 1.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c225-2]: The Open Group, Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 2: Assessment Procedures for the O-TTPS, Version 1.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c224]: The Open Group, The Open Group Commercial Aviation Reference Architecture Standard; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c239]: The Open Group, Technical Standard for SOSA® Reference Architecture, Edition 1.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c232]: The Open Group, FACE® Technical Standard, Edition 3.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c231]: The Open Group, Open Universal Domain Description Language (Open UDDL), Edition 1.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c262]: The Open Group, Open Agile Architecture™ Standard, Version 2.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c196]: The Open Group, Digital Practitioner Body of Knowledge™ Standard; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c247]: The Open Group, Zero Trust Commandments; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c246]: The Open Group, Security Principles for Architecture; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^v244]: The Open Group, Energistics Unit of Measure (UOM) Standard v1.0.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^p161]: The Open Group, Open Business Architecture (O-BA) – Part I; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^p171]: The Open Group, Open Business Architecture (O-BA) – Part II; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c24a]: The Open Group, The Open Group IT4IT™ Standard, Version 3.0.1: A Reference Architecture for Managing Digital; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c223]: The Open Group, O-DEF™, the Open Data Element Framework, Version 3.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^g180]: The Open Group, Open FAIR™ Risk Analysis Process Guide, Version 1.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^g21a]: The Open Group, Open FAIR™ Risk Analysis Example Guide; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^s182]: The Open Group, Healthcare Enterprise Reference Architecture (HERA) (Expired Snapshot); public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^s260]: The Open Group, Open Digital Transformation Architecture™ for Government (Snapshot); public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c243]: The Open Group, The Open Group Base Specifications, Issue 8; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.

[^c202]: The Open Group, O-DEF Version 2.0; public publication description and supersession notice inspected 2026-09-28. Full licensed text was not reviewed.
