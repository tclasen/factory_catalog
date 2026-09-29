---
type: Guide
title: "Evaluate agent coverage across tasks and conditions"
description: "Design representative agent evaluations with protected comparisons, qualified judges, and visible coverage gaps."
catalog_version: "v0.1.0"
status: draft
tags: [evaluation, quality, ai-research]
sources:
  - id: product-evals
    resource: https://hamel.dev/blog/posts/evals/
    title: "Your AI Product Needs Evals"
  - id: validators
    resource: https://arxiv.org/abs/2404.12272
    title: "Who Validates the Validators?"
  - id: helm
    resource: https://arxiv.org/abs/2211.09110
    title: "Holistic Evaluation of Language Models"
  - id: shades
    resource: https://proceedings.mlr.press/v81/buolamwini18a.html
    title: "Gender Shades"
  - id: multi-turn
    resource: https://developer.salesforce.com/blogs/2025/11/automate-multi-turn-agent-testing-with-conversation-history-in-agentforce
    title: "Automate Multi-Turn Agent Testing with Conversation History in Agentforce"
  - id: leakage
    resource: https://reproducible.cs.princeton.edu/
    title: "Leakage and the Reproducibility Crisis in ML-based Science"
---

# Evaluate agent coverage across tasks and conditions

[Research basis](../ai-leaders-research.md) · [Assessment records](../assessment-evidence-records.md) · [Adoption](../adoption.md)

## Purpose and applicability

Use when comparing agent configurations, promoting a changed model or harness, or checking whether a reported improvement applies to intended users. This guide applies [acceptance coverage](../controls/acceptance-coverage.md), [protected acceptance](../controls/protected-acceptance.md), [verifier qualification](../controls/verifier-qualification.md), and [measured process improvement](../controls/measured-process-improvement.md). It adds an assessment procedure, without establishing another general evaluation control.

Product evaluation needs task-specific feedback.[^product-evals] HELM provides a precedent for reporting multiple metrics and uncovered scenarios; Gender Shades demonstrates why aggregate performance can conceal differences across groups.[^helm][^shades] These findings motivate coverage analysis; their historical scores are not predictions about a current deployment.

## Build the evaluation record

| Field | Record before the acceptance run |
|---|---|
| Decision and owner | The release, configuration, or autonomy decision; accountable owner and evaluator |
| Target | Exact model, prompt, harness, tools, retrieval corpus, memory initialization, and evaluator revisions |
| Population | Eligible work and users, data period, environments, exclusions, and sampling method |
| Coverage | Task types, languages, user groups where relevant, difficulty, tool permissions, conversation length, source freshness, and failure classes |
| Evidence roles | Development examples, judge-calibration examples, protected acceptance examples, and later production observations |
| Criteria | Required outcomes, mandatory invariants, metric definitions, thresholds, error severity, repetition plan, and uncertainty method |
| Cost boundary | Model and tool usage, retries, human review, repair, queue delay, and end-to-end completion time |
| Disposition | Pass, fail, or inconclusive for each required condition; owner and next action |

Only collect user attributes needed and authorized for the evaluation under [approved data processing](../controls/approved-data-processing.md). If a relevant group cannot be assessed, report that limit and narrow the deployment claim. Never infer sensitive attributes just to fill a table.

## Procedure

1. **Define accepted behavior.** Include successful completion, appropriate refusal or escalation, and actual destination state for tool actions. Preserve valid alternative solutions. Choose task strata for the real deployment; a stratum is a defined subset such as long conversations or a supported language.
2. **Construct labeled evidence.** Sample authorized work records and add independently designed boundary and failure cases. Identify synthetic examples and inspect their labels. Check duplicates, shared documents or entities, preprocessing, and time boundaries across development and test sets. Leakage can invalidate a claimed comparison.[^leakage]
3. **Qualify the evaluator.** Use objective checks where feasible and competent reviewers for semantic judgments. Qualify model judges on independently labeled positives and plausible errors. Keep false acceptance, false rejection, disagreement, and variation visible. Apply the existing verifier control before relying on the judge.
4. **Version changing criteria.** Shankar and coauthors describe how reviewing outputs can change evaluation criteria.[^validators] During development, record the changed rationale and labels. Before acceptance, freeze the rubric. If a material flaw is discovered afterward, retain the original results, approve a revised rubric through the applicable owner, and reevaluate both baseline and candidate. Do not retrospectively recast a failed gate as a pass.
5. **Evaluate trajectories and results.** Include user corrections, topic switches, incomplete retrieval, permission denial, tool failure, interruption, and resumed work. Salesforce's tutorial illustrates replaying cumulative conversation history.[^multi-turn] Replay is useful but cannot by itself prove live tool effects or state isolation. Observe those separately.
6. **Compare on common conditions.** Use the same task distribution and accounting boundary for baseline and candidate. For stochastic behavior, declare repetitions and initial state, then retain all runs. Reset unintended cross-run memory. Record intentional learning as a separate condition. Report per-stratum outcomes, counts, uncertainty, and the overall result; a mean must not hide a failed invariant.
7. **Observe deployment within authority.** Where release is separately authorized, use bounded exposure and a rollback condition under [qualified artifact promotion](../controls/qualified-artifact-promotion.md). Production observations can reveal distribution changes and feed later development; preserve the independence of the next acceptance test.

## Assessment design

The following are proposed fixtures for the procedure, not executed assessments of an agent.

| Fixture | Expected observation |
|---|---|
| Candidate improves the overall score but fails a required supported-language stratum | The affected release claim fails or remains blocked; the average cannot override the requirement. |
| Same source document contributes near-duplicate development and test cases | Leakage is flagged and the affected comparison is withheld until repaired and rerun. |
| A judge approves a persuasive answer with a fabricated supporting citation | Qualification detects the false acceptance and prevents reliance on that property. |
| A valid alternative answer uses different wording and a correct permitted tool sequence | It receives the expected valid disposition rather than failing an exact-text or exact-path match. |
| A late user correction changes the intended destination | Subsequent tool effects follow the current authorized destination; stale context cannot count as success. |
| A revised rubric changes which candidate wins | Both candidates are rerun against the recorded new rubric, with the change visible. |
| Required observations or enough examples for a declared claim are unavailable | The result is inconclusive and the unsupported claim is narrowed. |

**Pass for the procedure:** required coverage and evidence are reconciled; known defective cases block the affected claim; valid alternatives are accepted; revisions and uncertainty are visible. **Fail:** a known failure, leaked test, unqualified judge, or hidden criterion change supports acceptance. **Inconclusive:** required observations or independent labels cannot support a decision. These dispositions assess the procedure; an agent's qualification has its own recorded thresholds and results.

Retain the sampling and coverage record, protected case references, labels and disagreements, candidate and evaluator revisions, all raw verdicts, observed tool effects, resource totals, and the signed-off disposition. Protect raw data according to its access and retention rules.

## Limits and adoption

There is no universal sample size, judge, metric, or confidence threshold. A coverage table can still miss important harm; involve people who understand the tasks and affected users. Full methods and code for the three academic papers were not reproduced in this research; only their abstracts were reviewed. The detailed procedure above is a catalog synthesis, not a procedure claimed by every source.

Record adoption of the linked controls using their identities, catalog v0.1.0, and exact commit URLs under the [adoption procedure](../adoption.md#record-the-adoption). Passing this guide's fixtures does not establish general model safety or authorize deployment.

[^product-evals]: [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/).
[^validators]: [Shankar and coauthors: Who Validates the Validators?](https://arxiv.org/abs/2404.12272), abstract reviewed.
[^helm]: [Liang and coauthors: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110), abstract reviewed.
[^shades]: [Buolamwini and Gebru: Gender Shades](https://proceedings.mlr.press/v81/buolamwini18a.html), abstract reviewed.
[^multi-turn]: [Salesforce: Multi-turn agent testing](https://developer.salesforce.com/blogs/2025/11/automate-multi-turn-agent-testing-with-conversation-history-in-agentforce).
[^leakage]: [Kapoor and Narayanan: Leakage and reproducibility](https://reproducible.cs.princeton.edu/).
