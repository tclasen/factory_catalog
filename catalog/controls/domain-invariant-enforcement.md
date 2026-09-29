---
type: Control
title: "Domain invariant enforcement"
description: "Enforce declared business rules at the point where a change becomes accepted."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: quality-and-validation
sources:
  - id: vernon
    resource: https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf
    title: "Effective Aggregate Design, Part I, Vaughn Vernon, 2011"
---

# Domain invariant enforcement

[Adoption](../adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent individually plausible changes from producing an invalid combined state. Apply when acceptance depends on a rule that must hold across related items. Vernon grounds aggregate boundaries in genuine business invariants and shows how oversized aggregates create unnecessary contention.[^vernon] This control adapts the consistency question to both software and human workflows.

## Requirement

For every invariant in scope, record its domain justification, covered state, acceptance boundary, owner, and enforcement mechanism. Require the rule to hold when the change is accepted. Distinguish immediate invariants from obligations allowed to complete later; give later obligations a deadline, responsible party, and unresolved or failure disposition.

## Implementation

1. Have a domain reviewer distinguish a mandatory rule from a preference. Link the rule to the [context and language](contextual-domain-language.md) revision.
2. Identify exactly which state must be checked together and which operations can alter it. Use the smallest boundary that covers the rule; document bypass paths.
3. Specify the acceptance mechanism: a database transaction, reservation, controlled register, or human sign-off with exclusive access to current state. A written instruction alone cannot guarantee concurrency safety.
4. Recheck at acceptance, including changes since preparation. Define rejection, rework, and authorized exception handling; an exception that changes a rule needs its own explicit scope and revision.
5. For work across boundaries, track pending obligations and reconcile them by the declared deadline. Do not describe temporary inconsistency as satisfaction of an immediate invariant.

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: every accepted change in the declared test set preserves its immediate invariants; later obligations remain visible until resolved.

Test a valid change, a direct violation, two conflicting changes prepared from the same initial state, and an attempted bypass. If deferred obligations are used, also test timely completion and expiry. A fictional education program has one remaining workshop seat: two requests may each look valid in isolation, but accepting both violates its capacity rule.

- **Pass:** the valid change succeeds; violating, conflicting, and bypassing changes cannot produce an accepted invalid state; any deferred case receives its predeclared completion or expiry disposition.
- **Fail:** any required case is omitted or an invalid state is accepted, including through a bypass or stale check.
- **Inconclusive:** the assessor cannot observe the final state or the claimed enforcement boundary.
- **Evidence:** rule revision and rationale, starting state, operations and interleaving, mechanism, final state, acceptance decisions, and pending-obligation records.

## Dependencies and limitations

Requires current state, authority over all relevant writers, and observable acceptance. Human procedures need an actual way to prevent overlapping acceptance if that is the claim. [Exclusive mutation ownership](exclusive-mutation-ownership.md) addresses competing and stale writers at the write boundary; current ownership alone does not establish that the resulting state satisfies a domain invariant. Technical aggregate patterns do not make a multi-party human process atomic. Use [outcome verification](outcome-verification.md) separately for beneficiary results and [bounded external action](bounded-external-action.md) for permission. No operational result is asserted.

[^vernon]: [Effective Aggregate Design, Part I, Vaughn Vernon, 2011](https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf).
