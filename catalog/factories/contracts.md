---
type: Factory Example
title: "Contract operations factory"
description: "A contract workflow with distinct drafting, negotiation, signing, and records authority."
catalog_version: "v0.1.0"
status: stable
example: true
domain: "Procurement and contracts"
work_types: ["analysis-and-diagnosis", "content-and-media-production", "evaluation-and-assurance", "coordination-and-relationship-work", "decision-making-and-adjudication", "case-and-transaction-processing", "knowledge-organization-and-stewardship"]
control_selections:
  - control: ../controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
---

# Example: contract operations factory

[Factory examples](./) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Fictional design case; proposed implementations; no assessments performed.**

## Factory profile

| Field | Design |
|---|---|
| Why / owner | Prepare an authorized agreement and track its obligations; procurement owner coordinates the process |
| Domain / work types | Procurement and contracts; analysis, drafting, evaluation, coordination, adjudication, case processing, stewardship |
| Inputs → artifacts | Approved brief and counterparty draft → comparison, revised draft, approval record, executed document, obligation register |
| Outcome | Authorized parties execute the intended agreement, and each identified obligation has an owner and due date or recorded interpretation issue |
| Measure | Before case closure, authorized reviewer reconciles the executed revision to approval and every identified obligation to the register; unresolved material issues prevent closure |
| Actors | Drafting agent, procurement reviewer, authorized signatory, records process |
| Context | Confidential terms; untrusted counterparty documents; signing and records systems; commitments may be difficult to reverse |

## Activities, autonomy, and authority

| Activity | Independent work allowed | Authority boundary |
|---|---|---|
| Compare and draft | Agent extracts terms and prepares revisions within the brief | Draft workspace only; no communicating offers or accepting terms |
| Review and negotiate | Reviewer coordinates changes within their mandate | Explicit communication and negotiation limits; escalation beyond mandate |
| Accept terms | Signatory decides within their recorded mandate | Signing service checks current authority and approved revision/destination |
| Record obligations | Process extracts candidate owners and dates | Writes require validated mapping and scoped records access; ambiguous terms escalate |

Workflow: intake → comparison → draft → review/negotiation loop → signatory approval → execution → reconciliation and records → closure. A material revision returns to review and invalidates any approval bound to the prior revision.

## Control selections

| Scenario or objective | Control | Applicability / proposed implementation |
|---|---|---|
| Comparison silently omits a changed obligation | [Evidence traceability](../controls/evidence-traceability.md) | Applicable: reviewer links material findings to exact clauses and draft revisions |
| Agent or reviewer accepts terms outside their mandate | [Bounded external action](../controls/bounded-external-action.md) | Applicable: enforce permissions at communication, signing, and records boundaries; signing approval binds revision and counterparty |
| Signed document is filed but obligations remain unassigned | [Outcome verification](../controls/outcome-verification.md) | Applicable: closure checklist reconciles execution and obligation ownership against the reviewed document |

## Assessment plan and evidence

Use a sandbox signing service. Test a valid approved revision and attempts with a changed revision, wrong recipient, expired/revoked grant, and drafting-agent identity. Exercise alternate and delegated paths. Verify authorized effects and absence of effects for denied attempts. Separately test a case with a signed artifact but missing obligation owner; the factory outcome must remain unmet.

Retain sanitized grant revisions, path inventory, attempt records, sandbox effects, document comparison, execution reconciliation, and obligation-check results. Approval records are evidence of authority within scope, not evidence that contractual terms are sound.

All implementations are **proposed** and assessments **not assessed**. No agreement was prepared, sent, or executed by this example.

## Remaining gaps and reassessment

Confidentiality, expert interpretation, identity verification, retention, duplicate actions, and recovery need additional controls. A new counterparty channel, signing tool, delegation, authority limit, or document revision triggers the relevant reassessment. The procurement owner coordinates it with the authority owner and reviewer.

## Selection and adoption

The selections above link to controls in this bundle revision. They describe a fictional design, not actual adoption or passing evidence. Before implementing a selection, follow the [adoption procedure](../adoption.md) to pin its control identity, catalog version, and exact source URL. The profile owner also owns applicability decisions; the reassessment triggers above apply to those decisions.
