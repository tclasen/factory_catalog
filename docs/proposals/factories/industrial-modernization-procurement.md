---
type: Factory Example
title: "Industrial modernization procurement factory"
description: "A fictional planning team prepares a multi-supplier modernization recommendation with scoped assurance and interface evidence."
status: draft
sources:
  - id: g182
    resource: https://publications.opengroup.org/g182
    title: "The Open Process Automation Business Guide"
  - id: g269
    resource: https://publications.opengroup.org/g269
    title: "O-PAS Adoption Guide, Version 2.0"
example: true
domain: "Industrial procurement and modernization planning"
activities: ["define modernization needs", "compare supplier assurance", "validate interface evidence", "recommend a procurement decision"]
control_selections:
  - control: ../controls/capability-investment-alignment.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/supplier-assurance-scope.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/interoperability-acceptance.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/risk-estimate-transparency.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Industrial modernization procurement factory

**Fictional design; proposed implementations; no operational assessments performed.**

[Ontology](../../../catalog/ontology.md) · [Adoption](../../../catalog/adoption.md)

## Factory profile

| Field | Proposed design |
|---|---|
| Purpose / owner | Prepare a reviewable modernization recommendation for a fictional facility; engineering program manager owns scope |
| Beneficiaries | Facility operations and procurement teams comparing continuity, maintainability, cost, and supplier responsibility |
| Inputs → outputs | Approved inventory, maintenance observations, supplier claims, business constraints → alternatives analysis, assurance matrix, interface test plan, unresolved-risk register |
| Intended outcome | Before an award recommendation, reviewers can identify support, evidence, assumptions, and remaining gaps for every material requirement in two options and the current arrangement |
| Actors | Operations staff supply context; analysts organize evidence; procurement verifies claims; qualified engineers assess interfaces; authorized owners decide |
| Workflow | Establish need → compare options → map supplier evidence → plan safe interface tests → review uncertainty → issue an internal recommendation |
| Autonomy | An AI assistant can summarize approved material and identify omissions; it stops at inaccessible evidence or a requirement needing engineering judgment |
| Authority | Drafting and analysis only; no purchase orders, contract acceptance, control-system commands, or plant modifications |
| Context | Existing and proposed equipment may coexist; supplier boundaries and operational consequences require explicit review |

The Open Process Automation business guide describes both replacements and new facilities; the Version 2.0 adoption guide addresses end-user adoption through ecosystem roles.[^g182][^g269] The factory here produces decision artifacts around industrial work. It does not operate a physical plant or prescribe a migration sequence.

## Control selections and rationale

| Risk or objective | Selected control and proposed mechanism |
|---|---|
| Procurement substitutes a preferred platform for a demonstrated need | [Capability investment alignment](../controls/capability-investment-alignment.md): compare maintainability evidence, target ability, alternatives, and resource dependencies |
| A vendor certificate is applied beyond its assessed offering | [Supplier assurance scope](../controls/supplier-assurance-scope.md): requirements-to-evidence matrix with exact versions and exclusions |
| Certified components fail to work together | [Interoperability acceptance](../controls/interoperability-acceptance.md): qualified engineers plan and later assess agreed interfaces in an authorized test environment |
| Confident cost/risk rankings hide weak assumptions | [Risk estimate transparency](../controls/risk-estimate-transparency.md): consistent horizons, input provenance, uncertainty, and sensitivity |
| Supplier marketing becomes an established operational claim | [Evidence traceability](../../../catalog/controls/evidence-traceability.md): distinguish assertions, tests, estimates, and unsupported conclusions |
| An internal recommendation creates an unintended commitment | [Bounded external action](../../../catalog/controls/bounded-external-action.md): require specific authority for any later solicitation, award, or contractual acceptance |
| A delivered report is mistaken for operational improvement | [Outcome verification](../../../catalog/controls/outcome-verification.md): assess decision usability now and operational outcomes only after a separately authorized implementation |

The planning activities **produce** a recommendation and evidence matrix. These artifacts **support** a decision but do not constitute an authority grant. Every selection above is proposed and not assessed.

## Assessment plan

Use fictional offers with one exactly scoped certificate, one wrong-version certificate, and a set of component assurances that leaves integration untested. The reviewer must limit the valid claim, reject the wrong-version evidence, and expose the integration gap with an accountable owner and decision disposition.

Then vary a material support-cost estimate enough to reverse the option ranking. The recommendation must disclose the sensitivity rather than present a stable preference. The decision-usability assessment checks coverage of every material requirement, including explicit unknowns. Retain inputs, revisions, fixture dispositions, reviewer, assumptions, and follow-up.

Any later hardware or interface test needs an approved environment, engineering procedure, and separate authorization. Simulated evidence must not be labeled as plant acceptance. No such tests have been performed for this example.

## Remaining gaps and reassessment

A real program needs applicable process-safety, cybersecurity, procurement, continuity, training, maintenance, and engineering assurance. Full standards and guide review is required before making O-PAS, FACE, SOSA, or O-TTPS-specific claims. Reassess on supplier changes, interface revisions, operating conditions, evidence expiry, or changed risk assumptions.

The program manager owns applicability; the qualified engineering and procurement reviewers own their evidence decisions. Pin exact source revisions and local adaptations for all selected controls through [adoption](../../../catalog/adoption.md) before use.

[^g182]: G182, The Open Process Automation Business Guide; public description accessed 2026-09-29 UTC; full guide not reviewed.
[^g269]: G269, O-PAS Adoption Guide, Version 2.0; public description accessed 2026-09-29 UTC; full guide not reviewed.
