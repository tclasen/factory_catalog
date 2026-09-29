---
type: Control
title: "Architecture decision traceability"
description: "Retain the link from material design choices to objectives, constraints, alternatives, and accountable decisions."
catalog_version: "v0.1.0"
status: draft
family: purpose-and-accountability
sources:
  - id: c220
    resource: https://publications.opengroup.org/c220
    title: "The TOGAF® Standard, 10th Edition"
---

# Architecture decision traceability

**Identity:** `controls/architecture-decision-traceability` · **Catalog:** v0.1.0 · **Family:** `purpose-and-accountability`

[Adoption](../adoption.md) · [Research map](../open-group-standards-opportunities.md)

## Purpose and applicability

Prevent a material organizational or system design choice from losing its rationale as work moves between planning and execution. Apply to choices affecting objectives, interfaces, responsibilities, operating constraints, or investment. Set materiality before review. TOGAF's architecture content and governance scope motivates this catalog adaptation; the requirement below is locally authored.[^c220]

## Requirement

Before accepting a material design decision, record its owner, scope, affected outcome, requirements/constraints and their revisions, alternatives considered, rationale, assumptions, and downstream artifacts. A designated reviewer must confirm that the decision is consistent with the stated constraints and that unresolved conflicts have an authorized disposition. Changes that invalidate the rationale must trigger renewed review before continued reliance on that decision.

## Implementation

1. Define the decision boundary and materiality criteria with the accountable owner. Separate a recommendation from a decision the owner is authorized to make.
2. Give each decision a local identifier and revision; link the exact input requirements, source evidence, rejected options, and affected activities/artifacts.
3. Record conflicts and exceptions with their approving authority, scope, and review condition. A decision record cannot grant itself an exception.
4. At acceptance, have the reviewer inspect the complete set of material choices for omissions and contradictory constraints.
5. Assign a change owner to assess whether revised objectives, requirements, assumptions, or artifacts invalidate any accepted decisions. Preserve the superseded rationale in the local evidence system and record the new disposition.

Mechanism: review procedure supported by a decision register and change notifications. Missing notifications and unrecorded decisions are bypass paths. [Enterprise capability planning](../guides/enterprise-capability-planning.md) supplies a record template; [evidence traceability](evidence-traceability.md) supports the factual rationale.

## Expected outcome and assessment

Expected outcome: every material choice in a declared planning/delivery revision is traceable to its basis and accountable disposition; invalidated choices are reopened before use.

Inspect all material decisions in that scope and the source requirements. In separate fixtures, omit a material decision, introduce a conflicting requirement without a disposition, and change an assumption so an accepted rationale is invalid. Include a consistent decision as a positive case.

- **Pass:** all scoped decisions meet the requirement; all three negative cases block acceptance or continued reliance pending review; the consistent case is accepted through the defined process.
- **Fail:** a material choice lacks the required trace, an unresolved conflict is accepted, or an invalidated rationale remains in use.
- **Inconclusive:** decision coverage, source revisions, or the review's effect on acceptance cannot be inspected.
- **Evidence:** declared scope/materiality, decision and input revisions, reviewer/authority records, changed assumption, fixture results, acceptance/reopening dispositions.

## Dependencies and limitations

Requires an owner able to identify material choices and a process that acts on review findings. Traceability does not prove that a design is optimal, affordable, lawful, or effective. Assess resulting benefits using [outcome verification](outcome-verification.md). This draft control has not been operationally assessed and does not establish TOGAF conformance.

[^c220]: The Open Group, The TOGAF® Standard, 10th Edition; public publication description and metadata inspected 2026-09-28. Full licensed text was not reviewed.
