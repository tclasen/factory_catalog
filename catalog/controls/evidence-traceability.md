---
type: Control
title: "Evidence traceability"
description: "Make material factual claims and their supporting evidence inspectable."
status: stable
family: knowledge-and-evidence
---

# Evidence traceability

[Controls](./) · [Adoption](../adoption.md) · [Control families](../control-families.md)

## Purpose and applicability

Make material factual claims inspectable so unsupported or misrepresented claims can be detected before reliance on them. Apply when an output presents factual claims as a basis for a decision, recommendation, publication, or instruction. Pure invention with no factual assertions can be excluded with recorded rationale. Mixed outputs still require factual portions to be assessed.

## Requirement

Before accepting an output, identify its material claims and link each to supporting evidence or explicitly mark it as an assumption, inference, or unsupported claim. Record source location and revision or access time. A designated reviewer must check that sources support the claims in context and that contradictions and limitations are represented. Unsupported material claims must be corrected, qualified, or removed before acceptance.

Material means that an error could change the output's conclusion or the recipient's action. Define this scope before review; do not narrow it afterward to obtain a pass.

## Implementation

1. Assign an output owner and reviewer; document whether review is independent of production.
2. Keep a claim table with claim location, source reference, source version/date, relevant passage or calculation, and claim status.
3. Distinguish direct support from inference. Retain contrary evidence and explain unresolved conflicts.
4. Have the reviewer inspect the full output for omitted material claims, then verify the table against sources.
5. Correct failures and retain the reviewed output revision, table, and disposition. Protect sensitive source material according to its access rules.

Mechanism: human procedure or an automated check with documented coverage. A model's assertion that it checked itself is not an independent review. Automated link checking establishes reachability, not support for a claim.

## Expected outcome and assessment

Expected outcome: every material claim in the accepted revision has inspectable support or an explicit qualification that prevents it from being presented as established fact.

Assess one declared output revision. Inspect all material claims, including those missing from the producer's table. Check source accessibility to the reviewer, relevant context, revisions, and qualification of inferences. In a separate fixture, insert a fabricated citation, a source that contradicts its claim, and an unsupported claim missing from the table; verify that acceptance is withheld for all three.

- **Pass:** all material claims in the assessed output meet the requirement, and all three negative cases are detected and withheld from acceptance.
- **Fail:** an identified material claim violates the requirement, or a negative case is accepted.
- **Inconclusive:** necessary sources or review records cannot be inspected; do not treat this as acceptance.
- **Evidence:** assessed revision, claim table, reviewer identity, source references, negative-case results, and dispositions.

For the [retrieval-poisoning scenario](../risks/retrieval-poisoning.md), use a reachable citation to an altered policy that contradicts the memo. The existing source-support check must still withhold acceptance. Successful link resolution does not satisfy the check; corpus admission is assessed separately under [retrieval corpus integrity](retrieval-corpus-integrity.md).

## Dependencies and limitations

Requires source access, suitable reviewer competence, and an acceptance process that acts on findings. Traceability does not prove source truth, completeness of research, or absence of coordinated misinformation. Review all material claims in the stated scope; sampling supports only a narrower finding. This catalog defines the assessment; it does not claim that an implementation has passed it.
