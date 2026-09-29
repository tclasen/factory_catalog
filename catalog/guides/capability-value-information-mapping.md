---
type: Guide
title: "Map capabilities, value, and information"
description: "Connect a beneficiary outcome to business abilities, service stages, participating actors, and shared information."
status: draft
sources:
  - id: g211
    resource: https://publications.opengroup.org/g211
    title: "TOGAF® Series Guide: Business Capabilities, Version 2"
  - id: g178
    resource: https://publications.opengroup.org/g178
    title: "TOGAF® Series Guide: Value Streams"
  - id: g190
    resource: https://publications.opengroup.org/g190
    title: "TOGAF® Series Guide: Information Mapping"
  - id: g206
    resource: https://publications.opengroup.org/g206
    title: "TOGAF® Series Guide: Organization Mapping"
---

# Map capabilities, value, and information

[Ontology](../ontology.md) · [Research basis](../open-group-guides-research.md) · [Adoption](../adoption.md)

## Purpose and source boundary

Use this procedure when planning or revising a knowledge-work service across departments or organizations. It brings together themes from capability, value-stream, organization, and information mapping guides.[^g211][^g178][^g206][^g190] The steps and record below are a catalog-designed synthesis of their public descriptions; no full-guide procedure or formal TOGAF mapping is claimed.

A capability here means an ability the organization needs. It is recorded in the local design alongside the people, activities, information, and resources that realize it. A value stage is a planning grouping of activities with an intended contribution. These labels do not add document types or relations to the catalog ontology.

## Procedure

1. Name the beneficiary, desired change, decision owner, scope, and constraints. Identify affected parties with [stakeholder concern validation](../controls/stakeholder-concern-validation.md).
2. Describe required abilities independently of preferred products. Assess observed gaps with [capability investment alignment](../controls/capability-investment-alignment.md).
3. Map the service trigger and stages. State each stage’s contribution and acceptance evidence using [value stream stage acceptance](../controls/value-stream-stage-acceptance.md).
4. Name participating actors, organizations, and responsible owners. Record authority separately; a role in a map is not a grant to act.
5. Map consumed and produced artifacts, their meaning, provenance, and sensitivity. Resolve cross-party differences using [information meaning agreement](../controls/information-meaning-agreement.md).
6. Identify risk scenarios and applicable controls. Check exchanges with [interoperability acceptance](../controls/interoperability-acceptance.md) and overall benefit with [outcome verification](../controls/outcome-verification.md).
7. Review the combined map with the relevant owners. Resolve gaps or record an owner, restriction, and review trigger. Pin adopted controls and cross-references to the same source revision using [adoption](../adoption.md).

## Local design record

| Field | What to record |
|---|---|
| Factory/context | Scope, service owner, participating organizations, exclusions, affected populations |
| Outcome | Beneficiary, criterion, baseline if claiming improvement, observation period, evaluator |
| Needed ability | Business meaning, present evidence, target, gap, dependency, responsible owner |
| Stage/activity | Trigger, work types, actor, entry condition, intended contribution, exit evidence |
| Artifact/information | Input/output revision, definition, population, units, time basis, source, steward, sensitivity |
| Exchange | Sending and receiving parties, allowed use, acceptance and failure behavior |
| Authority | Issuer, actor, permitted action, resource, limits, validity, approval conditions |
| Risk/control | Cause, condition, harm, affected party, control identity, applicability and rationale |
| Implementation/assessment | Mechanism and state; evaluated revision, method, evidence, result and limits |
| Open decision | Unknown or disagreement, decision owner, deadline/trigger, consequence of proceeding |

Small objects can remain rows in the factory’s design. Split an object into an independently linked concept only when reuse or a separate lifecycle warrants it and the domain schema supports the document type. A complete table is an artifact, not evidence that the service works.

## Worked fragment: library learning support

Fictional planning example; no implementation or assessment has occurred.

- **Factory seeks outcome:** adult learners can complete a supported application task, assessed by observed practice during the program. Publishing a workbook is an artifact milestone.
- **Needed ability:** explain and practice the task with accessible materials; current gap evidence would come from learner observation and feedback, not a proposed software purchase.
- **Factory performs activities:** intake needs, prepare material, facilitate practice, assess task completion. Classify them using [work types](../work-types.md), including teaching and capability development and evaluation and assurance.
- **Actors perform activities:** librarians facilitate; learners practice; a program lead owns acceptance. Any application submission needs separate authority.
- **Activities consume/produce artifacts:** learner brief, lesson material, practice record, assessment result. Retain only information necessary for the stated purpose under applicable access and retention rules.
- **Control supports outcome:** outcome verification assesses observed ability. **Control addresses risk:** information meaning agreement prevents “attended” being silently reported as “can perform the task”.

## Review questions

Can each stage identify a beneficiary contribution and recipient? Is every claimed ability supported by observable activity and adequate resources? Do information definitions agree at the boundaries? Are missing participants and capacity conflicts visible? Does the outcome measure assess the desired change?

Return a map for revision when it cannot answer these questions. Record unknowns and restrictions when evidence cannot be obtained. The formal pass/fail procedures belong to each selected control; this guide does not issue a composite passing result.

[^g211]: G211, Business Capabilities, Version 2; public description accessed 2026-09-29 UTC.
[^g178]: G178, Value Streams; public description accessed 2026-09-29 UTC.
[^g206]: G206, Organization Mapping; public description accessed 2026-09-29 UTC.
[^g190]: G190, Information Mapping; public description accessed 2026-09-29 UTC.
