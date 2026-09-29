---
type: Guide
title: "Domain-Driven Design for knowledge work"
description: "Research findings and selectable graph nodes for domain meaning, boundaries, rules, and collaboration."
status: draft
tags: [domain-driven-design, knowledge, coordination]
sources:
  - id: evans
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
    title: "Domain-Driven Design Reference, Eric Evans, March 2015"
  - id: bounded
    resource: https://martinfowler.com/bliki/BoundedContext.html
    title: "Bounded Context, Martin Fowler"
  - id: strategic
    resource: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis
    title: "Use domain analysis to model microservices, Microsoft"
  - id: tactical
    resource: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design
    title: "Use tactical DDD to design microservices, Microsoft"
  - id: vernon
    resource: https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf
    title: "Effective Aggregate Design, Part I, Vaughn Vernon, 2011"
  - id: maps
    resource: https://contextmapper.org/docs/context-map/
    title: "Context Map, Context Mapper"
  - id: storming
    resource: https://www.eventstorming.com/
    title: "EventStorming, official method website"
  - id: stories
    resource: https://domainstorytelling.org/quick-start-guide
    title: "Domain Storytelling Quick-Start Guide"
  - id: story-ddd
    resource: https://domainstorytelling.org/domain-driven-design
    title: "Domain-Driven Design with Domain Storytelling"
  - id: cqrs
    resource: https://martinfowler.com/bliki/CQRS.html
    title: "CQRS, Martin Fowler"
  - id: eventsourcing
    resource: https://martinfowler.com/eaaDev/EventSourcing.html
    title: "Event Sourcing, Martin Fowler"
---

# Domain-Driven Design for knowledge work

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## Research scope and evidence

This guide surveys foundational DDD patterns, strategic and tactical design, collaborative discovery, and related architecture choices. Sources were inspected on 2026-09-28. The bibliography covers eleven primary practitioner or official documentation sources: Evans's reference, Vernon's aggregate guidance, Fowler's explanations, Microsoft's architecture guidance, Context Mapper, EventStorming, and Domain Storytelling. This is a focused qualitative synthesis, not a systematic literature review or an empirical estimate of effectiveness.

DDD's original setting is software design. Its model and language practices offer candidate improvements to knowledge work. **The non-software procedures and examples in this guide are catalog proposals, not results demonstrated by the cited sources.** No workshop, deployment, or operational control assessment was performed. Definitions are paraphrased; no source framework is imported wholesale. Evans's reference is distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the linked controls adapt selected ideas into new requirements and assessments.

## What the research supports

### Shared meaning and continuous learning

DDD connects a domain model to the language practitioners use. A bounded context scopes that meaning; model refinement accompanies deeper understanding.[^evans] Domain Storytelling emphasizes shared language across conversation, diagrams, and implementation, with different languages allowed in different contexts.[^story-ddd]

**Catalog implication:** inspect how terms are used in actual work. A vocabulary page can be internally tidy while reports and prompts use incompatible definitions. [Contextual domain language](controls/contextual-domain-language.md) makes that discrepancy assessable. [Collaborative domain discovery](domain-discovery-workshops.md) provides a way to elicit examples and unresolved differences.

### Strategic design and investment

Microsoft distinguishes core, supporting, and generic subdomains to guide modeling effort: differentiation, custom supporting needs, and commonly solved capabilities require different investment choices. Its guidance presents domain analysis and boundary selection as iterative work.[^strategic]

**Catalog proposal:** for a selected outcome, list capabilities, beneficiaries, uncertainty, and consequences of failure. Identify where specialized knowledge creates value, where tailored support is needed, and where existing services may suffice. In a public research organization, value might mean mission-specific synthesis rather than commercial differentiation. Record the rationale with the [implementation selection](factory-implementation-selection.md) and [tradeoff](factory-implementation-tradeoffs.md) decisions. A generic capability can still be safety-critical; differentiation is not a risk ranking. Reassess classification when mission, demand, or available services change.

A subdomain describes part of the problem area; a bounded context specifies where a particular model applies. Treat their correspondence as a design hypothesis. Do not assign one graph directory, team, or deployed service per subdomain mechanically.

### Model boundaries and integration

Fowler explains why the same word can have different useful models and why a single enterprise model can become impractical. Context maps make relationships between those models explicit.[^bounded] Context Mapper distinguishes current from desired maps and models both symmetric relationships and upstream influence; an upstream dependency alone does not establish customer/supplier collaboration.[^maps]

**Catalog implication:** use [domain model boundaries](controls/domain-model-boundaries.md) for applicability and [context translation contracts](controls/context-translation-contracts.md) for meaning at handoffs. The [context record guide](domain-context-records.md) connects ownership, exchange rules, and unresolved questions. Diagram arrows must state whether they mean information flow, influence, or dependency. A link between nodes establishes none of these automatically.

### Tactical design and consistency

An entity preserves identity through change; a value object expresses a value through its attributes. Domain services express domain behavior that does not fit a single entity or value object; application services coordinate a use case. Domain events describe meaningful changes.[^tactical] Vernon emphasizes genuine business invariants when choosing aggregate consistency boundaries and warns that arbitrary large object clusters cause contention.[^vernon]

**Catalog implication:** [domain identity and values](controls/domain-identity-and-values.md) prevents mistaken matches; [domain invariant enforcement](controls/domain-invariant-enforcement.md) tests rules at acceptance; [domain event meaning](controls/domain-event-meaning.md) distinguishes requested from evidenced work. Their human procedures require observable mechanisms. A signature on a paper form does not provide transaction isolation when two people can independently accept conflicting changes.

DDD factories construct valid complex objects; repositories provide model-oriented access to stored aggregates.[^evans] These software patterns remain implementation options. A DDD factory is different from this catalog's knowledge-work Factory; a repository object is different from a Git repository. Neither term warrants changing the existing ontology.

### Discovery methods and architecture choices

EventStorming offers collaborative exploration of business domains, including organizational improvement and service design.[^storming] Domain Storytelling records concrete accounts of actors and work, then retells them for correction; its quick-start guidance separates individual scenarios from broader abstractions.[^stories] These methods can inform DDD without becoming mandatory rituals.

CQRS separates models used for updates and reads. Fowler warns that it can add substantial complexity where a shared model would suffice.[^cqrs] Event sourcing reconstructs state through event history; Fowler's article is explicitly unfinished draft material.[^eventsourcing] Neither is implied by adopting event vocabulary. A deployment decision needs its own evidence on operational cost, recovery, and maintainability. The proposed nodes impose no requirement to use microservices, event brokers, object-oriented programming, or a particular vendor.

## Node opportunities and graph relationships

The existing graph provides general evidence, outcome, and authority controls. These additions address the domain semantics those controls rely on. [Accepted work definition](controls/accepted-work-definition.md) establishes authorized scope and criteria; the language control checks what those criteria mean. [Planning consistency](controls/planning-consistency.md) handles changes across plans; the boundary and translation controls identify semantic dependencies to include in that review. [Decision rights and accountability](controls/decision-rights-and-accountability.md) assigns actionable authority; naming a model maintainer does not replace it. All additions are draft nodes under existing document types and families; their paths are identities. This table is the selection map for this guide, not a shared catalog registry.

| Opportunity and node | Gap addressed | Relationship to existing graph | Priority when applicable |
|---|---|---|---|
| [Contextual domain language](controls/contextual-domain-language.md) | Same term drives incompatible decisions | Specializes knowledge needed by evidence traceability | Start when ambiguity is material |
| [Domain model boundaries](controls/domain-model-boundaries.md) | A valid rule is applied outside its scope | Makes model applicability explicit within operating context | Start before combining models |
| [Context translation contracts](controls/context-translation-contracts.md) | A handoff preserves fields but loses meaning | Adds semantic checks to artifact exchanges | Select for cross-context exchange |
| [Domain identity and values](controls/domain-identity-and-values.md) | Similar records are mistaken for identical objects | Supports reliable evidence joins | Select before matching or aggregation |
| [Domain invariant enforcement](controls/domain-invariant-enforcement.md) | Accepted changes violate a business constraint | Complements outcome verification and bounded action | Select for mandatory acceptance rules |
| [Domain event meaning](controls/domain-event-meaning.md) | A request or report becomes an unsupported completion | Connects evidence to workflow transitions | Select for occurrence-based coordination |
| [Collaborative domain discovery](domain-discovery-workshops.md) | Implicit practice and disagreement are missing from models | Produces scoped inputs for work definition and controls | Use when domain understanding is uncertain |
| [Domain context and translation records](domain-context-records.md) | Models and interfaces lack inspectable records | Produces artifacts for the six controls | Use with the selected controls |

This research guide is also an OKF node. Links carry their relationship in surrounding prose; they do not mean adoption or successful assessment. For reuse, follow [adoption](adoption.md#record-the-adoption), including exact source commit URLs for each selected control. Shared indexes, taxonomies, and catalog version remain unchanged.

## Applications beyond software delivery

The following are fictional design sketches. They propose operational questions, not domain advice or claims of effectiveness.

| Work setting | Modeling question | Candidate selection and observable check |
|---|---|---|
| [Research](factories/research.md) | Does “verified” refer to source authenticity, extraction accuracy, or a supported conclusion? | Language and evidence controls; present an accurate extraction of an unsupported claim and check that the conclusion remains unsupported |
| [Learning](factories/learning.md) | Does “complete” mean submitted, graded, or demonstrated mastery? | Language and event controls; submission must not establish rubric attainment |
| [Contract operations](factories/contracts.md) | Are received drafts, reviewed terms, and accepted obligations distinguishable? | Translation and bounded action; a received draft must not trigger an acceptance commitment |
| Editorial production | Does acceptance by an editor imply permission to publish? | Boundary and event controls; editorial acceptance remains separate from publication authority |
| Service operations | Can two coordinators allocate the final slot independently? | Invariant control; concurrent requests must not exceed declared capacity |
| Knowledge curation | Do records with the same label identify the same subject? | Identity and translation controls; test equal labels, distinct namespaces, and an unresolved match |
| [Software delivery](factories/software-delivery.md) | Does the implemented behavior match the model and its rules? | Choose all applicable controls; test normal, invalid, and cross-context scenarios against the implemented boundary |

## Adoption experiment and remaining opportunities

Choose one costly misunderstanding or handoff and record a baseline sample, such as corrections caused by ambiguous statuses over a declared period. Select only the nodes addressing that problem. Name a domain reviewer and operator, prepare positive and adverse cases, run the selected assessments, and record evidence. Compare the same outcome measure after adoption with [outcome verification](controls/outcome-verification.md); differences alone do not establish causation. Track modeling and coordination cost alongside the benefit.

For investment decisions, first assess [capability investment alignment](controls/capability-investment-alignment.md); for model-change impact, use [planning consistency](controls/planning-consistency.md); for shared-data consumer compatibility, use [data contract evolution](controls/data-contract-evolution.md). Additional domain-specific requirements need distinct acceptance criteria and a demonstrated gap before becoming standalone controls. Full catalogs of DDD patterns, new schema types for every tactical object, and prescriptive microservice blueprints are deferred because the current guides and existing ontology can represent the useful decisions without them. Reviewers should decide whether these six control boundaries are independently useful and whether their proposed non-software assessments fit the intended adoption contexts.

[^evans]: [Domain-Driven Design Reference, Eric Evans, March 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).
[^bounded]: [Bounded Context, Martin Fowler](https://martinfowler.com/bliki/BoundedContext.html).
[^strategic]: [Use domain analysis to model microservices, Microsoft](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis).
[^tactical]: [Use tactical DDD to design microservices, Microsoft](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design).
[^vernon]: [Effective Aggregate Design, Part I, Vaughn Vernon, 2011](https://www.dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf).
[^maps]: [Context Map, Context Mapper](https://contextmapper.org/docs/context-map/).
[^storming]: [EventStorming, official method website](https://www.eventstorming.com/).
[^stories]: [Domain Storytelling Quick-Start Guide](https://domainstorytelling.org/quick-start-guide).
[^story-ddd]: [Domain-Driven Design with Domain Storytelling](https://domainstorytelling.org/domain-driven-design).
[^cqrs]: [CQRS, Martin Fowler](https://martinfowler.com/bliki/CQRS.html).
[^eventsourcing]: [Event Sourcing, Martin Fowler](https://martinfowler.com/eaaDev/EventSourcing.html).
