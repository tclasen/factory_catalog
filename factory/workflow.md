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

Use an existing issue as the work record when available; use the PR body for final
acceptance and handoff. Before a PR exists, save a short checkpoint in a unique
ignored path such as `build/work/<branch>.md` using the
[record fields](work-record.md). Record that path in the session. Copy the current
state into the PR body when publishing, then use that PR as the canonical record.
Do not commit per-task journals or edit a shared index for ordinary contributions.

A local checkpoint survives a session but is not a backup and does not survive
checkout deletion. Before transfer, make it accessible to the successor through
the existing issue/PR or an authorized shared artifact. Save intent before a
consequential action and observation after it. A crash between those saves leaves
an uncertain effect; reconcile it. Do not put credentials in either location.

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
