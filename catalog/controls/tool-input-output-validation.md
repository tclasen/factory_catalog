---
type: Control
title: "Tool input and output validation"
description: "Validate tool arguments and returned data before execution, rendering, or downstream use."
status: stable
family: quality-and-validation
sources:
  - id: AML.M0033
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6879
    title: "AML.M0033: Input and Output Validation for AI Agent Components"
  - id: AML.T0110
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L4896
    title: "AML.T0110: AI Agent Tool Poisoning"
---

# Tool input and output validation

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Contain malformed or unsafe data at component boundaries. Apply where model-generated arguments reach a tool or tool results enter another component, renderer, or execution path.

## Requirement

Define and enforce input and output contracts outside the model before execution or consumption. Contracts must specify allowed structure, sizes, value ranges, destination/path constraints, and handling of active content appropriate to the consumer. Reject or quarantine unresolved violations. Treat returned instructions as data with no power to alter policy. Revalidate at each downstream boundary where interpretation changes.

## Implementation

1. Inventory producers, tools, consumers, renderers, and transformations. Assign a contract owner for every interface.
2. Version schemas and semantic checks; constrain paths/URLs and rendering behavior. Specify encoding and normalization before checking.
3. Place validation before side effects and before output rendering or forwarding. Restrict bypass interfaces and protect contract configuration.
4. Record rejection reasons safely and test each consumer separately; a valid JSON envelope does not establish safe content.

## Expected outcome and assessment

Expected outcome: invalid arguments cannot cause tool effects and invalid results cannot trigger unsafe downstream interpretation.

Test valid arguments/results, wrong types, oversized values, forbidden paths or URLs, and a result containing active markup or an instruction to change policy. Include a multi-component path where a valid upstream string would become executable downstream. Observe execution and rendering effects.

**Pass:** valid cases work and every violating fixture is stopped before its forbidden effect, with no bypass. **Fail:** a violating effect, policy change, or rejected valid case. **Inconclusive:** a consumer or side effect is unobservable.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Validation does not prove factual truth or detect every malicious natural-language instruction. [Bounded external action](bounded-external-action.md) enforces authority, [sensitive data egress](sensitive-data-egress.md) enforces disclosure policy, and [execution isolation](execution-isolation.md) limits effects beyond the interface.

Addresses [compromised tool behavior](../risks/compromised-tool-behavior.md) and [retrieved instruction action](../risks/retrieved-instruction-action.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0033[^AML.M0033], AML.T0110[^AML.T0110]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0033]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0110]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
