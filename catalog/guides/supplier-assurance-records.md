---
type: Guide
title: "Maintain scoped supplier assurance records"
description: "Connect supplier claims to product scope, lifecycle evidence, discrepancies, and procurement decisions."
status: draft
sources:
  - id: c225-1
    resource: https://publications.opengroup.org/c225-1
    title: "Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 1: Requirements and Recommendations, Version 1.2"
  - id: c225-2
    resource: https://publications.opengroup.org/c225-2
    title: "Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 2: Assessment Procedures for the O-TTPS, Version 1.2"
---

# Maintain scoped supplier assurance records

[Research map](../open-group-standards-opportunities.md) · [Ontology](../ontology.md)

## Source and scope

O-TTPS 1.2 Part 1 addresses maliciously tainted and counterfeit COTS ICT products across their lifecycle; Part 2 describes assessment procedures for requirements in Part 1.[^c225-1][^c225-2] This guide proposes procurement and evidence-management records inspired by that scope. It does not reproduce an O-TTPS assessment or extend its certification to all suppliers and goods.

## Maintain a decision record

1. Identify the supplier legal entity, product/service, version or batch, origin, intended use, delivery path, and accountable procurement owner. Record subcontractors or resellers that matter to the claim.
2. For each claim, retain the issuer, exact wording/scope, source revision, applicable sites/products, issue/expiry dates when supplied, exclusions, and how the evidence was obtained. Record “unknown” where scope is missing.
3. Use [evidence traceability](../controls/evidence-traceability.md) to check that evidence supports the purchased item and lifecycle stage. Keep a supplier declaration, independent assessment, and local receiving test distinguishable.
4. Map local evidence needs across sourcing, receipt, maintenance, and disposal. Examples include authorized distribution evidence, item identifiers, integrity checks, update responsibility, and disposition records. These are proposed local checks, not claimed O-TTPS clauses.
5. Reconcile discrepancies before the procurement owner accepts the affected scope. Link unresolved assumptions to a [risk decision record](risk-analysis-decision-records.md); do not let an analyst's favorable summary authorize a purchase.
6. Reassess after product substitution, expired evidence, changed manufacturing/distribution path, a security incident, or material contract change.

## Embedded record and review test

| Field | Evidence question |
|---|---|
| Supplier/item identity | Does the evidence identify this entity, product, version/batch, and relevant site? |
| Assurance claim | Who made it, against which standard edition and assessment scope? |
| Lifecycle coverage | Which stages and subcontractor paths are covered or excluded? |
| Evidence and restrictions | Where is the source, which revision, who can inspect it, how long may it be retained? |
| Discrepancy and decision | What is unresolved, who owns resolution, who may accept or reject? |
| Reassessment | Expiry, substitution, incident, or other trigger |

A reviewer should reject a fictional packet where a valid certificate covers another product, where a distributor silently substitutes a component, or where expired evidence is presented as current. An inaccessible source yields an inconclusive finding, not an inferred pass. Retain the packet, review findings, and authorized disposition.

## Dependencies and limits

Pair this guide with [bounded external action](../controls/bounded-external-action.md) for orders and supplier commitments and [industrial exchange guidance](industrial-information-exchange.md) for received interfaces. Local technical admission mechanisms remain separate from procurement evidence. Certificates, traceable documents, and signatures cannot by themselves prove the absence of compromise. No supplier was assessed in writing this guide.

[^c225-1]: The Open Group, Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 1: Requirements and Recommendations, Version 1.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c225-2]: The Open Group, Open Trusted Technology Provider™ Standard (O-TTPS) – Mitigating Maliciously Tainted and Counterfeit Products: Part 2: Assessment Procedures for the O-TTPS, Version 1.2; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
