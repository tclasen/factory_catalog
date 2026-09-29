---
type: Guide
title: "Lessons from semantic_search"
description: "Apply revision-bound evidence, scoped evaluation, and recoverable knowledge updates to a factory."
status: stable
sources:
  - id: execution
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/process/execution.md
    title: "Execution and recovery protocol"
  - id: verification
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/process/verification.md
    title: "Verification strategy"
  - id: readiness
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/verification/factory-readiness.md
    title: "Integrated factory and product readiness"
  - id: evaluation
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/product/search-evaluation.md
    title: "Search evaluation specification"
  - id: publication
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/adr/0004-local-storage-and-revision-publication.md
    title: "Revision publication decision"
  - id: reporter
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/scripts/publish_local_acceptance.py
    title: "Local acceptance publisher"
  - id: reporter-tests
    resource: https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/tests/unit/test_publish_local_acceptance.py
    title: "Acceptance publisher unit tests"
---

# Lessons from semantic_search

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Catalog](../../catalog/index.md) · [Ontology](../../catalog/ontology.md) · [Adoption](../../catalog/adoption.md)

## Source and scope

This guide derives reusable practices from `tclasen/semantic_search` at commit
`0f2c6eead19e01108f97142ce1ded9f32b7a8bcc`, inspected on 2026-09-28. The source builds a video search application with an RDF knowledge graph and records its development and evaluation procedures. Its readiness document distinguishes delivered narrow pilots from an unfinished full product release.[^readiness]

The lessons below are adaptations of documented procedures and inspected code, not a report that the source factory or these practices passed an operational assessment. The publisher and its tests were read, not executed; its unit tests stub remote effects and evidence verification.[^reporter-tests] Source policies and project-specific approvals do not transfer authority to catalog adopters.

## 1. Bind evidence to the inputs that produced it

The execution protocol ties evidence to the artifact or tree, requirements, dependencies, configuration, fixtures, tools, and environment. It calls for reassessing affected evidence after changes and documenting why unaffected results can be reused.[^execution] The acceptance publisher checks the current committed revision, complete expected command inventory, successful results, and evidence validity; it rechecks the candidate after reading remote state.[^reporter]

**Apply:** extend the local assessment record with those input identities and a reason for any reuse. When uncommitted work is assessed, retain its tree or patch digest. Recheck at the decision that consumes the evidence. This specializes [evidence traceability](../../catalog/controls/evidence-traceability.md) and the ontology's revision-scoped [Assessment](../../catalog/ontology.md#concepts).

**Check:** change a relevant fixture or configuration after a passing run and confirm the affected acceptance is withheld. An unchanged, fully evidenced candidate should remain eligible. Retain both observations and the invalidation rationale. A revision check alone does not prove the evidence is authentic or eliminate every race.

## 2. Make missing coverage visible

The verification strategy maps acceptance criteria to checks in both directions and preserves failures, blocked cases, and omissions. Its readiness map gathers workflow assurance during actual product development; historical synthetic factory fixtures do not qualify product behavior.[^verification][^readiness]

**Apply:** list every required criterion, its check, target revision, observation, and remaining gap. Report covered versus required cases. Separate document readiness, implementation, installed behavior, and beneficiary outcomes using [outcome verification](../../catalog/controls/outcome-verification.md). An unavailable prerequisite should block only the dependent action or claim.

**Check:** omit one required case and verify the report cannot present full acceptance. Confirm that a document-only pass and a synthetic pilot remain explicitly limited. Keep this catalog's existing assessment states; describe an unrun or blocked check and its resume condition in the evidence record without inventing a new passing state.

## 3. Pair rejection tests with a permitted success case

The source requires positive controls alongside security and recovery denials so a system that rejects everything cannot pass. The publisher tests include both a complete-report publication path and rejections for incomplete, stale, dirty, or mismatched inputs.[^verification][^reporter-tests]

**Apply:** for each acceptance boundary, test a valid case and representative invalid cases; observe the resulting effects. This reinforces the positive and negative cases already required by [bounded external action](../../catalog/controls/bounded-external-action.md).

**Check:** an authorized matching request succeeds, while a missing grant or changed destination produces no external effect. A stub can assess decision logic; an end-to-end claim needs the real enforcement boundary in an isolated authorized environment. Record that distinction in the assessment.

## 4. Reconcile uncertain effects before retrying

The execution protocol requires inspection of actual state after an ambiguous commit, push, or deployment response. Ownership expiry alone does not authorize a new writer: prior writers must stop or be prevented from writing, and state must be reconciled. Attempt and resource limits survive handoffs.[^execution] The publisher makes no automatic retry after its status POST; its lost-response test expects exactly one attempt.[^reporter][^reporter-tests]

**Apply:** retain the logical operation ID, destination, intended revision, observed effects, current owner, attempts used, and resume condition. Inspect destination state before retrying a mutation. Tie the action to [bounded external action](../../catalog/controls/bounded-external-action.md), but record duplicate prevention, ownership enforcement, and recovery as additional mechanisms; that control does not establish them.

**Check:** simulate a successful mutation with a lost response, then resume. Verify one intended effect, preserved attempt accounting, and no publication by an obsolete owner. Use an isolated fixture with an observable destination; a checkpoint document alone cannot enforce ownership.

## 5. Evaluate extraction and retrieval separately

The search evaluation protocol compares retrieval on a reviewed reference graph with retrieval on extracted data. It groups related clips and paraphrases in the same source-level split, separates pilot tuning from held-out acceptance, and freezes thresholds before acceptance testing.[^evaluation]

**Apply:** for a knowledge factory, evaluate source-to-claim extraction separately from finding and using those claims. Compare against a fixed baseline on identical judged inputs. Include difficult negatives, missing modalities, unknown entities, and unsupported cases. Record the intended population and limits of a small pilot. This makes [outcome verification](../../catalog/controls/outcome-verification.md) useful for retrieval and synthesis work.

**Check:** an incorrect extracted fact must remain an extraction failure even when search retrieves it correctly. Report failures by stage and data stratum. Keep related source material out of opposing development and acceptance splits; once held-out cases inform tuning, obtain a fresh acceptance set before claiming generalization.

## 6. Preserve uncertainty instead of turning it into truth

The protocol distinguishes supported, contradicted, ambiguous, and unjudged labels. Model agreement is not independent ground truth, and missing annotations do not establish negative labels. It separates correct abstention from retrieval scores and reports excluded or provisional judgments.[^evaluation]

**Apply:** carry claim status, source revision, method, reviewer, and correction history through extraction, retrieval, and presentation. Require evidence for graph relationships as well as entities. Use [evidence traceability](../../catalog/controls/evidence-traceability.md) to expose unsupported joins and [outcome verification](../../catalog/controls/outcome-verification.md) to assess usefulness alongside abstention.

**Check:** supply an unjudged item, contradictory evidence, and a query with no reviewed match. Confirm uncertainty remains visible, unknown cases do not silently count as successes or errors, and refusing all queries cannot satisfy the usefulness criterion. The source's label states describe evidence; they do not replace catalog assessment results.

## 7. Preserve corrections through publication and recovery

The revision-publication decision stages and validates immutable revisions before publishing active references. Queries capture revision IDs; user corrections persist independently of disposable indexes. It explicitly leaves crash consistency and scale unverified, and a later decision supersedes its media-storage choice.[^publication]

**Apply:** identify authoritative sources and corrections separately from rebuildable views. Keep one result tied to a consistent revision, surface missing referenced data as an error, and preserve correction history during rebuild or restore. These are candidate mechanisms in the [knowledge and evidence, change and dependencies, and reliability and recovery families](../../catalog/control-families.md#families), not a mandate to adopt SQLite, RDF, or the source's architecture.

**Check:** interrupt publication before and after activation, rebuild after a correction, and restore a backup. Observe whether results mix revisions, corrections disappear, or missing data becomes an apparently valid empty answer. Retain source and correction digests and observed recovery results; a successful process restart is insufficient evidence.

## Use and remaining decisions

Select the relevant lessons for an activity, name its owner, record the local mechanism and acceptance criteria, and retain the resulting evidence. When adopting existing controls, preserve their identities, catalog version, and exact pinned catalog URLs under the [adoption procedure](../../catalog/adoption.md#record-the-adoption). Links in this guide express applicability and derivation, not adoption or a passing assessment.

Apply the existing [assessment evidence validity](../../catalog/controls/assessment-evidence-validity.md), [reconcile before retry](../../catalog/controls/reconcile-before-retry.md), [independent restoration](../proposals/controls/independent-restoration.md), and [data-preserving migration](../../catalog/controls/data-preserving-migration.md) controls for evidence reuse, uncertain effects, recovery, and correction-preserving transitions. Select them by their stated scope and assess the local implementation; the lessons do not establish an operational pass. Propose a new control only when a concrete requirement remains outside those scopes.

[^execution]: [Execution and recovery protocol](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/process/execution.md).
[^verification]: [Verification strategy](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/process/verification.md).
[^readiness]: [Integrated factory and product readiness](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/verification/factory-readiness.md).
[^evaluation]: [Search evaluation specification](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/product/search-evaluation.md).
[^publication]: [Revision publication decision](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/docs/adr/0004-local-storage-and-revision-publication.md).
[^reporter]: [Local acceptance publisher](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/scripts/publish_local_acceptance.py).
[^reporter-tests]: [Acceptance publisher unit tests](https://github.com/tclasen/semantic_search/blob/0f2c6eead19e01108f97142ce1ded9f32b7a8bcc/tests/unit/test_publish_local_acceptance.py).
