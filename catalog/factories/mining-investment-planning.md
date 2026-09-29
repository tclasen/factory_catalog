---
type: Factory Example
title: "Mining investment planning factory"
description: "A fictional decision-support workflow connecting exploration and mining capability gaps to investment options."
status: draft
example: true
domain: "Exploration and mining investment planning"
work_types: [analysis-and-diagnosis, forecasting-and-simulation, strategy-and-planning, evaluation-and-assurance, decision-making-and-adjudication]
control_selections:
  - control: ../controls/architecture-decision-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/risk-estimate-assumptions.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
sources:
  - id: c135
    resource: https://publications.opengroup.org/c135
    title: "The Exploration & Mining Business Reference Model"
  - id: c143
    resource: https://publications.opengroup.org/c143
    title: "The Exploration & Mining Business Capability Reference Map"
---

# Mining investment planning factory

[Ontology](../ontology.md) · [Adoption](../adoption.md) · [Enterprise planning guide](../guides/enterprise-capability-planning.md)

**Fictional design; proposed implementations; no assessments performed.** EMMM supplies exploration/mining business-model and capability references.[^c135][^c143] The local design below is illustrative; it does not claim a formal model mapping, verified reserves, safe operations, or investment performance.

## Factory profile

| Field | Proposed design |
|---|---|
| Purpose / accountable owner | Help an operations planning committee compare capability investments; planning director owns scope and acceptance |
| Inputs → artifacts | Approved operating observations, capability definitions, supplier evidence, and constraints → gap map, option comparison, decision records, unresolved-evidence register |
| Outcome / period | At a quarterly planning review, every shortlisted option has a stated capability gap, owner, evidence basis, uncertainty, and observation plan |
| Actors | Planning analyst/agent organizes evidence; operations specialists validate domain assumptions; committee chooses within its authority |
| Workflow | Define outcome → map current/desired capabilities → gather evidence → compare alternatives → challenge assumptions → accept recommendation → separately decide funding |
| Context | Supplier confidentiality, uncertain forecasts, constrained access to operational information; no control-system write access |
| Autonomy | Agent may draft mappings and calculations under approved assumptions; stops on missing evidence, conflicting constraints, or requests outside scope |
| Authority | Analysis and draft preparation only; funding, procurement, operating changes, and external communications require separate grants |

## Control selections and risks

| Concern | Applicable proposed implementation |
|---|---|
| An attractive initiative lacks a connection to the intended outcome | [Architecture decision traceability](../controls/architecture-decision-traceability.md): planning director requires gap/option/owner links and reviewed constraints |
| An uncertain disruption forecast is presented as a known benefit | [Risk estimate assumptions](../controls/risk-estimate-assumptions.md): operations specialist reviews basis, horizon, dependence, and sensitivity |
| Supplier or operational assertions lack source support | [Evidence traceability](../controls/evidence-traceability.md): analyst retains source revisions and specialist checks material claims |
| A complete presentation omits a material option or evaluation criterion | [Outcome verification](../controls/outcome-verification.md): committee assesses the declared comparison against the planning brief |

Use [supplier assurance records](../guides/supplier-assurance-records.md) for evidence scope and [industrial information exchange](../guides/industrial-information-exchange.md) if operational datasets must be transformed. The four controls selected here do not cover every such extension; reassess selections before adding those activities.

## Assessment plan

Run the full assessments of all four selected controls. Additional fictional fixtures: a preferred initiative with no capability gap, an hourly downtime estimate compared with an annual alternative, and a material operating constraint changed after the comparison was approved. Expected behavior: reject the orphan initiative, normalize or reject the incompatible estimate, and reopen the affected decision. Include a complete, consistent comparison as the positive case.

Retain the brief, capability definitions/versions, observations, estimates, alternatives, source lineage, reviewer identities, fixture results, and committee disposition. Review requires domain competence; missing operating evidence yields an inconclusive finding. No fixture has been executed.

## Gaps and reassessment

This decision-support example does not supply geological/reserve assurance, safety engineering, environmental permitting, community consultation, financial due diligence, or purchasing authority. Existing observations and supplier claims may be biased or stale. Reassess after material operating incidents, price/constraint changes, new suppliers, changed assumptions, or expanded agent authority; the planning director owns applicability decisions.

All four selections remain applicable/proposed/not-assessed. Follow [adoption](../adoption.md#record-the-adoption) to pin each identity, catalog version from the adopted revision, and exact source revision before implementing. Recommendation acceptance and authority to execute a funded change remain separate decisions.

[^c135]: The Open Group, The Exploration & Mining Business Reference Model; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
[^c143]: The Open Group, The Exploration & Mining Business Capability Reference Map; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
