---
type: Control
title: "Supplier assurance scope"
description: "Match supplier assurance claims to the exact offering, version, service boundary, and acceptance decision."
status: draft
family: change-and-dependencies
sources:
  - id: g255
    resource: https://publications.opengroup.org/g255
    title: "Open Trusted Technology Provider Management Guide, Version 1.0"
  - id: g241
    resource: https://publications.opengroup.org/g241
    title: "FACE Contract Guide, Version 3.1"
  - id: g244
    resource: https://publications.opengroup.org/g244
    title: "SOSA Acquisition and Contracting Guide, Version 1.0"
---

# Supplier assurance scope

[Adoption](../../../catalog/adoption.md) · [Control families](../../../catalog/control-families.md)

## Purpose and applicability

Address procurement decisions that treat a supplier’s general certification or reputation as evidence about every delivered product or service. Apply to technology procurement, outsourced analysis, managed services, and multi-supplier projects. Assurance for non-ICT services needs domain-specific criteria even when the review procedure is reusable.

## Requirement

Before relying on a supplier assurance claim in selection or acceptance, map it to the exact requirement, offering, version, organizational and service boundary, issuing body, validity conditions, and supporting evidence. Record exclusions and the party responsible for integrated performance. Missing or mismatched evidence must remain a gap with an explicit decision disposition; it must not be represented as satisfied conformity.

## Implementation

1. Have the procurement owner define assessable requirements and the evidence each needs before reviewing offers.
2. Retain a claim-to-requirement matrix. Distinguish supplier assertions, independent assessments, product certificates, and local acceptance tests.
3. Verify scope and currency at the issuing source where available. Record inaccessible evidence as unknown and ask the supplier or issuer to resolve it through the authorized procurement process.
4. Evaluate delivered artifacts and interfaces against the contract’s local acceptance criteria. Assign integration responsibility across suppliers and record exclusions.
5. Reassess on version, subcontractor, service boundary, certificate, or delivery changes. Have the decision owner record rejection, further testing, or acceptance of a clearly described gap within their authority.

Mechanism: procurement review with a controlled acceptance record. A spreadsheet of claims alone does not prevent an unauthorized award.

## Expected outcome and assessment

Expected outcome: all assurance-dependent acceptance decisions in scope show what was actually assessed and what remains uncovered.

Inspect one procurement record. Test an exactly scoped claim, a certificate for another product version, and individually assessed components with no integration evidence.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the matching evidence supports only its scoped requirement; the wrong-version claim is rejected as support; the integration gap remains explicit and is resolved or knowingly dispositioned by the authorized owner before acceptance.
- **Fail:** a supplier-wide claim substitutes for product evidence, an exception is presented as conformity, or an unowned integration gap is hidden.
- **Inconclusive:** the certificate, issuer record, delivered version, or acceptance decision cannot be inspected.
- **Evidence:** requirements, claim matrix, issuer checks and access times, offering revisions, local acceptance results, gaps, and signed or attributable decisions.

## Dependencies and limitations

Requires procurement and domain expertise. This does not establish O-TTPS, FACE, SOSA, legal, or safety conformity. The [contracts example](../../../catalog/factories/contracts.md) and [bounded external action](../../../catalog/controls/bounded-external-action.md) separately govern commitments. [Interoperability acceptance](interoperability-acceptance.md) supports interface assessment. Follow [adoption](../../../catalog/adoption.md) to pin the selected revision.

## Source basis

G255 introduces ICT product integrity and supply-chain risk to management. G241 addresses tailored solicitation and proposal requirements; G244 addresses acquisition and contracting for SOSA.[^g255][^g241][^g244] Generalizing these themes into an evidence-scope gate is this catalog’s proposal, not standard contract language.

[^g255]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g241]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g244]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
