---
type: Control
title: "Security event traceability"
description: "Preserve protected event records that connect security decisions to observed effects."
catalog_version: "v0.1.0"
status: stable
family: monitoring-and-improvement
sources:
  - id: AML.M0024
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6651
    title: "AML.M0024: AI Telemetry Logging"
---

# Security event traceability

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

**Identity:** `controls/security-event-traceability` · **Catalog:** v0.1.0 · **Family:** `monitoring-and-improvement`

## Purpose and applicability

Make security incidents and control decisions reconstructable. Apply to workflows where investigating data access, persistent changes, tool activity, or external effects is necessary. Scope logging to observable events; do not require private model reasoning.

## Requirement

Retain protected, time-ordered or causally linked records identifying the actor, job, relevant input/state revision, policy or grant decision, attempted operation, and observed result for declared security-relevant events. Detect missing or altered records and define behavior when logging is unavailable. Enforce access and retention rules and avoid storing unnecessary secrets or sensitive payloads.

## Implementation

1. Choose events and correlation identifiers across agents, tools, gateways, memory, and data stores; record expected coverage and timestamp uncertainty.
2. Send records to storage that executing actors cannot silently alter. Record evidence references or redacted metadata in place of raw sensitive content.
3. Define access, retention/deletion, integrity checks, and the stop or degraded-operation policy for logging failure.
4. Assign an investigator and rehearse reconstruction, including denied attempts and asynchronous child work.

## Expected outcome and assessment

Expected outcome: an authorized reviewer can connect a seeded event sequence to decisions and effects, or explicitly detect incomplete evidence.

Run a permitted action, denied action, memory update, and delegated action where applicable. Ask a reviewer to reconstruct their causal sequence. Remove or alter a test record, interrupt logging, attempt unauthorized log access, and include a synthetic secret in an input.

**Pass:** normal sequences are reconstructable; gaps/tampering are detected; outage behavior follows policy; unauthorized access and secret retention are prevented. **Fail:** misleading completeness, undetected required-event loss, exposed protected records, or violation of outage policy. **Inconclusive:** coverage or integrity cannot be independently checked.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires protected storage, correlation across services, and access to effect observations. Logs do not prevent attacks and can be incomplete despite valid signatures. [Sensitive data egress](sensitive-data-egress.md) includes log destinations. [Adversarial regression assessment](adversarial-regression-assessment.md) can use these records as evidence.

Addresses [authorized tool disclosure](../risks/authorized-tool-data-disclosure.md) and [compromised tool behavior](../risks/compromised-tool-behavior.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0024[^AML.M0024]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0024]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
