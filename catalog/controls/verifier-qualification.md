---
type: Control
title: "Verifier qualification"
description: "Test an evaluator against valid alternatives and plausible failures before relying on its verdicts."
catalog_version: "v0.1.0"
status: stable
family: quality-and-validation
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verifiers.md
    title: "Software Factory: Verifier qualification basis"
---

# Verifier qualification

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

**Identity:** `controls/verifier-qualification` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

## Purpose and applicability

Apply when an automated evaluator or repeatable review rubric determines acceptance, selects candidates, or enables greater autonomy. Prevent an evaluator's confident verdict from concealing incorrect output or rejecting an acceptable alternative.

## Requirement

Before relying on an evaluator, define its requirement coverage and qualify the exact evaluator revision against independently labeled valid and invalid cases. Declare acceptance thresholds before observing results. Required safety, authority, and data invariants must not be averaged away. Record uncovered properties, false acceptance, false rejection, and any instability. Withhold reliance for properties whose qualification fails or remains unknown.

## Implementation

1. Assign an evaluator owner and a reviewer competent to establish expected results from accepted intent. Record disagreements in labels.
2. Map consequential requirements to observable properties and checks. Use deterministic checks for objective properties and a calibrated rubric for judgments.
3. Assemble labeled cases: a normal valid candidate, a different valid design, plausible wrong output with a convincing success report, ineffective assertions, weakened candidate tests, and evidence for an older candidate.
4. Bind labels, fixtures, evaluator, configuration, and thresholds to revisions. For nondeterministic judgments, predeclare repeated trials and tolerated variation appropriate to consequences.
5. Execute qualification and retain every verdict, expected result, mismatch, and corrective decision. Repair and reassess failed properties before reliance.

## Expected outcome and assessment

Expected outcome: the evaluator accepts valid alternatives and detects declared failure classes within its measured scope.

Assess the deployed evaluator revision using the labeled set above. Independently inspect label correctness and requirement coverage. In a separate fixture, supply a deliberately defective evaluator that accepts a plausible wrong candidate; test whether the qualification process detects and blocks that evaluator. For a stochastic evaluator, inspect all prescribed repetitions.

- **Pass:** records and labels are complete; qualified evaluators meet predeclared thresholds and all mandatory invariant cases; a deliberately defective evaluator is withheld from reliance. Exclusions and uncertainty remain visible.
- **Fail:** an evaluator is relied on despite a failed mandatory case, changed threshold concealed after results, or unrecorded qualification failure. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** labels, execution evidence, or required repetitions cannot be inspected.
- **Evidence:** coverage map, labeled fixture revisions, evaluator identity, raw verdicts, error counts, thresholds, reviewer and time, and disposition.

## Dependencies and limitations

Depends on competent labeling and representative failures. Use [protected acceptance](protected-acceptance.md) where producer modification is a threat and [assessment evidence validity](assessment-evidence-validity.md) after changes. A perfect score on a small set does not establish general correctness. [Outcome verification](outcome-verification.md) still determines whether acceptance reflects the intended benefit.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verifiers.md).
