---
type: Guide
title: "Restart and handoff records"
description: "Preserve intent, ownership, uncertain effects, remaining limits, and the next safe action across sessions."
status: stable
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/assets/templates/restart-record.md
    title: "Software Factory: Restart and handoff records basis"
---

# Restart and handoff records

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## Use

Support [durable work handoff](controls/durable-work-handoff.md) in the project's existing work record. Small work may need only a concise note. Record references to authority and evidence, never secret values. A record preserves information; it does not schedule execution or enforce ownership.

## Suggested record

| Field | Content |
|---|---|
| Record identity | Format version, task ID, generation, record revision, writer and last reconciliation time |
| Intent | Accepted objective and source, scope, current phase, criteria, and outstanding obligations |
| Authority | Grant references and limits, current instructions, expiry, cancellation, and owner decisions |
| Ownership | Current owner, active writers/processes, shared resource scopes, leases or fencing references where used |
| Local state | Source/artifact/configuration revisions, dirty or unrelated files to preserve, compatibility requirements |
| Evidence | Observation references, assessed inputs, stale/unknown results, remaining verification |
| Resources | Cumulative attempts/usage, outstanding reservations, limits and remaining allowance, accounting source |
| Continuation | Blockers, reconciliation needed, next safe action, and owner of each remaining duty |

For each consequential operation retain:

| Operation identity | Destination and intended effect | State | Authoritative observation/time | Remaining duty |
|---|---|---|---|---|
| Stable provider ID/key where supported | Exact resource and payload/artifact revision | Intended, submitted, observed complete, failed, or unknown | Status/receipt reference with its limitations | Reconciliation, verification, observation, or authorized recovery |

Keep per-component outcomes for partially successful bulk operations.

## Write and resume

1. Save intent and identity before effects, using atomic record replacement where practical. State the possible crash-loss window.
2. After an observation, record what completed and what remains. A missing response leaves the effect unknown until reconciled.
3. On resume, reread current intent and restrictions. Verify actual local/recipient state and ownership; a checkpoint is a starting point, not current authority.
4. Apply [reconcile before retry](controls/reconcile-before-retry.md), [cumulative execution limits](controls/cumulative-execution-limits.md), and [assessment evidence validity](controls/assessment-evidence-validity.md) before relying on previous progress.
5. With competing workers, enforce [exclusive mutation ownership](controls/exclusive-mutation-ownership.md). Respect [cancellation](controls/cancellation-enforcement.md); late evidence must not reopen cancelled intent.
6. Validate record-format changes or stop dependent work if the reader cannot interpret consequential fields.

## Illustrative handoff

A publication response was lost. The record marks the submitted operation’s outcome unknown, gives the original operation ID, and retains two consumed attempts out of a three-attempt allowance. The next session queries the destination and observes completion. It records completion and finishes missing verification without publishing again or resetting the allowance.

## Review the record

Have a fresh reader identify the next safe action from the record and authorized systems. Check that cancellation, unknown effects, unrelated edits, remaining budgets, and observation duties survive the handoff. Use the control's assessment for an actual pass/fail decision; this example is not an executed trial.

## Source and scope

Adapted from the pinned Software Factory procedure.[^software-factory] The tables are suggested local record fields, not new required OKF frontmatter. Store actual records with their owning project and appropriate access and retention controls. A populated record is not evidence that its claimed observations are true. No operational assessment is asserted here.

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/assets/templates/restart-record.md).
