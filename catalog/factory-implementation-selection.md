---
type: Guide
title: "Select and assess factory implementation mechanisms"
description: "Allocate factory activities across implementation mechanisms, record the decision, and test the composed boundaries."
status: stable
sources:
  - id: tradeoffs
    resource: factory-implementation-tradeoffs.md
    title: "Factory implementation trade-offs"
---

# Select and assess factory implementation mechanisms

This procedure applies the [implementation research](factory-implementation-tradeoffs.md) to a particular factory.[^tradeoffs] It extends the local decisions made during [selection, adoption, and assessment](adoption.md), without imposing new catalog control requirements. The examples and proposed tests below have not been executed against a deployed factory.

## 1. Allocate by activity and consequence

Describe the factory's outcome, owner, inputs, actors, authority, persistent state, and external actions using the [ontology](ontology.md). Split activities at points where judgment, ownership, evidence, or permissions change. For example, preparing a report and publishing it can share data while requiring different authority.

For each activity, answer these questions in order:

1. **Can its essential operation be specified precisely?** Use ordinary code for exact transformations and predicates. Record which parts still require interpretation or uncertain inputs.
2. **Does it need adaptable judgment?** Use a human or model with concise prose criteria and explicit handling of uncertainty. Keep those criteria reviewable outside the implementation.
3. **Does a recognizable procedure recur?** Consider a skill to package the procedure, examples, and tested scripts. Verify discovery as well as execution.
4. **Does it need shared installation or authenticated capabilities?** Consider a plugin; inventory its components and service dependencies. Use existing tools when packaging adds no useful capability.
5. **Does work depend on a host event or specialized interface?** Consider an extension or hook. Name the supported host and versions, event timing, and behavior when absent or failing.
6. **Must a transition be prevented when prerequisites fail?** Place a protected check at the transition, with credentials and configuration the producer cannot bypass. Include external APIs and direct clients in coverage.

Multiple answers can apply. A skill might call a shared validator, an extension might display its findings, and a remote gate might require a trusted run before publication. Avoid adding all six mechanisms merely to fill the categories.

## 2. Record a reviewable decision

Use one record per activity or boundary when they have different owners or lifecycles. These are suggested local record fields, not additions to the catalog schema.

| Field | Record |
|---|---|
| Scope and outcome | Activity, beneficiary, acceptance criteria, intended outcome, excluded paths |
| Control adoption | Selected control identities, catalog version, exact source SHA, pinned source URLs, and adaptations under the [adoption procedure](adoption.md#record-the-adoption) |
| Alternatives | Simplest viable baseline, alternatives considered, and reason for the choice |
| Mechanisms | Instructions, human procedure, automated check, or technical restriction; identify the role of any skill, plugin, or extension |
| Components | Source and installed revisions, model/host settings, scripts, policy, fixtures, service/API configuration, dependencies |
| Trigger and interface | How invoked, required input/output, errors, missing dependencies, and state passed to the next activity |
| Authority boundary | Actor, grant issuer, permitted action/target/limits/validity, credentials, administrator, alternate paths, exceptions |
| Evidence binding | Artifact or payload identity, criteria and evaluator revisions, observations, evaluator identity, time, retention/access rules |
| Recovery | Durable state, operation identity, attempt limits, unknown-effect handling, ownership, resume and rollback conditions |
| Cost and ownership | Setup and maintenance owner; expected volume; execution, review, rework, and operating costs |
| State and assessment | Implementation state and assessment result separately; method, coverage, results, gaps, follow-up |
| Reassessment | Triggered by changed requirements, model, host, dependency, credentials, gates, destinations, or observed failures |

Do not manufacture a pinned adoption URL for unpublished local content. Pin the published revision actually consumed, including relative cross-control references. A package release number alone may not identify deployed service behavior; retain the relevant deployment/configuration identity too.

## 3. Compare a baseline with a candidate

Choose representative tasks before optimizing: common work, ambiguous cases, missing inputs, malformed artifacts, unavailable services, and requests that resemble the workflow but should not activate it. Use authorized fixtures for external effects. Keep required policy and authority identical across variants; do not remove them to make a faster baseline.

Hold task inputs, acceptance rubric, environment, and relevant tool/model settings constant where possible. Repeat runs when behavior varies, report sample size and variation, and keep a held-out set for final comparison. Changing several components at once can evaluate a proposed bundle but cannot isolate which change caused the result.

| Measure | What it helps decide |
|---|---|
| Accepted outcomes / attempted cases | Whether the mechanism improves useful completion; include failed and abandoned attempts |
| Correct and incorrect activation | Whether the intended procedure is selected without imposing itself on unrelated work |
| False acceptance and false rejection | Whether a validator or gate admits bad candidates or blocks valid work |
| Human review and rework | Whether automation shifts hidden labor to reviewers |
| End-to-end time and resource cost | Include queues, retries, review, and unsuccessful runs; keep token usage distinct from total cost |
| Coverage of authority tests | Which inventoried execution paths enforce grants before effects |
| Recovery observations | Whether interrupted work preserves evidence, ownership, and one intended effect |

Set thresholds and the disposition for missing evidence before seeing results, following [outcome verification](controls/outcome-verification.md). For high-consequence actions, favorable averages cannot compensate for a demonstrated authority bypass. Finite testing also cannot prove that every possible bypass has been excluded.

## 4. Test the composed system

Apply each adopted control's complete assessment. The following supplementary fixtures probe implementation composition; they do not replace those assessments or establish results merely by being listed.

| Fixture | Expected observation | Evidence to retain |
|---|---|---|
| Valid request, complete evidence, current grant | Intended transition succeeds once | Request and candidate identity, decision, observed destination state |
| Skill not selected, extension disabled, or direct API client used | Any mandatory authority restriction still holds on every inventoried path | Invocation route and boundary observations; mark unobservable paths inconclusive |
| Check fails, is skipped, is cancelled, times out, or returns malformed output | Required evidence remains unsatisfied; dependent acceptance is withheld | Each distinct case, actual host/gate semantics, transition result |
| Producer changes validator, fixtures, workflow, or reported status | Protected acceptance cannot silently adopt producer-controlled criteria or a forged result | Effective permissions, protected revisions, expected result issuer, attempted transition |
| Artifact, destination, policy, or grant changes after approval | Invalidated evidence or action-specific approval cannot authorize the changed action | Before/after identities, invalidation decision, external effects |
| Tool completes externally but response is lost | Unknown state is reconciled before retry; duplicate prevention is observed where claimed | Operation key, attempt record, authoritative destination observations |
| Source contains instructions to ignore the workflow | Source content remains data; protected restrictions survive | Input fixture, execution trace, observed effects, claim-review result |
| Gate rejects a valid alternative implementation | False rejection is identified and corrected through the authorized change process | Valid candidate, rationale, updated evaluator revision, rerun results |

A passing permission test supports a boundary claim. A successful agent task supports a claim about that task and configuration. Neither establishes source truth or long-term user benefit. Use [evidence traceability](controls/evidence-traceability.md) to retain inspectable support, and report missing coverage explicitly.

## 5. Worked allocations

These are hypothetical applications to existing catalog examples, with **proposed** implementation state and **not-assessed** assessment result. They illustrate choices without claiming adoption or changing the examples' requirements.

### Software delivery

Apply this allocation to the [software delivery factory](factories/software-delivery.md):

| Activity | Proposed allocation | Reason and remaining boundary |
|---|---|---|
| Define the analyst's intended result | Prose criteria and product-owner judgment | Interpretation changes with user needs; preserve criteria before observations |
| Implement the export | Agent procedure, optionally a skill | Adaptive development benefits from reusable steps; a skill is justified only if it recurs |
| Check format, contents, and denied requests | Shared deterministic test code, run locally and in trusted acceptance | Fast feedback plus required evidence; protect acceptance fixtures where independence is claimed |
| Make checks convenient | Optional editor extension | Add only if inline feedback measurably helps; absence must not bypass the gate |
| Distribute common tools | Optional plugin | Useful across teams; unnecessary for one repository with adequate existing tools |
| Integrate and deploy | Required repository checks plus a separately scoped delivery service or protected environment | Match the qualified artifact and destination; direct deployment credentials must obey the same grant |
| Observe analysts completing the task | Human observation and a structured evidence record | Passing code tests does not establish the user outcome |

For a GitHub implementation, inspect effective repository rules, expected check producer, supported events, skipped-job behavior, bypass permissions, environment rules, and all deployment credentials using the [research on external gates](factory-implementation-tradeoffs.md#external-gates-mandatory-only-with-protected-paths). A YAML file alone cannot establish this boundary.

### Research and publication

Apply this allocation to the [research factory](factories/research.md): prose defines the research question and evidential standard; a skill organizes repeatable retrieval and claim review; code validates citation structure and preserves source identities. A plugin is useful if authenticated source access is needed. A reviewer checks material claims in context. A publication service enforces the grant and any approval binding on the exact document and destination.

The semantic review cannot be replaced by a link checker. The publication gate can require a review record but still depends on the reviewer's competence and the integrity of that record. If outputs remain internal drafts and the assessed scope has no external execution path, an external publication gate may be unnecessary; record that scope and reassess when tools or destinations change under [bounded external action](controls/bounded-external-action.md).

## 6. Evolve without losing the decision

Adopt the smallest combination meeting the declared criteria, and retain why more elaborate options were deferred. Trial changes in an isolated scope; keep rollback artifacts and the previous assessment. Shadow a new validator before making it mandatory when that is compatible with existing protections. A shadow check observes behavior and supplies no new enforcement.

Reassess affected claims after changing a model, instruction, script, host, package, service, authority grant, or gate. Preserve an owner for unresolved outcome observation and for operational dependencies. If the implementation becomes harder to operate than the work warrants, simplify it while preserving the required control behavior.

These records instantiate the ontology's relationships: an **Implementation implements a Control revision** within an activity; an **Assessment evaluates that Implementation** and **uses Evidence**. Links to this guide express guidance and derivation. They do not confer authority, adoption, implementation, or a passing assessment.

[^tradeoffs]: Factory implementation trade-offs; primary-source research, evidence limits, and comparison of all six mechanisms.
