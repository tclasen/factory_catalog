---
type: Control
title: "Value stream stage acceptance"
description: "Define the value, evidence, and acceptance conditions at each stage of a service."
status: draft
family: workflow-and-coordination
sources:
  - id: g178
    resource: https://publications.opengroup.org/g178
    title: "TOGAF Series Guide: Value Streams"
  - id: g206
    resource: https://publications.opengroup.org/g206
    title: "TOGAF Series Guide: Organization Mapping"
---

# Value stream stage acceptance

[Adoption](../../../catalog/adoption.md) · [Control families](../../../catalog/control-families.md)

## Purpose and applicability

Address locally completed work that leaves a beneficiary without a usable result. Apply to services spanning teams or organizations: claims, procurement, research delivery, student support, and public administration. A single activity can use one stage if the beneficiary and acceptance conditions remain explicit.

## Requirement

Before operating a service, define its trigger, beneficiary, intended value, stages, and completion boundary. For each stage, name the responsible actor, entry conditions, output, recipient, acceptance evidence, and owner for rejected or stalled work. Report stage completion only after its declared acceptance conditions are met; record partial and failed paths separately.

## Implementation

1. Identify the beneficiary and the result they need; distinguish internal task completion from delivered value.
2. Map stages and their dependencies. Include rejection, withdrawal, rework, and escalation paths with response deadlines appropriate to the service.
3. Have each receiving party agree what constitutes usable input. Assign responsibility for gaps spanning organizations.
4. Record acceptance or rejection with the work identifier, artifact revision, time, and reason. Keep a visible queue for unaccepted work.
5. Review aged and repeatedly rejected cases. Assess overall benefit with [outcome verification](../../../catalog/controls/outcome-verification.md), even when every internal stage has completed.

Mechanism: a human service review and case record, optionally enforced by workflow state transitions. Sending a file alone must not mark recipient acceptance.

## Expected outcome and assessment

Expected outcome: all cases reported complete in the assessed scope have acceptance evidence at the declared boundaries.

Trace a complete case from trigger to beneficiary receipt. Test an accepted case, a case sent without recipient acceptance, and a rejected case with no initial rework owner.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the accepted case completes; the unaccepted case stays pending; the rejected case stays incomplete and is escalated to assign an owner. Records identify every stage and its evidence.
- **Fail:** transmission is reported as acceptance, a rejected case disappears, or responsibility for a required stage is missing without escalation.
- **Inconclusive:** case records or recipient evidence are unavailable.
- **Evidence:** stage map revision, acceptance criteria, case history, receipt or rejection evidence, escalation records, and fixture dispositions.

## Dependencies and limitations

Requires participating teams to recognize the acceptance mechanism and service owner. Recipient acceptance can itself be mistaken or coerced; it is not proof of beneficiary benefit. This control governs stage value and acceptance; use the [mapping guide](../guides/capability-value-information-mapping.md) to connect stages to abilities and information. Apply the [adoption procedure](../../../catalog/adoption.md) before implementation.

## Source basis

G178 describes developing and connecting a business value model. G206 relates capabilities and value streams to participating organizational units and third parties.[^g178][^g206] The operational gates and tests here are original catalog proposals based on those public descriptions.

[^g178]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g206]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
