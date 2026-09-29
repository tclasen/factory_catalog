---
type: Control
title: "Context translation contracts"
description: "Preserve meaning and expose information loss at domain handoffs."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: workflow-and-coordination
sources:
  - id: evans
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
    title: "Domain-Driven Design Reference, Eric Evans, March 2015"
---

# Context translation contracts

[Adoption](../../../catalog/adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent a handoff from changing the meaning of a decision or artifact without detection. Apply when two contexts exchange terms, statuses, identifiers, measurements, or rules. Evans describes an anticorruption layer as an adapter that protects a receiving model, and a published language as a documented interchange vocabulary.[^evans] The requirements below are a catalog adaptation and can be implemented as a reviewed human procedure.

This control defines the agreement at a handoff: who owns each meaning, which revisions are accepted, and how loss or unsupported input is handled. [Semantic mapping validation](semantic-mapping-validation.md) provides complementary review of whether a mapping preserves its declared meaning. For combinations of data products, [data semantic interoperability](data-semantic-interoperability.md) addresses join cardinality, populations, and reconciliation of the combined result.

## Requirement

For every interface in the adopted scope, identify producer, consumer, owners, applicable revisions, required meanings, mapping rules, information loss, and handling of unsupported input. Accept a translated result only when its required meaning is preserved or the receiving owner explicitly accepts a disclosed limitation under local authority.

## Implementation

1. Identify the two [contexts](domain-model-boundaries.md) and the decisions the receiver will make. Record who can change each side; use [context records](../domain-context-records.md) to make influence explicit.
2. Map terms, identity namespaces, units, status transitions, and missing-value meanings. Distinguish absent, unknown, false, and not applicable where the decision requires it.
3. Specify preconditions, accepted revisions, expected outputs, lossy cases, rejection or escalation, and a change notification owner. Do not invent a default for an unrecognized status.
4. Choose a manual translation table or an adapter with observable checks. If adopting an upstream meaning unchanged, record the decision and its consequences.
5. Validate normal and adverse cases before use and after relevant change. Keep original input references and the mapping revision under [evidence traceability](../../../catalog/controls/evidence-traceability.md).

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: all required meanings in the declared interface sample survive translation, and unsupported or lossy mappings receive their stated disposition.

Exercise a valid mapping, an unknown input value, a known lossy mapping, and a changed upstream definition. For a fictional contract workflow, “document received” must not map to “obligation accepted.” A round trip alone is insufficient: reviewers must check the decision meaning.

- **Pass:** the valid case produces the expected meaning; unsupported input is held or rejected; information loss is disclosed and handled before acceptance; changed definitions trigger review before reuse.
- **Fail:** a fabricated, obsolete, or materially altered meaning reaches an accepted output without the required disposition.
- **Inconclusive:** source meaning or downstream interpretation cannot be established.
- **Evidence:** interface and mapping revisions, input/output pairs, loss records, reviewer judgments, change cases, and dispositions.

## Dependencies and limitations

Depends on scoped language, [identity rules](domain-identity-and-values.md), and access to both sides' meaning or explicit uncertainty. Semantic translation is not an information-security boundary, permission grant, or proof of business correctness. Use [bounded external action](../../../catalog/controls/bounded-external-action.md) for consequential actions. Pin adopted controls separately. No implementation has been assessed here.

[^evans]: [Domain-Driven Design Reference, Eric Evans, March 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).
