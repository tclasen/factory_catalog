---
type: Guide
title: "Optional dispatcher and lead handoff"
description: "Describe a constrained dispatcher arrangement with safe lead succession and explicit return states."
catalog_version: "v0.1.0"
status: draft
sources:
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
  - id: readiness
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/readiness.md
    title: "Adoption and framework readiness"
---

# Optional dispatcher and lead handoff

[Factory decomposition](../semantic-search-factory-decomposition.md) · [Work record](factory-work-record.md)

## Applicability and source boundary

Use only when the host explicitly selects and authorizes a dispatcher/lead structure and the runtime supports it. This is one composition described in the source execution protocol, not a prerequisite for adopting the catalog or its controls.[^policies-execution] The source also permits bounded documentation maintenance by the current agent when dispatch adds no useful independent work. No delegation is authorized by this guide.

## Responsibilities

- **Dispatcher:** reads the host entry point, bootstrap protocol, and handoff location; passes the original request, binding paths, and actual runtime constraints to one fresh lead. Waits, relays progress/results, and retains user steering, interruption, approvals, and other higher-priority runtime duties.
- **Lead:** reads current instructions and actual state, chooses the authorized increment, plans, coordinates contributions, reviews, integrates, verifies delivery, and persists restart state.
- **Specialist:** performs a bounded assigned contribution within its permitted surfaces and limits; returns actual changes, evidence, failures, effects, and remaining obligations.

The dispatcher is not another integration owner or release reviewer. Actor counts include dispatcher, lead, and descendants; a fresh context does not create a fresh resource allowance. Model/reasoning choices follow [task configuration selection](../controls/task-configuration-selection.md) only where those controls are actually available and authorized.

## Return protocol

These are source protocol messages, not additions to catalog assessment states.

| Return | Required content and next action |
|---|---|
| `COMPLETE` | Lead supplies delivery evidence for the agreed endpoint and limitations. Dispatcher relays it and ends the run. |
| `CONTINUE` | Lead supplies a durable packet and remaining scope/limits. After prior writers stop or lose write access, one successor reconciles actual state before mutation. |
| `BLOCKED` | Lead names the exact unfinished gate and smallest required decision or external change. Stop dependent work; do not reinterpret it as success. |
| `CHECKPOINT` | Preserve unfinished work, consumed allowance, and remaining obligations. Stop affected implementation/heavy checks; expansion requires the appropriate direction. |

## Failure handling

A missing or ambiguous return is not permission to start another writer. Seek clarification from the same lead when available; otherwise preserve the interrupted state and establish safe predecessor stop before recovery. A missing packet is a different problem: once prior execution cannot act, one recovery lead reconstructs from the original request and observable state. Missing essential authority or scope stays blocked.[^policies-execution]

Apply [safe work resumption](../controls/safe-work-resumption.md), [bounded execution](../controls/bounded-execution.md), and [isolated parallel work](../controls/isolated-parallel-work.md). The dispatcher relays new user scope and stops affected execution when required. It does not invent replacement grants, a custom scheduler, unattended runs, or new tasks to evade limits.

## Walkthrough and limitations

Walk normal completion, same-task continuation, exhausted allowance, a lost return, a missing packet, and a predecessor still able to publish.[^readiness] Check that exactly one authorized lead can write, cumulative limits survive, and incomplete work never becomes a success claim. If the selected runtime cannot provide this structure, record that limitation rather than pretending the roles were isolated.

These checks assess a proposed procedure. A written role split does not technically isolate credentials, processes, or authority and has not been operationally qualified here.

[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
[^readiness]: [Adoption and framework readiness](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/readiness.md).
