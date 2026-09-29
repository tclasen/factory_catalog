---
type: Guide
title: "Collaborative domain discovery"
description: "Elicit and challenge domain models using concrete stories, events, and practitioner review."
status: draft
tags: [domain-driven-design, knowledge, coordination]
sources:
  - id: storming
    resource: https://www.eventstorming.com/
    title: "EventStorming, official method website"
  - id: stories
    resource: https://domainstorytelling.org/quick-start-guide
    title: "Domain Storytelling Quick-Start Guide"
---

# Collaborative domain discovery

[Domain model selection](guides/domain-model-selection.md) · [Context records](domain-context-records.md)

## Purpose and source limits

Use this procedure when implicit domain knowledge, contested terminology, or hidden handoffs prevent reliable work definition. EventStorming supports exploration across business roles; Domain Storytelling uses concrete stories and retelling to expose misunderstandings.[^storming][^stories] The facilitation and assessment procedure below is a proposed catalog adaptation. It can support education, research, editorial work, service operations, and software design.

## Prepare

1. State one decision the model must support, the outcome, and the boundary of the session. Identify a facilitator, people doing the work, a domain reviewer, and downstream users. Record missing perspectives.
2. Select an ordinary case and at least one exception or disputed case from permitted evidence. Use redacted or fictional cases when actual records cannot be shared; disclose that limitation.
3. Choose a story walkthrough for detailed actor/work understanding or an event-oriented map for chronology and interactions. A mixed session may use both, but label the representation and its assumptions.
4. Label the model as current practice or proposed operation. Set a time limit and retain an unresolved-question list so consensus pressure does not erase disagreement.

## Facilitate and record

Have the practitioner describe a concrete case, then draw or write who acts, what they use, what they produce, and who receives it. Read the account back. Ask the practitioner to correct it before abstracting a general rule. Domain Storytelling explicitly favors concrete scenarios and distinguishes current from future scope.[^stories]

For an event-oriented view, distinguish a request, a decision, and an evidenced occurrence. Ask what happens before and after each occurrence, who knows it happened, and what evidence they retain. Mark missing steps, disputed causal claims, and incompatible meanings. Do not require a broker, event store, or software implementation to use the exercise.

Build the following small record:

| Record | Minimum content | Feeds |
|---|---|---|
| Case | Purpose, scope, participants, source, ordinary or exceptional, current or proposed | [Evidence traceability](controls/evidence-traceability.md) |
| Story step | Actor, action, input, output, recipient, sequence, rule, uncertainty | Activity and Artifact in the [ontology](ontology.md#concepts) |
| Disagreement | Competing interpretations, example, affected decision, reviewer, next action | [Contextual domain language](controls/contextual-domain-language.md) |
| Boundary hypothesis | Where a meaning or rule changes, counterexample, owner, interface | [Domain model boundaries](controls/domain-model-boundaries.md) |
| Occurrence | What happened, evidence, subject identity, relevant times | [Domain event meaning](controls/domain-event-meaning.md) |

## Challenge the model

Walk a second ordinary case and the selected exception through the model. Ask where the model makes the wrong prediction or cannot explain the evidence. Revise it or mark the limitation; do not relabel an exception merely to preserve the diagram.

Use these proposed prompts:

- Two roles use the same word: do they make the same decision from it?
- Two records share attributes: must they remain distinct identities?
- Two changes look valid separately: can their combination violate a rule?
- A report arrives late: what actually happened and what was known earlier?
- An outside status changes meaning: who notices before the next handoff?

Connect the resulting vocabulary, boundaries, and mappings to [context records](domain-context-records.md). Apply the selected controls with their own adoption references; workshop attendance is not adoption.

## Exit criteria and assessment evidence

The session produces a reviewable model, identified uncertainties, and named next actions. Before treating it as usable for the chosen decision, a domain reviewer must confirm that both ordinary and exceptional cases can be explained or are explicitly outside scope. Record source references, model revision, corrections, reviewer identity, date, and unresolved questions.

**Ready for a scoped pilot:** required perspectives are represented or their absence is explicitly accepted by the accountable owner; no unresolved issue affecting the chosen decision is hidden; the ordinary and exception walkthroughs have retained results. **Needs further discovery:** a material disagreement or missing perspective prevents interpreting the case. These are workshop dispositions, not replacements for the catalog's control assessment states.

A facilitator or AI can draft and challenge a model but cannot manufacture expert confirmation. A successful walkthrough establishes only that the model explains those cases. Operational benefit still needs [outcome verification](controls/outcome-verification.md).

[^storming]: [EventStorming, official method website](https://www.eventstorming.com/).
[^stories]: [Domain Storytelling Quick-Start Guide](https://domainstorytelling.org/quick-start-guide).
