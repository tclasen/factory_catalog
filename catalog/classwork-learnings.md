---
type: Guide
title: "Apply classwork learnings"
description: "Apply source intake, graph reconciliation, learning assessment, and action evidence to existing catalog controls."
catalog_version: "v0.1.0"
status: draft
sources:
  - id: intake
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-source-intake/SKILL.md
    title: "classwork: Source intake procedure"
  - id: synthesis
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-knowledge-synthesis/SKILL.md
    title: "classwork: Knowledge synthesis procedure"
  - id: policy
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/AGENTS.md
    title: "classwork: Graph and learner workspace policy"
  - id: competency
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/education/competency-and-prerequisite-structure.md
    title: "classwork: Competency and prerequisite structure"
  - id: transfer
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/foundations/learning-assessment-and-transfer.md
    title: "classwork: Learning, assessment, and transfer"
  - id: provenance
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/information-systems/information-provenance-and-trust.md
    title: "classwork: Information provenance and trust"
  - id: assurance
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/assurance/assurance-case.md
    title: "classwork: Assurance case"
  - id: loop
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/artificial-intelligence/agent-control-loops-and-tool-use.md
    title: "classwork: Agent control loops and tool use"
---

# Apply classwork learnings

[Catalog](index.md) · [Adoption](adoption.md) · [Ontology](ontology.md)

## Scope and interpretation

This guide extracts reusable practices from `tclasen/classwork` at commit `12d29b3ae730c565135604f027b502b87b225758`. It uses the catalog's existing Guide type, controls, and relationships. The source repository's workflow instructions are evidence about its design; they do not govern this catalog. Its ontology classifications and teaching domain are not adopted here.

The source documents prescribe practices and explain concepts. They do not establish that those practices improved learning, prevented incidents, or passed this catalog's control assessments. The applications and review fixtures below are proposed catalog adaptations. No operational assessment or document verification event is asserted, and the underlying publications cited by classwork were not independently reviewed for this extraction.

## 1. Resolve the source before integrating its claims

Classwork's intake procedure checks the exact edition, source identity, suitability, and storage rights before integration. Its synthesis procedure searches existing concepts and determines whether new information confirms, qualifies, contradicts, or supersedes them.[^intake][^synthesis]

**Application:** use [evidence traceability](controls/evidence-traceability.md) to keep a compact intake record: source revision, claim, supporting location, existing concept, proposed change, and unresolved conflict. Link a source when storing a copy is unnecessary. If retaining an artifact, check redistribution rights and integrity first. A citation to a secondary summary supports what that summary says; it does not establish independent verification of its primary sources.

**Review fixture:** supply two editions with a changed material claim and one conflicting source. Check that the draft identifies the edition actually used, preserves the conflict, and qualifies the conclusion. Withhold acceptance if it silently combines editions or hides contrary evidence. The [research example](factories/research.md#source-intake-extension) applies this to a comparison memo.

## 2. Reconcile canonical concepts and explain relationships

Classwork searches before creating a concept, retains one canonical treatment per distinct topic, and explains substantive relationships through contextual links. It calls for relevant backlinks and synchronized indexes. Its graph can support different learning routes; learner-specific plans remain outside the shared bundle.[^synthesis][^policy]

**Application:** before extending this graph, search titles, bodies, and incoming links. Update the existing concept when the meaning matches; create a new one only when it needs a distinct identity. Explain whether a link supplies a prerequisite, evidence, example, or limitation, using the [ontology's relationship conventions](ontology.md#relationships-in-use). Keep individual learner observations outside reusable knowledge and apply access restrictions to them.

**Review fixture:** propose an addition under a synonym for an existing topic. Pass the reconciliation check only if the change reuses the canonical concept or explains a meaningful distinction, preserves valid incoming links, and updates the index. Separately review whether each relationship makes sense: a resolving link alone cannot establish that. Keep the catalog's existing schema and control identities; any new classifications require a design decision.

## 3. Assess capability under stated conditions

Classwork defines competency in terms of observable performance, conditions, and evidence. It recommends diagnosing prerequisites and distinguishes an undemonstrated skill from evidence that a learner lacks it. Transfer means applying learning in a different, related context.[^competency][^transfer]

**Application:** implement [outcome verification](controls/outcome-verification.md) with an entry task, a stated rubric, an unseen follow-up task, and a record of assistance given. Use prerequisite gaps to choose practice. Keep a lesson's completion separate from what the learner demonstrates. The [learning example](factories/learning.md#prerequisites-and-transfer-extension) adds a proposed application without changing its existing outcome threshold.

**Review fixture:** compare a learner who repeats a worked example with one who explains the decision in a new scenario. Inspect whether the rubric and report distinguish recall, assisted performance, and independent application. Missing follow-up evidence leaves the outcome unverified. These checks assess reporting discipline; a particular lesson's effectiveness still needs observations.

## 4. Connect provenance to an explicit argument

Classwork treats provenance as a record of origin and transformation. Its assurance case explains why particular evidence supports a bounded claim, including assumptions and rebuttals.[^provenance][^assurance]

**Application:** in the [adoption assessment record](adoption.md#implement-and-assess), retain the input and output revisions, responsible actor, relevant transformation, observation time, and inference from evidence to conclusion. Review whether the evidence covers the actual system and operating context. Use [evidence traceability](controls/evidence-traceability.md) for support and [outcome verification](controls/outcome-verification.md) for the success claim.

**Review fixture:** present authentic evidence from an earlier system revision alongside a claim about a changed system. Withhold that claim unless the reviewer explains why the evidence still applies or obtains new evidence. Preserve unresolved gaps and the reassessment decision. Complete lineage alone does not establish truth or a valid inference.

## 5. Verify agent actions and bound recovery

Classwork's agent loop separates a proposed action, authorization, execution, observation, verification, and recovery. It describes timeouts, bounded retries, and handling ambiguous results.[^loop]

**Application:** compose [bounded external action](controls/bounded-external-action.md) with [outcome verification](controls/outcome-verification.md). Record the grant used, target, attempted operation, observed effect, and completion criterion. Set attempt and time limits locally. Before retrying a side effect after a timeout, determine whether it already occurred; use duplicate prevention or escalate when the result is ambiguous.

**Review fixture:** in a safe test environment, simulate a timeout after an action has taken effect. Check that recovery verifies the effect or stops within its declared limit, and that it does not create a duplicate effect. Retain the action trace and disposition. This is a proposed recovery check, not a claim that the current controls completely cover retry safety.

## Decisions still open

This addition preserves the current families, control requirements, schema, and v0.1.0 baseline hold. Graph reconciliation, learner-data handling, and bounded recovery may justify dedicated controls later. Decide that after reviewing concrete implementations, their failure cases, and overlap with existing controls. Each adopter still needs a pinned catalog revision and local assessment evidence.

[^intake]: [Source intake procedure](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-source-intake/SKILL.md), pinned classwork revision.
[^synthesis]: [Knowledge synthesis procedure](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-knowledge-synthesis/SKILL.md), pinned classwork revision.
[^policy]: [Graph and learner workspace policy](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/AGENTS.md), pinned classwork revision.
[^competency]: [Competency and prerequisite structure](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/education/competency-and-prerequisite-structure.md), pinned classwork revision.
[^transfer]: [Learning, assessment, and transfer](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/foundations/learning-assessment-and-transfer.md), pinned classwork revision.
[^provenance]: [Information provenance and trust](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/information-systems/information-provenance-and-trust.md), pinned classwork revision.
[^assurance]: [Assurance case](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/assurance/assurance-case.md), pinned classwork revision.
[^loop]: [Agent control loops and tool use](https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/artificial-intelligence/agent-control-loops-and-tool-use.md), pinned classwork revision.
