---
type: Guide
title: "Domain context and translation records"
description: "Record model scope, inter-context influence, and semantic handoffs without changing the catalog schema."
status: draft
tags: [domain-driven-design, knowledge, coordination]
sources:
  - id: maps
    resource: https://contextmapper.org/docs/context-map/
    title: "Context Map, Context Mapper"
  - id: evans
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
    title: "Domain-Driven Design Reference, Eric Evans, March 2015"
---

# Domain context and translation records

[Domain model selection](guides/domain-model-selection.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## Purpose and representation

Use these records with [domain model boundaries](controls/domain-model-boundaries.md) and [context translation contracts](controls/context-translation-contracts.md). They are local artifact templates, not new ontology types or required OKF frontmatter. A small record can remain inside a factory's implementation document. Split it into a linked concept only when it needs independent reuse or lifecycle.

Context maps distinguish model relationships. Context Mapper supports separate current and desired states, symmetric partnerships/shared kernels, and upstream/downstream influence.[^maps] These records adapt that distinction to human and AI work. A blank or unknown field is an unresolved question, not approval.

## Context record template

| Field | Fill with |
|---|---|
| Identity and revision | Local record identity, effective revision/date, current or proposed state |
| Purpose | Decisions this model supports and beneficiary |
| Scope | Included and excluded work, applicable conditions, counterexample |
| Model maintainer | Person or role accountable for meaning; domain reviewers and missing perspectives |
| Language | Terms, verbs, rules, examples, and unresolved meanings under [contextual domain language](controls/contextual-domain-language.md) |
| Objects | [Identity namespaces and value equality rules](controls/domain-identity-and-values.md) |
| Rules | [Invariants](controls/domain-invariant-enforcement.md), acceptance mechanism, and deferred obligations |
| Occurrences | [Events](controls/domain-event-meaning.md), supporting evidence, and downstream interpretation |
| Interfaces | Producer, consumer, exchanged artifacts, relationship, translation record |
| Separate boundaries | Team ownership, deployments if any, information access, and authority references |
| Change | Affected consumers, reviewer, migration or correction needs, reassessment trigger |
| Assessment | Selected pinned control revisions, cases, evaluator, evidence, result and limitations |

## Relationship decisions

Evans describes several integration strategies.[^evans] The short descriptions below name options; selecting a label does not establish that participants have accepted its obligations.

| Option | Meaning | Proposed review question |
|---|---|---|
| Partnership | Coordinated evolution by mutually dependent teams | Can both parties commit to joint interface changes? |
| Shared kernel | Deliberately shared model subset | What exact content is shared and who must review changes? |
| Customer/supplier | Downstream priorities influence upstream planning | Is that influence observable in an agreed process? |
| Conformist | Receiver adopts the upstream model | Which local needs become difficult to express? |
| Anticorruption layer | Receiver translates into its own model | Who maintains and tests the translation? |
| Open host service and published language | A stable integration service and documented interchange terms | Which versions and consumers are supported? |
| Separate ways | Deliberately avoid integration | What duplication cost is accepted? |

Describe actual influence separately from the direction data travels. Record constraints if the upstream cannot cooperate. Do not claim a negotiated relationship merely because a consumer uses a producer's output.

## Translation record template

Record producer and consumer context revisions, owners, relationship, artifact versions, trigger, source and destination terms, identity mapping, units, preconditions, missing values, allowed transformations, information loss, unsupported cases, evidence, and change notification. Add expected outputs for normal, ambiguous, lossy, and revised-input cases. State which downstream decision the translation may support and which it cannot support.

### Fictional example: learning evidence

**Status:** proposed paper workflow; no implementation or assessment performed. The program coordinator owns the handoff, a teaching lead owns submission terminology, and an assessment lead owns rubric judgments. This example supplements the [learning factory](factories/learning.md).

| Item | Proposed record |
|---|---|
| Teaching context | Tracks a learner's submission for assignment revision A; “complete” means all required files received |
| Assessment context | Tracks demonstrated criteria against rubric revision R; its completion decision requires reviewer evidence |
| Relationship | Proposed customer/supplier agreement; assessor feedback must enter the coordinator's intake review before the relationship is considered established |
| Interchange language | Learner reference, assignment revision, submission revision, received time, file inventory, explicit status `received` |
| Translation | Teaching “complete” becomes assessment “ready for review”; it supplies no attained-criteria result |
| Identity and values | Learner reference is contextual identity; rubric score includes rubric revision and scale |
| Unsupported input | Unknown assignment revision or ambiguous learner reference remains unresolved and returns to the coordinator |
| Information loss | Receipt completeness says nothing about quality; the receiver keeps quality judgment pending |
| Authority | Intake permission does not permit issuing a certificate or publishing learner records |
| Change trigger | Assignment/rubric revision, changed definition, or new consumer requires mapping review |

Proposed checks: a valid submission enters review; a submission with unknown revision is held; a “received” event never becomes “mastery demonstrated”; a corrected learner reference triggers review of affected evidence. Assess the selected controls separately and retain observed results. This example's proposed outcomes are not passing evidence.

## Use and maintenance

Keep the current model and proposed changes separately identifiable. On a change, list impacted terms, mappings, rules, artifacts, and recipients, then use [planning consistency](controls/planning-consistency.md) to reconcile dependent work and rerun affected assessments. Retain exact source revisions under [evidence traceability](controls/evidence-traceability.md). These records describe mechanisms; their existence does not enforce a boundary or prove the chosen model is useful.

[^maps]: [Context Map, Context Mapper](https://contextmapper.org/docs/context-map/).
[^evans]: [Domain-Driven Design Reference, Eric Evans, March 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).
