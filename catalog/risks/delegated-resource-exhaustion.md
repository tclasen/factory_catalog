---
type: Risk Scenario
title: "Delegated work exhausts shared resources"
description: "An adversary or faulty workflow induces repeated operations, retries, or recursive delegation."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: AML.T0034.002
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L2302
    title: "AML.T0034.002: Agentic Resource Consumption"
  - id: AML.M0036
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L7016
    title: "AML.M0036: Limit AI Workload Resource Consumption"
---

# Delegated work exhausts shared resources

[ATLAS assessment guide](../atlas-threat-assessment.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Identity:** `risks/delegated-resource-exhaustion` · **Catalog:** v0.1.0

## Cause and enabling conditions

A single research request spawns child searches that each consume what they assume is an independent budget. Concurrent calls and delayed metering allow spending to continue after the parent stops.

## Threatened outcomes and affected parties

Service availability, operating budgets, and timely useful work are threatened. The job owner and other users of shared capacity may be affected.

## Candidate controls

- [Workflow resource budgets](../controls/workflow-resource-budgets.md) addresses this scenario by the following mechanism: enforces shared limits including retries and in-flight work.
- [Security event traceability](../controls/security-event-traceability.md) addresses this scenario by the following mechanism: connects job and child decisions to effects.
- [Outcome verification](../controls/outcome-verification.md) addresses this scenario by the following mechanism: distinguishes resource consumption from a useful outcome.

These are applicability candidates, not adoption or effectiveness claims. The local factory owner records applicability, scope, assumptions, an assessment owner, and a reassessment trigger using the [adoption procedure](../adoption.md).

## Assessment example

Run a normal bounded job, recursive child requests, a retry storm, and concurrent children racing for the remaining allocation. Observe aggregate and in-flight use after stopping and resuming. Retain ledger/configuration revisions and child records. Total use must remain within predeclared bounds while the normal job succeeds.

Evaluate each selected control using its own criteria. A forbidden effect is a failure; missing observations are inconclusive. This is a hypothetical fixture, with no local implementation or assessment asserted.

## Limits and reassessment

Budgets do not guarantee useful results or fair allocation among users. External billing delay can make a ceiling unverifiable without conservative reservations. Reassess when pricing, call costs, retry policy, or delegation changes.

## Source basis

This scenario is a catalog interpretation informed by AML.T0034.002[^AML.T0034.002], AML.M0036[^AML.M0036]. Source case studies illustrate reported conditions, not current vendor vulnerability status or local attack probability.

[^AML.T0034.002]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.M0036]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
