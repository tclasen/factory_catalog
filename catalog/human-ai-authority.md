---
type: Guide
title: "Allocate human and AI authority across a factory"
description: "Research and a practical method for assigning decision rights, accountable owners, oversight, and changing autonomy over time."
catalog_version: "v0.1.0"
status: draft
sources:
  - id: automation
    resource: https://www.researchgate.net/publication/11596569_A_model_for_types_and_levels_of_human_interaction_with_automation
    title: "Parasuraman, Sheridan and Wickens (2000), A model for types and levels of human interaction with automation"
  - id: ironies
    resource: https://tc.ifac-control.org/4/1/newsletter/ironies-of-automation/@@download/file/Bainbridge1983_Automatica_Ironies%20of%20automation.pdf
    title: "Bainbridge (1983), Ironies of automation"
  - id: crumple
    resource: https://estsjournal.org/index.php/ests/article/view/260
    title: "Elish (2019), Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction"
  - id: combinations
    resource: https://www.nature.com/articles/s41562-024-02024-1
    title: "Vaccaro, Almaatouq and Malone (2024), When combinations of humans and AI are useful"
  - id: rmf
    resource: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
    title: "NIST AI RMF 1.0 (2023), Core"
  - id: oecd
    resource: https://www.oecd.org/en/topics/ai-principles.html
    title: "OECD AI Principles, revised 2024"
  - id: diligence
    resource: https://www.oecd.org/en/publications/oecd-due-diligence-guidance-for-responsible-ai_41671712-en/full-report/component-4.html
    title: "OECD (2026), Due Diligence Guidance for Responsible AI, practical framework"
  - id: eu14
    resource: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14
    title: "Regulation (EU) 2024/1689, Article 14, Commission Service Desk reproduction"
  - id: eu26
    resource: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26
    title: "Regulation (EU) 2024/1689, Article 26, Commission Service Desk reproduction"
  - id: auditing
    resource: https://arxiv.org/html/2001.00973v1
    title: "Raji et al. (2020), Closing the AI Accountability Gap"
  - id: agency
    resource: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
    title: "OWASP LLM06:2025, Excessive Agency"
---

# Allocate human and AI authority across a factory

[Ontology](ontology.md) · [Adoption](adoption.md) · [Decision rights control](controls/decision-rights-and-accountability.md) · [Autonomy change control](controls/autonomy-change-gates.md) · [Worked example](factories/support-resolution.md)

## Recommendation and scope

Choose autonomy for each action in its operating context. Give an actor only the discretion and permissions needed for that action, assign an accountable person or organizational role with resources to respond, and test the complete human–AI arrangement. Expand scope when relevant evidence supports it; reduce or suspend scope when its assumptions stop holding. Increasing autonomy is an option, not a maturity target.

This guide concerns the catalog's **knowledge-work factories**. Industrial and aviation research supplies useful human-factors lessons, but does not establish that a knowledge-work design is effective. Physical factories also need domain-specific safety engineering beyond this guide.

The research was inspected on **2026-09-28**. It is a targeted synthesis of foundational automation research, empirical human–AI research, governance frameworks, legislation, and agent security guidance, not a systematic literature review. The source table distinguishes their evidential roles. The working modes, allocation tables, and decision procedure below are **catalog recommendations**, not a scale prescribed or validated by those sources. They add no ontology fields or work-type values. The new controls are individually selectable proposals; adoption still requires an exact source revision.

## What the research supports

| Source and locator | Finding relevant to a factory | Implication and evidence limit |
|---|---|---|
| Parasuraman, Sheridan and Wickens, 2000, sections II–IV[^automation] | Automation can vary separately for acquiring information, analysing it, selecting decisions, and implementing actions. Human performance, reliability, and consequences inform allocation. | Split a workflow at these boundaries. This is a design model from automation research, not an LLM capability certification. |
| Bainbridge, 1983, sections 1.1 and 2.3[^ironies] | Automation can leave people with difficult exception handling while disuse erodes the skills needed to recover. | Budget practice and realistic recovery exercises. The paper identifies mechanisms and design problems; it supplies no universal staffing ratio. |
| Elish, 2019, introduction and conclusion[^crumple] | Responsibility may be concentrated on a nearby operator who had limited control over a distributed automated system. | Trace design, deployment, supervision, and incident decisions separately. These qualitative cases expose an accountability problem, not a rule assigning legal liability. |
| Vaccaro et al., 2024, abstract, results and limitations[^combinations] | Across 106 experiments reported in 74 papers, human–AI combinations performed worse on average than the better of human or AI alone; results differed by task. | Compare human, AI, and combined arrangements on the actual work. Studies covered January 2020–June 2023, with heterogeneous designs and possible publication bias; this does not establish the best arrangement for current agents. |
| NIST AI RMF 1.0, GOVERN 2–3, MAP 3.5, MEASURE 2, MANAGE 2.4 and 4.1[^rmf] | Defines differentiated responsibilities, assessment of oversight, and mechanisms for monitoring, override, deactivation, and recovery. | Carry ownership and evidence through the lifecycle. It is voluntary guidance; its outcomes are not a certification checklist. This guide uses version 1.0, whose resource page reports a revision in progress. |
| OECD AI Principles, accountability principle[^oecd] | Connects accountability to actor roles and context, with traceability and ongoing risk management across the lifecycle. | Keep the chain from grant through action to outcome inspectable. Principles do not determine a numeric autonomy threshold. |
| OECD Due Diligence Guidance, 2026, steps 2–6[^diligence] | Links impact assessment, prevention, tracking, communication, and appropriate remediation, including across business relationships. | Include affected people, suppliers, complaints, and remedy in the operating design. This is due-diligence guidance, not evidence that a particular control works. |
| EU AI Act, Articles 14(1)–(4) and 26(2)[^eu14][^eu26] | For covered high-risk systems, oversight design includes understanding limitations, avoiding overreliance, overriding, and stopping; deployers assign competent, trained people with authority and support. | Human oversight needs practical capability. These are scoped legal provisions, not a blanket requirement for human approval of every AI action. Determine classification, jurisdiction, applicable dates, amendments, and other obligations for each deployment. |
| Raji et al., 2020, auditing framework[^auditing] | Proposes internal auditing across development stages with connected documentation. | Retain decision evidence as work progresses. A completed audit record does not itself demonstrate acceptable outcomes. |
| OWASP LLM06:2025, prevention and mitigation[^agency] | Identifies excessive functionality, permissions, and autonomy as sources of harmful actions; recommends constrained tools and downstream enforcement. | Separate model reasoning from credential and grant enforcement. Security practice guidance does not assess business correctness or all human impacts. |

Taken together, these sources support asking **where human participation helps, what authority makes it meaningful, and what evidence justifies the allocation**. They do not establish a universally correct percentage of human involvement.

## Separate five questions

| Question | Local record | Example |
|---|---|---|
| What can the actor do? | Capability and demonstrated limits | A model can draft a refund explanation. |
| What may it do? | Authority grant, issuer, scope, limits, validity | A service may issue refunds only for eligible orders within a cap. |
| What can it choose independently? | Activity-specific autonomy and escalation | It chooses wording, but cannot invent an exception to eligibility. |
| What work must it perform? | Responsibility, inputs, outputs, handoffs | The review team checks disputed eligibility. |
| Who must explain and address the effects? | Accountable owner, resources, review and remedy route | The service owner investigates erroneous refunds and funds correction. |

For this guide, accountability means an obligation to answer for a decision and arrange correction within one's role. Record legal obligations separately; a local assignment does not settle liability or remove other actors' duties. An AI can execute work and produce evidence. Naming it as the sole accountable owner leaves the organizational obligations in this guide unmet. Give owners actual access, budget, stop authority, and escalation support.

Human-only work also needs authority, evidence, review, and recovery. Human discretion can be broad while technical permissions remain narrow. Conversely, an automated process may have powerful credentials but almost no permitted decision discretion. Neither arrangement is captured by counting AI-generated outputs.

## A sliding scale for interaction

Use these working modes to describe an **activity**, alongside its explicit grant. They are shorthand within this guide, not global catalog taxonomy or numerical risk scores.

| Mode | Allocation of work and decision | Human interaction | Required boundary to describe |
|---|---|---|---|
| Human execution | People gather, decide, and act; no AI participates | People perform the work and its review | Human authority, competence, and checks |
| AI assistance | AI retrieves, analyses, or drafts; person decides and acts | Review before a person uses or releases the result | Drafts cannot silently enter production or become binding decisions |
| Approval before execution | AI proposes a concrete action; authorized person approves it; automation executes | Approval bound to payload, resource, destination, and relevant context | Changes invalidate approval; timeout leaves the dependent action blocked |
| Supervised execution | AI decides and acts within a grant while a person can intervene | Monitoring and exception handling, sometimes a defined pre-action veto window | Demonstrated intervention time; no-response behavior explicitly granted |
| Bounded autonomous operation | AI completes a defined class of work without routine human intervention | People set limits, inspect samples and outcomes, handle appeals, and revise grants | Enforced scope, aggregate budgets, stop triggers, and recovery |
| Autonomous operation and adaptation | AI also chooses plans, coordinates actors, and changes permitted operating parameters | People govern purposes, protected constraints, and evidence requirements | Explicit adaptation envelope; no self-expansion of authority or weakening of acceptance |
| Fully AI governed endpoint | AI sets goals, permissions, acceptance, and its own governing rules, with no accountable human organization or intervention | None | A conceptual endpoint for discussion; unsupported for adoption by this guide's accountability controls |

“Purely AI driven” can mean fully automated **production** under accountable organizational governance. That fits bounded operation or adaptation. Removing human governance as well creates a different accountability question; this guide has no evidence-based method for making an unbounded, self-authorizing factory acceptable.

A research pipeline can autonomously retrieve approved sources, use AI assistance for uncertain analysis, require approval for publication, and autonomously stop on access failures. Give each part its own allocation. Record whether supervision occurs before an effect, during an interval when it can still be prevented, or only after the fact. An audit after publication cannot prevent the original disclosure.

## Allocate rights by action

For each row below name the **proposer, decision-maker, approver when required, executor, evaluator, accountable owner, stop authority, and appeal recipient**. One person may hold several roles where justified; consequential conflicts may require separation. Two agents with the same writable criteria, credentials, or blind spots do not demonstrate independent assurance.

These are starting recommendations. Local obligations and evidence can demand narrower permissions. A standing grant is sufficient for routine actions already within its scope; repeated confirmations are not an outcome measure.

| Action class | Reasonable starting allocation | Reserve or escalate | Evidence and accountable role |
|---|---|---|---|
| Set purpose, beneficiaries, prohibited uses, and risk tolerance | AI assists with options; organizational owner decides | Changes to whose interests count or acceptable harms | Approved objectives, affected-party input; factory owner |
| Intake, classify, prioritize, or reject work | Automate routine routing; sample results | Ambiguous scope, consequential rejection, systematically excluded cases | Routing errors and appeals; intake owner |
| Retrieve data and query tools | Bounded reads with purpose and destination limits | Sensitive access, new sources, cross-tenant data, query leakage to external providers | Access records and provenance; data owner |
| Analyse, forecast, advise, or draft | Assistance or bounded creation in a controlled workspace | Uncertainty that changes a consequential decision; unsupported claims | Source coverage and representative quality checks; domain owner |
| Plan tasks, allocate budgets, delegate | Autonomy within granted objective and shared aggregate limits | New objectives, destinations, actor types, or subdelegation rights | Parent/child grants and total effects; workflow owner |
| Evaluate and accept work | Automate objective checks; qualify evaluators | Subjective tradeoffs, disputed evidence, evaluator conflicts, high consequences | False acceptance and rejection tests; acceptance owner |
| Publish, send, deploy, transact, or sign | Exact approval initially; standing grants for demonstrated bounded cases | Irreversible effects, commitments, high exposure, changed payload or target | Boundary tests and destination effects; release or transaction owner |
| Decide outcomes affecting people | AI assistance with an authorized decision process | Rights, eligibility, contested facts, exceptions requiring judgment | Error distribution, reasons, accessible appeal; decision owner |
| Store memory, admit knowledge, delete records | Bounded routine retention under approved policy | New purposes, authoritative memory changes, irreversible deletion, legal holds | Provenance, retention and restoration evidence; information owner |
| Retry, contain, roll back, or compensate | Pre-authorize specific protective actions with budgets | Unknown prior effects, destructive recovery, compensation beyond limits | Actual destination state and recovery exercise; incident owner |
| Change model, tools, prompts, retrieval, or workflow | AI proposes and tests; separate change authorization | Changed assumptions, permissions, monitors, or evaluation criteria | Revision-bound comparison and rollback plan; change owner |
| Issue grants, waive controls, change policy, or retire the factory | Protected governance decision; automate its authorized execution | Self-approval, hidden exceptions, unresolved obligations | Grant changes, expiry, residual obligations; governance owner |

Inventory concrete verbs and side effects under these classes. “Research” can include paid queries or sending confidential search text; “draft” can trigger a shared-system notification. Local actions can alter later authority through memory, instructions, tests, or deployment configuration. A workflow label is insufficient evidence of low consequence.

## Allocate rights across the lifecycle

Distinguish the lifecycle of **the factory** from that of **each work item**. A design-time approval is not approval for every future output; a successful output is not approval to change the factory.

| Factory stage | Decision to record | Evidence and gate | Continuing owner |
|---|---|---|---|
| Purpose and feasibility | Whether the outcome warrants AI use; alternatives and exclusions | Human-only or conventional automation baseline, affected parties, obligations | Sponsor / factory owner |
| Design and procurement | Activity allocations, supplier duties, access, failure behavior | Decision-rights record, enforceability and supplier limitations | Design and procurement owners |
| Build and qualification | Whether the complete arrangement meets criteria | Representative cases, adversarial inputs, oversight and recovery drills | Engineering and assessment owners |
| Pilot and release | Exact scope, revision, destinations, exposure and trial end | Bounded grant, predeclared thresholds, monitored rollout | Deployment owner |
| Routine operation | Continue, route exceptions, remedy outcomes | Outcome samples, incidents, complaints, resource and workload data | Operations and domain owners |
| Change and expansion | Requalify affected claims and permit any larger scope | Old/new comparison, grant revision, rollback and retirement of old permissions | Change authority |
| Incident and recovery | Contain, investigate, restore, notify and compensate | Known effects, evidence preservation, tested restart conditions | Incident owner and accountable executive |
| Retirement | Stop new work and complete or transfer obligations | Revoke credentials and delegated grants; reconcile queued actions, retain required evidence, handle appeals | Named successor or closure owner |

For each work item, bind intake → planning → production → evaluation → external action → outcome follow-up to current grants and evidence. Recheck at crossings where consequences change. A human approver may authorize a complete bounded batch; the system must still enforce per-item eligibility and aggregate limits. Reconcile in-flight work after revocation instead of assuming cancellation undoes completed effects.

## Find the appropriate boundary

Run this procedure with domain, operations, security, and affected-party perspectives proportionate to the decision. Keep unresolved disagreements with the accountable decision-maker and the reason for proceeding or withholding the action.

1. **Define the action and outcome.** Specify exact resources, destinations, beneficiaries, inputs, and side effects. Split actions with different consequences. Map existing grants and obligations before considering greater autonomy.
2. **Describe credible failure scenarios.** Consider severity, reversibility, exposure and scale, uncertainty, adversarial input, dependencies, and who bears the harm. Include cumulative effects across agents and repeated small actions. Treat uncertainty as a reason to investigate or narrow scope, not as evidence of low risk.
3. **Apply hard constraints.** Prohibited actions, required authorized judgment, absent permission, unmanageable harms, or unenforceable boundaries rule out the dependent autonomous action. Faster production cannot compensate for a failed constraint. Keep harmless preparatory work available where authorized.
4. **Choose the control mechanism.** Prefer narrow resources, smaller batches, technical limits, independent checks, and recoverable intermediate states. Add human judgment where it can resolve context or value questions. Where people cannot intervene in time, use preventive restrictions, automatic containment, or a slower action boundary.
5. **Compare candidate arrangements.** Measure the existing human process, AI alone in a safe test setting, and the proposed combined process where feasible. Record when a comparison is infeasible. Include quality, severe errors, affected-group outcomes, delay, cost, review effort, and harm from inaction. Human-only work is a baseline to measure, not presumed perfection.
6. **Authorize a narrow trial.** State acceptance thresholds and exposure limits before seeing results. Identify an evaluator, owner, trial expiry, stop conditions, and fallback. Decide whether the evidence supports the specific grant; capability demonstrations alone do not issue it.
7. **Observe and revisit.** Inspect routine samples as well as escalations. Compare actual use with the granted scope. Review whether human participation helps, whether controls still operate, and whether the selected mode should remain, expand, contract, or end.

Use the following questions instead of averaging everything into an autonomy score:

| Dimension | Question that changes the allocation |
|---|---|
| Consequence | Could one mistake materially harm someone, disclose protected information, or create an unwanted commitment? |
| Reversibility | Can the actual effect be reversed within the necessary time, including copied information and downstream reliance? |
| Detectability | Who can notice the error, using evidence independent of the actor's own report? |
| Intervention | Can detection, notification, judgment and stopping finish before harm? |
| Novelty | Does this case differ from the evaluated population, language, tool behavior, or domain? |
| Scale and composition | What can repeated actions or cooperating actors do within the shared budget? |
| Human capacity | Does the reviewer have skill, evidence, available time, authority, and a manageable queue? |
| Governance and remedy | Who can challenge the outcome, obtain correction, revoke authority, and resource the response? |

## Make human participation effective

For a review boundary, supply the actual proposal, evidence, alternatives, uncertainty, destination, consequences, and the remaining time. Give the person a clear way to reject, edit, stop, or escalate. Preserve the reason and the action actually executed. Use [bounded external action](controls/bounded-external-action.md) to bind any action-specific approval.

Test review with plausible wrong proposals, missing evidence, and valid alternatives under realistic workload. Measure missed errors, unnecessary rejection, response times, queue age, and outcomes after override. Approval rate and number of clicks are weak evidence of oversight quality. Preserve occasional independent judgments before revealing the AI recommendation where appropriate to assess reliance.

For supervision, a useful design check is:

**detection time + notification time + human decision time + enforcement time < time available to prevent the effect.**

Use conservative measured values, relevant tail latency, and margin; averages alone hide slow cases. If a message leaves immediately, a person reading an alert minutes later cannot veto it. If supervisory coverage disappears, route to a preauthorized safe state. Silence only permits continuation when the standing grant explicitly allows that behavior; it never supplies a missing approval.

Maintain practice for tasks people must take over. Test handoff with a summary of current state, completed effects, pending actions, uncertainty, and available recovery options. A manual fallback that staff cannot perform is an unimplemented fallback. Periodic audit may suffice for a bounded low-consequence action even when real-time supervision adds little value.

## Evolve autonomy with evidence

Use [autonomy change gates](controls/autonomy-change-gates.md) to make changes explicit. A useful sequence is offline comparison → shadow operation without effects → bounded pilot → routine operation. Shadow results cannot prove execution, recovery, or real operator behavior; test those separately. Stages may be combined when justified, and a successful trial may correctly end with no expansion.

Define the evidence package for each proposed change:

- Exact model, tools, prompts, data/retrieval, workflow, grant, and enforcement revisions; known supplier changes or unknown version details.
- Action population, exclusions, case mix, observation window, sample size, and relevant baseline.
- Artifact quality and beneficiary outcomes; severity-specific failures and subgroup results where relevant; uncertainty and unobserved harms.
- Review performance, intervention latency, unauthorized attempts, bypass tests, aggregate consumption, and exercised recovery.
- Decision-maker, accepted residual risk, scope and duration of the resulting grant, and explicit conditions for reducing or stopping it.

Do not promote based on an uneventful calendar interval or a single accuracy average. Successful easy cases say little about rare severe failures. Select sample sizes and statistical methods for the tolerated failure rate and dependence between observations. Repeated cases from the same template or incident may provide much less evidence than their count suggests. No universal accuracy percentage justifies every delegation.

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

## Document this in an OKF bundle

Keep reusable requirements in the [decision rights](controls/decision-rights-and-accountability.md) and [autonomy change](controls/autonomy-change-gates.md) controls. Keep local thresholds, actors, grants, and evidence in the factory's implementation and assessment records. Use the existing ontology's embedded objects; no shared registry or new schema is required.

For each activity, copy this record structure and fill every relevant cell. Placeholders and unresolved decisions are not grants.

| Record section | Contents to record |
|---|---|
| Identity and context | Factory/activity, revision, intended outcome, work types, data, users, destinations, exclusions |
| Rights and responsibility | Proposer, decider, approver, executor, evaluator, accountable owner, stop authority, appeal owner |
| Allocation rationale | Working mode for each sub-action, credible failures, constraints, alternatives considered, residual risk |
| Grant | Issuer, actor, action, resources/destinations, per-action and aggregate limits, delegation, start/expiry, revocation, approval conditions |
| Oversight | Evidence visible to reviewers, competence and staffing, timing, queue limits, no-response and handoff behavior |
| Change and recovery | Protected policy and criteria, authorized adaptation, promotion/demotion triggers, safe state, restart authority |
| Assessment | Target revision, evaluator, method, predeclared criteria, observation period, evidence, result and limits |
| Adoption and follow-up | Exact control commit/version/URL, local adaptations, next review, unresolved gaps, remedy obligations |

Use [evidence traceability](controls/evidence-traceability.md) for claims and [outcome verification](controls/outcome-verification.md) for beneficiary results. Preserve source IDs and matching footnotes for research claims. An OKF `verified` event concerns document verification; it is neither runtime authorization nor a passed operational assessment. Record actual grants and test results separately.

The [support resolution example](factories/support-resolution.md) shows one factory moving through different allocations without changing accountability or granting itself broader authority. Discuss the initial action boundaries, evidence sufficiency, and retained human decisions with the adopting organization before deployment. Those remain local decisions; this guide supplies a method for making them reviewable.

[^automation]: [Parasuraman, Sheridan and Wickens (2000)](https://www.researchgate.net/publication/11596569_A_model_for_types_and_levels_of_human_interaction_with_automation), IEEE Transactions on Systems, Man, and Cybernetics—Part A 30(3), 286–297, DOI 10.1109/3468.844354; author-uploaded full text inspected.
[^ironies]: [Bainbridge (1983)](https://tc.ifac-control.org/4/1/newsletter/ironies-of-automation/@@download/file/Bainbridge1983_Automatica_Ironies%20of%20automation.pdf), Automatica 19(6), 775–779; IFAC-hosted paper.
[^crumple]: [Elish (2019)](https://estsjournal.org/index.php/ests/article/view/260), Engaging Science, Technology, and Society 5, 40–60; journal article and full text.
[^combinations]: [Vaccaro, Almaatouq and Malone (2024)](https://www.nature.com/articles/s41562-024-02024-1), Nature Human Behaviour 8, 2293–2303.
[^rmf]: [NIST AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), specified subcategories; official HTML reproduction.
[^oecd]: [OECD AI Principles](https://www.oecd.org/en/topics/ai-principles.html), accountability principle, revised 2024.
[^diligence]: [OECD Due Diligence Guidance for Responsible AI (2026)](https://www.oecd.org/en/publications/oecd-due-diligence-guidance-for-responsible-ai_41671712-en/full-report/component-4.html), practical framework, particularly step 6 on remediation.
[^eu14]: [EU AI Act Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14), paragraphs 1–4 of the reproduced enacted text; applicability must be established for the deployment.
[^eu26]: [EU AI Act Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26), paragraph 2 of the reproduced enacted text.
[^auditing]: [Raji et al. (2020)](https://arxiv.org/html/2001.00973v1), framework for internal algorithmic auditing, accepted at ACM FAT* 2020.
[^agency]: [OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), prevention and mitigation strategies.
