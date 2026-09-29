---
type: Control
title: "Required guidance selection"
description: "Select applicable instructions before dependent actions and keep unresolved requirements visible."
status: stable
family: knowledge-and-evidence
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/progressive-disclosure.md
    title: "Software Factory: Required guidance selection basis"
---

# Required guidance selection

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when agents or people select instructions through indexes, task routes, retrieval, or summaries. Prevent a short context or apparently optional profile from hiding a requirement that the next action actually triggers.

## Requirement

Select guidance using the next action, relevant changed inputs, and actual consequences. Retrieve the applicable definitions, conditions, and exceptions before dependent work. Preserve binding host rules and unfinished authority, effect, recovery, and verification obligations through transitions. If required guidance is unavailable, search its canonical source and block dependent actions until resolved; continue independent authorized work. Record completed procedures by evidence reference and reopen them when relevant inputs change.

## Implementation

1. Give each route an explicit trigger and each procedure an exit condition. Keep universal requirements accessible at entry.
2. Identify the next action and triggered procedures; follow only links needed to interpret or fulfill them. A link alone does not make every downstream document mandatory.
3. Recover relevant omitted text after truncation and resolve missing references from the maintained package. Do not replace a missing required rule with memory.
4. Carry open obligations and evidence pointers in the work record. Release completed procedural detail from summaries while retaining its result and reopening conditions.
5. On routing changes, assess both omitted requirements and irrelevant retrieval using declared task cases; keep performance claims separate from discoverability checks.

## Expected outcome and assessment

Expected outcome: all applicable requirements govern the next action, while completed and unrelated procedures need not be repeatedly loaded.

Define expected requirements independently for a routine correction, a consequential migration, an ambiguous multi-policy task, a missing reference, a truncated read, and a transition with an unfinished observation duty. Inspect selected content and actual action order; include an unrelated profile to test selective reading.

- **Pass:** required guidance is available before dependent actions; unresolved requirements block those actions; independent work can continue; open obligations survive transitions; unrelated guidance is not treated as mandatory without a trigger.
- **Fail:** a required rule is omitted or invented, a dependent mutation proceeds through a missing-rule block, or a pending obligation disappears from the handoff. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** selected content or action order cannot be established from available traces.
- **Evidence:** package/route identities, task cases, expected requirement map, observed reads and actions, omissions, blocks, and transition records.

## Dependencies and limitations

Requires maintained canonical instructions and task-aware interpretation. Link checking establishes reachability, not correct selection. Self-reported reads alone provide limited evidence; expose that limit. [Durable work handoff](durable-work-handoff.md) preserves obligations and [assessment evidence validity](assessment-evidence-validity.md) governs reopening results. This control does not claim to evict text from a model context window or reduce cost.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/progressive-disclosure.md).
