---
type: Control
title: "Local quality gates"
description: "Enforce configured static checks and relevant behavioral tests before code acceptance."
status: draft
family: quality-and-validation
sources:
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
  - id: templates-project
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md
    title: "Project binding template"
---

# Local quality gates

[Adoption](../adoption.md) · [Delivery lifecycle](../guides/factory-delivery-lifecycle.md)

Draft requirement adapted from the source factory policies.[^policies-verification][^templates-project] The assessment below is a catalog proposal; no local implementation or operational pass is asserted.

## Purpose and applicability

Apply to software changes, including development tools and tests. Documentation-only work uses document checks.

## Requirement

Pin appropriate formatter, linter, and type-checking tools; enable compatible stable diagnostics and fail on warnings within the declared scope. Run non-mutating acceptance checks and applicable behavioral tests on the final integrated candidate. Missing required tools, unexplained skips, and known failures block acceptance. Exceptions must be narrow, justified, owned, and subject to review.

## Implementation

1. Record tools, versions, checked paths, rules, and exact commands in the project binding; separate formatting from validation.
2. Select test layers from requirements and risk. Consider security, concurrency, recovery, accessibility, performance, compatibility, and other relevant methods; record inapplicability.
3. For each exception retain rule/location, reason, residual risk, owner, and review/removal condition. Reassess on affected changes and tool upgrades.
4. Use fast checks during editing and the full applicable suite on the final candidate. Record security database freshness when a required scan uses one.

Mechanism: an owned procedure with automated checks where available; record the actual enforcement and bypass paths.

## Expected outcome and assessment

Expected outcome: configured quality failures and missing required checks stop code acceptance.

Declare the implementation, revision, scope, evaluator, and applicable paths before assessment. Exercise every listed case and each named failure variant on an authorized isolated fixture, or inspect equivalent retained observations with matching scope. Record why any conditional case does not apply:

| Case | Required observation |
|---|---|
| A conforming candidate passes all applicable checks | Acceptance is eligible and validation leaves source unchanged. |
| An applicable diagnostic warning or meaningful behavioral defect is introduced | The corresponding check fails and acceptance is withheld. |
| A required tool is missing or a test is silently skipped | The gap blocks acceptance instead of becoming a successful skip. |
| A narrow authorized exception exists | Only its recorded scope is excluded; unrelated violations still fail. |

- **Pass:** All cases behave as specified, required commands cover the declared scope, and exceptions remain bounded.
- **Fail:** Formatting alone is reported as acceptance, required failures are suppressed, or a missing tool is treated as a pass.
- **Inconclusive:** required records or effects cannot be inspected well enough to decide. Do not present this as a pass.
- **Evidence:** Pinned configuration, exception register, source-before/after identities, commands, exit statuses, and behavioral results.

## Dependencies and limitations

Requires language-appropriate tools and [acceptance coverage](acceptance-coverage.md). Static checks and coverage percentages alone do not prove correctness. Tool installation remains subject to actual authority.

[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
[^templates-project]: [Project binding template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md).
