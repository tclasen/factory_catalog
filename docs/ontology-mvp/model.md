# Proposed ontology

[MVP overview](index.md)

## Concepts

Use these as conceptual types before committing to a storage schema. A record may embed small objects such as an authority grant or outcome; each object does not need its own file.

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
3. **Applicability is a decision.** Use applicable, not applicable, or undetermined, with rationale, assumptions, owner, and a condition or date for reassessment.
4. **Implementation is a separate state.** Use proposed, implemented, or retired. Record partial coverage and exceptions explicitly.
5. **Assessment is a separate result.** Use not assessed, pass, fail, or inconclusive. A pass applies only to its method, scope, time, and target revision. Changed conditions can require reassessment.
6. **Control instructions are not enforcement.** Identify whether the mechanism is instructions, human procedure, an automated check, or a technical restriction. Record bypass paths and dependencies.
7. **Evidence is scoped.** A successful permission test does not establish factual accuracy; a quality review does not establish authority to publish.
8. **Composition adds questions.** Check shared memory, credentials, handoffs, and combined authority. Passing individual control tests does not establish that the complete system is safe.

## Small relationship example

This YAML is an illustrative instance notation, not OKF frontmatter or an adopted schema. IDs are local example labels, not catalog control identities. Unlisted profile fields remain in the [contract example](examples/contracts.md). File references are relative to this document.

```yaml
factory: contract-example
activities:
  - id: prepare-draft
    work_types: [analysis-and-diagnosis, content-and-media-production]
    actor: drafting-agent
    produces: draft-revision-7
    autonomy: prepare drafts within the approved brief
    authority: draft-workspace-only
  - id: accept-terms
    work_types: [decision-making-and-adjudication]
    actor: authorized-signatory
    authority: signatory-mandate
control_selection:
  control: controls/bounded-external-action.md
  applicability: applicable
  rationale: accepting terms creates an external commitment
  implementation_state: proposed
  assessment_result: not assessed
```

The example shows a proposed control selection, not an adoption. Before actual adoption, replace navigation-only references with the stable control identity, v0.1.0, and an exact published commit URL, and pin all cross-control references as well. Do not fill a source commit with an invented SHA or a moving branch URL.

## Decisions proposed for review

| Decision | Proposed approach | Reason / tradeoff |
|---|---|---|
| Representation | Markdown definitions and explicit links first | Readable by people and agents; automated inference is deferred |
| Classification | Multiple work-type labels, one primary control family plus tags | Useful browsing without forcing a factory into one category |
| Record granularity | Embed small objects; split when independently reused or versioned | Avoid dozens of files for one small factory |
| Identity | Stable semantic concept paths after approval; families as metadata | Reclassification need not move a published control |
| Adoption | Separate reusable control, local implementation, and assessment | Preserves provenance and prevents overstated assurance |
| Applicability | Explain contextual triggers and justified exclusions | Work type or domain alone cannot determine required controls |

No RDF/OWL vocabulary, graph database, reasoner, numeric risk score, or fixed autonomy ladder is needed to review this MVP. Add machinery only when an identified use case requires it.
