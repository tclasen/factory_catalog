---
type: Control
title: "Bounded external action"
description: "Enforce scoped authority before an action affects an external party or system."
status: stable
family: authority-and-access
---

# Bounded external action

[Controls](./) · [Adoption](../adoption.md) · [Control families](../control-families.md)

## Purpose and applicability

Prevent execution of external actions outside a recorded authority grant. Apply when a factory can publish, send communications, modify another system, spend, deploy, or make commitments. It can be excluded only if the assessed scope has no such execution path; revisit that decision when tools or permissions change.

## Requirement

Every external execution path must enforce an explicit grant for the actor, action, resource or destination, applicable limits, and validity period. Deny missing or invalid grants. If approval of a particular action is required, bind it to the exact payload or artifact revision and destination; modification invalidates that approval. An actor must not expand its own grant or bypass the enforcement point through alternate credentials or tools.

Approval can be a bounded standing grant or approval for a particular action. This control does not require a new human confirmation for every routine action already covered by valid authority.

## Implementation

1. Inventory external actions and all execution paths, including delegated actors and alternate tools.
2. Assign an authority owner. Record issuers, actors, allowed actions, destinations, limits, expiry/revocation, and any approval condition.
3. Enforce grants at the credential, service, gateway, or equivalent execution boundary. Keep grant administration outside the executing actor's permissions.
4. For action-specific approval, bind the approved revision and destination to execution and reject changes. Check current grant validity at execution time.
5. Record authorized and denied attempts with actor, grant reference, action, target, revision, time, and result; avoid retaining secrets or unnecessary payload data.
6. Define escalation when authority is missing and test revocation. Do not grant broader authority merely to make a blocked test pass.

## Expected outcome and assessment

Expected outcome: valid actions succeed within their scope, while attempts outside that scope are denied before an external effect occurs.

Use a sandbox or dry-run endpoint with observable effects. Test every inventoried path, including delegation where supported:

- A valid grant and matching action succeeds.
- No grant, expired grant, and revoked grant each deny execution.
- Wrong actor, action, destination, or an exceeded limit each deny execution.
- Where action-specific approval is configured, a changed payload or artifact revision denies execution.
- An attempt to alter the grant or use an alternate path cannot bypass enforcement.

**Pass:** every applicable case behaves as required and denied cases produce no external effect. **Fail:** any unauthorized effect, bypass, or rejection of the valid positive case. **Inconclusive:** a path or external effect cannot be observed; coverage is not established. Record conditional cases that do not apply and why.

For the [retrieved-instruction scenario](../risks/retrieved-instruction-action.md), the wrong-destination and bypass cases can be initiated by a retrieved document and repeated through a delegated actor. A child using a discovered credential remains outside the parent grant unless independently authorized. This is an example of the existing scope and alternate-path tests, not a new approval requirement.

Retain the path inventory, grant/configuration revision, test inputs, sanitized execution records, observed effects, evaluator, and test time.

## Dependencies and limitations

Requires trustworthy identity, an enforceable boundary, complete path inventory, and protected authority administration. Prompt instructions alone do not satisfy this requirement. Permission does not establish that an action is wise, accurate, lawful, or recoverable. Duplicate-action protection and service repair or rollback are outside this control's requirement; an adopter must select separately applicable controls and authority for those needs. [Reconcile before retry](reconcile-before-retry.md) addresses uncertain effects before a repeated mutation. This catalog defines the assessment; it does not claim that an implementation has passed it.
