---
type: Guide
title: "Assess human oversight"
description: "Test whether reviewers have the evidence, workload capacity, intervention time, and practiced fallback needed for their assigned role."
status: draft
sources:
  - id: allocation
    resource: ../human-ai-authority.md
    title: "Allocate human and AI authority across a factory"
---

# Assess human oversight

## Use and evidence limits

Use this note to assess the practical human participation assigned under [decision rights and accountability](../controls/decision-rights-and-accountability.md). Changes in reviewer capacity can also trigger [reassessment of autonomy](autonomy-change-evidence.md). These are catalog recommendations derived from the [authority allocation guide](../human-ai-authority.md), whose research synthesis preserves source attribution and evidence limits.[^allocation] They do not establish operational effectiveness or a universally correct autonomy level.

## Assess the review and intervention boundary

For a review boundary, supply the actual proposal, evidence, alternatives, uncertainty, destination, consequences, and the remaining time. Give the person a clear way to reject, edit, stop, or escalate. Preserve the reason and the action actually executed. Use [bounded external action](../controls/bounded-external-action.md) to bind any action-specific approval.

Test review with plausible wrong proposals, missing evidence, and valid alternatives under realistic workload. Measure missed errors, unnecessary rejection, response times, queue age, and outcomes after override. For a repeatable review rubric, [verifier qualification](../controls/verifier-qualification.md) supplies labeled cases and revision-specific qualification. Where producer modification threatens acceptance, [protected acceptance](../controls/protected-acceptance.md) addresses that separate boundary. Approval rate and number of clicks are weak evidence of oversight quality. Preserve occasional independent judgments before revealing the AI recommendation where appropriate to assess reliance.

For supervision, a useful design check is:

**detection time + notification time + human decision time + enforcement time < time available to prevent the effect.**

Use conservative measured values, relevant tail latency, and margin; averages alone hide slow cases. If a message leaves immediately, a person reading an alert minutes later cannot veto it. If supervisory coverage disappears, route to a preauthorized safe state. Silence only permits continuation when the standing grant explicitly allows that behavior; it never supplies a missing approval.

Maintain practice for tasks people must take over. Test handoff with a summary of current state, completed effects, pending actions, uncertainty, and available recovery options. Use [cancellation enforcement](../controls/cancellation-enforcement.md) when stopping queued or delegated work must prevent new effects and reconcile actions already in flight. A manual fallback that staff cannot perform is an unimplemented fallback. Periodic audit may suffice for a bounded low-consequence action even when real-time supervision adds little value.

Record the assessed revision, criteria, observations, and limits using [assessment evidence records](../assessment-evidence-records.md). Keep actual thresholds, actors, grants, and results with the adopting factory; this note adds no required OKF fields.

[^allocation]: [Research synthesis and its source limitations](../human-ai-authority.md#what-the-research-supports), inspected for the original guide on 2026-09-28; a targeted synthesis, not a systematic literature review.
