# Review worksheet

[MVP overview](index.md)

## Questions the model must answer

These are conceptual walkthroughs, not executed control assessments.

| Question | Where to inspect | Current answer / limitation |
|---|---|---|
| Can the same work type appear in different domains? | [Vocabulary](vocabulary.md), all examples | Evaluation appears in research, learning, and contracts; domain is a separate profile field |
| Can one factory contain different authority boundaries? | [Contract activities](examples/contracts.md#activities-autonomy-and-authority) | Drafting, negotiation, signing, and records have separate permissions |
| Can a control be justified without a security threat? | [Outcome verification](controls/outcome-verification.md) | It supports useful outcomes and truthful reporting, including ordinary failure |
| Can completed work fail to achieve its purpose? | [Learning](examples/learning.md) | Completing a course does not establish improved ability |
| Can a control pass when the outcome fails? | [Outcome assessment](controls/outcome-verification.md#expected-outcome-and-assessment) | Yes, if it correctly detects and reports failure and follows its procedure |
| Can an exclusion be challenged? | [Research](examples/research.md) | Exclusion depends on tool inventory; unknown paths make applicability undetermined |
| Can a reader distinguish proposed from effective? | All controls and examples | No implementation or effectiveness assessment is claimed; document validation is separate |
| Can individually assessed components still leave system risk? | [Model rules](model.md#rules-that-preserve-meaning) | Shared credentials, memory, handoffs, and combined powers require system review |

## Try describing another factory

Use this compact worksheet; leave unknowns explicit.

1. **Purpose:** beneficiary, intended outcome, accountable owner, exclusions.
2. **Work:** types, domain, input/output artifacts, workflow, roles.
3. **Operating boundaries:** activity-specific autonomy, authority, escalation, tools, memory, sensitive data, external exposure.
4. **Risks and objectives:** cause/condition/harm scenarios and desired quality outcomes.
5. **Control selections:** applicable / not applicable / undetermined; rationale, assumptions, decision owner, reassessment trigger.
6. **Implementation:** proposed / implemented / retired; scope, owner, mechanism, limits, dependencies, adoption references when real.
7. **Assessment:** method, criteria, target revision, evaluator, time, evidence, result; missing evidence and residual risks.

If fields do not fit, record the mismatch before adding new categories. A software deployment example is a useful next case for dependency changes, machine-verifiable tests, and recovery, which this MVP does not fully cover.

## Decisions for the owner

- Is this the right conceptual boundary: factories, work, governance, and evidence?
- Are the work labels useful, especially combined labels such as monitoring/response and case/transaction processing?
- Are control families understandable without forcing duplicate controls into multiple locations?
- Is the distinction between control, implementation, and assessment clear enough for reuse?
- Which concepts should become independent OKF documents, and which should remain embedded fields?

Proposed next increment after review: agree the minimum domain schema and identity policy, then author a small OKF bundle from approved concepts. Do not interpret approval to iterate on this prototype as baseline or release approval.

## Version impact and validation boundary

This adds compatible design documentation. Intended impact is **minor** for new content under CONTRIBUTING.md; the baseline hold keeps the catalog at **v0.1.0**. No existing adopted identities or references change, and no migration is required.

Review Markdown links, heading targets, table consistency, completeness of the stated assessment procedures, and the examples' applicability reasoning. These checks validate the proposal as documentation. Operational control assessments require implementations and runtime evidence that this MVP does not provide.
