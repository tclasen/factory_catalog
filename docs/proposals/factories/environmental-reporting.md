---
type: Factory Example
title: "Environmental reporting factory"
description: "A fictional workflow for inspectable site-energy totals and environmental reporting inputs."
status: draft
example: true
domain: "Environmental reporting"
activities: ["collect activity measurements", "reconcile reporting boundaries", "review and publish environmental totals"]
control_selections:
  - control: ../controls/environmental-measurement-reconciliation.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/information-meaning-agreement.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/measurement-basis-validation.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/semantic-mapping-validation.md
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
sources:
  - id: g259
    resource: https://publications.opengroup.org/g259
    title: "The Open Footprint Business Guide"
  - id: c267
    resource: https://publications.opengroup.org/c267
    title: "The Open Footprint® Standard, Edition 1.0"
  - id: v244
    resource: https://publications.opengroup.org/v244
    title: "Energistics Unit of Measure (UOM) Standard v1.0.1"
---

# Environmental reporting factory

[Ontology](../../../catalog/ontology.md) · [Adoption](../../../catalog/adoption.md)

**Fictional design; all implementations proposed; no assessments performed.** Open Footprint provides an environmental data-model reference; Energistics provides unit-dictionary resources.[^c267][^v244] This example does not implement those schemas or claim compliant emissions accounting.

G259’s public description motivates exploring an extensible environmental information model.[^g259] The reconciliation and reporting procedures here are catalog proposals, not an implementation of the Open Footprint schema or a statutory accounting method.

## Factory profile

| Field | Proposed design |
|---|---|
| Purpose / owner | Produce an inspectable monthly site-energy packet; sustainability reporting lead owns scope and acceptance |
| Beneficiary | Operations team comparing usage and deciding where further investigation is needed |
| Inputs → artifacts | Approved meter exports and supplier statements → normalized energy records, mapping table, exceptions, and draft report |
| Outcome and period | Before each monthly acceptance, reviewer can reconcile every included site's quantity to its basis and see missing coverage |
| Actors | Analyst/agent prepares records; energy specialist reviews basis; reporting lead accepts; authorized signatory separately approves publication |
| Workflow | Define boundary → ingest → validate meaning/basis → reconcile → review → accept draft → separately authorize publication |
| Context | Multiple sites, reporting periods, units, revisions, and restricted supplier data; read-only source access and controlled draft workspace |
| Autonomy | Agent may classify and calculate within approved methods; stops on ambiguous units, unreconciled overlaps, or missing material data |
| Authority | Read approved records and write drafts; no supplier commitments, regulatory submissions, or publication without a separate valid grant |

## Activities and relationships

Stewards **produce** measurement artifacts; reconciliation **consumes** those artifacts and **produces** a ledger with evidence links. Review **evaluates** the declared report revision using that ledger. The factory **seeks** inspectable reporting; actual environmental reduction is a separate outcome requiring later observations.

## Risks, controls, and proposed implementation

| Risk / intended outcome | Selection and owner |
|---|---|
| Incomplete totals or comparisons with changed reporting boundaries | [Environmental measurement reconciliation](../controls/environmental-measurement-reconciliation.md): reporting lead records population coverage and qualifies incompatible comparisons |
| Producers and consumers disagree on missing-value or aggregation meaning | [Information meaning agreement](../controls/information-meaning-agreement.md): stewards agree business definitions and permitted interpretations |
| kWh/MWh confusion, double counting, period mismatch | [Measurement basis validation](../controls/measurement-basis-validation.md): energy specialist reviews full reporting population, conversions, and exclusions |
| Supplier “consumption” fields mean different things | [Semantic mapping validation](../controls/semantic-mapping-validation.md): analyst maintains reviewed field definitions and loss/unknown rules |
| An assertion cannot be traced to the accepted source revision | [Evidence traceability](../../../catalog/controls/evidence-traceability.md): reporting lead reviews material claims and source lineage |
| Polished report conceals excluded sites | [Outcome verification](../../../catalog/controls/outcome-verification.md): lead checks declared coverage and reconciliation before monthly acceptance |
| Draft is published through an available connector without approval | [Bounded external action](../../../catalog/controls/bounded-external-action.md): signatory grant and enforced destination/payload restrictions govern publication |

## Assessment plan and expected evidence

Run every selected control's complete assessment against the implemented scope. Domain fixtures add a repeated meter interval, a site missing the final week's readings, and a supplier revising a previously accepted value. Expected behavior: prevent duplication, show incomplete coverage without zero-filling, and reopen affected totals after the correction. Include an ordinary complete packet as a positive case.

Retain original exports, source permissions, mapping/method revisions, included/excluded population, calculations, reviewer findings, corrected report revision, and publication-grant tests. A missing observation is inconclusive; any uncorrected incompatible or duplicated quantity fails the relevant check. These are test plans, not results.

### Illustrative reconciliation fixture

Use a fictional ledger: site A records **1,000 kWh**, site B records **2 MWh**, and site C has **no measurement**. Under the fixture’s declared energy-unit conversion, the known subtotal is **3,000 kWh**; the complete three-site total remains unknown. The report must label both the subtotal and the missing site. No emissions factor or emissions total is inferred from these energy values.

Reviewers check the arithmetic, input traceability, boundary, and missing-data statement. Add a prior-period comparison that includes site C: an apparent decline must not be accepted as an established improvement until a comparable basis is available. Also test a duplicated meter record and a release request for an unapproved revision. Retain fixture inputs, report revision, expected/observed dispositions, reviewer, and follow-up.

These are planned tests; no operational effectiveness or compliance result is asserted.

## Gaps, reassessment, and adoption

Accuracy/calibration, emissions-factor selection, organizational accounting boundaries, regulatory requirements, privacy, and independent assurance need additional domain decisions. Energy totals alone are not emissions totals. Reassess after site/period/method changes, new sources, corrections, or added publishing tools; reporting lead owns applicability review.

Every selected control is applicable to this proposed workflow, proposed for implementation, and not-assessed. Before use, retain the control identity, catalog version, and exact-commit adoption URL under the [adoption procedure](../../../catalog/adoption.md#record-the-adoption). Neither the example nor its sources establish a passing reporting system.

[^c267]: The Open Group, The Open Footprint® Standard, Edition 1.0; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^v244]: The Open Group, Energistics Unit of Measure (UOM) Standard v1.0.1; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.

[^g259]: G259, The Open Footprint Business Guide; public product description accessed 2026-09-29 UTC; full guide not reviewed.
