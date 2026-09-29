---
type: Guide
title: "Select domain modeling controls"
description: "Choose controls for ambiguous language, model boundaries, identity, invariants, and handoffs."
status: draft
sources:
  - id: evans
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
    title: "Domain-Driven Design Reference, Eric Evans, March 2015"
  - id: bounded
    resource: https://martinfowler.com/bliki/BoundedContext.html
    title: "Bounded Context, Martin Fowler"
---

# Select domain modeling controls

[Adoption](../../../catalog/adoption.md) · [Domain discovery](../domain-discovery-workshops.md) · [Context records](../domain-context-records.md)

## Start with a costly misunderstanding

Choose a concrete decision or handoff and collect examples from its practitioners. Record the intended outcome, accountable owner, model scope, and current rework or failure. Shared language and bounded models inform this procedure.[^evans][^bounded] Non-software applications are catalog proposals, not demonstrated outcomes from those sources.

| Observed problem | Select and assess |
|---|---|
| One term leads to incompatible decisions | [Contextual domain language](../controls/contextual-domain-language.md) |
| A valid rule is applied outside its context | [Domain model boundaries](../controls/domain-model-boundaries.md) |
| A handoff preserves fields but changes meaning | [Context translation contracts](../controls/context-translation-contracts.md) |
| Equal labels are treated as identical subjects | [Domain identity and values](../controls/domain-identity-and-values.md) |
| Concurrent accepted actions break a business rule | [Domain invariant enforcement](../controls/domain-invariant-enforcement.md) |
| Requested or reported work is treated as completed | [Domain event meaning](../controls/domain-event-meaning.md) |

## Implement and test one boundary

Use the context record for actors, terms, namespaces, rules, upstream dependencies, translation decisions, and unresolved meanings. Distinguish current from intended arrangements. An arrow must state whether it means information flow, influence, or dependency. Record authority separately.

Test normal, invalid, and cross-context cases with a domain reviewer. For contracts, receiving a draft must not establish acceptance. For teaching, submission must not establish mastery. For a shared service, two coordinators must not allocate the last slot twice. An accurate extraction of an unsupported claim must remain unsupported in research.

Retain the original misunderstanding, selected controls, target revisions, before/after examples, reviewer dispositions, and coordination cost. Run each control's full assessment; use [outcome verification](../../../catalog/controls/outcome-verification.md) for any claimed reduction in rework. No workshop or operational assessment is asserted here.

## Implementation choices

A model does not require microservices, event sourcing, or a graph database. Separate read/write models or event histories need their own cost, recovery, and maintainability evidence. Prefer the simplest arrangement that supports the selected controls. Use [capability investment alignment](../controls/capability-investment-alignment.md) for investment and [data contract evolution](../controls/data-contract-evolution.md) for affected consumers.

[^evans]: Eric Evans, Domain-Driven Design Reference, March 2015; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^bounded]: Martin Fowler, Bounded Context; source review inherited from the repository's 2026-09-28 research.
