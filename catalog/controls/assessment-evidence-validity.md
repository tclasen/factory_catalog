---
type: Control
title: "Assessment evidence validity"
description: "Bind assessment results to their inputs and prevent stale results from satisfying current acceptance."
status: stable
family: knowledge-and-evidence
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verification-selection.md
    title: "Software Factory: Assessment evidence validity basis"
---

# Assessment evidence validity

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply whenever an assessment result is reused, summarized, or used to permit acceptance or delivery. Prevent a correct result for an earlier artifact or environment from being presented as current evidence.

## Requirement

Record the artifact, criteria, evaluator, fixtures, configuration, tools, relevant dependencies and environment, and observation period to which each result applies. Before reuse, compare those inputs with the current target. Invalidate results affected by changes, missing identity, or exceeded freshness conditions; rerun the required checks before relying on them. Preserve unaffected results with their original identities and times. New timestamps alone must not refresh evidence.

## Implementation

1. Name the assessment owner and map each claim to the checks and inputs on which it depends.
2. Use immutable revisions or digests where available, with a recorded retrieval time and limitation otherwise. For uncommitted work, retain a tree or patch digest covering the assessed content. Define freshness conditions for changing external data.
3. Retain execution state separately from assessment result: blocked or unrun checks cannot supply passing observations.
4. At the consuming decision, including after integration or installation, compare bound inputs and explain which changes affect which claims. Treat unknown material dependencies as unresolved.
5. Run affected checks and required final integration gates. Keep failed attempts and coverage gaps visible. Keep earlier results inspectable and mark which claims they can no longer support.

## Expected outcome and assessment

Expected outcome: every relied-on result applies to the actual target and context, and stale evidence cannot close a current gate.

Use the [assessment evidence record](../assessment-evidence-records.md). Test unchanged inputs; then change the artifact, criteria, evaluator, fixture, configuration, tools, the environment, and one relevant dependency in separate cases. Include an uncommitted candidate whose patch changes before acceptance. Test an expired observation, a missing identity, a blocked check, and an unrelated change that does not affect the claim.

- **Pass:** unchanged and justified unaffected evidence remains usable; each affected, expired, missing, or blocked case cannot satisfy the gate until valid evidence exists; original records are retained.
- **Fail:** stale evidence satisfies acceptance, an unrun check is reported as passed, or previous evidence is relabeled as a fresh observation. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** input identity or the dependency relationship cannot be established sufficiently to decide applicability.
- **Evidence:** dependency map, before/after identities, freshness rules, reuse decisions, rerun outputs, and evaluator/time/result records.

## Dependencies and limitations

Requires inspectable identities and a credible dependency map. [Evidence traceability](evidence-traceability.md) links claims to records; this control checks continued applicability. Use [qualified artifact promotion](qualified-artifact-promotion.md) to check the destination object. Valid evidence can still be incorrect if the evaluator or original observation was unsound.

## Source and adoption

The pinned Software Factory guidance[^software-factory] supports mapping changed behavior and failure risk to selected checks and evidence, invalidating results when relevant source, configuration, dependency, fixture, or accepted-criteria inputs change, preserving unaffected results with their original identity, and rerunning affected checks and required integration gates. The input inventory, dependency map, freshness rules, and assessment cases above are catalog adaptations proposed for this control; they are not presented as requirements from that source or as reported operational results. Two earlier citations were removed from the support basis because the `semantic_search` repository is private and its policy text is not available to every catalog consumer. Authenticated GitHub access on 2026-09-29 confirmed the exact paths (`factory/policies/verification.md` and `factory/policies/execution.md`) at pinned commit `70cfad0de635197f36f14e5276dec145483c5128`; this control does not rely on their contents as support. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verification-selection.md).
