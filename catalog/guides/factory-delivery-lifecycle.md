---
type: Guide
title: "Factory delivery lifecycle"
description: "Compose intake, execution, verification, delivery, and operational controls around one accountable owner."
status: draft
sources:
  - id: workflows-lifecycle
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/lifecycle.md
    title: "Intent-to-delivery workflow"
  - id: agents
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/AGENTS.md
    title: "Agent operating contract"
  - id: policies-planning
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md
    title: "Requirements and planning"
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
---

# Factory delivery lifecycle

[Software delivery example](../factories/software-delivery.md)

## Purpose and scope

Use to compose selected controls into a bounded work process. The source lifecycle assigns responsibilities and exit evidence from intake through operation; it is written guidance, not an executable scheduler.[^workflows-lifecycle] The source operating contract makes the lead accountable for the whole authorized outcome.[^agents]

## Stages and relationships

| Stage | Accountable action and linked controls | Exit evidence / failure route |
|---|---|---|
| Start or resume | Lead reads the [project binding](factory-project-binding.md) and applies [safe work resumption](../controls/safe-work-resumption.md). | Current scope, authority, ownership, and effects reconciled; essential unknowns block dependent mutation. |
| Intake and discovery | Owner/planner applies [accepted work definition](../controls/accepted-work-definition.md). | Observable criteria, accepted scope, exclusions, and dependencies; unresolved consequential intent returns to the decision owner. |
| Plan and select | Lead applies [planning consistency](../controls/planning-consistency.md) and chooses the smallest useful dependency-ready increment advancing the user's priority. | Consistent plans and ready prerequisites; no invented work to fill capacity. |
| Design and prepare | Designer records substantive decisions, risks, checks, and recovery; apply [approved data processing](../controls/approved-data-processing.md). | Reviewable approach within authority; documentation remains documentation unless implementation is authorized. |
| Implement | Lead applies [bounded execution](../controls/bounded-execution.md) and, if authorized/useful, [isolated parallel work](../controls/isolated-parallel-work.md). | Coherent candidate with current work record; repeated failure returns to bounded diagnosis. |
| Verify and review | Reviewer applies [acceptance coverage](../controls/acceptance-coverage.md), [assessment evidence validity](../controls/assessment-evidence-validity.md), and applicable [local quality gates](../controls/local-quality-gates.md). | Exact candidate meets required checks and review; failures return to repair or legitimate requirement reconciliation. |
| Integrate and deliver | One integrator applies [verified delivery](../controls/verified-delivery.md) within [bounded external action](../controls/bounded-external-action.md). | Agreed endpoint independently verified; conflict resolution reopens affected checks and unknown effects require reconciliation. |
| Operate and improve | Authorized operator applies relevant recovery/change/retirement controls; lead applies [instruction change control](../controls/instruction-change-control.md). | Observed health or exact blocker; feedback returns to intake, and remaining defects stay tracked. |

The stage describes current activity. It is separate from control applicability, implementation state, assessment result, and an OKF document's lifecycle status. A role may be performed by the lead unless actual separation requirements apply. This guide does not impose extra human approval or automatic delegation.

## Readiness and completion boundaries

Respect an explicitly requested factory-first prerequisite: product work cannot be selected while its required factory obligations remain unmet. When qualification using the product would create a dependency cycle, identify a separately authorized representative target or ask for the needed scope decision. Priority does not authorize creating that target. Outside such a prerequisite, an unrelated blocked action need not stop independent authorized work.[^policies-planning]

The source's default completion gate includes main integration.[^policies-delivery] Here the endpoint is defined by the adopter's accepted scope and actual repository rules. A PR-only task stops after verified PR delivery; no source policy can authorize a merge. Document delivery, installed behavior, and beneficiary outcomes require distinct evidence under [outcome verification](../controls/outcome-verification.md).

## Walkthroughs

Trace one accepted documentation correction and one authorized software change through the table. Verify every transition has an owner, required evidence, and failure route. Then inject a failed integration check, denied deployment, interrupted writer, and failed rollback. Delivery must remain open at the exact unmet stage; recovery must preserve acknowledged data, and cancellation must remain cancellation.

The walkthrough checks the usability of the process definition. Runtime effectiveness requires assessment of its local implementations.

[^workflows-lifecycle]: [Intent-to-delivery workflow](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/lifecycle.md).
[^agents]: [Agent operating contract](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/AGENTS.md).
[^policies-planning]: [Requirements and planning](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md).
[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md).
