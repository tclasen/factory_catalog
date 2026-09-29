---
type: Control
title: "Information meaning agreement"
description: "Resolve differences in business meaning before exchanging or combining information."
catalog_version: "v0.1.0"
status: draft
family: knowledge-and-evidence
sources:
  - id: g190
    resource: https://publications.opengroup.org/g190
    title: "TOGAF Series Guide: Information Mapping"
  - id: g225
    resource: https://publications.opengroup.org/g225
    title: "The Open Group Guide to the O-DEF Standard, 2nd Edition"
---

# Information meaning agreement

[Adoption](../adoption.md) · [Control families](../control-families.md)

**Identity:** `controls/information-meaning-agreement` · **Catalog:** v0.1.0 · **Family:** `knowledge-and-evidence`

## Purpose and applicability

Address decisions corrupted by apparently compatible information with different meanings. Apply when teams combine records, exchange reports, reuse knowledge, or compare measures across organizations. Examples include different meanings of enrolled student, active supplier, completed case, and emissions total.

## Requirement

Before material information is combined or reused, have its producer and consumer agree the intended meaning, population, units, time basis, identity rules, owner, and permitted interpretation. Record versioned mappings and known losses of meaning. Ambiguous or incompatible values must be quarantined, qualified, or transformed under an approved rule before use; an identical field name or identifier is insufficient evidence of equivalence.

## Implementation

1. Scope material concepts with the decision owner. Record business definitions separately from physical column names and file formats.
2. Assign a steward on each side of an exchange. Capture examples, counterexamples, units, inclusion rules, missing-value behavior, and the relevant definition revision.
3. Record identity matching rules, relationships, transformations, precision loss, and unresolved differences. Explicitly distinguish zero from unknown.
4. Have producers and consumers review representative records. Validate transformations against agreed examples before admitting the exchange.
5. Reassess dependent reports when definitions change, retaining prior mappings and identifying outputs requiring correction.

Mechanism: steward review plus a maintained mapping record; optional schema and transformation checks provide only their stated coverage.

## Expected outcome and assessment

Expected outcome: every material concept used in the declared exchange has an agreed interpretation or a visible unresolved restriction.

Review one exchange and its downstream use. Test a valid mapping, matching field names with different populations, and an unknown value that would otherwise be converted to zero.

Declare the assessed revision, scope, evaluator, and time. A pass requires all scoped records to meet the requirement as well as the fixture results below. Any unmet mandatory requirement is a failure; missing evidence does not override an observed failure. A documented exception must not be reported as satisfying an unmet requirement.

- **Pass:** the valid mapping is accepted; population differences are resolved or qualified before use; unknown remains distinguishable from zero. Every scoped concept has owner and revision records.
- **Fail:** matching syntax is treated as proof of meaning, an unresolved difference is hidden, or a changed definition silently alters prior claims.
- **Inconclusive:** source definitions or representative records cannot be inspected.
- **Evidence:** definition and mapping revisions, steward decisions, example records, transformation results, affected-output list, and restrictions.

## Dependencies and limitations

Requires domain knowledge and access to representative data under its access rules. Agreement does not establish that records are true or that reuse is permitted. [Evidence traceability](evidence-traceability.md) addresses support for claims; [interoperability acceptance](interoperability-acceptance.md) addresses the broader exchange. Retain pinned references under [adoption](../adoption.md).

## Source basis

G190 focuses on business-critical information before solution design. G225 describes the O-DEF guide’s second edition and its treatment of roles.[^g190][^g225] These motivate a semantic review; the specific fields and tests are this catalog’s synthesis. No O-DEF identifiers or formal mappings are asserted.

[^g190]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
[^g225]: Public product description, accessed 2026-09-29 UTC; full guide not reviewed.
