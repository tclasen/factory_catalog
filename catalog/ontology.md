---
type: Ontology
title: "Factory definitions and record schema"
description: "Shared meanings and metadata needed to select, implement, and assess factory controls."
status: stable
---

# Factory definitions and record schema

[Catalog](index.md) · [Adoption](adoption.md) · [Control families](control-families.md)

## Concepts

| Term | Meaning and required local context |
|---|---|
| Factory | A system producing knowledge-work outcomes; describe purpose, accountable owner, activities, and operating context |
| Activity | Work with identified actors, inputs, outputs, dependencies, autonomy, and authority |
| Actor | A person, team, process, or AI system with an assigned role and responsibility |
| Artifact | An inspectable input or output with identity, revision, provenance, and sensitivity |
| Outcome | A desired change for a beneficiary, judged by a criterion and observation period |
| Authority grant | Permission for an actor/action/resource, with issuer, limits, validity, and approval conditions |
| Context | Domain, exposure, data sensitivity, scale, obligations, reversibility, and unknowns affecting applicability |
| Risk scenario | A cause acting through a condition to threaten an outcome or artifact and affected parties |
| Control | A selectable requirement with applicability, implementation, assessment, and limitations |
| Implementation | A local mechanism applying a particular control revision within owned scope |
| Assessment | Evaluation of an identified target revision using a method, criteria, evaluator, time, result, and evidence |
| Evidence | An observation or artifact supporting a specific finding, with origin, time, scope, and access restrictions |

## Relationships

A factory performs activities that consume/produce artifacts and seek outcomes. Actors perform work under separately recorded authority. Controls address risks or support outcomes; a local implementation applies a pinned control revision. Assessments evaluate implementations or outcomes using evidence. One control can address several risks, and an artifact can serve as evidence without being duplicated.

### Relationships in use

Links express relationships whose meaning is stated in the surrounding prose. A control link can mean a candidate selection, dependency, example, or evidence source; it never establishes adoption, permission, or successful assessment by itself. Record workflow order and handoffs explicitly.

## Rules that preserve meaning

- Missing authority is not permission; missing assessment is not a pass. Keep unknowns explicit.
- Record autonomy, authority, and escalation per activity. Capability does not grant authority.
- Separate applicability, implementation state, and assessment result. A pass is limited to its method, scope, time, and target revision.
- Identify the actual mechanism: instructions, human procedure, automated check, or technical restriction. Document bypass paths and incomplete coverage.
- Keep artifact acceptance, beneficiary outcome, and control assessment separate. A control can pass by correctly detecting an unmet outcome.
- Assess composed workflows, including shared credentials, memory, and handoffs. Individual passing controls do not establish system-wide effectiveness.

## Document types and metadata

Concepts use OKF 0.2 with `type`, `title`, and `description`. Identity is the bundle-relative path without `.md`; the sole catalog version is [VERSION](VERSION) at the consumed commit. Sources and keyed footnotes retain provenance. Local records may be embedded in a document; they need separate identities only when reuse or lifecycle requires them.

| Type | Purpose | Additional metadata |
|---|---|---|
| Ontology | Shared definitions and record schema | None |
| Taxonomy | Control browsing vocabulary | None |
| Guide | A concrete design, implementation, or assessment procedure | None |
| Risk Scenario | Hypothetical cause, conditions, harm, candidate controls, and assessment example | None |
| Control | Individually selectable and assessable requirement | `family` from [control families](control-families.md) |
| Factory Example | Fictional application of selected controls | `example: true`, non-empty `domain`, non-empty `activities` list, non-empty `control_selections` list |

`activities` contains free-text descriptions of the work performed, such as “compare contract terms” or “assess independent learner performance”. It has no external taxonomy dependency. `domain` names the subject matter. Each control selection contains:

| Field | Value |
|---|---|
| `control` | Relative Markdown path to a Control |
| `applicability` | `applicable`, `not-applicable`, or `undetermined` |
| `implementation_state` | `not-planned`, `proposed`, `implemented`, or `retired` |
| `assessment_result` | `not-assessed`, `pass`, `fail`, or `inconclusive` |

The body explains scope, rationale, assumptions, owner, mechanisms, evidence needs, and reassessment triggers. Real adoption uses the [adoption record](adoption.md#record-the-adoption). An example is not an observed deployment; a risk scenario is not an incident report.

## Identity and lifecycle

Derive control identity from its path and family from frontmatter. Paths are independent of family names. Read version and content at the same pinned commit; keep historical adoption records unchanged. Before v1, paths and definitions may change without compatibility aliases.

`draft` marks proposed definitions needing review; `stable` means ready for consumption. Neither asserts implementation, effectiveness, or release approval. Absent `verified` metadata asserts no document verification event. Document verification and local operational assessment are separate.
