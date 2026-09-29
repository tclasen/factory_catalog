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

The following companion requirements were considered at the same v1 revision.
Their dispositions keep missing implementation distinct from non-applicability.

| Pinned companion | Decision and next trigger |
|---|---|
| [controls/qualified-artifact-promotion](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/qualified-artifact-promotion.md) | Applicable; proposed beyond PR tree comparison. Package/install paths are outside this adoption. Assess matching, changed/missing/extra artifacts and unavailable destination evidence before claiming promotion qualified. |
| [controls/cumulative-execution-limits](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/cumulative-execution-limits.md) | Applicable when host/user allowances exist; proposed. The work record preserves counts, but durable host accounting and enforcement are not qualified. Unknown usage must not create capacity; reassess before bounded spending or delegation. |
| [controls/exclusive-mutation-ownership](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/exclusive-mutation-ownership.md) | Undetermined for host-level enforcement; owner must resolve before concurrent writers or transfer to an active predecessor. Serial work is selected, but a separate checkout alone does not prove exclusion. |
| [controls/measured-process-improvement](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/controls/measured-process-improvement.md) | Not applicable to this explicit adoption request without a measured-benefit claim. Select a predeclared comparison before claiming faster, cheaper, or better maintenance. |

Companion assessments are **not-assessed**. The work lead owns task-specific
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
in our issue/PR procedure. These changes require no new local operating mechanism.

The release excludes the following previously selected or considered drafts.
They are no longer selected catalog controls or composition guides in this binding.
Their useful local procedures remain repository policy, with the original source
provenance in the prior record. This does not promote the deferred drafts into v1
or claim an equivalent stable replacement.

| Deferred pre-v1 identity | Local disposition / authoritative procedure |
|---|---|
| `controls/accepted-work-definition` | Retain intake scope, owner and criteria in [work record](work-record.md#intent-and-boundary). |
| `controls/acceptance-coverage` | Retain criterion mapping and reconciliation in [work record](work-record.md#plan-and-acceptance) and [workflow](workflow.md). |
| `controls/verified-delivery` | Retain signed PR, tested-tree comparison and destination checks under [contribution policy](../CONTRIBUTING.md#5-verify-and-open-a-pull-request). Qualified artifact promotion remains proposed beyond that mechanism. |
| `controls/planning-consistency` | Retain updates to scope, checklist and affected checks in [workflow](workflow.md#the-work-record-follows-the-task). |
| `controls/instruction-change-control` | Retain observed-defect, authority and review-trigger rules in [workflow](workflow.md#improve-without-rewriting-the-evidence). |
| `controls/safe-work-resumption` | Retain state and predecessor reconciliation in [workflow](workflow.md#resume-uncertainty-and-cancellation). Writer exclusion remains unqualified, as recorded above. |
| `controls/bounded-execution` | Retain boundary, usage and stop/checkpoint fields in [work record](work-record.md#current-state-and-limits). Durable accounting and enforcement remain proposed. |
| `controls/local-quality-gates` | Keep task-specific tooling checks under [contribution policy](../CONTRIBUTING.md#5-verify-and-open-a-pull-request). Not applicable to this documentation update; tooling work must select tools or record narrow owned exceptions. No formatter/linter/type-checker qualification is implied. |
| `guides/factory-project-binding` | Keep the project-owned [binding](README.md). |
| `guides/factory-delivery-lifecycle` | Keep the project-owned [workflow](workflow.md). |
| `guides/factory-work-record` | Keep the project-owned [work record](work-record.md). |
| `guides/factory-adoption-readiness` | Keep scoped criteria, verification and gap review in the [workflow](workflow.md). No blanket readiness claim. |

Reassess after a lost obligation, conflicting tracker state, inaccessible handoff,
changed storage/authority, or a control upgrade. No scheduler, automatic completeness
proof or storage backup is provided by this adoption. Historical process trials and
the binding's review trigger are not restarted by this source update.
