---
type: Factory Example
title: "Government data science factory across an air gap"
description: "A government contract gathers low-side insights, transfers auditable files, and continues analysis and fusion with restricted data in an air-gapped AI factory."
status: draft
example: true
domain: "Government data science and evidence fusion"
work_types: [research-and-discovery, analysis-and-diagnosis, software-and-computational-development, evaluation-and-assurance]
tags: [government, air-gap, security, auditability]
control_selections:
  - control: ../controls/approved-data-processing.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/execution-isolation.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/sensitive-data-egress.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/protected-acceptance.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/local-quality-gates.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/qualified-artifact-promotion.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/security-event-traceability.md
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
  - control: ../controls/data-lineage-impact.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/semantic-mapping-validation.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Example: government data science factory across an air gap

[Factory examples](./) · [Ontology](../ontology.md) · [Adoption](../adoption.md) · [Compartmented research example](compartmented-research.md)

**Fictional government contract; proposed implementations; no assessments performed.** A contractor studies infrastructure reliability for a government customer under strict security and auditability requirements. A low-side AI factory gathers and analyzes approved evidence. Its files and insights are brought into an air-gapped AI factory, where analysis continues and the findings are fused with restricted asset and incident data unavailable on the low side. This is a proposed local design, not a claim of compliance with a named security regime.

## Factory profile

| Field | Design |
|---|---|
| Purpose / accountable owner | Produce a supported internal assessment of infrastructure reliability; contractor research lead owns production and customer analysis owner owns acceptance |
| Low-side inputs | Approved research question, public or otherwise permitted observations, source snapshots, methods, and synthetic internal-data fixtures |
| Transfer artifacts | Evidence tables, source extracts permitted for transfer, collection dates, analytical code/notebooks, dependency bundle, schemas, mappings, preliminary insights with uncertainty, and revision-bound evidence |
| Air-gapped inputs | Admitted low-side package plus sensitive asset inventories, operational measurements, and incident records available only inside the environment |
| Internal output | Revised transformations and models, fused datasets with lineage, evaluated findings, uncertainty/conflict register, and an internal assessment for named recipients |
| Intended outcome / measure | By the agreed review date, every customer question has a traceable finding or accepted explicit unknown; all material joins and quantitative claims have reviewed meaning and reproducible computational evidence within declared tolerances |
| Actors | Collection and analysis agents on each side; optional analysts and reviewers; source/data owners; transfer custodian; platform owner; independent evaluation owner; customer analysis owner |
| Contract constraints | Approved sources and uses, handling labels, processing locations, transfer route, personnel access, retention, publication restrictions, and acceptance duties are recorded before work starts |

Low-side access is limited to data and processing approved for that environment. The research question itself is reviewed for sensitive implications. The internal factory runs inference, tools, rendering, and evidence storage locally; it cannot query the public web, use an external model API, or export telemetry. An air gap does not make imported evidence trustworthy or remove internal access restrictions.

## Two factories and their handoff

Use the [air-gapped artifact transfer procedure](../guides/air-gapped-artifact-transfer.md) for packaging, admission, internal requalification, and audit continuity. The following stages specialize it for this contract.

| Stage / owner | Work performed | Required gate and retained output |
|---|---|---|
| Question definition / customer and data owners | Define questions, permitted collection, material claims, and internal fusion needs without disclosing restricted details to the low side | Approved low-side brief and separately protected internal acceptance criteria |
| Low-side research and development / first AI factory | Gather evidence, clean observations, develop analysis code, run experiments, and draft insights with or without human analysts | Deterministic schema, type, range, duplicate, missingness, unit, timestamp, code-quality, and computation tests; retain source identity, collection time, transformations, and claim support |
| Package / research lead | Freeze transferable source material, code, environments, results, assumptions, uncertainty, and limitations | Apply [package qualification](../guides/air-gapped-artifact-transfer.md#package-and-admit), including source-use permissions, to the analytical package |
| Transfer and admission / authorized custodian and receiving service | Carry the package through the customer-approved procedure | Apply [custody, quarantine, and admission gates](../guides/air-gapped-artifact-transfer.md#package-and-admit); retain receiving package identity |
| Internal processing and fusion / second AI factory | Re-run admitted analysis; develop new transformations, resolve identities, combine approved internal data, revise hypotheses, and evaluate new insights with or without human analysts | Deterministic pipeline and data checks repeat against local snapshots; protected fusion fixtures test joins, units, temporal alignment, missing data, and claimed results; each changed dataset/code/model/configuration is a new candidate |
| Internal acceptance / evaluator and customer analysis owner | Review evidence, uncertainty, and analytical fitness; authorize delivery to named internal recipients | Protected verdict, complete lineage, disclosed conflicts and limits, verified delivered artifact, and question-by-question acceptance |

The low-side result is a preliminary input. Internal analysis can confirm, qualify, or reject it. For example, a regional outage pattern may disappear after matching public events to internal asset identities and correcting observation windows; both findings and the reason for revision stay in the internal record.

## Human participation, autonomy, and authority

Each side independently permits human-assisted or unattended AI work for named activities. Deterministic checks remain mandatory in both modes. Standing grants specify data access, tools, outputs, resource limits, stop conditions, and recipients. Producers cannot alter protected evaluation criteria or grant themselves new data access. Where a selected control or the contract requires competent human/domain review, that activity stays assigned to an authorized reviewer; an unattended analysis run waits for the decision before acceptance.

Agents may explore approved data and create internal candidates, but cannot authorize transfer, broaden source use, change handling labels, or release conclusions beyond the named audience. A successful schema check cannot decide whether two variables mean the same thing, and repeatable code cannot establish that a hypothesis is true.

Apply the [separate return-transfer procedure](../guides/air-gapped-artifact-transfer.md#separately-authorize-return-transfers) to follow-up questions and artifacts. Internal prompts, embeddings, model weights adapted to restricted data, aggregate statistics, logs, and inferred relationships remain protected derived data unless explicitly cleared for the destination.

## Selected controls and proposed implementation

All selections are applicable, proposed, and not assessed. The research lead owns the selections with the data and evaluation owners. Before implementation, [record adoption](../adoption.md#record-the-adoption) with each control's identity, catalog version from the adopted revision, exact catalog commit, and pinned source URL; resolve dependencies at that revision.

| Risk / control | Owner and proposed mechanism |
|---|---|
| A dataset or derived insight is processed outside its permitted scope — [Approved data processing](../controls/approved-data-processing.md) | Data owners record permitted sources, uses, models, environments, and evidence destinations for both factories |
| Imported content executes with unrestricted access — [Execution isolation](../controls/execution-isolation.md) | Platform owner isolates collection, candidate execution, internal datasets, credentials, and evaluator resources |
| A follow-up question or derived artifact leaks restricted information — [Sensitive data egress](../controls/sensitive-data-egress.md) | Data owner enforces payload/destination review at each outgoing channel, including media and audit exports |
| An agent treats access as permission to transfer or publish — [Bounded external action](../controls/bounded-external-action.md) | Transfer and delivery services enforce actor, action, artifact, recipient, limits, expiry, and revocation |
| A producer edits expected results to fit its analysis — [Protected acceptance](../controls/protected-acceptance.md) | Evaluation owner protects canonical datasets, expected results, evaluator code, and verdicts from producer changes |
| Analytical code silently skips required validation — [Local quality gates](../controls/local-quality-gates.md) | Engineering owners pin static and behavioral checks for pipeline code on both sides; data checks supplement code checks |
| A changed table or internal rebuild inherits prior acceptance — [Qualified artifact promotion](../controls/qualified-artifact-promotion.md) | Delivery owners bind qualification to the full package and configuration and verify receiving artifacts; internal derivatives obtain their own qualification |
| Audit records cannot explain a data access or transfer — [Security event traceability](../controls/security-event-traceability.md) | Audit owner protects causal records of access, execution, admission, denial, review, and delivery |
| A polished insight hides weak or conflicting support — [Evidence traceability](../controls/evidence-traceability.md) | Research evaluator retains claim-to-source/analysis links, separates observation from inference, and records contradictory evidence |
| A report leaves the customer's questions unanswered — [Outcome verification](../controls/outcome-verification.md) | Customer owner checks each agreed question against a supported finding or accepted unknown |
| Fusion loses the source of a result or omits an affected consumer — [Data lineage impact](../controls/data-lineage-impact.md) | Data steward links actual runs, input snapshots, transformations, outputs, manual transfer events, and consumers; distinguishes observed lineage from declared dependencies |
| Matching column names conceal incompatible meaning — [Semantic mapping validation](../controls/semantic-mapping-validation.md) | Domain reviewers approve definitions, identifiers, units, time bases, cardinality, null semantics, and equivalent/lossy/unresolved mappings before reliance |

## Audit and assessment plan

The internal audit chain links the transferred package to original source revisions, collection windows, filters, missingness decisions, code and dependency versions, model configuration, seeds where relevant, actual run identifiers, internal dataset snapshots, mappings, and final claims. Record deterministic evaluator versions, expected results/tolerances, observed outputs, reviewer/grant identities, and exception dispositions. Fixed seeds alone do not guarantee repeatability across runtimes; define which computations must reproduce exactly and which require explicit numerical tolerances. Keep AI-generated narrative claims tied to inspectable evidence even when generation varies.

Apply [audit continuity](../guides/air-gapped-artifact-transfer.md#preserve-audit-continuity), keeping sensitive lineage identifiers, source extracts, and analytical outputs in approved internal evidence storage.

Run the full assessments of selected controls and these integrated exercises with synthetic sources and internal datasets:

1. Complete the question-to-delivery workflow in each permitted participation mode. Reconstruct one final finding through both factories, including the manual transfer and internal fusion run.
2. Modify a table or notebook after package approval, supply a missing/extra file, or redirect the destination. Deny admission; legitimate unchanged packages must still succeed.
3. Seed an entity collision, incompatible unit, shifted observation window, duplicate join key, and null incorrectly converted to zero. Block or visibly qualify each affected finding before acceptance; domain review resolves material ambiguity.
4. Give two apparently independent sources the same underlying origin. Preserve that dependence and prevent it from being counted as independent corroboration; retain contrary evidence from the internal data.
5. Change an internal input snapshot or transformation after qualification. Invalidate affected results, identify downstream consumers, and rerun required checks. Remove a lineage/custody record and verify that complete traceability is no longer claimed.
6. Try to alter protected expected values, forge a verdict, skip a deterministic test, or open an external connection from a child process. Confirm enforced denial and retained evidence of the attempt.
7. Attempt to release synthetic restricted values through a follow-up question, report, embedding, or log. Inspect recipient effects; prohibited release must fail while an explicitly permitted payload can pass.
8. Present a computationally valid analysis that does not answer one agreed question. Customer acceptance must expose the gap or record an accepted unknown instead of claiming all questions were resolved.

Record expected and observed effects, evaluator, time, scope, artifact identities, and dispositions. A failed requirement fails its assessment; unavailable observations are inconclusive. No exercise or operational effectiveness is asserted here.

## Remaining decisions and limits

Before operation, the customer must define actual contractual obligations, handling and transfer procedures, permitted data uses, source rights, reviewer competence, evidence retention, statistical validation, model/dependency admission, and incident response. Dataset representativeness, spurious correlation, selection bias, source deception, and re-identification remain material risks beyond deterministic schema and arithmetic checks. Reassess when questions, sources, mappings, models, autonomy, permissions, transfer routes, or intended decisions change. This example claims neither causal truth nor government certification.
