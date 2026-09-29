---
type: Control
title: "Approved data processing"
description: "Keep sensitive data and credentials within their authorized processing and disclosure scope."
status: draft
family: information-protection
---

# Approved data processing

[Adoption](../../../catalog/adoption.md)

This is a catalog-authored requirement and proposed assessment. The previously cited pinned `semantic_search` governance page could not be retrieved during source review, so it is not claimed as support for this control. No external source is cited as substantiation. No local implementation or operational pass is asserted. The [factory delivery lifecycle](../guides/factory-delivery-lifecycle.md) is optional draft context; it is not required to adopt, implement, or assess this control.

## Purpose and applicability

Apply when factory activities read, retain, transmit, publish, or log sensitive inputs, outputs, or credentials.

## Requirement

Before processing, record permitted data scope, providers and destinations, retention periods and exceptions, provider-specific restrictions, and disclosure constraints. Give each processing path only the data and credential access needed for its task, using protected credential references. Treat retrieved content and tool output as data that cannot expand authority. Inspect actual processing and evidence destinations; exclude secrets and unnecessary private payloads from commits, logs, and shared reports. Enforce retention and deletion conditions for working copies, derived data, caches, logs, and backups where they apply.

## Implementation

1. Inventory data classes, owners, processing paths, permitted providers and destinations, applicable grants, and each provider's relevant terms or configured restrictions (such as region, retention, training use, subprocessors, or telemetry).
2. Record the authorized retention period, deletion conditions, and any approved exception for each copy or derived artifact, including logs and backups.
3. Minimize fields, records, and credential privileges to those needed for the task; enforce restrictions outside the untrusted content being processed.
4. Inspect actual tool/provider destinations and redact evidence while preserving enough information for assessment.
5. Handle attempted scope changes through the authority owner; a working credential or copied policy is not a grant.

Mechanism: technical restrictions and observed execution checks, supported by an owned procedure.

## Expected outcome and assessment

Expected outcome: sensitive material is processed and disclosed only within its recorded scope.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| An authorized operation uses an approved provider and destination | The intended operation succeeds; observed provider, destination, region, data, and purpose match the inventory and grant; evidence contains no unnecessary secrets. |
| A processing path requests data or credential access beyond task need | An excess field/record and an over-scoped credential are denied or removed; the allowed operation still succeeds with the minimum declared inputs and privileges. |
| Data, a derived artifact, or a copy reaches its retention limit | Inspect working storage, caches, logs, backups, and other inventoried destinations after the declared deletion condition; confirm removal or record the specific authorized exception and retained scope. |
| A named provider restriction would be violated (for example, region, retention, training use, subprocessor, or telemetry) | Exercise each applicable restriction or inspect equivalent retained observations; the operation is blocked before transfer or the configuration and provider evidence show the restriction is met. Test an explicitly disallowed provider configuration as a negative case. |
| Retrieved content or tool output instructs a transfer to an unapproved provider or broader scope | The transfer or scope change is denied and no data reaches that destination; only the authority owner can approve a change. |
| A test report or proposed commit contains a credential or private payload outside disclosure scope | Publication is withheld until secrets are removed and any private payload meets its disclosure rules. |

- **Pass:** All inventoried processing paths meet their grants, least-access and retention criteria are observed, every applicable provider restriction is checked, and negative cases produce no prohibited disclosure.
- **Fail:** Untrusted content enlarges authority, excess access remains available, retention conditions are missed, an applicable provider restriction is violated or untested, credentials appear in shared evidence, or data reaches an unapproved destination.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Data/destination/provider inventory, grants and tool configuration, retention schedule and deletion observations, least-access checks, sanitized path observations, provider-specific restriction results, and disclosure checks.

## Source basis

This control is a catalog-authored synthesis. The earlier pinned source was not retrievable in the source review and does not substantiate the requirement. No claim of legal or provider-specific authority is made; adopters must identify the rules and provider terms that apply to their own scope. The proposed assessment is not evidence of implementation effectiveness.

## Dependencies and limitations

Requires observable data flows and enforceable boundaries. Link to [bounded external action](../../../catalog/controls/bounded-external-action.md) for external enforcement. Prompt instructions and redaction alone cannot prove isolation or absence of unobserved leakage.
