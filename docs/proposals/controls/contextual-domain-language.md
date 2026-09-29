---
type: Control
title: "Contextual domain language"
description: "Keep material terms and rules consistent within their declared domain context."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: knowledge-and-evidence
sources:
  - id: story-ddd
    resource: https://domainstorytelling.org/domain-driven-design
    title: "Domain-Driven Design with Domain Storytelling"
---

# Contextual domain language

[Adoption](../../../catalog/adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent people or agents from applying the wrong meaning to a familiar word. Apply when terminology affects decisions, handoffs, comparisons, or acceptance. DDD uses a shared language within each bounded context; the language can differ elsewhere.[^story-ddd] The following requirements are a catalog adaptation for human and AI work.

## Requirement

For each adopted scope, maintain a revisioned set of material terms, definitions, rules, examples, and exclusions with a named domain reviewer. Use those meanings in working artifacts and instructions. Identify unresolved ambiguity before it affects a dependent decision; preserve distinct contextual meanings instead of silently merging them.

## Implementation

1. Select the activity and domain reviewer. Use [collaborative discovery](../domain-discovery-workshops.md) to collect terms from real cases and disagreements.
2. Record each term's context, definition, source or reviewer rationale, example, counterexample, and effective revision. Include verbs and decision rules, not only nouns.
3. Compare forms, reports, prompts, rubrics, and code where present with the agreed meanings. Record and correct conflicting usage.
4. When a term crosses a [model boundary](domain-model-boundaries.md), attach its context and use an explicit [translation](context-translation-contracts.md).
5. On a meaning change, identify affected artifacts and reassess dependent decisions. Keep unresolved terms visible and route them to the reviewer.

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: every material use in the declared assessment sample resolves to its intended contextual meaning or an explicit unresolved issue before a dependent decision.

Declare the artifact sample, reviewer, revision, and material terms before assessment. Inspect one normal case, one ambiguous same-word case, and one changed-definition case. For example, teaching staff may use “complete” for submitted coursework while an assessor uses it for meeting a rubric.

- **Pass:** the normal case uses the agreed meaning; the ambiguity is disambiguated or held for review; the revision change identifies and reassesses affected uses. No sampled material conflict remains hidden.
- **Fail:** a conflicting or obsolete meaning silently supports a decision, or any required record is absent.
- **Inconclusive:** artifacts or knowledgeable reviewers are unavailable to determine semantic agreement.
- **Evidence:** scoped vocabulary revision, sampled artifacts, reviewer observations, disagreements, corrections, and resulting dispositions.

## Dependencies and limitations

Requires access to domain practitioners and [evidence traceability](../../../catalog/controls/evidence-traceability.md). A glossary alone does not demonstrate consistent use or factual truth. Agreement among agents is insufficient evidence of practitioner agreement. Preserve exact adoption references using the linked adoption procedure. No operational effectiveness is asserted.

[^story-ddd]: [Domain-Driven Design with Domain Storytelling](https://domainstorytelling.org/domain-driven-design).
