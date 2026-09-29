---
type: Factory Example
title: "Government software factory across an air gap"
description: "A government contract develops sensitive software in low-side and air-gapped AI factories with controlled file transfer and auditable acceptance."
status: draft
example: true
domain: "Government software delivery"
work_types: [design-and-specification, software-and-computational-development, evaluation-and-assurance, monitoring-and-operational-response]
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
---

# Example: government software factory across an air gap

[Factory examples](./) · [Ontology](../ontology.md) · [Adoption](../adoption.md) · [Software delivery example](software-delivery.md)

**Fictional government contract; proposed implementations; no assessments performed.** The contractor must deliver sensitive software with strict security and auditability. Two AI factories perform substantive development: one on the low side and another inside the customer's air-gapped environment. Files cross through a separately authorized transfer procedure. This example specifies local design choices, not compliance with a named government security regime.

## Factory profile

| Field | Design |
|---|---|
| Purpose / accountable owner | Build a maintenance-planning service for a government customer; contractor delivery lead owns delivery and the customer acceptance owner owns acceptance |
| Low-side inputs | Requirements explicitly approved for low-side processing, synthetic fixtures, approved source and dependencies; sensitive operational details stay inside the air gap |
| Transfer artifacts | Source snapshot, build recipes, dependency inventory and approved offline dependencies, tests, documentation, manifest, and evidence for that exact package |
| Air-gapped inputs and outputs | Admitted package plus local sensitive requirements, interfaces, and test data → further code changes, internal build, acceptance evidence, and a deployable internal release |
| Intended outcome / measure | During an authorized ten-working-day pilot, designated customer operators complete every agreed maintenance-planning scenario, with no unauthorized record access or unresolved critical acceptance defect; unobserved scenarios remain unverified |
| Actors | Low-side and internal AI agents; optional developers and reviewers; security/data owner; transfer custodian; platform owner; independent acceptance owner; internal release operator |
| Contract constraints | Customer-defined processing locations, data markings, personnel access, transfer channels, evidence retention, review duties, and acceptance criteria are recorded before execution |

“Low side” means the environment approved for the lower-sensitivity portion of this contract; it does not mean every input may be public or sent to any model provider. If a requirement cannot be disclosed there, only an approved abstraction or synthetic equivalent may be used. The air-gapped factory uses locally available models, tools, dependency stores, and evidence storage without external inference, telemetry, package downloads, or remote rendering.

## Two factories and their handoff

Use the [air-gapped artifact transfer procedure](../guides/air-gapped-artifact-transfer.md) for packaging, admission, internal requalification, and audit continuity. The following stages specialize it for this contract.

| Stage / owner | Work performed | Required gate and retained output |
|---|---|---|
| Scope / customer and security owners | Separate low-side requirements from sensitive local requirements; declare acceptance criteria and authority for each activity | Approved brief, handling rules, grants, and independently protected acceptance configuration |
| Low-side development / development factory | AI agents design, implement, debug, and iterate with or without human developers | Deterministic format, lint, type, unit, integration, security, and dependency checks as applicable; bind commands, tool versions, fixtures, and results to the final source/build revision |
| Package / low-side release owner | Assemble source, build recipes, offline dependencies, tests, documentation, and revision-bound evidence | Apply [package qualification](../guides/air-gapped-artifact-transfer.md#package-and-admit) to the software distributable |
| Transfer and admission / authorized custodian and receiving service | Carry the package through the customer-approved procedure | Apply [custody, quarantine, and admission gates](../guides/air-gapped-artifact-transfer.md#package-and-admit); retain receiving package identity |
| Internal development / air-gapped factory | Import into an isolated workspace; adapt code to sensitive interfaces, implement local features, and debug against approved internal fixtures, with or without human developers | Rebuild with admitted tools and dependencies; run deterministic checks again plus sensitive integration and access-control tests; every internal edit or relevant configuration change creates a new candidate requiring affected qualification |
| Internal acceptance and release / acceptance owner and release operator | Evaluate the internal candidate against protected criteria, authorize deployment, and observe the pilot | Independent acceptance verdict, separate release grant, destination artifact/configuration verification, and customer outcome evidence |

## Human participation, autonomy, and authority

Each factory may use human-assisted development, unattended AI development, or a mix by activity. The two sides choose independently. Unattended work uses bounded standing grants, deterministic gates outside the producer's write authority, run limits, and a stop path for ambiguity or failure. Optional human participation in development does not remove any review, transfer, or acceptance duty required by the contract. Work waits when a mandatory human decision is unavailable.

Agents may edit their assigned workspace and run admitted tools. They cannot change acceptance criteria, signing trust, security policy, transfer permissions, or deployment grants. A separate acceptance service evaluates candidates without exposing its credentials to candidate code. Neither a human review nor an AI review replaces required deterministic checks; those checks also cannot establish every security property or customer outcome.

Apply the [separate return-transfer procedure](../guides/air-gapped-artifact-transfer.md#separately-authorize-return-transfers) to code, logs, screenshots, prompts, crash dumps, and derived test results; they remain inside unless the exact content and destination are approved.

## Selected controls and proposed implementation

All selections are applicable, proposed, and not assessed. The delivery lead owns the selection record with the security and acceptance owners. Before implementation, use the [adoption record](../adoption.md#record-the-adoption) to pin every selected control's identity, catalog version from the adopted revision, exact catalog commit, and source URL. Resolve dependencies at that same revision.

| Risk / control | Owner and proposed mechanism |
|---|---|
| Sensitive requirements reach an unapproved provider — [Approved data processing](../controls/approved-data-processing.md) | Security owner declares permitted data, models, processing sites, and evidence destinations on each side |
| Imported code gains access to unrelated data or shared credentials — [Execution isolation](../controls/execution-isolation.md) | Platform owner enforces workload resource allowlists, separate identities, mediated state import, and cleanup |
| Internal diagnostics leak through a permitted channel — [Sensitive data egress](../controls/sensitive-data-egress.md) | Data owner controls exact payload, audience, channel, and handling of derived data and removable media |
| Passing tests are treated as authority to transfer or deploy — [Bounded external action](../controls/bounded-external-action.md) | Transfer and release owners enforce separate grants bound to actor, artifact, destination, limits, and validity |
| The producer weakens acceptance — [Protected acceptance](../controls/protected-acceptance.md) | Acceptance owner protects criteria, fixtures, evaluator code, credentials, and verdict records from producer writes |
| A candidate bypasses required checks on either side — [Local quality gates](../controls/local-quality-gates.md) | Each engineering owner pins applicable deterministic checks and blocks missing, failed, or unexplained skipped checks |
| A different package or internal rebuild inherits an old pass — [Qualified artifact promotion](../controls/qualified-artifact-promotion.md) | Release owners bind evidence to complete artifacts and configuration; verify receiving and installed bytes; requalify internal changes |
| A reviewer cannot reconstruct access, transfer, or release — [Security event traceability](../controls/security-event-traceability.md) | Audit owner protects causal event records and detects gaps, alteration, and logging outages |
| A completion claim lacks support — [Evidence traceability](../controls/evidence-traceability.md) | Evaluator maps requirements and material claims to revision-bound observations, contradictions, and explicit gaps |
| Technically accepted code does not serve the customer — [Outcome verification](../controls/outcome-verification.md) | Customer owner assesses declared pilot scenarios separately from build and release success |

## Audit and assessment plan

Apply [audit continuity](../guides/air-gapped-artifact-transfer.md#preserve-audit-continuity) from the contract requirement through the low-side revision, package, internal code changes and build, acceptance verdict, and deployed artifact. Link customer scenario observations to that internal release.

Run every selected control's assessment before claiming effectiveness. Add these integrated cases using synthetic sensitive fixtures:

1. Complete a benign change through both factories, in each permitted human-participation mode. Verify internal development actually changes and requalifies the imported candidate and that customer scenarios succeed.
2. Alter, omit, or add a file after package approval; supply an untrusted signature or wrong destination. Receiving admission must reject the package before use.
3. Introduce a defect visible only against internal fixtures. Low-side success must not permit internal acceptance; repair and reassess the changed internal candidate.
4. Attempt to weaken a protected test, forge a verdict, skip a required check, or modify a grant using producer credentials. Confirm denial and no transfer/deployment effect.
5. Put synthetic sensitive markers in logs and generated artifacts; attempt outbound telemetry and return-media disclosure. Confirm prohibited recipients receive nothing, while an explicitly permitted transfer succeeds.
6. Remove a custody record, interrupt audit storage, or lose the admission acknowledgement. Detect incomplete evidence, inspect receiving state before retrying, and keep completion unresolved until reconciled.

Retain expected and observed effects, fixture/configuration identities, evaluator, time, and dispositions. Failed cases fail the relevant assessment; unobservable effects are inconclusive. These are proposed exercises, not executed tests of a deployed factory.

## Remaining decisions and limits

Before operation, the customer must supply the actual contract obligations, handling rules, approved transfer procedure, trust/key administration, model and dependency admission policy, evaluator qualification, incident response, and retention schedule. Reassess when requirements, sensitivity, tools/models, autonomy, authority, transfer routes, or acceptance criteria change. Air-gap isolation and deterministic checks do not alone establish secure software, certification, or contractual compliance.
