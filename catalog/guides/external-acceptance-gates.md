---
type: Guide
title: "External acceptance gates"
description: "Assess protected evaluators, credentials, and transition paths before treating remote checks as mandatory gates."
status: stable
sources:
  - id: checks
    resource: https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks
    title: "GitHub: Troubleshooting required status checks"
  - id: environments
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
    title: "GitHub: Deployments and environments"
  - id: actions-security
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: "GitHub Actions secure use reference"
  - id: privileged-prs
    resource: https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target
    title: "GitHub: Securely using pull_request_target"
---

# External acceptance gates

This note develops the [factory implementation comparison](../factory-implementation-tradeoffs.md). The cited product documentation was inspected on **2026-09-28**; it describes behavior and does not establish factory effectiveness. No deployed factory or live security configuration was assessed. Check mutable documentation against the installed product before implementation. Recommendations are catalog inferences.

An **external gate** is a decision boundary outside the producing agent's effective control. A remotely hosted check is not independent if the agent can rewrite its criteria, forge its result, or bypass it.

## Mandatory only with protected paths

GitHub documents that required checks apply to the relevant latest revision, with head versus test-merge behavior. A conditionally skipped job can report success, whereas an entire workflow skipped by filters can leave checks pending. Merge queues need the `merge_group` trigger, and checks can be restricted to an expected GitHub App.[^checks]

Environment protection applies to jobs referencing that environment. GitHub supports required reviewers, optional prevention of self-review, and configurable administrator bypass; availability depends on plan and repository visibility.[^environments]

Therefore, assess the entire transition: candidate, evaluator, required result, repository rules, credentials, and destination. An Actions workflow that runs a linter is an automated check. It becomes part of an enforced merge boundary when effective repository rules require it and relevant bypasses are controlled. A merge gate does not cover direct deployment, data export, or email sent before merge.

For Actions, use least-privilege job permissions, reviewed dependencies pinned to full commit SHAs, and safe handling of untrusted event data.[^actions-security] GitHub specifically warns against building or running untrusted PR code with secrets or a privileged token in `pull_request_target` workflows.[^privileged-prs] Protect the evaluator and credentials while allowing contributors to test proposed changes in an unprivileged environment. Remote execution alone does not supply that separation.

Use the [implementation selection procedure](../factory-implementation-selection.md) to record the choice and test the composed system. Assess evaluator independence with [protected acceptance](../controls/protected-acceptance.md), and cover action grants with [bounded external action](../controls/bounded-external-action.md).

[^checks]: GitHub, Troubleshooting required status checks; revision, skipping, merge queues, and expected sources.
[^environments]: GitHub, Deployments and environments; protected jobs, reviews, bypass, and availability limits.
[^actions-security]: GitHub Actions secure use reference; permissions, untrusted data, and dependency pinning.
[^privileged-prs]: GitHub, Securely using pull_request_target; privileged execution of untrusted PR content.
