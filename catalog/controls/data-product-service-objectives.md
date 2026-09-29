---
type: Control
title: "Data product service objectives"
description: "Measure data quality and delivery against consumer needs and act on breaches."
catalog_version: "v0.1.0"
status: draft
tags: [data-mesh, data-stewardship]
family: monitoring-and-improvement
sources:
  - id: design
    resource: https://martinfowler.com/articles/designing-data-products.html
    title: "Designing data products"
---

# Data product service objectives

[Adoption](../adoption.md) · [Data mesh research](../data-mesh-architectures.md)

**Identity:** `controls/data-product-service-objectives` · **Catalog:** v0.1.0 · **Family:** `monitoring-and-improvement`

## Purpose and applicability

Apply to recurring analytical products where timeliness or quality affects a decision. Designing data products connects consumer use cases to service objectives.[^design]

## Requirement

Agree measurable objectives and observation windows with consumers, instrument the corresponding indicators, and define breach responses and notification targets. Publish measured status with coverage and missing observations. Do not report an unobserved period as healthy.

## Implementation

1. Select indicators that reflect the decision: source-event-to-availability delay, expected record completeness, reconciliation accuracy, or successful authorized reads. State numerator, denominator, clock, late-arrival treatment, exclusions, and thresholds.
2. Measure freshness against the underlying event or expected delivery, not merely the last successful pipeline run. Separate infrastructure availability from usable data.
3. Name the responder and define whether a breach quarantines data, adds a warning, or pauses dependent decisions. Agree notification and recovery targets.
4. Review objectives when consumer needs change. Apply [outcome verification](outcome-verification.md) to whether the product improves the intended work.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Consumers receive usable status and breach responses within agreed targets, including when measurement itself fails.

For one declared product and observation window, calculate indicators from retained observations. Test normal delivery, a successful job containing stale data, missing monitoring events, and an actual threshold breach. Observe consumer-visible status and the response timeline.

- **Pass:** the scoped implementation meets the requirement, and calculations match reference results, the normal case is healthy, stale and breached data trigger agreed responses, and missing observations are shown as unknown.
- **Fail:** a requirement is violated; in particular, a breached or unobserved interval is reported healthy, calculations omit required records, or responses miss their agreed target.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** objective revision, source times, indicator inputs and calculations, monitor coverage, notification timestamps, and response records.

## Dependencies and limitations

Requires [contracts](data-product-contract.md) and staffed [ownership](data-product-accountability.md). Passing a service objective is scoped to the declared window and cannot establish causal business benefit. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^design]: [Designing data products](https://martinfowler.com/articles/designing-data-products.html).
