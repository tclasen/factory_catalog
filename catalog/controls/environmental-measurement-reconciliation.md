---
type: Control
title: "Environmental measurement reconciliation"
description: "Preserve boundaries, units, methods, and missing data when assembling environmental reports."
catalog_version: "v0.1.0"
status: draft
family: knowledge-and-evidence
sources:
  - id: g259
    resource: https://publications.opengroup.org/g259
    title: "The Open Footprint Business Guide"
  - id: g242
    resource: https://publications.opengroup.org/g242
    title: "TOGAF Series Guide: Environmentally Sustainable Information Systems"
---

# Environmental measurement reconciliation

[Adoption](../adoption.md) · [Control families](../control-families.md)

**Identity:** `controls/environmental-measurement-reconciliation` · **Catalog:** v0.1.0 · **Family:** `knowledge-and-evidence`

## Purpose and applicability

Address misleading environmental totals or improvement claims caused by mixed boundaries, units, periods, and methods. Apply to emissions, energy, water, or waste reporting assembled from multiple records. Select a domain-approved accounting method separately; this control does not choose one.

## Requirement

Before accepting a consolidated environmental measure, record its reporting boundary, period, included sources, units, calculation method and revision, conversions or factors, exclusions, missing inputs, and reviewer. Reconcile inputs to the declared population; distinguish measured, estimated, and unavailable values. A comparison must explain changes in boundary or method, and must not claim improvement from an unexplained change in scope.

## Implementation

1. Assign a reporting owner and domain-qualified reviewer. Define the facilities, activities, categories, and period covered, plus tolerances for reconciliation.
2. Retain original observations and provenance. For each transformation, record formula, factor version, applicable geography/time, units, and estimate status where relevant.
3. Check duplicates, missing facilities or periods, unit conversions, and aggregation rules. Reconcile the sum to the input ledger, documenting adjustments.
4. Compare with prior reporting only after checking boundary and method compatibility. Restate or qualify comparisons when they differ.
5. Have the reviewer accept, return, or restrict the claim. Preserve the released report revision and its evidence; route publication through [bounded external action](bounded-external-action.md).

Mechanism: reconciliation procedure and review, optionally supported by deterministic calculations. Review must inspect assumptions as well as arithmetic.

## Expected outcome and assessment

Expected outcome: every published measure in the assessed scope can be traced to its population, method, and inputs without hiding incompleteness.

Recalculate a declared report. Test a complete compatible ledger, mixed units, a missing site represented as zero, and an apparent reduction caused only by excluding a facility.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the complete ledger reconciles within the predeclared tolerance; mixed units are normalized with recorded conversions; the missing site stays visible as missing; the changed-boundary comparison is restated or explicitly qualified before acceptance.
- **Fail:** an input gap is silently zero-filled, incompatible units are added, or a scope change is reported as an established improvement.
- **Inconclusive:** source inputs or factor/method versions needed for reconstruction cannot be inspected.
- **Evidence:** boundary record, source ledger, transformation versions, reconciliation results, exceptions, comparison basis, and review disposition.

## Dependencies and limitations

Requires a suitable accounting method and competent domain review. No reporting-standard compliance, assurance opinion, or Open Footprint conformance follows from passing this procedure. [Information meaning agreement](information-meaning-agreement.md) governs shared definitions, [evidence traceability](evidence-traceability.md) governs claims, and [outcome verification](outcome-verification.md) governs claimed improvements. Follow [adoption](../adoption.md).

## Source basis

G259 introduces the strategic purpose and extensibility of the Open Footprint Data Model; G242 proposes an architecture approach to reducing information-system environmental impact.[^g259][^g242] The reconciliation checks above are original catalog design; the public descriptions do not establish detailed accounting rules.

[^g259]: Public product description, accessed 2026-09-29 UTC; full guide and data model not reviewed.
[^g242]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
