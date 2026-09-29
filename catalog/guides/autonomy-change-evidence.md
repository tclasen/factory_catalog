---
type: Guide
title: "Evidence for changing autonomy"
description: "Assemble scoped trial evidence and define triggers for expanding, reducing, suspending, or restoring autonomy."
status: draft
sources:
  - id: allocation
    resource: ../human-ai-authority.md
    title: "Allocate human and AI authority across a factory"
---

# Evidence for changing autonomy

## Use and evidence limits

Use this note to prepare a proposed autonomy change and its monitoring and recovery evidence. Assess [human oversight](human-oversight-assessment.md) where the proposed scope depends on review or intervention. These are catalog recommendations derived from the [authority allocation guide](../human-ai-authority.md), whose research synthesis preserves source attribution and evidence limits.[^allocation] They do not establish operational effectiveness or a universally correct autonomy level.

## Trial sequence and evidence package

Use [autonomy change gates](../controls/autonomy-change-gates.md) to make changes explicit. A useful sequence is offline comparison → shadow operation without effects → bounded pilot → routine operation. Shadow results cannot prove execution, recovery, or real operator behavior; test those separately. Stages may be combined when justified, and a successful trial may correctly end with no expansion.

Define the evidence package for each proposed change:

- Exact model, tools, prompts, data/retrieval, workflow, grant, and enforcement revisions; known supplier changes or unknown version details.
- Action population, exclusions, case mix, observation window, sample size, and relevant baseline.
- Artifact quality and beneficiary outcomes; severity-specific failures and subgroup results where relevant; uncertainty and unobserved harms.
- Review performance, intervention latency, unauthorized attempts, bypass tests, aggregate consumption, and exercised recovery.
- Decision-maker, accepted residual risk, scope and duration of the resulting grant, and explicit conditions for reducing or stopping it.

Do not promote based on an uneventful calendar interval or a single accuracy average. Successful easy cases say little about rare severe failures. Select sample sizes and statistical methods for the tolerated failure rate and dependence between observations. Repeated cases from the same template or incident may provide much less evidence than their count suggests. No universal accuracy percentage justifies every delegation.

## Change triggers and restoration

| Trigger | Recommended immediate disposition | Evidence needed before restoring or expanding scope |
|---|---|---|
| Unauthorized action, bypass, or protected configuration change | Contain affected paths; revoke or narrow grants; preserve records | Cause, effect reconciliation, corrected enforcement and negative tests |
| Quality drift, novel case mix, rising appeals, or unequal harm | Restrict affected classes; route to qualified review or pause | Representative reassessment and remedy of affected outcomes |
| Reviewer overload, absence, or failed intervention drill | Reduce throughput, switch to safe bounded behavior, or pause dependent work | Available staffing, practiced handoff, demonstrated timing |
| Model, supplier, prompt, tool, retrieval, memory policy, or workflow change | Identify affected claims; withhold unsupported expanded scope | Relevant comparisons, regression checks, and refreshed grants |
| Monitoring loss, unknown effects, or stale evidence | Apply predeclared safe state; reconcile before retries | Restored observability and known destination state |
| New legal or contractual constraint, changed beneficiaries or purpose | Reassess affected permissions before continued use | Applicable obligation review and authorized scope decision |
| Stronger results under unchanged scope | Consider a separate expansion proposal | Evidence covering the proposed additional consequences and limits |

Automatic mode switches can implement a preauthorized policy inside a tested envelope. An agent may reduce its activity or stop under that policy. It cannot treat its own confidence, a new model, or a favorable self-evaluation as permission to enlarge the envelope. Restore suspended authority only through the recorded recovery gate.

Record the assessed revision, criteria, observations, and limits using [assessment evidence records](../assessment-evidence-records.md). Keep actual thresholds, actors, grants, and results with the adopting factory; this note adds no required OKF fields.

[^allocation]: [Research synthesis and its source limitations](../human-ai-authority.md#what-the-research-supports), inspected for the original guide on 2026-09-28; a targeted synthesis, not a systematic literature review.
