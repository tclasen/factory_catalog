---
type: Control
title: "Sensitive data egress"
description: "Enforce permitted data and destination combinations before information leaves a protected scope."
status: stable
family: information-protection
sources:
  - id: AML.T0086
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L4208
    title: "AML.T0086: Exfiltration via AI Agent Tool Invocation"
  - id: AML.M0033
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6879
    title: "AML.M0033: Input and Output Validation for AI Agent Components"
---

# Sensitive data egress

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Prevent disclosure through otherwise usable tools. Apply when a workflow handles restricted data and can send information outside its authorized audience, including through queries, rendered links, logs, or connector arguments. Exclusion requires evidence that no such data or egress path exists.

## Requirement

Before information crosses the declared protection boundary, enforce a policy for data class, recipient, destination, purpose, and channel. Unknown classifications or destinations must be withheld or routed to an authorized reviewer before release. Tool permission alone must not authorize a payload. Protect policy administration from the executing actor and cover indirect network effects and alternate routes.

## Implementation

1. Inventory outgoing channels and the last enforceable point before transmission, including redirects, browser rendering, telemetry, and delegated tools.
2. Assign a data owner to approve the data/destination policy and exception scope. Define handling of derived, encoded, and combined data; document inspection limits.
3. Enforce the policy outside the model using restricted credentials, gateways, recipient checks, and data inspection or containment. Where reliable inspection is unavailable, restrict the route or require bounded review.
4. Check the actual recipient and payload at transmission. Record policy decisions without duplicating secrets; expire exceptions and reassess after connector changes.

## Expected outcome and assessment

Expected outcome: restricted test information reaches only permitted recipients through permitted channels.

For each route, attempt a prohibited transfer using a synthetic private marker, including a tool argument, query string, generated link, redirect, and declared encoding variants where supported. Also test a permitted transfer, unknown destination/classification, and an attempt to change policy. Observe destination receipts and network effects, not just response text.

**Pass:** prohibited and unresolved transfers produce no disclosure, allowed transfers succeed, and policy cannot be bypassed. **Fail:** any forbidden receipt, bypass, or failed positive case. **Inconclusive:** a route or recipient effect cannot be observed.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires a data inventory and enforceable egress boundary. Content inspection cannot prove detection of every encoding or inference. [Bounded external action](bounded-external-action.md) governs authority; this control adds payload restrictions. [Execution isolation](execution-isolation.md) can close uninspectable routes.

Addresses [disclosure through authorized tool use](../risks/authorized-tool-data-disclosure.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.T0086[^AML.T0086], AML.M0033[^AML.M0033]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.T0086]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
[^AML.M0033]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
