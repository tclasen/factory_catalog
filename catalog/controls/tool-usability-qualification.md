---
type: Control
title: "Tool usability qualification"
description: "Qualify whether intended callers select tools, identify objects, and interpret results correctly."
status: draft
family: quality-and-validation
sources:
  - id: ap-tools
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/semantic-tool-output.md
    title: "Agent Patterns: Semantic tool output"
  - id: ap-descriptions
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/tool-description-quality.md
    title: "Agent Patterns: Tool description quality"
---

# Tool usability qualification

[Adoption](../adoption.md)

## Purpose and applicability

Apply before allowing an agent or human operator to rely on a new or changed tool interface. A schema-valid request can still select the wrong object or misunderstand a partial response.

## Requirement

Qualify the interface with representative intended callers and tasks on a pinned tool, caller, instructions, and environment configuration. Predeclare task outcomes, repetitions, acceptable selection/repair errors, and mandatory identity and authority invariants. Test selection, arguments, result interpretation, continuation, and recovery. Withhold qualification when a required criterion fails or evidence is unavailable; requalify affected behavior after changes.

## Implementation

1. Name the interface owner and intended caller population; include the agent model/harness where applicable.
2. Provide purpose, preconditions, stable object IDs with readable labels, completeness/continuation signals, and actionable errors. Error messages cannot confer permission.
3. Use realistic ambiguous choices and safe destinations; accept equivalent valid strategies rather than one exact sequence.
4. Inspect destination state and output meaning. Record errors, repairs, latency, and outcome evidence across all declared trials.

## Expected outcome and assessment

Expected outcome: qualified callers complete permitted tasks without silent identity substitution or false completeness claims.

Include similarly named tools, same-name objects with different IDs, paginated and empty results, a recoverable invalid parameter, and a denied action. Include an ordinary successful task. Test whether qualification rejects an interface whose caller silently changes the wrong object or treats one page as the complete result.

- **Pass:** all declared task thresholds are met; mandatory identity/authority invariants hold; partial/empty/denied results are distinguished; known defective interfaces are withheld.
- **Fail:** a silent wrong-object action, authority expansion, false complete result, or another unmet mandatory criterion is accepted for use.
- **Inconclusive:** destination effects, representative callers, or sufficient planned trials are unavailable.
- **Evidence:** configuration identities, task set, criteria, every trial and repair, observed effects, qualification decision, owner, and time.

## Dependencies and limitations

Use [tool input/output validation](tool-input-output-validation.md) for contracts and [dependency admission](tool-and-dependency-admission.md) for trusted artifacts. This control tests usability for the declared callers; it does not replace enforced permissions or prove general reliability from a small task set.

Adapted from Agent Patterns' tool guidance, CC BY 4.0.[^ap-tools][^ap-descriptions] Proposed assessment, not an executed qualification.

[^ap-tools]: Agent Patterns, pinned semantic tool output guidance; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^ap-descriptions]: Agent Patterns, pinned tool description quality guidance.
