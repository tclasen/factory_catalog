---
type: Risk Scenario
title: "Authorized tool use discloses prohibited data"
description: "An adversary influences a payload sent through a tool the worker is otherwise allowed to use."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: AML.T0086
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L4208
    title: "AML.T0086: Exfiltration via AI Agent Tool Invocation"
  - id: AML.CS0035
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L8348
    title: "AML.CS0035: Data Exfiltration from Slack AI via Indirect Prompt Injection"
---

# Authorized tool use discloses prohibited data

[ATLAS assessment guide](../atlas-threat-assessment.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Identity:** `risks/authorized-tool-data-disclosure` · **Catalog:** v0.1.0

## Cause and enabling conditions

A contract activity can update a shared document but includes private terms in an update to an unauthorized audience. Sensitive information may also travel through generated links, search parameters, or logs.

## Threatened outcomes and affected parties

Private artifacts and confidentiality commitments are threatened. Contract parties, data subjects, and the accountable organization may be affected.

## Candidate controls

- [Sensitive data egress](../controls/sensitive-data-egress.md) addresses this scenario by the following mechanism: enforces data and recipient combinations before transmission.
- [Bounded external action](../controls/bounded-external-action.md) addresses this scenario by the following mechanism: constrains the action and destination but does not establish payload safety.
- [Security event traceability](../controls/security-event-traceability.md) addresses this scenario by the following mechanism: provides protected evidence for reconstruction.

These are applicability candidates, not adoption or effectiveness claims. The local factory owner records applicability, scope, assumptions, an assessment owner, and a reassessment trigger using the [adoption procedure](../adoption.md).

## Assessment example

Use a synthetic private marker in a permitted tool call directed at a prohibited recipient. Observe actual receipts and rendered/network effects; pair it with an allowed non-sensitive transfer. Retain sanitized decisions and destination observations. No forbidden marker may arrive, while the allowed transfer succeeds.

Evaluate each selected control using its own criteria. A forbidden effect is a failure; missing observations are inconclusive. This is a hypothetical fixture, with no local implementation or assessment asserted.

## Limits and reassessment

A permitted recipient can misuse information after receipt. Detection of one marker does not prove resistance to every encoding or inference. Reassess when data classes, audiences, or outgoing channels change.

## Source basis

This scenario is a catalog interpretation informed by AML.T0086[^AML.T0086], AML.CS0035[^AML.CS0035]. Source case studies illustrate reported conditions, not current vendor vulnerability status or local attack probability.

[^AML.T0086]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.CS0035]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
