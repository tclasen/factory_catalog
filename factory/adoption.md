# Catalog controls adopted for maintenance

## Source and scope

By-reference selection updated on 2026-09-29 for this repository's maintenance
activities to Factory Catalog **v1.0.0**, read from `catalog/VERSION` at published
release commit `5aadd9cb822fbc3c9aef68c039038f1594e42c67`. The
[release](https://github.com/tclasen/factory_catalog/releases/tag/v1.0.0) and its
annotated tag target were inspected through GitHub before adoption.

Each current catalog link below pins that exact revision. Resolve relative
references inside those sources at the same commit and version; a related link
does not automatically select every reachable control. Current checkout contents
may differ. This is a deliberate adoption update, not a catalog version change.

Owner for implementation and per-task assessment: the named work lead. Repository
owner: policy, technical authority boundaries, and residual-risk decisions. All
selected rows are **applicable**, with rationale below. Reassess on changes to
actors, authority, tools, workflow, evidence, or requirements, and at the review
trigger in the [binding](README.md#success-and-review). P0 establishes evidence
and authority first; P1 supports interruption and recovery.

## Selection and local implementation

“Implemented” means the stated local procedure is present; it does not mean the
control passed assessment. These are procedural mechanisms supported by existing
checks. Bypass by an actor ignoring instructions remains possible. Proposed rows
retain unmet technical requirements.

| Pinned identity | Priority | Applicability rationale | Local mechanism / gap | Implementation |
|---|---|---|---|---|
| [controls/assessment-evidence-validity](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/assessment-evidence-validity.md) | P0 | A pass on old content cannot accept new content. | Staged tree, tool/environment and result records; invalidate affected evidence after changes. | implemented |
| [controls/evidence-traceability](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/evidence-traceability.md) | P0 | Catalog claims affect adopter decisions. | Existing source provenance plus claim review fields; lead discloses self-review and unsupported claims. | implemented |
| [controls/outcome-verification](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/outcome-verification.md) | P0 | Published prose does not prove a useful maintenance process. | Predeclared per-task outcome and separate artifact/outcome reporting; owner reviews later usability. | implemented |
| [controls/bounded-external-action](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/bounded-external-action.md) | P0 | Publication credentials may exceed a task grant. | Host permissions and GitHub protections cover some boundaries; per-path grant enforcement is not established. Owner must qualify or restrict uncovered paths. | proposed |
| [controls/durable-work-handoff](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/durable-work-handoff.md) | P1 | Session loss can lose obligations and effects. | Checkpoint then issue/PR, before/after effects; successor reconciles actual state. Crash window is explicit. | implemented |
| [controls/reconcile-before-retry](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/reconcile-before-retry.md) | P1 | An uncertain response can cause duplicate publication. | Retain branch/SHA and PR head/base intent, query GitHub before repeating writes, block unknown effects. | implemented |
| [controls/qualified-artifact-promotion](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/qualified-artifact-promotion.md) | P0 | Publishing a PR must preserve the qualified candidate. | [Delivery qualification](workflow.md#delivery-qualification) binds the complete Git tree and relevant configuration to local checks and independently reads back the remote commit/tree. Scope is source-only PR delivery; package/install paths require a new task-specific implementation. | implemented |
| [controls/exclusive-mutation-ownership](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/exclusive-mutation-ownership.md) | P1 | Ownership transfer, stale writers or concurrent writes can corrupt shared task state. | [Resumption](workflow.md#resume-uncertainty-and-cancellation) requires evidence of effective exclusion before transfer. Serial work and separate checkouts alone do not qualify receiving-boundary enforcement; owner must resolve the gap before a competing writer can act. | proposed |
| [controls/cumulative-execution-limits](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/cumulative-execution-limits.md) | P1 | Applicable host/user allowances must survive attempts and resumption. | [Resource accounting](workflow.md#resource-accounting-and-stopping) preserves usage and reservations. Durable metering and enforcement remain unqualified; unknown usage cannot create capacity. | proposed |
| [controls/workflow-resource-budgets](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/workflow-resource-budgets.md) | P1 | Model/tool jobs consume shared time and capacity even without billing. | [Resource accounting](workflow.md#resource-accounting-and-stopping) identifies resources, owner, bounds and in-flight exposure. Aggregate admission/cancellation enforcement is not established; unknown bounds remain an explicit gap for the owner. | proposed |

Assessment baseline for this adoption: **not-assessed** for every selected row.
Task-specific observations remain with their assessed revision and issue/PR.
Run every applicable case in the pinned control before reporting a control pass;
source comparison and repository checks cannot establish operational effectiveness.

## Dependencies and deliberate limits

Evidence traceability and validity support outcome and delivery claims. Handoff
and retry reconciliation share the [work record](work-record.md). Local scope,
acceptance, planning, delivery and execution procedures remain required by the
[workflow](workflow.md) and [CONTRIBUTING](../CONTRIBUTING.md); their pre-v1 source
drafts are dispositioned below. None of these mechanisms grants authority.

The following companion requirement was considered at the same v1 revision.
Its disposition keeps an absent benefit claim distinct from missing implementation.

| Pinned companion | Decision and next trigger |
|---|---|
| [controls/measured-process-improvement](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/measured-process-improvement.md) | Not applicable to this explicit adoption request without a measured-benefit claim. Select a predeclared comparison before claiming faster, cheaper, or better maintenance. |

The companion assessment is **not-assessed**. The work lead owns task-specific
follow-up; the repository owner owns permission/enforcement changes. Missing
enforcement remains a gap; prompt rules cannot satisfy a technical boundary.
No permissions, credentials, branch rules, services or recurring jobs are changed
by this adoption. An uncovered path is not qualified for autonomous operation.

## Composition basis and maintenance

The current catalog procedures used by this binding are:

- [adoption](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/adoption.md)
- [guides/durable-task-tracking](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/guides/durable-task-tracking.md)
- [restart-and-handoff-records](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/restart-and-handoff-records.md)
- [assessment-evidence-records](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/assessment-evidence-records.md)

Local adaptations: GitHub issues/PRs hold one current checklist with owned items,
evidence links, update triggers, readback and parent reconciliation. An ignored
checkpoint covers pre-publication work; essential state must be published before
handoff. Delivery stops at the authorized repository endpoint. The lead can perform
roles unless independent review is required. Existing contribution policy remains
canonical. Serial work does not need a dispatcher or blanket control adoption.

For a control update, compare the pinned requirement and assessment with the
proposed source, explain local impact in the PR, rerun affected assessments, and
retain prior adoption and task evidence. Updating this record never silently
updates earlier results or the catalog's release version.

## Migration from the pre-v1 binding

The [prior adoption record](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/factory/adoption.md)
retains the original `v0.1.0` selection at
`d5476d34c36364520dd2757475523651aa5c66cd` and the durable-tracking reselection at
`70896c440662d12f38848f9dcde61ef563403327`, including their exact source links,
implementation states and assessment baseline. Historical versions and observations
remain unchanged there.

All ten retained controls and companions were compared with their adopted sources.
Their requirements and assessments are unchanged. Evidence validity and retry
reconciliation clarify their public support basis; evidence traceability adds an
authorship statement. Bounded external action removes an optional deferred service
recovery link. Durable work handoff adds the stable tracking guide already reflected
in our issue/PR procedure. Those source changes require no new mechanism. The
replacement compositions below explicitly select additional coverage and retain
its implementation gaps.

The release deferred eleven previously selected or considered drafts and retired
the duplicate work-record guide in [PR #67](https://github.com/tclasen/factory_catalog/pull/67).
The former identities are no longer selected. The four clean or near-clean
replacements below use stable v1 requirements and guidance; remaining duties stay
explicit local policy. Selection does not close the stated implementation or
assessment gaps. Other deferred items retain their local procedures and historical
provenance without claiming a stable replacement.

| Former pre-v1 identity | Local disposition / authoritative procedure |
|---|---|
| `controls/accepted-work-definition` | Retain intake scope, owner and criteria in [work record](work-record.md#intent-and-boundary). |
| `controls/acceptance-coverage` | Retain criterion mapping and reconciliation in [work record](work-record.md#plan-and-acceptance) and [workflow](workflow.md). |
| `controls/verified-delivery` | Use [delivery composition](#delivery-composition): qualified artifact promotion, assessment evidence validity, bounded external action and outcome verification. Local stage and endpoint checks remain required. |
| `controls/planning-consistency` | Retain updates to scope, checklist and affected checks in [workflow](workflow.md#the-work-record-follows-the-task). |
| `controls/instruction-change-control` | Retain observed-defect, authority and review-trigger rules in [workflow](workflow.md#improve-without-rewriting-the-evidence). |
| `controls/safe-work-resumption` | Use [resumption composition](#resumption-composition): durable work handoff, exclusive mutation ownership, reconcile before retry and assessment evidence validity. Effective writer exclusion remains a technical gap. |
| `controls/bounded-execution` | Use [execution composition](#execution-composition): cumulative execution limits and workflow resource budgets. Keep the local task boundary, failure diagnosis and checkpoint policy. |
| `controls/local-quality-gates` | Keep task-specific tooling checks under [contribution policy](../CONTRIBUTING.md#5-verify-and-open-a-pull-request). Not applicable to this documentation update; tooling work must select tools or record narrow owned exceptions. No formatter/linter/type-checker qualification is implied. |
| `guides/factory-project-binding` | Keep the project-owned [binding](README.md). |
| `guides/factory-delivery-lifecycle` | Keep the project-owned [workflow](workflow.md). |
| `guides/factory-work-record` | Retired duplicate. Use [record composition](#record-composition): restart and handoff records plus durable task tracking, adapted in the local work record. |
| `guides/factory-adoption-readiness` | Keep scoped criteria, verification and gap review in the [workflow](workflow.md). No blanket readiness claim. |

Reassess after a lost obligation, conflicting tracker state, inaccessible handoff,
changed storage/authority, or a control upgrade. No scheduler, automatic completeness
proof or storage backup is provided by this adoption. Historical process trials and
the binding's review trigger are not restarted by this source update.

## Replacement compositions

All controls named here use the pinned source URLs, version, owners, implementation
states and assessment baseline above. These are local compositions, not new catalog
controls or a claim that every former requirement has an identical v1 definition.

### Record composition

The stable restart and handoff record supplies identity, intent, authority,
ownership, current state, evidence, resources, operation effects and continuation.
Durable task tracking supplies the canonical checklist and reconciliation procedure.
The [local record](work-record.md) adapts both and adds repository delivery fields;
its evidence section uses the stable assessment evidence record. No duplicate
catalog work-record guide is needed. Record-format changes require validation or
blocked dependent resumption; an inaccessible record cannot establish readiness.

### Resumption composition

Durable work handoff governs record preservation and state reconciliation; exclusive
mutation ownership governs effective exclusion of prior/stale writers; reconcile
before retry resolves uncertain effects; evidence validity reopens stale checks.
Use [the resume procedure](workflow.md#resume-uncertainty-and-cancellation) before
successor writes. Missing authority, unreadable state or unresolved ownership blocks
the affected mutation. A record or cooperative stop alone cannot establish fencing.
The work lead records evidence; the repository owner resolves enforcement gaps.

### Execution composition

Cumulative execution limits carries actual usage and reservations across retries
and resumption. Workflow resource budgets covers aggregate job admission, child
work and in-flight exposure. The local [resource procedure](workflow.md#resource-accounting-and-stopping)
retains the former task-boundary, repeated-failure diagnosis and checkpoint duties.
These controls are selected as proposed mechanisms: bookkeeping is not enforceable
metering or a shared budget boundary. Unknown telemetry and missing bounds stay
visible; neither a restart nor a missing measurement supplies fresh capacity.

### Delivery composition

Qualified artifact promotion checks the destination object; evidence validity binds
qualification to the candidate and configuration; bounded external action governs
authority; outcome verification limits claims to observed stages and benefits.
The local [delivery procedure](workflow.md#delivery-qualification) defines the stages,
endpoint, complete source artifact and required remote observations. Signed PR
publication is the normal endpoint; merge, release and installed behavior require
their own scope and evidence. A changed tree, incompatible configuration or unknown
destination blocks the affected delivery claim. The PR procedure is implemented;
authority enforcement remains proposed and full control assessments remain unrun.
