# Outcome verification

[MVP overview](../index.md) · [Vocabulary](../vocabulary.md)

**Proposed control • v0.1.0 • family: Quality and validation**

This document is a review specimen, not an adopted catalog control. Its path is provisional. Actual adoption requires an approved stable identity and an exact source commit URL.

## Purpose and applicability

Prevent artifact completion from being mistaken for achievement of the factory's purpose. Apply whenever success is claimed for a beneficiary or downstream process. If only artifact delivery is in scope, explicitly limit the claim and assess its acceptance criteria; do not infer downstream benefit.

## Requirement

Before execution, record the intended outcome, beneficiary, measure, threshold, observation period, evaluator, and disposition for failure or unavailable evidence. Keep artifact acceptance and outcome verification separate. Report success only to the extent supported by the specified observations; disclose substitutions, missing data, and changes to criteria.

## Implementation

1. Define the desired change and plausible failure modes with the accountable owner.
2. Choose an observable measure that reflects the outcome. Identify proxies and their limitations. Use a baseline when claiming improvement.
3. Set criteria and an observation period before results are known. Define pause, rework, escalation, or follow-up for failure and uncertainty.
4. Assign an evaluator and provide protected access to the required evidence.
5. Collect observations, compare them with the criteria, and report artifact acceptance separately from outcome attainment.
6. Version changes to criteria and re-evaluate affected claims; do not retroactively lower thresholds and present an unchanged success claim.

## Expected outcome and assessment

Expected outcome: every success claim is bounded by a predeclared criterion and available evidence, and unmet or unobserved outcomes remain visible.

Inspect one completed case or a declared test fixture. Verify that criteria predate observations, evidence matches the beneficiary and period, calculations or judgments follow the method, and reporting reflects the result. Test cases with a completed artifact but failed outcome, missing evidence, and a met outcome.

- **Pass:** the control's records and method are complete, the three cases are reported respectively as unmet, unverified, and met, and required follow-up is recorded.
- **Fail:** unsupported success is reported, a result is misclassified, or a required procedure is omitted.
- **Inconclusive:** the assessment cannot inspect enough records to determine whether the procedure was followed.
- **Evidence:** versioned criteria, observation records, calculations or rubric, evaluator, result, and follow-up disposition.

A control assessment can pass while the factory outcome is unmet: truthful detection of failure is successful operation of this control. “Unverified” describes the outcome claim; the control assessment may still pass if it correctly handles unavailable outcome evidence.

## Dependencies and limitations

Requires a meaningful measure, evidence access, and an owner able to act on results. Observing improvement does not by itself establish causation. Long-term or subjective outcomes may remain uncertain; disclose that uncertainty. No assessment has been run for this proposal.
