---
type: Guide
title: "Assess semantic answer caches"
description: "Test whether cached AI answers remain authorized, current, and equivalent for the requesting task."
status: draft
tags: [retrieval, cache, privacy, assessment]
sources:
  - id: redis-cache
    resource: https://redis.io/blog/what-is-semantic-caching/
    title: "What is semantic caching? Guide to faster, smarter LLM apps"
    author: human:jim-allen-wallace
  - id: platform-cache
    resource: https://huyenchip.com/2024/07/25/genai-platform.html
    title: "Building A Generative AI Platform"
    author: human:chip-huyen
---

# Assess semantic answer caches

[Retrieval poisoning](../risks/retrieval-poisoning.md) · [Adoption](../adoption.md)

## Purpose and applicability

Use when an application reuses a previously generated answer for an identical or similar query. Redis's current article describes semantic lookup that can reuse stored responses for similar queries; Huyen's 2024 architecture post distinguishes semantic caching from prompt and exact caching and describes failure risks in the matching path.[^redis-cache][^platform-cache] These descriptions motivate the proposed assessment below; they do not establish the effectiveness of a particular cache or this assessment. Savings and accuracy claims need local evidence.

This guide applies [approved data processing](../controls/approved-data-processing.md), [retrieval corpus integrity](../controls/retrieval-corpus-integrity.md), [data lineage impact](../controls/data-lineage-impact.md), and [persistent state recovery](../controls/persistent-state-recovery.md). The catalog already covers stale or poisoned cached material. The added procedure focuses on deciding whether two requests may safely share an answer.

Distinguish an **answer cache**, which reuses output, from provider prompt/prefix caching, which can reuse computation while still generating a new answer. Identify which mechanism is actually in scope before applying these cases.

## Record the reuse contract

| Area | Record |
|---|---|
| Owner and scope | Cache owner, eligible task classes, authorized writers, users/tenants, and prohibited reuse classes |
| Identity and authorization | Principal, tenant, data-access scope, policy revision, and where current permissions are enforced |
| Meaning | Entities, time period, units, jurisdiction or locale where relevant, conversation state, and other answer-changing constraints |
| Provenance | Answer revision, underlying source identifiers and revisions, generation configuration, and validation evidence |
| Matching | Exact or semantic match, embedding/matcher version, threshold, filters, and tested false-hit cases |
| Freshness | Expiry policy, source/policy change signals, revocation and deletion path, and maximum permitted propagation delay |
| Recovery and measurement | Bypass behavior, invalidation ownership, cost/latency accounting, and protected audit evidence |

Do not store raw credentials in cache keys or telemetry. A stored permission label must not replace current authorization. Where enforcement cannot isolate users or tenants, disable reuse for that sensitive scope until a suitable boundary is established.

## Procedure

1. **Select eligible tasks.** Begin with stable, authorized content whose answer-changing inputs are known. Exclude decisions requiring current individualized state when that state cannot be included and revalidated. Caching must not bypass [bounded external action](../controls/bounded-external-action.md) for actions or commitments.
2. **Define equivalence before similarity.** State which changes make the prior answer invalid. Similar wording can refer to another customer, date, unit, product version, or instruction. Apply authorization and exact constraint filters at the retrieval/enforcement boundary; use semantic similarity only within eligible candidates. Recheck the result before serving it.
3. **Preserve dependencies.** Bind the cached answer to source, policy, and relevant generation revisions. Trace edits, withdrawals, corrections, permission changes, and deletion requirements into invalidation. Choose expiry and invalidation delays from the task's obligations. Expiry alone cannot satisfy an immediate revocation requirement.
4. **Handle concurrent change.** Exercise source withdrawal or permission revocation while a hit is in flight and while a stale writer attempts to repopulate the cache. Use a generation/version check or another enforceable mechanism to prevent disallowed reuse. Record the actual mechanism and its limits.
5. **Qualify matching.** Build independently labeled valid paraphrases and deceptive near matches. Test both false hits and missed valid hits with the actual matcher and corpus. Choose thresholds from local evidence; a vendor example threshold is not a universal setting.
6. **Compare with a bypassed cache.** Use the same task set and quality floor. Count cache lookup/embedding cost, refresh work, invalidations, failed attempts, and human repair. Report useful accepted hits separately from gross hit rate. Apply [measurement basis validation](../controls/measurement-basis-validation.md) to savings claims.
7. **Recover on uncertainty.** Bypass the cache or withhold the affected answer when permission, source state, or equivalence is unresolved. A bypass still follows normal tool/provider grants and execution budgets. Reassess after changes to the matcher, corpus, policies, or eligible task classes.

## Assessment design

Use synthetic users and documents in an authorized isolated test environment. The fixtures are proposed; no cache implementation was executed in this research.

| Fixture | Expected observation |
|---|---|
| A valid paraphrase with the same authorized scope and current sources | The correct cached answer can be used and its provenance is retained. |
| Nearly identical questions from users with different entitlements | Protected output is never served outside its current authorized scope. |
| A changed date, account identifier, unit, or negation | The prior answer is rejected unless the reuse contract establishes actual equivalence. |
| A previously valid source is corrected or withdrawn | Affected answers stop being served within the declared bound and required correction/deletion behavior is observed. |
| Permission is revoked between lookup and response | Enforcement prevents prohibited disclosure, including concurrent requests. |
| A stale writer repopulates an invalidated entry | Version or equivalent enforcement prevents the stale answer from becoming eligible. |
| A poisoned answer has derived cache copies | Recovery removes or quarantines all in-scope copies and tests for reinsertion. |
| Cache hit rate improves while factual quality falls | The quality floor blocks acceptance; the report cannot call the change a successful optimization. |
| A cache is unavailable | Bypass or a scoped stop follows the defined budgets and permissions. |

**Pass:** authorized positive cases work, prohibited reuse is prevented, invalidation meets its obligations, and quality and accounting evidence support the declared claim. **Fail:** any mandatory boundary is violated, a known stale answer is treated as current, or a quality loss is hidden by hit rate. **Inconclusive:** relevant state or effects cannot be observed well enough to decide.

Retain fixture labels, users and grants, source/policy revisions, match decisions, invalidation timing, concurrent-writer observations, protected output checks, cost totals, and the owner's disposition. Avoid copying sensitive answers into widely shared logs.

## Limits and adoption

The reuse contract and fixtures are catalog interpretations, not vendor requirements or proven mitigations. Matching tests cannot establish all future semantic equivalences. Invalidation depends on complete lineage and functioning enforcement; document inaccessible stores and untested paths. Reuse the broader [corpus integrity](../controls/retrieval-corpus-integrity.md) and [state recovery](../controls/persistent-state-recovery.md) assessments for those dependencies.

Retain linked control identities, catalog version from the adopted revision, and exact source commit URLs under the [adoption procedure](../adoption.md#record-the-adoption). No product-specific threshold or implementation is prescribed.

[^redis-cache]: [Jim Allen Wallace, Redis: What is semantic caching? Guide to faster, smarter LLM apps](https://redis.io/blog/what-is-semantic-caching/). The page displays January 20, 2026 as its date; accessed 2026-09-29 UTC. No immutable revision or verified last-modified date was identified. This is a vendor-authored page; its performance claims are not evidence for this guide's proposed assessment.
[^platform-cache]: [Chip Huyen: Building A Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html). The page displays July 25, 2024; accessed 2026-09-29 UTC. No immutable revision or verified last-modified date was identified.
