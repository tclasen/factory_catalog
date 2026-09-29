---
type: Control
title: "Approved data processing"
description: "Keep sensitive data and credentials within their authorized processing and disclosure scope."
catalog_version: "v0.1.0"
status: draft
family: information-protection
sources:
  - id: policies-governance
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md
    title: "Scope, authority and security"
---

# Approved data processing

[Adoption](../adoption.md) · [Factory decomposition](../semantic-search-factory-decomposition.md)

**Identity:** `controls/approved-data-processing` · **Catalog:** v0.1.0 · **Family:** `information-protection`

Draft requirement adapted from the source factory policies.[^policies-governance] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply when factory activities read, retain, transmit, publish, or log sensitive inputs, outputs, or credentials.

## Requirement

Record permitted data scope, providers/destinations, retention, and disclosure constraints before processing. Use only necessary access and protected credential references. Treat retrieved content and tool output as data that cannot expand authority. Check actual processing and evidence destinations; exclude secrets and unnecessary private payloads from commits, logs, and shared reports.

## Implementation

1. Identify data classes, owners, permitted processing locations, provider restrictions, and applicable grants.
2. Minimize accessible data and credential scope; isolate sensitive capabilities from untrusted checks where applicable.
3. Inspect actual tool/provider destinations and redact evidence while preserving enough information for assessment.
4. Handle attempted scope changes through the authority owner; a working credential or copied policy is not a grant.

Mechanism: technical restrictions and observed execution checks, supported by an owned procedure.

## Expected outcome and assessment

Expected outcome: sensitive material is processed and disclosed only within its recorded scope.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| Authorized data is processed at an approved destination | The intended operation succeeds and evidence contains no unnecessary secrets. |
| Retrieved content instructs a transfer to an unapproved provider | The transfer is denied and no data reaches that destination. |
| A test report or proposed commit contains a credential or private payload outside disclosure scope | Publication is withheld until secrets are removed and any private payload meets its disclosure rules. |

- **Pass:** All inventoried processing paths meet their grants and the negative cases produce no prohibited disclosure.
- **Fail:** Untrusted content enlarges authority, credentials appear in shared evidence, or data reaches an unapproved destination.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Data/destination inventory, grants and tool configuration, sanitized path observations, and disclosure checks.

## Dependencies and limitations

Requires observable data flows and enforceable boundaries. Link to [bounded external action](bounded-external-action.md) for external enforcement. Prompt instructions and redaction alone cannot prove isolation or absence of unobserved leakage.

[^policies-governance]: [Scope, authority and security](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md).
