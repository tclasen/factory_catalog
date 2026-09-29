# Maintenance work record

Use these fields in the task's existing issue/PR or a pre-publication checkpoint
under the [workflow](workflow.md). Keep entries proportionate: a small correction
can use a sentence per section. Mark unknowns explicitly; omit a conditional field
only with a reason. Update current state without erasing failed evidence.

## Intent and boundary

- Request/source, intended beneficiary and outcome:
- Lead and decision owner; accepted scope and exclusions:
- Authority source, actor, actions/destinations, limits/duration, approval conditions:
- Outcome measure, threshold, observation period, evaluator, and failure/unknown disposition:
- Dependencies and consequential unknowns:

## Plan and acceptance

| Criterion | Changed surfaces / implementation | Planned check | Actual evidence and result |
|---|---|---|---|
| Fill before implementation | Map every changed surface | Include relevant denied/failure/recovery paths | Keep missing, failed, or stale evidence visible |

## Current state and limits

- Stage; checkout, branch, base and candidate SHA or staged tree digest:
- Reserved edit surfaces; other writers/processes and unrelated work to preserve:
- Runtime/model configuration when known; tool versions and relevant environment:
- Applicable host/user resource limits, issuer/units, cumulative usage/attempts,
  outstanding reservations, remaining allowance, and next checkpoint:
- Unknown telemetry and resulting limits on claims; no numeric budget means no invented quota:
- Blockers, changed scope/assumptions, and invalidated evidence:

## Evidence and review

For each check or control assessment, record the target tree/revision, criterion
or pinned control, evaluator and independence, time, procedure/command, fixtures,
tools/configuration/environment, output reference, actual result, limitations,
and follow-up. Record passing checks out of required checks and justify exclusions.
Bind uncommitted evidence to `git write-tree` after staging and verify the working
tree matches the index. Compare that tree with the published commit's tree.
Changes to relevant inputs invalidate affected evidence; preserve the prior record.

For material factual claims, retain claim location, source revision/access time,
supporting passage or calculation, direct support/inference/unknown status, and
contrary evidence. Review the complete output for omitted material claims. Link
existing provenance instead of copying it. State when the producer also reviewed.

## Effects and delivery

- Before mutation: action, destination, intended revision, authority, and operation identity:
- After mutation: receipt and independent destination observation; unknown/partial effects:
- Local checks, signed commit, remote signature verification, PR head, CI, and PR URL:
- Applicable completion stages and unmet stages; merging/release follow repository policy:
- Artifact acceptance / control assessment / observed beneficiary outcome, separately:

## Handoff and improvement

- Remaining work, next safe action, decision owner, and resume condition:
- Predecessor stop/access evidence and checkpoint location if transferring:
- Process defect/friction, evidence, proposed correction, and review trigger:
- Version impact, breaking effects, unverified claims, and remaining review decisions:
