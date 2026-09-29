---
type: Control
title: "Adversarial regression assessment"
description: "Rerun scoped attack and legitimate-work fixtures after relevant changes and enforce the declared disposition."
status: stable
family: quality-and-validation
sources:
  - id: AML.M0035
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L6928
    title: "AML.M0035: AI Red Team"
---

# Adversarial regression assessment

[Controls](./) · [Adoption](../adoption.md) · [ATLAS assessment guide](../atlas-threat-assessment.md)

## Purpose and applicability

Detect security regressions in the complete workflow. Apply when a factory exposes AI components to adversarial inputs or changes models, tools, grants, memory, retrieval, or execution boundaries. Use authorized isolated environments for harmful, costly, or disclosure-oriented fixtures.

## Requirement

Maintain a versioned set of applicable risk scenarios, attack fixtures, legitimate positive cases, expected effects, and evidence requirements. Define reassessment triggers and release/operation dispositions before observing results. Execute the relevant suite against the changed system revision and enforce the disposition for fail or inconclusive results. Record untested scenarios explicitly and preserve failures for remediation and retest.

## Implementation

1. Assign assessment and release owners, authorized scope, synthetic data, resource limits, stop conditions, and cleanup responsibilities.
2. Map scenarios to the selected control revisions and actual execution paths. Include composed and later-session behavior where relevant.
3. Pin system and fixture versions. Specify observable success/failure criteria and how stochastic behavior is sampled; declare run counts and thresholds in advance.
4. Run the suite, retain failures and uncertainty, enforce the release disposition, and retest fixes. Do not silently remove failing cases or lower thresholds to obtain a pass.

## Expected outcome and assessment

Expected outcome: applicable regressions are detected and the declared release or operation decision follows the evidence.

Assess the assessment process using a known-good fixture system, a deliberately weakened boundary, missing observations, and a relevant configuration change. Include a legitimate task that a blanket deny-all defense would break. Verify that the change triggers the suite and that failed/inconclusive cases reach the predeclared disposition.

**Pass:** the known-good and positive cases meet their criteria, the seeded weakness fails, missing evidence is inconclusive, and all required triggers/dispositions occur. **Fail:** a missed seeded weakness, misreported result, omitted required run, or bypassed disposition. **Inconclusive:** process evidence is insufficient. This process assessment can pass while the tested factory fails security fixtures.

Retain the scope and path inventory, policy and implementation revisions, predeclared criteria, sanitized fixture inputs, observations, evaluator, time, and dispositions. Use synthetic data and isolated test resources. A pass applies only to the tested scope and revision; omitted paths remain unassessed.

## Dependencies and limitations

Depends on representative scenarios and observable effects; a finite suite does not establish universal resistance. Apply each selected control's own criteria. [Security event traceability](security-event-traceability.md) supports investigation, while [outcome verification](outcome-verification.md) assesses beneficiary outcomes separately.

Addresses the scenarios linked from the [ATLAS assessment guide](../atlas-threat-assessment.md). Adopt this control and any selected dependencies using the [pinned adoption record](../adoption.md#record-the-adoption); resolve relative references against the same catalog revision.

## Source basis

This catalog requirement and its assessment are an adaptation informed by AML.M0035[^AML.M0035]. The mapping is a catalog interpretation, not a MITRE endorsement or evidence of effectiveness. No operational assessment is asserted.

[^AML.M0035]: MITRE ATLAS content 2026.09; pinned entry in `sources`.
