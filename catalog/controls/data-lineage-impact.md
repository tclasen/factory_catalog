---
type: Control
title: "Data lineage and impact assessment"
description: "Trace revisions and downstream consumers before data changes or corrections."
status: draft
tags: [data-mesh, data-stewardship]
family: change-and-dependencies
sources:
  - id: lineage
    resource: https://openlineage.io/docs/spec/object-model/
    title: "OpenLineage Object Model"
---

# Data lineage and impact assessment

[Adoption](../adoption.md) · [Data product design](../guides/data-product-design.md)

## Purpose and applicability

Apply when changes to source data or transformations can affect downstream analysis, reports, or decisions. OpenLineage distinguishes design metadata from events tied to a specific job run.[^lineage]

## Requirement

For each in-scope product revision, retain inspectable input revisions, transformation identity, output identity, and known consumer dependencies. Distinguish declared relationships from observed execution. Before a material change or correction, identify affected consumers and unresolved lineage gaps and obtain an authorized disposition for them.

## Implementation

1. Capture run or manual-processing records, timestamps, inputs, transformation revision, outputs, and restricted evidence locations. A human spreadsheet transformation still needs an identifiable procedure and output.
2. Reconcile the dependency graph with independently collected schedules, subscriptions, and consumer declarations. Record unmanaged exports as a coverage limit.
3. Trace a proposed correction forward and a reported defect backward. Inform affected owners and identify results requiring recomputation or review.
4. Keep [evidence traceability](evidence-traceability.md) for material claims and use [contract evolution](data-contract-evolution.md) for consumer transitions.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Within declared coverage, a change assessment identifies affected product revisions and consumers without presenting unknown dependencies as absent.

Use a fixture chain with two upstream inputs and two downstream consumers, including a manual export. Compare observed records with independently prepared ground truth. Remove one lineage event and introduce a stale declared edge; both must surface as gaps before change approval.

- **Pass:** the scoped implementation meets the requirement, and normal traces match the fixture, affected consumers are identified, and both missing and stale evidence prevent an unsupported complete-coverage claim.
- **Fail:** a requirement is violated; in particular, an affected fixture consumer is silently omitted or design metadata is represented as proof of an actual run.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** fixture ground truth, lineage records, coverage reconciliation, impact report, notices, and authorized gap dispositions.

## Dependencies and limitations

Requires observable processing and consumer participation. It cannot discover every offline copy. A dependency edge is not proof of permission, causation, or data quality. Protect identifiers and query text in lineage metadata. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^lineage]: [OpenLineage Object Model](https://openlineage.io/docs/spec/object-model/).
