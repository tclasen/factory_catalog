---
type: Guide
title: "Factory work record"
description: "Keep the minimum durable state needed to review, transfer, and resume a bounded work item."
status: draft
sources:
  - id: templates-work-item
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md
    title: "Work-item template"
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
---

# Factory work record

[Delivery lifecycle](factory-delivery-lifecycle.md) · [Project binding](factory-project-binding.md)

## Purpose and trigger

Use for a work item that needs durable review or safe handoff. Adapted from the source work-item template and execution protocol.[^templates-work-item][^policies-execution] Small serial changes can use an existing requirement and evidence note; this guide does not require a new tracker or journal service.

## Record owned by the work lead

| Field | Minimum useful content |
|---|---|
| Identity and intent | Work ID, original request, accepted requirement/criteria, current outcome and exclusions |
| Ownership | Accountable lead, predecessor/descendants where relevant, reserved write surfaces, actual stop or access restrictions |
| Current state | Stage, completed actions, blockers, exact workspace/base/candidate, dirty and unrelated work to preserve |
| Assignments | Bounded contribution scopes, inputs, constraints, separate editing checkouts, return criteria and status |
| Configuration | Actual model/reasoning settings when selectable, alternatives, dated rationale and uncertainty |
| Limits | Applicable allowance, cumulative attempts/consumption, remaining time/resources/slots, next checkpoint |
| Evidence | Exact assessed inputs, commands/procedures, actual outcomes, failures, gaps, protected evidence references |
| Effects | Intended external operation and destination, identifiers, observed result or uncertainty, recovery obligations |
| Delivery | Agreed endpoint and completed/unmet stages with evidence |
| Next action | Remaining scope, essential decisions, safe resume step, successor and handoff disposition if applicable |

## Procedure

1. Establish [accepted work definition](../controls/accepted-work-definition.md) and the relevant project binding.
2. Update the record at meaningful state changes and before consequential effects or transfer. Reference old evidence instead of recursively copying the record's history.
3. Keep it short enough to find pending obligations without reading the full conversation. Protect secrets and sensitive payloads through access-controlled references.
4. Apply [safe work resumption](../controls/safe-work-resumption.md) before successor writes. Reconcile actual files, processes, grants, and remote effects; the record can be stale.
5. Preserve [bounded execution](../controls/bounded-execution.md) counters and apply [assessment evidence validity](../controls/assessment-evidence-validity.md). Separate incomplete, cancelled, blocked, and delivered work in prose without changing the catalog's assessment vocabulary.

## Review and failure handling

Walk a transfer with an uncommitted change, one failed check, and an uncertain external effect. The recipient must locate each, preserve unrelated work, and choose the earliest required reconciliation step. Walk a missing packet: reconstruction may use original intent and actual state only after prior writers are stopped or excluded. If authority or scope cannot be recovered, record the specific missing input and stop dependent mutation.

A usable record supports recovery; it does not prove exclusive ownership, dispatch a successor, establish a passing check, or authorize an external action.

[^templates-work-item]: [Work-item template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md).
[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
