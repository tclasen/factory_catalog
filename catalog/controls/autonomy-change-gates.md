---
type: Control
title: "Autonomy change gates"
description: "Require scoped evidence and independent authorization to expand autonomy, with tested reduction, suspension, and recovery rules."
catalog_version: "v0.1.0"
status: draft
family: change-and-dependencies
sources:
  - id: allocation
    resource: ../human-ai-authority.md
    title: "Allocate human and AI authority across a factory"
---

# Autonomy change gates

[Adoption](../adoption.md) · [Research and allocation guide](../human-ai-authority.md)

**Identity:** `controls/autonomy-change-gates` · **Catalog:** v0.1.0 · **Family:** `change-and-dependencies`

## Purpose and applicability

Prevent autonomy from expanding through unreviewed capability, configuration, workload, or permission changes. Apply when a factory introduces or changes independent planning, decisions, execution, delegation, or adaptation, or continues operating as supporting assumptions change. A fixed scope still needs expiry and reassessment when dependencies or context change.

This proposed control implements the guide's recommendation to treat autonomy as a revisable allocation supported by scoped evidence.[^allocation]

## Requirement

Before operating an autonomous scope, establish its permitted actions, context, limits, revisions, owner, evidence, review/expiry conditions, and fallback. Every expansion must identify the proposed difference, predeclare acceptance criteria for it, assess relevant quality, authority, oversight, and recovery behavior, and receive authorization from a change authority outside the executing actor's effective control. Missing, failed, or inconclusive required evidence must withhold the expansion.

Protect governing grants, acceptance criteria, and enforcement settings from self-modification by the executing actor. Automated adaptation and mode switching are allowed only within an explicitly authorized and assessed envelope. Outside it, a new authorization is required. Self-reported confidence, time without reported incidents, and a model upgrade are insufficient authority to expand.

Monitor predeclared conditions for reducing, suspending, or retiring autonomy, including loss of required observation. Apply a defined safe disposition within the specified response time. Restore suspended scope only after recorded recovery criteria and authorization are satisfied. Continued operation must remain supported by current evidence for its actual conditions.

## Implementation

1. Record the present and proposed action scope, population, destinations, aggregate exposure, delegation, model/tool/instruction/data revisions, and human roles. Name the owner and protected change authority. State how unknown supplier versions constrain evidence.
2. Define relevant outcomes and harmful failure classes, baseline, test population, sample rationale, thresholds, observation period, evaluator, and uncertainty treatment before the trial. Use [outcome verification](outcome-verification.md) and retain [evidence traceability](evidence-traceability.md). Qualify the evaluator and record conflicts.
3. Test the proposal in proportionate stages, such as offline comparison, shadow use, and a limited pilot. Give any pilot its own grant and exposure budget; test execution and recovery separately from shadow accuracy. Include rare severe cases, out-of-scope cases, adversarial inputs, and composition across agents where relevant.
4. Review the complete evidence against the declared criteria. Authorize an explicit scope and validity period, or record withheld expansion and next steps. A failed expansion need not stop an unchanged scope whose evidence and authority remain valid.
5. Enforce the new grant only for the assessed configuration and context. Control rollout, revoke superseded permissions, and reconcile queued and in-flight work. Prevent mixed versions from silently inheriting broader permissions.
6. Monitor quality, impacts, authority violations, workload, drift, dependency changes, complaints, and evidence freshness. Define who acts, the deadline, and the safe response for each trigger. Exercise missing telemetry and failed fallback as well as normal triggers.
7. After suspension, reconcile effects, address causes, requalify affected claims, and obtain the recorded restart authorization. Keep prior records available to explain decisions; do not rewrite acceptance thresholds to turn a failed trial into a pass.

## Expected outcome and assessment

Expected outcome: expanded discretion operates only within an authorized, evidenced scope; invalidated conditions lead to a timely bounded response; restoration follows the recovery gate.

Inspect the current allocation and one proposed transition, using a declared fixture if no operational transition exists. In an observable safe environment exercise every distinct change/enforcement path:

| Case | Required observation |
|---|---|
| Complete evidence meeting criteria and valid change authorization | Only the specified new scope becomes available for the assessed revision |
| Missing, failed, inconclusive, stale, or wrong-revision required evidence | Expansion is withheld; reason and owner are recorded |
| Executing actor edits its grant, criteria, monitor, or change approval | Protected change is denied, including alternate credentials and delegated paths |
| Allowed adaptation within the assessed envelope | Change succeeds within limits and remains traceable |
| Adaptation, delegation, destination, or aggregate exposure exceeds the envelope | Expanded effect is denied and routed to the change authority |
| Drift, consequential failure, expired grant, reviewer loss, or telemetry loss | Each configured trigger produces the declared safe response within its deadline |
| Suspension during queued/in-flight work | No new unauthorized work starts; outstanding effects and obligations are reconciled |
| Premature restart, followed by a properly qualified restart | Premature restart is denied; restored scope requires recovery evidence and authorization |

**Pass:** all required records exist, every applicable case produces the required behavior, response criteria are met, and valid positive cases succeed. **Fail:** any required gate is bypassed, criteria are changed retroactively to claim success, mandated containment is late or absent, or a valid positive case fails. **Inconclusive:** evidence or effects are insufficient to decide. Explain conditional cases that cannot arise in the assessed design; inability to test an existing path is incomplete coverage.

Retain scope and configuration differences, criteria and baseline revisions, test populations and limitations, trial grants, observations, evaluator, authorization record, actual deployed revision, trigger/response timing, effect reconciliation, recovery evidence, assessment time and result. Structural document checks do not count as this assessment.

## Dependencies and limitations

Requires protected change administration, current grants, observable outcomes, meaningful evaluators, and a workable safe state. [Bounded external action](bounded-external-action.md) enforces external authority; [decision rights and accountability](decision-rights-and-accountability.md) establishes people and roles able to act. These linked controls require their own pinned adoption records and assessments when selected. This control sets no universal risk threshold, statistical confidence level, or mandatory progression toward greater autonomy. It cannot establish acceptable rare-event risk from a small successful trial. No deployment or effective implementation is claimed here.

[^allocation]: [Research and the procedure for evolving autonomy](../human-ai-authority.md#evolve-autonomy-with-evidence).
