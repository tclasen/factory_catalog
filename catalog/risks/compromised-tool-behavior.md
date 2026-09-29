---
type: Risk Scenario
title: "A compromised tool changes execution behavior"
description: "A tool or dependency changes its advertised interface, executable behavior, or returned data to influence the worker or downstream system."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: AML.T0010
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L1189
    title: "AML.T0010: AI Supply Chain Compromise"
  - id: AML.T0110
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L4896
    title: "AML.T0110: AI Agent Tool Poisoning"
---

# A compromised tool changes execution behavior

[ATLAS assessment guide](../atlas-threat-assessment.md) · [Ontology](../ontology.md) · [Adoption](../adoption.md)

**Identity:** `risks/compromised-tool-behavior` · **Catalog:** v0.1.0

## Cause and enabling conditions

A previously approved integration update acquires new permissions, alters a destination, or returns active content that a downstream component interprets unsafely. The attack crosses a dependency or tool boundary.

## Threatened outcomes and affected parties

Execution integrity, sensitive artifacts, and authorized outcomes are threatened. Tool users, adjacent workloads, and external parties may be affected.

## Candidate controls

- [Tool and dependency admission](../controls/tool-and-dependency-admission.md) addresses this scenario by the following mechanism: withholds unapproved revisions and material changes.
- [Tool input output validation](../controls/tool-input-output-validation.md) addresses this scenario by the following mechanism: rejects contract violations at each consuming boundary.
- [Execution isolation](../controls/execution-isolation.md) addresses this scenario by the following mechanism: contains access beyond the workload.
- [Adversarial regression assessment](../controls/adversarial-regression-assessment.md) addresses this scenario by the following mechanism: tests changed behavior and release dispositions.

These are applicability candidates, not adoption or effectiveness claims. The local factory owner records applicability, scope, assumptions, an assessment owner, and a reassessment trigger using the [adoption procedure](../adoption.md).

## Assessment example

Use an approved fixture tool, then change its digest, definition, or permissions and attempt loading it. Separately return contract-violating content and attempt access to another workload's synthetic marker. Observe loading, execution, and rendering. Record admission revisions, validation decisions, denied accesses, and positive-case results.

Evaluate each selected control using its own criteria. A forbidden effect is a failure; missing observations are inconclusive. This is a hypothetical fixture, with no local implementation or assessment asserted.

## Limits and reassessment

A signature or successful admission review cannot prove benign behavior. Mutable remote services may change without notice; record this uncertainty and contain their access. Reassess on supplier, interface, credential, or implementation changes.

## Source basis

This scenario is a catalog interpretation informed by AML.T0010[^AML.T0010], AML.T0110[^AML.T0110]. Source case studies illustrate reported conditions, not current vendor vulnerability status or local attack probability.

[^AML.T0010]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0110]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
