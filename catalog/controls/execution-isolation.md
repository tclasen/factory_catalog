---
type: Control
title: "Execution isolation"
description: "Restrict workload access to files, networks, credentials, and other execution contexts."
catalog_version: "v0.1.0"
status: stable
family: authority-and-access
sources:
  - id: AML.M0032
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6853
    title: "AML.M0032: Segmentation of AI Agent Components"
---

# Execution isolation

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

**Identity:** `controls/execution-isolation` · **Catalog:** v0.1.0 · **Family:** `authority-and-access`

## Purpose and applicability

Contain code, tools, and processes that may act unexpectedly. Apply to execution environments with access to host resources, networks, credentials, or shared infrastructure. Define the workload boundary explicitly, including containers, subprocesses, and delegated actors.

## Requirement

Enforce an explicit resource allowlist for each workload outside its control. Deny access to other workloads' data and credentials, unapproved host resources, and forbidden network destinations. The workload must not modify its own isolation policy. Start from a declared clean environment and mediate any approved state import; release or revoke workload resources at termination.

## Implementation

1. Inventory filesystem mounts, network routes, identity sources, host interfaces, subprocesses, and shared services.
2. Assign least-privilege identities and an isolation policy for each workload. Avoid shared administrative credentials; separate state by user/tenant.
3. Configure sandbox, operating-system, or service boundaries and restrict access to their administration. Declare the retained state and cleanup mechanism.
4. Observe actual access decisions, test indirect routes and child processes, and verify cleanup before reusing an environment.

## Expected outcome and assessment

Expected outcome: the workload can perform permitted work while forbidden resources remain inaccessible.

Place synthetic markers in another workload, a forbidden host location, and an unapproved credential store. Test reads/writes, forbidden network access, child-process attempts, and isolation-policy modification. Run an allowed task and then start a new workload to check for unauthorized state or credential carryover.

**Pass:** all forbidden accesses are denied, legitimate work succeeds, policy remains protected, and cleanup prevents forbidden carryover. **Fail:** any escape, cross-scope access, policy bypass, residual exposure, or failed positive case. **Inconclusive:** a boundary or termination effect cannot be observed.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Requires trustworthy isolation infrastructure and a complete resource inventory. A container name or a prompt instruction is not evidence of isolation. This does not establish resistance to every platform vulnerability. Combine with [bounded external action](bounded-external-action.md) for grants and [sensitive data egress](sensitive-data-egress.md) for permitted-channel payloads.

Addresses [compromised tool execution](../risks/compromised-tool-behavior.md) and [injected action requests](../risks/retrieved-instruction-action.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0032[^AML.M0032]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0032]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
