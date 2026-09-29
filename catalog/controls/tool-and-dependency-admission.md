---
type: Control
title: "Tool and dependency admission"
description: "Admit reviewed tool and dependency revisions and reassess material changes before use."
status: stable
family: change-and-dependencies
sources:
  - id: AML.M0014
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6270
    title: "AML.M0014: Verify AI Artifacts"
  - id: AML.M0023
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6629
    title: "AML.M0023: AI Bill of Materials"
  - id: AML.T0110
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L4896
    title: "AML.T0110: AI Agent Tool Poisoning"
---

# Tool and dependency admission

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Reduce exposure to altered or unreviewed capabilities. Apply when installing, connecting, updating, or loading tools, models, packages, agent instructions, or other executable dependencies, including remotely hosted tools.

## Requirement

Admit a dependency only after an accountable reviewer records its identity, origin, revision or integrity evidence, requested permissions, review result, and approved scope. Verify the admitted identity at use. Material changes to code, tool definitions, permissions, or service behavior must be held for reassessment before continued use. When a remote implementation cannot be pinned or inspected, record that limitation and approve an explicit constrained access policy rather than asserting artifact verification.

## Implementation

1. Inventory direct and transitive dependencies and distinguish tool descriptions, executable implementations, and runtime responses.
2. Define review criteria and material-change triggers. Inspect provenance, integrity, permissions, and behavior in an isolated environment; assign approval outside the executing actor.
3. Bind admission to the tested revision and configuration. Gate installation/loading and invalidate admission on detected material changes.
4. For mutable remote services, define monitoring, access restrictions, and stop conditions for changes that cannot be verified before every invocation. Retain replacement and rollback references.

## Expected outcome and assessment

Expected outcome: only dependencies with current admission records operate within their approved scope.

Load an approved fixture; then attempt an unapproved package, altered digest, changed tool definition or permission request, and an actor-created approval. Exercise the declared remote-change stop condition where remote services are in scope.

**Pass:** the approved fixture works; altered or unapproved fixtures are withheld; remote limitations and stop behavior match the approved policy. **Fail:** an unreviewed change runs contrary to policy, approval is forged, or the approved fixture fails. **Inconclusive:** identity or a claimed change-detection mechanism cannot be checked.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

A valid signature establishes provenance, not benign behavior. Remote services can change without observable notice; this residual risk must remain explicit. [Execution isolation](execution-isolation.md) contains effects; [tool input and output validation](tool-input-output-validation.md) checks runtime boundaries.

Addresses [compromised tool behavior](../risks/compromised-tool-behavior.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0014[^AML.M0014], AML.M0023[^AML.M0023], AML.T0110[^AML.T0110]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0014]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.M0023]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0110]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
