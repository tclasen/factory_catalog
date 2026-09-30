# The catalog maintenance factory

This repository uses its own controls to maintain the catalog. Contributors follow
this operating binding alongside [CONTRIBUTING](../CONTRIBUTING.md), which remains
the authority for contribution, security, versioning, and verification policy.
Start each task here, then use the [workflow](workflow.md) and
[work record](work-record.md). The [adoption record](adoption.md) identifies the
current v1 catalog selection, local implementations, migration dispositions, and
gaps.

## Project binding

| Field | Local binding and basis |
|---|---|
| Purpose and beneficiaries | Maintain useful, independently adoptable controls for human and AI knowledge work; beneficiaries are catalog adopters and maintainers. Observed in [README](../README.md). |
| Owner | Repository owner decides product scope and policy. The contributor leading each work item owns its record, implementation, verification, and handoff; name that lead in the record. Reviewers own their review decisions. |
| Authorized work | The user's accepted maintenance request, bounded by repository instructions. This binding implements the explicit request to apply the factory to its own repository. Future work still needs an accepted request. |
| Activities | Intake, research, control selection and authoring, source review, tooling maintenance, validation, PR delivery, review, and improvement from observed defects. |
| Inputs and outputs | User requests, issues, sources, current files and review feedback become scoped changes, checks, evidence, and signed pull requests. Research stays in `docs/research/`; reusable product content stays in `catalog/`; local operations stay here. |
| Knowledge and state | Git holds source and revisions; issues/PRs hold decisions and task evidence; a task-local checkpoint holds pre-publication or interrupted work. No shared task registry or maintenance log is required. |
| Authority | The request and [security controls](../CONTRIBUTING.md#2-prepare-a-branch-and-follow-security-controls) govern actions. Record grants for the current actor, destination, scope, limits, and duration in each work item. Tool availability is not a grant. Merge/release decisions follow the existing owner and review rules. |
| Exposure | Source, PR descriptions, and CI output are public. Keep secrets and sensitive source payloads out of these surfaces; use authorized protected references when needed. Additional providers or sensitive data processing need a task-specific authority decision. |
| Execution | One lead works serially by default. Concurrent work follows [parallel contributions](../CONTRIBUTING.md#parallel-contributions) and requires isolated checkouts and bounded assignments. A dispatcher is not selected. |
| Tools and environment | Git, authenticated `gh`, `uv`, and the repository scripts. Script dependency versions live in their inline metadata; CI settings live in [the workflow](../.github/workflows/validate.yml). Record actual versions and unavailable tools with each assessment. |
| Quality and delivery | [Required checks](../CONTRIBUTING.md#5-verify-and-open-a-pull-request) plus checks mapped to the task's criteria. The normal task endpoint is a verified PR targeting `main`; integration and a release are separately governed stages. |
| Operations | This factory operates through contributor sessions and existing CI. There is no hosted factory service, background agent, uptime commitment, or automatic task selection. Git/PR state supports recovery; unpublished work needs a checkpoint accessible to its successor. |

## Success and review

For each work item, declare beneficiary, observable outcome, threshold, observation
period, evaluator, and failure disposition before implementation. The default
maintenance outcome is that a reviewer can trace every changed requirement to
accepted intent and current evidence, and find every remaining obligation at
handoff. Require coverage of every declared criterion; keep missing observations
open. Artifact checks alone cannot establish usefulness to catalog adopters.

The first adoption PR is the first operational trial. Record its actual results
there. During the next three completed maintenance PRs, the lead records missing
intake fields, lost handoff obligations, stale evidence, and workflow friction in
each PR. On the third handoff, ask the repository owner to keep, revise, or remove
parts of the process based on those observations. Also reopen review after a
missed gate, changed authority/tooling, or control update. This is a review trigger
for ordinary authorized work, not a scheduled job. No throughput or cost benefit
has been measured; comparative claims need a predeclared baseline and method.

## Canonical homes

- Product mission: [README](../README.md); product definitions: [ontology](../catalog/ontology.md).
- Contribution/security/release/check rules: [CONTRIBUTING](../CONTRIBUTING.md).
- Agent entry rules: [AGENTS](../AGENTS.md).
- Local factory context: this binding; selected requirements: [adoption](adoption.md).
- Task intent, decisions, evidence, blockers, and next action: its existing issue/PR.

Update the authoritative rule and affected links when learning changes it. Keep
historical evidence attached to its original task and revision. Do not edit
reusable catalog requirements merely to fit this repository's implementation.
