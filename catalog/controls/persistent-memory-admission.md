---
type: Control
title: "Persistent memory admission"
description: "Authorize durable memory changes and preserve their origin before later sessions can use them."
catalog_version: "v0.1.0"
status: stable
family: knowledge-and-evidence
sources:
  - id: AML.M0031
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6794
    title: "AML.M0031: Memory Hardening"
  - id: AML.T0080.000
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L3932
    title: "AML.T0080.000: Memory"
---

# Persistent memory admission

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

**Identity:** `controls/persistent-memory-admission` · **Catalog:** v0.1.0 · **Family:** `knowledge-and-evidence`

## Purpose and applicability

Prevent untrusted content from silently changing future work. Apply to saved preferences, summaries, chat histories, experience stores, and other agent state reused across sessions. A workflow with no durable state may exclude it after inventory.

## Requirement

Every durable creation, update, or deletion must have an authorized actor and user/tenant scope, an identifiable origin, a retained revision history under defined retention rules, and an admission decision before the state is used. Retrieved content cannot authorize its own persistence. Hold unresolved writes outside active memory; enforce scope and policy outside the model.

## Implementation

1. Inventory explicit memory APIs and implicit persistence such as automatic summarization and checkpointing.
2. Assign the memory owner and define admissible content, authorized writers, user/tenant boundaries, retention, and the handling of conflicting updates.
3. Mediate all writes, including delegated and background writes. Record source revision, writer, scope, time, decision, and prior/new revision references.
4. Keep pending entries unavailable to retrieval. Provide authorized correction/deletion and a way to identify derived state for recovery.

## Expected outcome and assessment

Expected outcome: later sessions consume only memory admitted within their scope, with inspectable provenance.

Test a legitimate user preference, an indirect instruction to save a preference, a cross-tenant write, an unauthorized deletion, and an automatic-summary route. Inspect stored revisions and begin a fresh session after each test. Check that pending entries remain unavailable and an authorized correction takes effect.

**Pass:** authorized changes work with complete provenance; unauthorized or unresolved changes never enter usable state or affect the fresh session. **Fail:** unauthorized persistence, missing required provenance, or rejected authorized changes. **Inconclusive:** stored state or a persistence route cannot be inspected.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Admission does not establish that accepted content is true. Use [evidence traceability](evidence-traceability.md) for factual support and [persistent state recovery](persistent-state-recovery.md) for contamination already admitted. Recovery is separately selectable; an admission pass does not imply recoverability.

Addresses [poisoned memory influencing later work](../risks/poisoned-persistent-memory.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0031[^AML.M0031], AML.T0080.000[^AML.T0080.000]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0031]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.T0080.000]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
