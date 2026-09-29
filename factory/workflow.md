# Maintenance workflow

Use the [project binding](README.md) and [work record](work-record.md). This is a
human/agent procedure supported by existing repository checks. It does not enforce
credential boundaries or start agents.

| Stage / trigger | Lead's action | Exit evidence and failure route |
|---|---|---|
| Start a request | Read current entry instructions, inspect files and relevant issues/PRs, and prepare the branch under repository policy. Record intent and scope before dependent edits. | Named lead, accepted criteria, relevant grants, base/checkout, and preserved unrelated work. Essential unknowns block only dependent actions. |
| Select and plan | Map each criterion to changed surfaces and checks. Consult the selected controls when their trigger applies. Read bundle admission rules and pinned OKF specification for product edits. | Smallest useful increment, dependencies, applicability decisions, and check map. Ideas beyond the request stay proposals. |
| Implement | Make the scoped changes. Keep the task record current at changes in scope, ownership, evidence, or effects. Stop unchanged failure loops and diagnose before retrying. | Candidate maps to criteria. Changed assumptions reopen affected plans and checks. Preserve cumulative limits and attempts. |
| Verify | Stage new files and run the required check command from CONTRIBUTING. Review the whole diff, affected links, sources, and semantic admission. Reconcile every criterion with final results. | Tree/revision-bound results, warnings with dispositions, review limitations, and remaining gaps. A required failure, skipped check, or unavailable tool leaves acceptance open. |
| Deliver | Follow signed topic-branch publication policy. Compare the tested tree with the commit, then inspect the PR head, GitHub signature verification, and remote checks. | PR URL, matching candidate, signature and check evidence. Unknown or failed stages remain incomplete. Resolve an ambiguous remote response before repeating mutation. |
| Learn and hand off | Report artifact acceptance, control assessments, and beneficiary outcome separately. Retain defects and the next decision in the task record. | Clear authorized endpoint, remaining work, and process observations. Feed actionable corrections into an authorized task at their canonical home. |

## The work record follows the task

For work spanning sessions or PRs, use one GitHub issue body as the canonical
current checklist. Keep that parent open until every accepted criterion is
reconciled; a merged PR completes only its bounded contribution. Use a PR body
as the canonical record only for a single-PR task with no remaining parent scope.
Follow the [pinned catalog procedure](https://github.com/tclasen/factory_catalog/blob/5aadd9cb822fbc3c9aef68c039038f1594e42c67/catalog/guides/durable-task-tracking.md)
recorded in the [adoption](adoption.md#composition-basis-and-maintenance).

At intake, record the canonical URL in the local checkpoint and every child PR.
Create an issue when accepted work has none and needs durable tracking. Find it
on resume through the request, linked PR, or repository open-issue search; if
several records match, reconcile their scope before writing. Do not make chat
history the only locator. The [work record](work-record.md) supplies the checklist
fields. Child issues own bounded criteria; the parent links them and their blockers.

Before edits, map all accepted obligations to checklist rows. Update the current
issue body after scope changes, meaningful results, failures, delivery, and before
every handoff/final response. Comments hold dated evidence; they do not replace
updating stale current state. Mark done only with linked evidence for that item's
criterion and target revision. Keep blocked and cancelled duties with reasons,
owners and resume conditions. Reconcile the parent when child work finishes.

Before publication, save a checkpoint under a unique ignored `build/work/` path.
It is a convenience copy, not a backup or competing source of truth. Publish all
essential state and verify remote readback before handoff or checkout deletion.
If GitHub is unavailable, preserve pending local updates, report the unsynchronized
state and stop only actions that depend on missing shared state. No record or
procedure schedules a future session. Do not commit per-task journals or catalogs
of tasks into the product bundle.

Read the latest issue before replacing its body and coordinate any other writer;
preserve new decisions instead of overwriting them. Keep previous evidence in
comments/PRs and record material scope/status corrections. Save operation intent
before consequential effects, then record observed effects and remaining duties.
A crash between those saves leaves an uncertain effect to reconcile. Keep secrets
and sensitive source payloads out of public records.

## Resume, uncertainty, and cancellation

Before resuming writes, read the record and current instructions, confirm prior
writers/processes stopped or lost access, and inspect actual checkout, dirty work,
branch, remote head, checks, and authority. A branch name or old checkpoint cannot
prove exclusive ownership. If ownership or essential intent cannot be established,
preserve work and block dependent mutation. If the record is missing or unreadable,
reconstruct only supported facts from the request and actual systems.

For an uncertain push, compare the remote branch SHA with the intended commit. For
an uncertain PR creation, query the repository's PRs by head/base and inspect the
candidate before creating another. If state remains unavailable, retain the block;
do not assume a retry is harmless. Record partial effects individually. On
cancellation, stop owned execution safely, preserve unfinished work and effects,
and report cancellation rather than completion.

## Improve without rewriting the evidence

Record the observed defect and source, the proposed cause as a hypothesis when
uncertain, the smallest correction, its authority, and a review/removal trigger.
Changes to scope or criteria update the work record and affected checks before
work resumes. Earlier results retain their original meaning. A rule change cannot
waive a failed gate, expand permissions, or manufacture an outcome. Retain failed
and blocked observations when assessing whether a process change helped.
