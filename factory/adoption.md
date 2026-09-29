# Catalog controls adopted for maintenance

## Source and scope

By-reference selection recorded on 2026-09-29 for this repository's maintenance
activities. Source revision: `d5476d34c36364520dd2757475523651aa5c66cd`; catalog version read at that
revision: `v0.1.0`. This historical version belongs to this adoption record;
it must not change merely because the catalog releases another version. The
published commit was inspected through GitHub before adoption.

Each link below is the exact adopted source URL; its label is the bundle-relative
control identity without `.md`. Relative references inside those source controls
resolve within `https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/` at the same version and SHA. Keep that resolution when
reading dependencies; current checkout contents may differ. A related link does
not automatically select every reachable control.

Owner for implementation and per-task assessment: the named work lead. Repository
owner: policy, technical authority boundaries, and residual-risk decisions. All
rows are **applicable**, with rationale below. Reassess on changes to actors,
authority, tools, workflow, evidence, or these requirements, and at the review
trigger in the [binding](README.md#success-and-review). P0 establishes scope,
evidence and delivery first; P1 supports change, interruption and improvement.

## Selection and local implementation

“Implemented” means the stated local procedure is present in this candidate; it
does not mean the control passed assessment or is active on `main`. These are
procedural mechanisms supported by existing checks. Bypass by an actor ignoring
instructions remains possible. Proposed rows retain unmet technical requirements.

| Pinned identity | Priority | Applicability rationale | Local mechanism / gap | Implementation |
|---|---|---|---|---|
| [controls/accepted-work-definition](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/accepted-work-definition.md) | P0 | Every change needs accepted scope. | Work record intent and criterion map before edits; lead resolves consequential unknowns. | implemented |
| [controls/acceptance-coverage](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/acceptance-coverage.md) | P0 | Partial check success can hide an unmet requirement. | Criterion/check/result map and final reconciliation in the PR; lead owns coverage. | implemented |
| [controls/assessment-evidence-validity](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/assessment-evidence-validity.md) | P0 | A pass on old content cannot accept new content. | Staged tree, tool/environment and result records; invalidate affected evidence after changes. | implemented |
| [controls/evidence-traceability](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/evidence-traceability.md) | P0 | Catalog claims affect adopter decisions. | Existing source provenance plus claim review fields; lead discloses self-review and unsupported claims. | implemented |
| [controls/outcome-verification](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/outcome-verification.md) | P0 | Published prose does not prove a useful maintenance process. | Predeclared per-task outcome and separate artifact/outcome reporting; owner reviews later usability. | implemented |
| [controls/verified-delivery](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/verified-delivery.md) | P0 | Local files alone do not meet the repository endpoint. | Signed PR, tree/head comparison, remote verification and CI; lead retains partial stages. | implemented |
| [controls/bounded-external-action](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/bounded-external-action.md) | P0 | Publication credentials may exceed a task grant. | Host permissions and GitHub protections cover some boundaries; per-path grant enforcement is not established. Owner must qualify or restrict uncovered paths. | proposed |
| [controls/planning-consistency](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/planning-consistency.md) | P1 | Scope changes can leave contradictory checks. | Update affected intent, artifacts and checks together; retain superseded evidence with its scope. | implemented |
| [controls/instruction-change-control](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/instruction-change-control.md) | P1 | Dogfooding findings must not silently change authority. | Workflow improvement procedure records observation, source, authority and review trigger. | implemented |
| [controls/durable-work-handoff](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/durable-work-handoff.md) | P1 | Session loss can lose obligations and effects. | Checkpoint then issue/PR, before/after effects; successor reconciles actual state. Crash window is explicit. | implemented |
| [controls/safe-work-resumption](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/safe-work-resumption.md) | P1 | A stale checkpoint can cause overlapping writers. | Resume procedure requires stopped/fenced predecessors and state inspection. Actual writer exclusion depends on the host and remains unqualified. | proposed |
| [controls/reconcile-before-retry](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/reconcile-before-retry.md) | P1 | An uncertain response can cause duplicate publication. | Retain branch/SHA and PR head/base intent, query GitHub before repeating writes, block unknown effects. | implemented |
| [controls/bounded-execution](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/bounded-execution.md) | P1 | Retries and handoffs can hide consumed allowances. | Work boundary, cumulative attempts/limits, diagnosis and checkpoint fields; host limits apply. | implemented |

Assessment baseline for every selected row: **not-assessed**. The first adoption
PR records actual scoped observations, failures and remaining cases against its
exact candidate; subsequent task assessments live with their task. Do not overwrite
this baseline to imply that a later pass applied to an earlier implementation.
Run every applicable case in the pinned control before reporting a control pass;
a walkthrough or a successful catalog validator is insufficient for that claim.

## Dependencies and deliberate limits

Accepted scope feeds acceptance coverage and planning consistency. Evidence
traceability and validity support outcome and delivery claims. Instruction changes
use the same scope and evidence gates. Handoff, resumption, retry reconciliation,
and execution limits share one work record; they do not grant additional authority.

The following companion requirements were considered. Their source identity,
version and revision follow the source record above; their local disposition is
explicit so missing implementation cannot be mistaken for non-applicability.

| Pinned companion | Decision and next trigger |
|---|---|
| [controls/qualified-artifact-promotion](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/qualified-artifact-promotion.md) | Applicable; proposed beyond PR tree comparison. Package/install paths are outside this adoption. Assess matching, changed/missing/extra artifacts and unavailable destination evidence before claiming promotion qualified. |
| [controls/cumulative-execution-limits](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/cumulative-execution-limits.md) | Applicable when host/user allowances exist; proposed. The work record preserves counts, but durable host accounting and enforcement are not qualified. Unknown usage must not create capacity; reassess before bounded spending or delegation. |
| [controls/exclusive-mutation-ownership](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/exclusive-mutation-ownership.md) | Undetermined for host-level enforcement; owner must resolve before concurrent writers or transfer to an active predecessor. Serial work is selected, but a separate checkout alone does not prove exclusion. |
| [controls/local-quality-gates](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/local-quality-gates.md) | Not applicable to this documentation-only increment; applicable/proposed for software tooling changes. Existing catalog CI is not evidence of pinned formatter/linter/type-checker coverage. The tooling task must select tools or record narrow owned exceptions before acceptance. |
| [controls/measured-process-improvement](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/controls/measured-process-improvement.md) | Not applicable to this explicit adoption request without a measured-benefit claim. Select a predeclared comparison before claiming faster, cheaper, or better maintenance. |

Companion assessments are **not-assessed**. The work lead owns task-specific
follow-up; the repository owner owns permission/enforcement changes. Missing
enforcement must remain a gap; prompt rules cannot satisfy a technical boundary.
No permissions, credentials, branch rules, services or recurring jobs are changed
by this adoption. An uncovered path is not qualified for autonomous operation.

## Composition basis and maintenance

The local binding, workflow and record adapt these guides, all from the same
source revision and version:

- [guides/factory-project-binding](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/guides/factory-project-binding.md)
- [guides/factory-delivery-lifecycle](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/guides/factory-delivery-lifecycle.md)
- [guides/factory-work-record](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/guides/factory-work-record.md)
- [guides/factory-adoption-readiness](https://github.com/tclasen/factory_catalog/blob/d5476d34c36364520dd2757475523651aa5c66cd/catalog/guides/factory-adoption-readiness.md)

Local adaptations: GitHub issues/PRs replace a new tracker; a local checkpoint
covers the period before publication; delivery stops at the authorized repository
endpoint; the current lead can perform roles unless independent review is required.
Existing contribution policy remains canonical. A dispatcher, blanket adoption of
all controls, and a new catalog schema are unnecessary for this serial process.

For a control update, compare the pinned requirement and assessment with the
proposed source, explain local impact in the PR, rerun affected assessments, and
retain the old adoption through Git history and its PR evidence. Updating this
record never silently updates prior task evidence or the catalog's release version.
