---
type: Control
title: "Decision rights and accountability"
description: "Assign decision rights and accountable owners with demonstrated means to review, intervene, and address effects."
catalog_version: "v0.1.0"
status: draft
family: purpose-and-accountability
sources:
  - id: allocation
    resource: ../human-ai-authority.md
    title: "Allocate human and AI authority across a factory"
---

# Decision rights and accountability

[Adoption](../adoption.md) · [Research and allocation guide](../human-ai-authority.md)

**Identity:** `controls/decision-rights-and-accountability` · **Catalog:** v0.1.0 · **Family:** `purpose-and-accountability`

## Purpose and applicability

Prevent actions from proceeding with ambiguous decision rights or nominal accountability that lacks the ability to act. Apply to human, mixed, and automated factory activities, including lifecycle decisions, delegation, exceptions, and recovery. Assess only the declared factory/activity scope; list exclusions and revisit them when work crosses a boundary.

This proposed control turns the guide's research synthesis into a selectable requirement.[^allocation] It does not assign legal liability or require human approval for every action.

## Requirement

Before an activity operates, record who proposes, decides, approves when required, executes, evaluates, can stop the activity, and handles appeals or correction. Assign an accountable human or organizational role with a named incumbent or resolvable duty assignment, escalation route, and resources to address effects. AI execution must not be the only accountability assignment.

Record the authority and autonomy of each actor, including scope, limits, delegation, validity, protected decisions, and no-response behavior. Identify role conflicts and the separation or compensating checks used. Roles alone do not issue grants. Missing or conflicting authority must block the dependent action and route it to the designated owner.

Where prevention depends on human review or intervention, demonstrate that the person has the competence, evidence, time, access, and authority needed under representative workload. Define measurable review and response criteria before assessment. Provide a tested safe disposition when that capacity is unavailable. After-the-fact review must not be counted as prevention of an already completed effect.

## Implementation

1. Inventory activities and actual execution paths, including permissions administration, evaluation, persistent memory, delegated work, and incident response. Split actions where consequences or rights differ.
2. Record the roles above, the accountable assignment, decision rationale, grant references, and handoff acceptance. Small teams may combine roles when conflicts and compensating checks are documented; separation required by local obligations remains mandatory.
3. Give reviewers and owners access to relevant evidence, protected reporting, stop mechanisms, and a route to resources for correction. Define an accessible challenge route for affected parties appropriate to the activity.
4. Specify which decisions use a standing grant, which require approval of an exact action, and which are reserved. Enforce external permissions using [bounded external action](bounded-external-action.md); role documentation alone does not enforce them.
5. Declare severe-error detection criteria, permitted review errors, response deadlines, staffing/queue limits, and the safe behavior on absent approval or unavailable supervision. Explain why those values fit the potential effects. If prevention cannot fit the available time, change the action boundary or use preventive restrictions.
6. Exercise valid and invalid proposals, reviewer absence, disputed outcomes, and handoffs. Retain observations and correct defects. Reassess after changes to roles, workload, interfaces, consequence, or authority; use [autonomy change gates](autonomy-change-gates.md) when discretion changes.

## Expected outcome and assessment

Expected outcome: every inventoried activity has an actionable allocation of rights and accountability, and dependent actions do not proceed when their required authority or oversight is unavailable.

Inspect the complete scope inventory and role/grant records. In a safe test setting exercise each distinct authority and oversight mechanism, with representative normal and peak workload. Include the following cases, retaining configuration and observed effects:

| Case | Required observation |
|---|---|
| Valid routine action within a standing grant | Correct actor executes without an unrequired new approval; the decision and owner are traceable |
| Missing/conflicting owner, rights, or required approval | Dependent action is withheld and routed to a resolvable owner; no default self-authorization |
| Plausible materially wrong proposal, missing evidence, and valid alternative | Required reviewer distinguishes them to the predeclared criteria; evidence and reasons are retained |
| Reviewer absent or queue beyond declared capacity | Configured safe disposition occurs before an unapproved or unsupervised dependent effect |
| Stop or revocation during queued and in-flight work | New effects are prevented within declared timing; completed and unavoidable effects are reconciled and assigned for follow-up |
| Delegation or shift handoff | Receiving actor has scoped authority, current state and obligations; accountability remains resolvable |
| Affected party challenges a completed outcome | Challenge reaches an authorized reviewer with evidence access and authority to arrange correction or escalate |

**Pass:** all inventory records are complete, all applicable cases meet predeclared criteria, valid actions succeed, and no action bypasses required authority or oversight. **Fail:** a required record or mechanism is absent, criteria are missed, a valid action is wrongly blocked, or a forbidden effect occurs. **Inconclusive:** records, representative workload, or effects cannot be observed well enough to decide. Mark a case not applicable only with a rationale showing that its path is absent; this does not permit omitting accountability for the remaining scope.

Retain the activity and path inventory, role and grant revisions, competence and coverage evidence, fixtures, timing and queue observations, decision reasons, actual effects, evaluator, assessment time, results, and unresolved follow-up. Use sanitized references with access controls rather than unnecessary personal or sensitive content.

## Dependencies and limitations

Requires trustworthy identities, observable effects, enforceable permissions, available staff where assigned, and resourced incident/appeal handling. Human procedure and technical restrictions implement different parts of this control. Technical enforcement, outcome quality, and evidence integrity need their own assessments. A successful drill supports only its tested conditions; it does not prove that a person will detect every future failure. No operational effectiveness is asserted by this document.

[^allocation]: [Research, source limitations, and allocation procedure](../human-ai-authority.md).
