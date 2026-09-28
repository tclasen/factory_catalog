# Knowledge-work factory ontology: review MVP

**Proposal • catalog v0.1.0 • no baseline approval implied**

A knowledge-work factory is a repeatable system in which people, software, and optionally AI turn inputs into useful artifacts, decisions, or actions, with explicit ways to judge and improve the results.

This MVP describes those systems through a small ontology: named concepts and explicit relationships. Taxonomies provide browsing views of work types and control families. The purpose is to help a person or agent explain **what a factory does, why it exists, how it operates, which controls apply, and what evidence supports its operation**.

## Review in this order

1. [Model and proposed design decisions](model.md): concepts, relationships, identity, and evidence semantics.
2. [Vocabulary](vocabulary.md): 16 work types and 11 candidate control families.
3. [Public research example](examples/research.md): evidence quality and untrusted sources.
4. [Learning example](examples/learning.md): artifacts versus human outcomes.
5. [Contract operations example](examples/contracts.md): activity-specific authority and commitments.
6. [Review worksheet](review.md): questions the model must answer and unresolved choices.

## Three proposed controls

| Control | Why it is in the MVP |
|---|---|
| [Evidence traceability](controls/evidence-traceability.md) | Makes the relationship between claims and supporting material inspectable |
| [Bounded external action](controls/bounded-external-action.md) | Separates independent preparation from permission to affect other parties |
| [Outcome verification](controls/outcome-verification.md) | Separates producing an artifact from achieving the intended result |

Each control has an applicability condition, requirement, implementation procedure, assessment, pass/fail criteria, and limitations. These are proposed procedures; none has been implemented or shown effective here.

## Scope and status

This is a documentation prototype, with linked examples and one structured relationship example. The examples are fictional design cases. Their measures and thresholds illustrate how to make a requirement assessable; they are not universal recommendations.

The MVP records the direction discussed with the owner: a lightweight ontology with taxonomic views; work type separate from domain; autonomy separate from authority; artifacts separate from outcomes; reusable controls separate from local implementations and evidence. The owner requested a reviewable MVP, not approval of its vocabulary or schema.

The files live under `docs/` because the domain schema and control identities remain proposals. They do not initialize the OKF bundle or establish adopted controls. Following design review, agreed concepts can be authored in `catalog/` against the pinned OKF specification. Catalog version remains v0.1.0. No release or tag changes are proposed.

The eventual model should support both URL and copied-content adoption. An actual adoption must record the control's stable identity, catalog version, exact source commit URL, local adaptations, and assessment evidence. Proposal links here are navigation links, not adoption records.

## What success looks like for this review

A reviewer can describe a new factory, identify a relevant risk or desired outcome, select a candidate control with a reason, and distinguish a proposed implementation from a tested one. The examples exercise these questions conceptually; they do not demonstrate operational effectiveness.
