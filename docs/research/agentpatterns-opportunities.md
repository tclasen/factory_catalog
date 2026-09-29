---
type: Guide
title: "Evaluate Agent Patterns additions"
description: "Prioritize gaps in retrieval, context preservation, tool usability, and evaluation without duplicating existing factory controls."
status: draft
sources:
  - id: ap-about
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/about.md
    title: "Agent Patterns: About"
  - id: ap-listing
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/exhaustive-retrieval-for-listing-questions.md
    title: "Agent Patterns: Exhaustive retrieval for listing questions"
  - id: ap-sufficiency
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/retrieval-sufficiency-gate.md
    title: "Agent Patterns: Retrieval sufficiency gate"
  - id: ap-retention
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/per-type-retention-under-compaction.md
    title: "Agent Patterns: Per-type retention under compaction"
  - id: ap-reacquisition
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/reacquisition-cost-measurement.md
    title: "Agent Patterns: Reacquisition cost"
  - id: ap-tools
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/semantic-tool-output.md
    title: "Agent Patterns: Semantic tool output"
  - id: ap-descriptions
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/tool-description-quality.md
    title: "Agent Patterns: Tool description quality"
  - id: ap-evals
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/verification/multi-run-shuffled-order-evaluation.md
    title: "Agent Patterns: Multi-run shuffled-order evaluation"
  - id: ap-delegation
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/patterns/agent-design/delegation-threshold-calibration.md
    title: "Agent Patterns: Delegation threshold calibration"
  - id: ap-traces
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/observability/subagent-otel-trace-correlation.md
    title: "Agent Patterns: Subagent trace correlation"
  - id: tools-primary
    resource: https://www.anthropic.com/engineering/writing-tools-for-agents
    title: "Anthropic: Writing effective tools for agents"
  - id: compaction-primary
    resource: https://arxiv.org/abs/2606.22528v2
    title: "Chen: Governance Decay, v2"
  - id: memory-primary
    resource: https://arxiv.org/abs/2608.18066v2
    title: "Ye et al.: On the Fragility of Self-Improving Agents, v2"
  - id: retrieval-primary
    resource: https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf
    title: "Cormack and Grossman: TREC 2015 Total Recall Track Overview"
  - id: delegation-primary
    resource: https://www.anthropic.com/engineering/multi-agent-research-system
    title: "Anthropic: How we built our multi-agent research system"
  - id: otel-primary
    resource: https://opentelemetry.io/docs/concepts/context-propagation/
    title: "OpenTelemetry: Context propagation"
---

# Evaluate Agent Patterns additions

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Catalog](../../catalog/index.md) · [Ontology](../../catalog/ontology.md) · [Control families](../../catalog/control-families.md)

## Recommendation and comparison scope

Prioritize **retrieval completeness** and **tool usability qualification** as candidate controls. Add focused assessment guidance for **context compaction**, **learning across tasks**, **delegation economics**, and **operational trace correlation**. These are proposed boundaries for review; this guide establishes no new control requirements or operational passes.

The source comparison began with 44 concept files at `02dc936979bf60bb9f03d71ec629a796f2d91b1c`. The coverage map below is reconciled with catalog revision `fe67a36`: the security and factory-operation controls from PRs #18 and #19 are available in the catalog. The original external-source review remains bounded by the source revisions and inspection scope below. Check the current control requirements before implementing a recommendation.

Source: [AgentPatterns.ai](https://agentpatterns.ai/), inspected on 2026-09-28, and its public Markdown mirror at `7d655a99fdebfa373ceacfcb3a6171c53da1b883`. The mirror contains 1,657 Markdown files, including navigation and repository guidance. This review scans topic navigation and the file inventory, then reads selected relevant pages; it is not an exhaustive validation of every article or citation. Tool-specific setup, training, GEO, and framework inventories receive only scope screening.

Agent Patterns describes itself as a practitioner reference and publishes its corpus with sources.[^ap-about] Credit: **Agent Patterns**, © 2025–2026, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with the [pinned source license](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/LICENSE). The comparisons and proposed assessments here are rewritten adaptations; they do not imply endorsement. Pinned source pages and their underlying references remain linked below.

## Highest-priority additions

Priority reflects a concrete uncovered decision or failure test, applicability across factories, and a feasible assessment. It does not rank proven effectiveness.

### 1. Retrieval completeness and evidence sufficiency

**Source contribution:** distinguish a ranked search result from an exhaustive answer, and require a separate reason to believe the evidence covers the question.[^ap-listing][^ap-sufficiency] NIST's Total Recall work provides primary precedent for assessing recall, effort, and stopping rules.[^retrieval-primary]

**Existing coverage:** [evidence traceability](../../catalog/controls/evidence-traceability.md) checks support for claims; [semantic_search lessons](semantic-search-learnings.md#5-evaluate-extraction-and-retrieval-separately) separate extraction and retrieval evaluation. [Retrieval corpus integrity](../../catalog/controls/retrieval-corpus-integrity.md) governs source admission and withdrawal. None supplies a dedicated procedure for substantiating “all matching items” or withholding a completeness claim when retrieval is truncated.

**Proposed node:** a control in `knowledge-and-evidence`, provisionally titled “Retrieval coverage qualification.” Define the corpus revision and accessible scope, required answer shape, independent coverage signal, and disposition for incomplete retrieval. Prefer a complete index, pagination, or structured query when available. Report inaccessible sources, unknown coverage, and budget exhaustion explicitly. An empty result, a repeated search with no new hits, or a confident answer does not alone establish completeness. Structural coverage also does not prove correct synthesis.

**Assessment design:** use a known fixture with matches beyond the first page, duplicates, a withdrawn item, and an inaccessible partition. A complete authorized enumeration should succeed. Missing matches must prevent an exhaustive claim; unavailable partitions must narrow the claim. Retain expected and retrieved sets, corpus/query revisions, continuation state, omissions, and the final disposition. Select thresholds for the actual use case; do not import a universal iteration count or confidence threshold.

### 2. Tool usability qualification

**Source contribution:** evaluate whether tool descriptions, outputs, and errors help an agent choose and use a tool correctly.[^ap-descriptions][^ap-tools] Anthropic's primary guidance combines realistic task evaluation with description refinement, output shaping, and inspection of tool errors.[^tools-primary]

**Existing coverage:** [controlled dependency change](../../catalog/controls/controlled-dependency-change.md) requires qualification of changed tools. [Tool and dependency admission](../../catalog/controls/tool-and-dependency-admission.md) and [tool input/output validation](../../catalog/controls/tool-input-output-validation.md) govern admission and contracts. These protect identity and contracts, but do not explicitly assess whether a permitted, valid interface is understandable enough for its intended callers.

**Proposed node:** a control in `quality-and-validation`, provisionally titled “Agent tool usability qualification.” Assess selection, parameter construction, interpretation, pagination, and recovery using representative tasks on a pinned model/harness/tool configuration. Accept equivalent valid strategies. Preserve stable object IDs alongside readable labels whenever subsequent actions depend on identity; two people or files can share a name. Errors may explain a permitted correction but cannot grant new authority.

**Assessment design:** include two similarly named tools, same-name objects with different IDs, partial results, empty results, and a recoverable invalid parameter. Check actual destination state and task outcomes. Reject qualification if the agent silently acts on the wrong object or mistakes partial output for a complete result. Retain selection errors, repair attempts, latency, and outcome evidence. Use predeclared repeated trials for variable behavior; passing schema tests alone cannot qualify usability.

### 3. Context preservation through compaction

**Source contribution:** test which constraints and task state survive compression, and count work spent reacquiring omitted information.[^ap-retention][^ap-reacquisition] Chen's primary paper abstract reports compaction-induced loss of constraints in its benchmark; that supports testing the failure mode, not claiming universal protection from a particular mitigation.[^compaction-primary]

**Existing coverage:** [safe work resumption](../../catalog/controls/safe-work-resumption.md) already preserves scope, grants, evidence, and outstanding obligations. The [work record](../../catalog/guides/factory-work-record.md) supplies a durable representation; [required guidance selection](../../catalog/controls/required-guidance-selection.md) and [durable work handoff](../../catalog/controls/durable-work-handoff.md) cover instruction discovery and persisted obligations. The remaining addition is a compaction-specific test procedure and measurement of information loss during a continuing session.

**Proposed form:** a guide applying those controls, rather than another general memory or handoff control. Inventory authoritative constraints, unresolved effects, source references, and completed work before compression. Recover canonical material before dependent action when a summary is insufficient. Treat a summary as a derived artifact; pinning text is no substitute for [external enforcement](../../catalog/controls/bounded-external-action.md).

**Assessment design:** compare uncompressed and repeatedly compacted runs with a late correction, an unresolved external effect, and an omitted constraint. Authorized work should still succeed; lost essential state must trigger recovery or a scoped stop. Record preserved and missing items, changed decisions, reacquisition calls, total cost, and latency. Retained evidence may include past events needed for audit or recovery; do not copy a blanket rule that episodic material is disposable.

## Further additions through existing concepts

### 4. Evaluation of learning across tasks

The site's repeated-run and shuffled-order article identifies task ordering as an evaluation variable when agents retain learned material.[^ap-evals] The inspected abstract of Ye et al. v2 confirms the focus on variance, task order, and underspecified memory; the site's article cites v1. Neither was reproduced in this review.[^memory-primary]

[Outcome verification](../../catalog/controls/outcome-verification.md), [autonomy change gates](../../catalog/controls/autonomy-change-gates.md), and [measured process improvement](../../catalog/controls/measured-process-improvement.md) already supply the general comparison requirements. Add a **specialized assessment guide**: reset initial memory between independent replicates, preserve intentional learning within each stream, record order and initial state, and compare fixed-memory and updating-memory conditions. Test plausible alternative orders when they represent the intended workload; preserve a required production order when shuffling would invalidate the task. Report variation, failures, and uncertainty, not only the best run. A gain that disappears or reverses under an applicable order cannot support an unconditional improvement claim. Choose repetitions and analysis for the decision; no universal minimum establishes reliability.

### 5. Delegation and context economics

The site's delegation guidance surfaces coordination, duplicated context, and review overhead.[^ap-delegation] Anthropic's account describes both benefits and substantial token costs in its research system, with limits for tightly dependent tasks.[^delegation-primary]

[Task configuration selection](../../catalog/controls/task-configuration-selection.md) already includes review, repair, latency, and total delivery cost. [Implementation selection](../../catalog/factory-implementation-selection.md) and [human/AI authority allocation](../../catalog/human-ai-authority.md) cover broader mechanism choices. Add a **comparison example** for direct execution, one agent, and delegated agents. Record task dependency, handoff preparation, duplicate retrieval, synthesis, human review, retries, and billed usage. Include the reacquisition cost of context compression.[^ap-reacquisition] Hold outcome criteria and accounting boundaries constant; state whether resource ceilings or realized spend are matched. Recommend delegation only within a supported task class and existing authority. Neither more agents nor fewer prompt tokens establishes a benefit. Assess with one independent task set and one tightly coupled set, keeping negative results visible.

### 6. Operational trace correlation

The site's trace-correlation page proposes linking agent and parent identities across execution boundaries.[^ap-traces] OpenTelemetry documents propagation of context across services; this does not establish coverage of every shell, queue, or connector in a local factory.[^otel-primary]

[Evidence traceability](../../catalog/controls/evidence-traceability.md) covers material claims; [bounded execution](../../catalog/controls/bounded-execution.md) covers limits. [Security event traceability](../../catalog/controls/security-event-traceability.md) already requires correlation and asynchronous-child investigation. Add an **implementation guide** that extends this work to quality, latency, and cost diagnosis. Relate work item, actor, parent, attempt, tool, revision, and observed outcome across queued and resumed operations. Test a missing child event, a retry, and an interrupted trace. The operator should reconstruct the declared workflow or see an explicit coverage gap. Use synthetic inputs and protected references, constrain telemetry destinations under [approved data processing](../../catalog/controls/approved-data-processing.md), and avoid using per-run IDs as unbounded metric dimensions. Correlation is not evidence authenticity; no new trace-storage product is implied.

## Content already captured or better deferred

| Site theme | Catalog disposition |
|---|---|
| Scoped permissions, approval, human oversight | Reuse [bounded external action](../../catalog/controls/bounded-external-action.md), [decision rights](../../catalog/controls/decision-rights-and-accountability.md), and [autonomy change gates](../../catalog/controls/autonomy-change-gates.md). |
| Retry safety, stopping, cancellation, parallel writers | Reuse [reconcile before retry](../../catalog/controls/reconcile-before-retry.md), [bounded execution](../../catalog/controls/bounded-execution.md), [safe resumption](../../catalog/controls/safe-work-resumption.md), and [isolated work](../../catalog/controls/isolated-parallel-work.md). Use [cancellation enforcement](../../catalog/controls/cancellation-enforcement.md), [exclusive mutation ownership](../../catalog/controls/exclusive-mutation-ownership.md), and [cumulative execution limits](../../catalog/controls/cumulative-execution-limits.md) for their specific boundaries. |
| Prompt injection, egress, memory poisoning, tool admission | Extend the [ATLAS assessment](../../catalog/atlas-threat-assessment.md) and its linked security controls; avoid duplicate controls under new pattern names. |
| Evaluator independence, protected tests, artifact qualification | Reuse [verifier qualification](../../catalog/controls/verifier-qualification.md), [protected acceptance](../../catalog/controls/protected-acceptance.md), and [qualified artifact promotion](../../catalog/controls/qualified-artifact-promotion.md) for the core concerns. |
| Instruction lifecycle and enforcement outside prompts | Reuse [instruction change control](../../catalog/controls/instruction-change-control.md) and [implementation trade-offs](../../catalog/factory-implementation-tradeoffs.md). |
| Product commands, framework taxonomies, training curricula, GEO | Defer unless a concrete factory outcome requires them. Product instructions age quickly; additional vocabulary alone does not create an assessable control. |

## Source quality and next decisions

Use this site to discover candidate mechanisms and primary references. Its value is breadth, linked evidence, and stated trade-offs. Its article labels and quantitative examples are not catalog assessments. The retrieval-sufficiency page itself identifies a proposed architecture whose evaluation it could not verify.[^ap-sufficiency] Several selected pages are marked emerging in their source metadata.

Primary-source checks here cover the tool-engineering article, the multi-agent research account, OpenTelemetry context propagation, the TREC overview, and the abstracts of the two pinned research papers. Benchmark code, full empirical methods for those papers, and the site's remaining citations were not audited. No numerical improvement claim is adopted.

For a next contribution, settle the two proposed control boundaries first, then author their full requirements and pass/fail assessments. Start the compaction guide alongside existing resumption and guidance-selection work. Keep the other three as focused guides or examples unless review identifies an independent requirement. Use existing families and ontology relationships; links here express overlap, application, and supporting evidence, not adoption or a pass. Actual adoption still requires the [pinned adoption record](../../catalog/adoption.md#record-the-adoption).

[^ap-about]: [Agent Patterns: About](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/about.md).
[^ap-listing]: [Agent Patterns: Exhaustive retrieval for listing questions](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/exhaustive-retrieval-for-listing-questions.md).
[^ap-sufficiency]: [Agent Patterns: Retrieval sufficiency gate](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/retrieval-sufficiency-gate.md).
[^ap-retention]: [Agent Patterns: Per-type retention under compaction](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/per-type-retention-under-compaction.md).
[^ap-reacquisition]: [Agent Patterns: Reacquisition cost](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/context-engineering/reacquisition-cost-measurement.md).
[^ap-tools]: [Agent Patterns: Semantic tool output](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/semantic-tool-output.md).
[^ap-descriptions]: [Agent Patterns: Tool description quality](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/tool-engineering/tool-description-quality.md).
[^ap-evals]: [Agent Patterns: Multi-run shuffled-order evaluation](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/verification/multi-run-shuffled-order-evaluation.md).
[^ap-delegation]: [Agent Patterns: Delegation threshold calibration](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/patterns/agent-design/delegation-threshold-calibration.md).
[^ap-traces]: [Agent Patterns: Subagent trace correlation](https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/observability/subagent-otel-trace-correlation.md).
[^tools-primary]: [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
[^compaction-primary]: [Chen: Governance Decay, v2](https://arxiv.org/abs/2606.22528v2).
[^memory-primary]: [Ye et al.: On the Fragility of Self-Improving Agents, v2](https://arxiv.org/abs/2608.18066v2).
[^retrieval-primary]: [Cormack and Grossman: TREC 2015 Total Recall Track Overview](https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf).
[^delegation-primary]: [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).
[^otel-primary]: [OpenTelemetry: Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/).
