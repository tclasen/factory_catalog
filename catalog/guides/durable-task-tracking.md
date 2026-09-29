---
type: Guide
title: "Track unfinished work across sessions"
description: "Choose a canonical task record, keep an evidence-backed checklist current, and recover work without conversation memory."
status: stable
---

# Track unfinished work across sessions

## Select controls for the failure

Use [durable work handoff](../controls/durable-work-handoff.md) when a session,
conversation summary, notebook, or worker may disappear. The record fields and
steps below state the task-tracking procedure directly; a separate acceptance or
planning control is not a prerequisite. The guide adds no control or mandatory
tracker product. Pin selected controls and their dependencies through
[adoption](../adoption.md).

The failure addressed is a saved history that cannot answer “what remains?”
without reconstructing a conversation. Examples include a research report whose
source checks outlive one editor, or a release delivered through several PRs.

## Choose one current record

For shared work, prefer the existing issue or project tracker with durable access
and edit history. Keep the current checklist in its main description; use comments
for dated observations and evidence. For work spanning several deliveries, retain
the parent record until its whole scope is reconciled. A child issue or PR owns
its bounded contribution, not completion of the parent outcome.

For offline or sensitive work, use a versioned file in approved durable storage.
An ignored scratch file is a checkpoint, not the only recoverable copy. Publish or
back up essential state before handoff or checkout removal, verify readback, and
record where successors can find it. If storage is unavailable, retain a pending
local checkpoint and disclose that shared handoff is incomplete. Do not copy
protected evidence into a public tracker.

Give the record an owner, a stable locator discoverable from project entry
instructions, the accepted request, current scope, authority references, and a
last-reconciled revision/time. Keep a short next action at the top. Conversation
summaries and local caches can point to it; they must not be needed to recover
accepted duties. This procedure does not schedule future work or restart an agent.

## Keep obligations explicit

A useful checklist row contains:

| Field | Meaning |
|---|---|
| Local item ID and criterion | Stable within this task; concrete result needed for completion |
| State and owner | Open, active, blocked, done, or cancelled; person/role responsible |
| Dependencies | Other item IDs, needed evidence or owner decision; avoid circular prerequisites |
| Evidence and target | Result reference and exact artifact/source revision; missing or stale evidence stays visible |
| Next action | A step that advances this item, or the blocker and condition for resuming |

These are suggested local workflow states, not new catalog assessment values.
A checked box means the item's criterion has current evidence. Cancellation keeps
its rationale and authority; it is not successful completion. Split large items
when independent ownership, evidence, or interruption would otherwise be hidden.
Use linked child records rather than copying competing checklists between files.

Before implementation, reconcile rows with the accepted request in both
directions: every obligation has a row, and every row has authorized scope.
Reconcile again after scope changes, meaningful observations, failures, delivery,
and before yielding or handing off. Update the current description as well as
appending evidence; a new comment alone does not fix a stale checklist. Keep
superseded evidence and explain changes of meaning rather than relabeling old passes.

Read the latest record before editing. With concurrent writers, coordinate ownership
or use the storage system's revision conflict checks; do not blindly overwrite a
newer update. Verify the saved result from the destination. A crash between an
external effect and its recorded observation leaves an unknown effect to reconcile.

## Resume without conversational memory

1. Find the canonical record from the project entry point or linked work item.
2. Read accepted intent, current checklist, authority, blockers and evidence links.
   Inspect relevant child records; do not require reading every historical comment.
3. Reconcile claims against actual files, deliveries, approvals and revisions.
   Missing evidence cannot establish done; a merged PR establishes only its scope.
4. Reconcile ownership and current state before resuming. Use stable
   [reconcile before retry](../controls/reconcile-before-retry.md) for uncertain
   effects. Resolve conflicting records through authoritative observations; stop
   only dependent actions when essential state remains unknown.
5. Restore a current next action and save/read back the reconciled record before
   dependent mutation. Preserve cumulative limits and unrelated work.

## Recovery exercise

Hide the conversation and local checkpoint. Give a reader the project entry point,
canonical record and authorized source systems. They should find every outstanding
obligation, owner, blocker, evidence location and next safe action. Then exercise:

| Fixture | Expected decision |
|---|---|
| One child PR merged, parent criteria still incomplete | Mark only supported child work done; keep parent open |
| A checked item has missing or stale evidence | Reopen or block that acceptance claim; preserve the old observation |
| A comment records failure but the current description says done | Reconcile the contradiction and update current state before dependent work |
| Local checkpoint deleted; shared record accessible | Recover all essential duties from the shared record |
| Shared record inaccessible or two writers disagree on authority | Preserve local evidence and block dependent mutation pending reconciliation |
| A new request adds a required check | Add the obligation, update dependencies and invalidate affected acceptance |

Record input revisions, observed decisions, omissions and corrections. These are
proposed usability fixtures. A producer conducting them is not an independent
fresh reader, and this subset does not establish a full control assessment. Use
the selected controls' complete assessment cases before claiming a control pass.
