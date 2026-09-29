---
type: Factory Example
title: "Support resolution with evolving autonomy"
description: "A fictional support factory assigns action-specific rights and expands or reduces refund autonomy using explicit evidence gates."
status: draft
example: true
domain: "Customer support for a digital subscription service"
activities: ["diagnose a support case", "prepare a response", "authorize the remedy", "verify case resolution"]
control_selections:
  - control: ../controls/decision-rights-and-accountability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../controls/autonomy-change-gates.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/bounded-external-action.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/evidence-traceability.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
  - control: ../../../catalog/controls/outcome-verification.md
    applicability: applicable
    implementation_state: proposed
    assessment_result: not-assessed
sources:
  - id: allocation
    resource: ../human-ai-authority.md
    title: "Allocate human and AI authority across a factory"
---

# Example: support resolution with evolving autonomy

[Allocation guide](../human-ai-authority.md) · [Adoption](../../../catalog/adoption.md) · [Factory examples](./)

**Fictional design; all implementations proposed and not assessed.** Roles, amounts, sample sizes, and deadlines below are invented local choices for discussion. They are not universal safe thresholds or results of an experiment.[^allocation]

## Factory profile

Resolve eligible duplicate charges accurately, explain the resolution, and provide a route to challenge errors. The support director is accountable for the service and resources correction; the payments owner controls refund grants. The security owner administers credentials, and a separate change reviewer assesses expansions. Duty rosters resolve each role to a person. Customers supply case details; authorized billing records supply transaction evidence. Outputs are a case record, proposed or executed refund, customer response, and outcome evidence.

The proposed outcome measure is correct resolution within two working days for at least 95% of eligible pilot cases, with no known unauthorized refund or cross-account disclosure. Inspect unresolved and reopened cases over a 30-day follow-up period; a closed ticket alone does not establish resolution. Unknown outcomes remain unverified. Severe failures trigger containment regardless of the aggregate percentage. These criteria need local validation before adoption.

## Rights by action

| Activity | Proposed initial mode and actors | Boundary / accountable owner |
|---|---|---|
| Define eligibility, exclusions, and appeal policy | AI may assist; support director and payments owner decide within organizational authority | Agent cannot alter policy; director owns policy effects |
| Retrieve billing facts | Agent reads only the authenticated customer's relevant records | Data boundary enforces account scope; data owner handles access defects |
| Draft response and proposed refund | Agent analyses and drafts within case scope | No sending or payment effect; support director owns review quality |
| Approve an individual refund | Qualified payments reviewer decides using billing evidence | Approval bound to transaction, amount, account, and proposal revision; payments owner accountable |
| Execute approved refund | Payment service validates approval and executes | One operation identity; uncertain result requires reconciliation before retry |
| Send customer explanation | Support reviewer approves exact message, then service sends | Correct account and destination; sending is a separate grant |
| Review a disputed decision | Authorized support reviewer can overturn or escalate | Customer gets an accessible appeal route; director resources remedy |
| Freeze automated refunds | Monitor or on-call operator acts under a protective standing grant | Independent stop path; payments owner owns reconciliation and restart |
| Change grants, criteria, or model | Agent proposes; protected change authority decides | Execution actor cannot approve its own expansion |

The agent may read and draft without repeated permission inside existing grants. Approval of a refund does not authorize a different message or policy change. Other factories may validly combine these permissions in an explicit grant.

## Proposed evolution

| Stage | Scope | Gate and retained human decision |
|---|---|---|
| Human baseline | Staff diagnose, decide, pay, and communicate | Measure incorrect decisions, response time, rework, and customer outcomes; human operation is not assumed flawless |
| Assistance | Agent drafts; staff decide and act | Compare against baseline using representative cases and qualified reviewers |
| Approval before execution | Agent proposes, staff approve exact action, service executes | Boundary, approval binding, duplicate prevention, and reviewer-capacity tests |
| Shadow proposal for autonomous refunds | Agent recommends actions without affecting accounts | Compare eligibility and amounts with independently adjudicated records; shadow accuracy leaves execution behavior untested |
| Bounded pilot | Only exact duplicate charges in a defined product and jurisdiction; up to USD 25 per case and USD 250 total per day across all agents; at most 100 live cases over 14 days, whichever ends first | Separate pilot grant; exclude disputes, fraud indicators, mixed currencies, ambiguous records, and new account types; people handle exceptions and appeals |
| Routine bounded operation | Possible continuation of the pilot scope with a fresh validity period | Review complete results and 30-day outcomes; continuation is not automatic; larger amounts or populations need a separate proposal |
| Permitted adaptation | Agent changes routing priority only inside approved queue and fairness constraints | Refund eligibility, budgets, credentials, acceptance criteria, and monitors remain protected |

The pilot should include fixture tests for every listed exclusion and at least 20 deliberately invalid proposals, all of which must be blocked. Require zero unauthorized effects in those tests, valid eligible cases to execute correctly, and outcome criteria to be met before considering routine operation. The 100-case cap limits exposure; it is insufficient to establish a very low rate of rare harms. Report sample limitations and obtain the payments owner's explicit residual-risk decision. A pending follow-up period leaves the promotion gate incomplete.

Pilot grants expire at their case or time limit. During outcome follow-up, refunds return to the qualified approval mode. The payments service reserves budget atomically across concurrent actors so individually valid requests cannot exceed the shared cap. Child grants can only narrow the parent's scope and share its budget. No live grant is created by this example.

## Oversight, containment, and recovery

Payments take effect too quickly for an after-the-fact alert to prevent them. Prevention relies on eligibility, grant, approval, and budget checks at execution. Human audit supplies detection and correction. For approval-mode work, expired approvals or reviewer absence keep the payment blocked; queue overload routes cases to the support lead without silently granting autonomy.

Proposed suspension triggers are any unauthorized payment or cross-account disclosure, missing required transaction telemetry, budget inconsistency, unqualified model/tool change, or grant expiry. The payment gateway blocks new autonomous requests immediately upon detecting the trigger; test a maximum five-second revocation propagation time on other paths. The consequence analysis must determine whether this delay is acceptable before a pilot. A revocation does not reverse an already settled payment.

The on-call operator inventories pending and completed transactions from the authoritative payment system, preserves evidence, and assigns customer correction. An ambiguous timeout never triggers an unexamined second refund. If destination state remains unknown, automated retries stay blocked. The incident owner can arrange a human path for urgent cases within separate grants. Restart requires corrected cause, affected checks rerun, reconciled effects, and the payments owner's authorization through the protected change process.

## Controls and assessment plan

All five selections are applicable, proposed, and not assessed. Before use, retain each control's identity, catalog version from the adopted revision, full published source commit, pinned URL, scope, owner, and adaptations as specified in [adoption](../../../catalog/adoption.md#record-the-adoption). Resolve cross-control references against the same revision.

| Selected control / local owner | Evidence to produce |
|---|---|
| [Decision rights and accountability](../controls/decision-rights-and-accountability.md) / support director | Complete rights record; plausible wrong and valid proposals; absent reviewer, overloaded queue, handoff, stop and appeal exercises |
| [Autonomy change gates](../controls/autonomy-change-gates.md) / change authority | Old/new scope, predeclared criteria, baseline and representative cases; rejected self-expansion, wrong-revision evidence, telemetry loss, expiry and premature restart fixtures |
| [Bounded external action](../../../catalog/controls/bounded-external-action.md) / payments owner | Every positive and negative grant case, changed approval payload, alternate/delegated path, concurrent budget and revocation tests; observed payment effects |
| [Evidence traceability](../../../catalog/controls/evidence-traceability.md) / assessment owner | Claims tied to policy, billing facts, grant, model/tool and candidate revisions; fabricated, contradictory, and missing-evidence fixtures |
| [Outcome verification](../../../catalog/controls/outcome-verification.md) / support director | Separate artifact, payment and customer-resolution observations; met, unmet and missing-outcome cases with follow-up |

Run each control's full assessment; the examples in the table do not replace its complete criteria. Store sanitized records with appropriate access and retention, preserving the ability to investigate complaints. A passing catalog validator proves neither successful refunds nor effective oversight.

## Remaining decisions and gaps

Before deployment, the organization must justify eligibility rules, jurisdictions, amounts, capacity, latency, statistical evidence, retention, and customer remedy. It also needs implemented privacy protection, identity verification, fraud defenses, payment idempotency, supplier management, and incident communication. The selected controls do not provide a complete payment compliance or security program.

On retirement, revoke all delegated grants, stop new intake, settle or transfer open cases, preserve required evidence, and leave an identified owner for appeals and corrections. Automation ending does not erase those obligations.

[^allocation]: [Research synthesis and recommended allocation method](../human-ai-authority.md); this example illustrates the method and adds no empirical effectiveness claim.
