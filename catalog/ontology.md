---
type: Ontology
title: "Factory ontology"
description: "Concepts, relationships, and record conventions for describing factories and their controls."
catalog_version: "v0.1.0"
status: stable
---

# Factory ontology

[Catalog](index.md) · [Work types](work-types.md) · [Control families](control-families.md)

## Concepts

The ontology defines the following concepts and relationships. A record may embed small objects such as an authority grant or outcome; each object does not need its own file. The document types and metadata used in this bundle are defined below.

| Concept | Meaning | Minimum information |
|---|---|---|
| Factory | A particular system organized to produce knowledge-based outcomes | Purpose, accountable owner, activities, operating context |
| Activity | Work performed within a factory | Work types, actors, inputs, outputs, autonomy, authority references |
| Actor | A person, team, process, or AI system with a role | Identity, role, responsibility |
| Artifact | An input or output that can be inspected | Identity, revision, provenance, sensitivity |
| Outcome | A desired change or state | Beneficiary, success criterion, observation period |
| Authority grant | Permission for an actor to perform an action within a scope | Issuer, actor, action, resource/destination, limits, validity, approval conditions |
| Context | Conditions that affect operation and applicability | Domain, data, exposure, scale, obligations, reversibility, unknowns |
| Risk scenario | A cause or threat acting through a condition to produce harm | Cause, condition, unwanted outcome, affected parties |
| Control | A reusable requirement that addresses risk or supports an outcome | Purpose, applicability, requirement, implementation guidance, assessment, limitations |
| Implementation | How a factory applies a particular control revision | Scope, owner, mechanism, parameters, adaptations, adoption reference |
| Assessment | An evaluation of an implementation or factory outcome | Target revision, method, criteria, evaluator, time, result, evidence references |
| Evidence | A retained observation or artifact supporting an assessment | Origin, time, scope, integrity/reference information, access restrictions |
| Blueprint | A reusable arrangement of activities, roles, and controls | Assumptions, required capabilities, interfaces, control selections |

Evidence may itself be an artifact. Treat “evidence” as its role in an assessment; do not duplicate a report merely because it supports a finding. A blueprint describes a reusable arrangement; a factory describes a particular system, and an example may describe a hypothetical factory without claiming deployment.

## Relationships

| Subject | Relationship | Object | Meaning |
|---|---|---|---|
| Factory | performs | Activity | Work is within the factory's scope |
| Factory | seeks | Outcome | The outcome explains the factory's purpose |
| Factory | operates under | Context | Applicability depends on these conditions |
| Factory | instantiates | Blueprint | Optional connection to a reusable design |
| Actor | performs | Activity | Responsibility is assigned |
| Activity | consumes / produces | Artifact | Inputs and outputs are explicit |
| Activity | contributes to | Outcome | Contribution is intended, not proven |
| Authority grant | permits | Actor + action + scope | Permission is constrained, not inferred from capability |
| Risk scenario | threatens | Outcome or artifact | Describes possible harm in a stated context |
| Control | addresses | Risk scenario | A rationale, not proof that risk is eliminated |
| Control | supports | Outcome | Controls can enable quality and value as well as reduce risk |
| Implementation | implements | Control revision | A local mechanism realizes a reusable requirement |
| Implementation | applies within | Factory or activity | Prevents assuming universal coverage |
| Assessment | evaluates | Implementation or outcome | Establishes the subject of the finding |
| Assessment | uses | Evidence | The finding can be inspected |

Most relationships allow many objects: an activity can have several work types, and one control can address several risks. Relationship names do not imply ordering; a workflow must separately state dependencies and handoffs.

## Rules that preserve meaning

1. **Missing means unknown.** Absence of an authority grant is not permission. Absence of an assessment is not a pass. Absence of a risk record does not establish safety.
2. **Autonomy is activity-specific.** Record what can be planned and performed independently, stop conditions, and escalation. Record authority separately, including delegation limits.
3. **Applicability is a decision.** Use applicable, not-applicable, or undetermined, with rationale, assumptions, owner, and a condition or date for reassessment.
4. **Implementation is a separate state.** Use not-planned, proposed, implemented, or retired. Record partial coverage and exceptions explicitly.
5. **Assessment is a separate result.** Use not-assessed, pass, fail, or inconclusive. A pass applies only to its method, scope, time, and target revision. Changed conditions can require reassessment.
6. **Control instructions are not enforcement.** Identify whether the mechanism is instructions, human procedure, an automated check, or a technical restriction. Record bypass paths and dependencies.
7. **Evidence is scoped.** A successful permission test does not establish factual accuracy; a quality review does not establish authority to publish.
8. **Composition adds questions.** Check shared memory, credentials, handoffs, and combined authority. Passing individual control tests does not establish that the complete system is safe.

## Document types and metadata

This bundle uses OKF 0.2. Its domain-specific fields extend OKF; they do not redefine the format's required fields or trust signals. Every concept has `type`, `title`, `description`, and `catalog_version`. Catalog version is `v0.1.0`. An OKF concept's identity is its bundle-relative path without `.md`, for example `controls/evidence-traceability`.

| Document type | Purpose | Additional fields |
|---|---|---|
| Ontology | Definitions and relationships | None |
| Taxonomy | Enumerated browsing vocabulary | None |
| Guide | A reusable procedure for using the catalog | None |
| Control | A reusable, assessable requirement | `family`: a value from the control-family taxonomy |
| Factory Example | A fictional factory profile | `example: true`, `domain`, `work_types`, `control_selections` |

`work_types` is a list of values from the [work taxonomy](work-types.md). `domain` is free text describing subject matter. A `control_selections` entry contains:

| Field | Meaning / values |
|---|---|
| `control` | Relative Markdown path to the control, resolved from the containing concept |
| `applicability` | `applicable`, `not-applicable`, or `undetermined` |
| `implementation_state` | `not-planned`, `proposed`, `implemented`, or `retired` |
| `assessment_result` | `not-assessed`, `pass`, `fail`, or `inconclusive` |

The body records rationale, assumptions, owner, scope, implementation details, evidence expectations, and reassessment triggers. `not-planned` records no planned implementation; it does not imply that a control is unnecessary. Partial implementation is described explicitly and does not earn a passing result. Real adoption adds the [pinned adoption record](adoption.md#record-the-adoption); selection alone is not adoption.

Each concept is a Markdown file. Small local objects such as grants and outcomes can be tables or structured blocks in that concept. Split them into independently linked concepts when they need their own identity, reuse, or lifecycle. The conceptual ontology is broader than the document types needed for this initial collection.

## Relationships in use

In the [contract factory](factories/contracts.md), a drafting agent **performs** comparison and drafting activities that **produce** revised artifacts. An authorized signatory **performs** acceptance under a separate authority grant. The factory **seeks** an authorized agreement with tracked obligations. Its selection of [bounded external action](controls/bounded-external-action.md) **addresses** the risk of unauthorized commitments. A local implementation enforces that control; an assessment evaluates the implementation using execution records and observed effects as evidence.

Markdown links assert relationships; surrounding prose names their meaning. The `control` field in a selection is a structured link to a reusable requirement. Generic OKF readers can navigate the documents without understanding these extensions. A graph consumer must not infer that any link means adoption, permission, or successful assessment.

## Identity and lifecycle

Control paths stay independent of family names so a classification change does not move the control. Preserve published identities and document replacements and migration when a change is unavoidable. For interim revisions, use exact commit SHAs with catalog version v0.1.0.

`status: stable` means that a definition is ready for consumption under OKF. It does not signify an approved release baseline, human verification, implementation, or effectiveness. The absence of `verified` means no document verification event is asserted. Local assessment results remain separate from OKF document verification.

## Design basis

The initial design uses an ontology for relationships and taxonomies for browsing; separates work type from domain, autonomy from authority, artifacts from outcomes, and controls from implementation evidence; and keeps small objects embedded until reuse justifies separate concepts. It uses 16 work types, 11 control families, and semantic control paths. These decisions implement the owner's direction to establish the discussed content directly in the catalog. Baseline approval and release changes remain separate decisions.

No formal reasoner or graph database is required. Test future schema changes against concrete factories and preserve the distinctions above.
