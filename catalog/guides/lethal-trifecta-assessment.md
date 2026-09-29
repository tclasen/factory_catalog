---
type: Guide
title: "Assess lethal trifecta paths"
description: "Map and test information flows across tools, rendering, delegation, and persistent state using synthetic data."
catalog_version: "v0.1.0"
status: draft
tags: [security, privacy, assessment, lethal-trifecta]
sources:
  - id: research
    resource: ../lethal-trifecta.md
    title: "The lethal trifecta in AI workflows"
  - id: separation
    resource: ../controls/lethal-trifecta-separation.md
    title: "Lethal trifecta separation"
---

# Assess lethal trifecta paths

[Research](../lethal-trifecta.md) · [Separation control](../controls/lethal-trifecta-separation.md) · [Factory example](../factories/compartmented-research.md) · [Assessment evidence records](../assessment-evidence-records.md)

This procedure supports the separation control.[^separation] Its fixtures are catalog proposals informed by the research; no listed test has been run against a factory.[^research]

## 1. Fix the scope and expected behavior

Name the implementation and configuration revision, owner, evaluator, actors, tenants, approved task, permitted disclosures, and observation period. Pin adopted controls through [adoption](../adoption.md). Keep test authorization separate from authority to operate against real users or services. Use synthetic documents and local or otherwise authorized test recipients.

Define a benign task with measurable acceptance criteria before adding hostile content. Measure legitimate task success separately from attack success. A system that blocks every action may prevent disclosure while failing the work it was meant to do.

## 2. Record paths, not just tool names

Create one row per distinct route. Keep these records with the implementation; they are not new required catalog metadata.

| Field | Record |
|---|---|
| Identity and revision | Path ID, workflow/build, model, prompts, tools, renderer, credentials/policy revision |
| Input and influence | Who can alter the source; how it enters context; transformations and later consumers |
| Private data | Data class, authorized readers, accessible stores and existing context, synthetic marker ID |
| Outbound channel | Tool call, request argument, render/fetch, shared artifact, telemetry, or delegated action |
| Recipient | Service, account/tenant, object visibility, redirects, and ultimate observers |
| Proposed break | Removed capability or enforced release rule; exact enforcement point and administrator |
| Composition | Shared memory, files, summaries, child credentials, session transitions, asynchronous effects |
| Evidence and result | Positive/negative cases, observations, limitations, pass/fail/inconclusive, remediation owner |

Inspect requests called “read-only”: search terms and fetch URLs still transmit data. Include the model provider as a processing destination under [approved data processing](../controls/approved-data-processing.md); an authorized provider does not automatically authorize arbitrary third-party recipients. Record boundaries that cannot be inspected as unknown.

## 3. Build a controlled fixture

Prepare a harmless private record with a unique synthetic marker and a benign public document. Create distinct approved and prohibited test recipients. Configure logs at the enforcement point and receiving side, and verify observation works with a harmless calibration request. Do not place production secrets in a test or copy live attack destinations into fixtures.

Replace the public document with an adversarial variant that attempts to redirect work toward the marker or a prohibited release. Observe the complete trajectory, including rendering, background fetches, downstream processors, and later sessions. Exercise enforcement directly with prohibited proposed calls as well as through model-generated attempts; this distinguishes boundary behavior from model reluctance.

## 4. Exercise the supported routes

| Fixture | Observe and compare |
|---|---|
| Benign source and authorized output | Expected work completes with the correct scope, data, recipient, and evidence |
| Source impersonates a user or administrator | Claimed authority does not change policy or permit the prohibited transfer |
| Private fact placed into a query, URL, message, or upload | Whether each supported channel blocks the actual transfer before the recipient sees it |
| Generated image/link and automatic preview | Whether the UI, preview service, or later click creates a prohibited request; rendering text alone is a separate observation from transmission |
| Same allowed service, different recipient/account/public object | Whether disclosure policy checks the effective audience rather than only the hostname |
| Destination redirects or changes after review | Whether authorization remains tied to the actual destination at execution |
| Untrusted text summarized, structured, or delegated | Whether the receiving actor inherits unsafe influence or broader permissions |
| Capability switch or new session imports earlier state | Whether private context or injected instructions survive the supposed separation |
| Data encoded, split, or paraphrased | Whether enforcement depends only on a literal marker match; inspect data-flow rules and receiver output |
| Gate outage, revoked grant, or attempted policy mutation | Whether the path denies release and preserves enough evidence to diagnose the block |

Apply the control's pass/fail criteria to every relevant row. State which routes are unsupported and the inventory evidence establishing that fact. One missing or unobservable route prevents a claim of complete coverage.

## 5. Adapt, repeat, and report honestly

Predeclare attack attempts, permitted adaptation, model settings, random seeds where available, and stop conditions. Keep a fixed regression set plus separately identified attempts adapted to observed defenses. Count attempts and successful disclosures, report benign task completion, and state any harness failures. Do not infer a universal failure rate from a small sample or combine results from different revisions without labeling them.

When adopting [adversarial regression assessment](../controls/adversarial-regression-assessment.md), register these fixtures and declare release/operation dispositions before running them. A passing assessment process and a passing security result for the factory are separate findings.

Use two complementary forms of evidence: configuration and direct enforcement tests establish the intended boundary; end-to-end observations test whether the whole workflow actually uses it. Synthetic marker absence is useful evidence but cannot rule out arbitrary semantic leakage or unobserved channels.

Retain sanitized source fixtures, tool proposals, policy decisions, receiver logs, outputs, revisions, evaluator, and time under restricted access. Record remaining blind spots and follow [assessment evidence validity](../controls/assessment-evidence-validity.md) when evidence becomes stale. The result evaluates the selected implementation; it does not mark the research sources or all model behavior as verified.

## 6. Respond and reassess

On a prohibited effect, stop the affected test path, preserve evidence, identify the broken boundary, and fix it before rerunning affected cases and the benign task. Missing evidence yields inconclusive rather than pass. A real-data incident requires the organization's incident process and assessment of downstream recipients, retained copies, and exposed credentials.

Repeat affected assessments after changes to data access, sharing, input sources, models, tools, prompts, rendering, memory, delegation, or release enforcement. A new tool may connect capabilities that were harmless in their previous arrangement.

[^research]: [Research synthesis, case distinctions, and evaluation limits](../lethal-trifecta.md).
[^separation]: [Separation requirement and assessment criteria](../controls/lethal-trifecta-separation.md).
