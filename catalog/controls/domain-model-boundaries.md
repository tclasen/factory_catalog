---
type: Control
title: "Domain model boundaries"
description: "Declare where a model applies and who maintains its meaning and interfaces."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: purpose-and-accountability
sources:
  - id: bounded
    resource: https://martinfowler.com/bliki/BoundedContext.html
    title: "Bounded Context, Martin Fowler"
  - id: maps
    resource: https://contextmapper.org/docs/context-map/
    title: "Context Map, Context Mapper"
---

# Domain model boundaries

[Adoption](../adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent rules or assumptions from one activity being silently applied to another. Apply where models differ across teams, workflows, products, or datasets. Fowler describes bounded contexts as scopes of internally consistent models with explicit relationships.[^bounded] This control adapts that idea to knowledge work.

## Requirement

Record the purpose, included and excluded decisions, domain language, artifacts, maintainer, and interfaces of each model in scope. Mark whether the boundary describes current operation or a proposed design. Check the declared context before reusing a rule or combining information from another model.

## Implementation

1. Select concrete cases with different meanings or rules. Propose a boundary where those differences need to remain explicit.
2. Complete a [context record](../domain-context-records.md) and connect its [domain language](contextual-domain-language.md), input and output artifacts, and owner.
3. Describe existing relationships first. Label proposed changes separately. Context Mapper explicitly distinguishes current and desired maps.[^maps]
4. Walk a case across each interface. Record translation ownership, shared definitions, and unresolved assumptions using [translation contracts](context-translation-contracts.md).
5. Revisit the boundary when rules, ownership, or dependencies change. Identify affected users and checks before applying the new model revision.

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: the sampled decisions and exchanges have a known applicable model; out-of-context reuse is detected before acceptance.

Declare the contexts and interfaces being assessed. Inspect a valid case, an excluded case offered to the model, and a cross-context case with conflicting meanings. Inspect a proposed boundary change as well.

- **Pass:** the valid case is processed in scope; the excluded case is redirected or held; the conflicting meanings invoke a documented mapping or unresolved disposition; the proposal is visibly distinct from current operation and lists affected interfaces.
- **Fail:** a material decision uses an inapplicable model or a proposed boundary is represented as already operating.
- **Inconclusive:** evidence cannot establish the scope of a sampled decision or the actual interface behavior.
- **Evidence:** context revisions, current and proposed maps, case walkthroughs, routing observations, interface owners, and change impact records.

## Dependencies and limitations

Requires identifiable decisions and model maintainers. A bounded context is a semantic boundary. Record team ownership, software deployment, information access, and [authority grants](../ontology.md#concepts) separately; a model diagram enforces none of them. The ontology's operating Context describes conditions and is not automatically a DDD bounded context. A single document can contain several models if their scopes are explicit. No operational assessment is claimed.

[^bounded]: [Bounded Context, Martin Fowler](https://martinfowler.com/bliki/BoundedContext.html).
[^maps]: [Context Map, Context Mapper](https://contextmapper.org/docs/context-map/).
