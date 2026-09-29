---
type: Guide
title: "Apply research from 100 AI leaders and corporate sources"
description: "Use an annotated research set to choose evidence and assessments for agents, enterprise AI, and AI factory infrastructure."
status: draft
tags: [ai-research, assessment, adoption]
sources:
  - id: agents
    resource: https://www.anthropic.com/engineering/building-effective-agents
    title: "Building effective agents"
  - id: factory
    resource: https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html
    title: "Building AI Factories for the Enterprise"
  - id: evals
    resource: https://hamel.dev/blog/posts/evals/
    title: "Your AI Product Needs Evals"
---

# Apply research from 100 AI leaders and corporate sources

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## What to use first

Use the three assessment guides below to turn published ideas into local evidence. They apply existing controls and add concrete records and failure cases. They establish no new control families, actor registry, or operational passes.

| Priority | Addition | Decision it supports | Existing coverage it applies |
|---|---|---|---|
| 1 | [Agent evaluation coverage](guides/agent-evaluation-coverage.md) | Whether an agent improvement holds across relevant tasks, users, conversation turns, and failure classes | Acceptance coverage, protected acceptance, verifier qualification, measured process improvement |
| 2 | [AI factory workload qualification](guides/ai-factory-workload-qualification.md) | Whether a combined infrastructure stack can deliver accepted work under normal load, bursts, and failure | Task configuration selection, resource budgets, dependency change, service recovery |
| 3 | [Semantic cache assessment](guides/semantic-cache-assessment.md) | Whether answer reuse preserves permission, meaning, freshness, and quality | Approved data processing, corpus integrity, persistent-state recovery |

Priority is an editorial judgment about the catalog's needs, based on applicability and a feasible assessment. It is not a ranking of published effectiveness. The existing [Agent Patterns review](agentpatterns-opportunities.md) already identifies retrieval coverage, tool usability, and compaction opportunities; this research complements those proposals.

## Selection and review method

**Scope:** 100 named entries: 60 corporate organizations or separately identifiable product/platform teams and 40 individuals. “Top” is interpreted as a curated set of influential builders, researchers, educators, infrastructure suppliers, and enterprise practitioners with material relevant to this catalog. No defensible universal ranking combines research impact, infrastructure scale, business adoption, and educational usefulness, so ordinal ranks and unsupported market-share claims are omitted.

Each entry was selected for at least one observable contribution: a published technical method or research paper, an operating platform with implementation documentation, a production or enterprise account, or a substantial educational resource. Its selection basis, reviewed source, transferable learning, graph connection, and limitation are recorded together. The set deliberately includes competing approaches and perspectives. It is purposive research, not a systematic census or an independently scored league table.

**Inspection date:** 2026-09-28, America/Los_Angeles. Current documentation and older foundational material are both included. A source's inspection date is not its publication date. Preserve paper versions and document revisions when adopting a method; mutable pages, product names, availability, and interfaces can change.

**Review coverage:** primary material was reached for all 100 entries after checking replacement pages where needed. The depth is deliberately visible:

| Label | Entries | Meaning |
|---|---:|---|
| Sections | 63 | Selected relevant article, documentation, specification, or research-resource sections inspected; not a complete corpus audit |
| Abstract | 11 | Author list and published abstract inspected; full methods, code, and results not reproduced |
| Product | 8 | Product explanation or policy page screened; vendor claims remain unverified |
| Hub | 6 | Resource collection, article summaries, or learning introduction screened; linked works not all reviewed |
| Curriculum | 6 | Course description and syllabus/outline inspected; lessons and learner outcomes not assessed |
| Position | 6 | Strategy, mission, or position essay inspected; predictions treated as views |

Search located primary pages; it was not treated as a substitute for reviewing them. Direct text retrieval recovered several pages the research browser could not render. HPE's readable QuickSpecs replaced its empty administration page. LeCun's coauthored I-JEPA abstract replaced an inaccessible position paper. Liu's Instructor project documentation replaced an unavailable linked RAG course. These substitutions narrow the findings to the material named in each entry.

The 100 entries do not represent 100 independent evidence streams. Individuals may work with listed organizations; papers have coauthors; platform teams can share a corporate parent; supplier blogs may reuse the same benchmark. Corporate sources include AWS under Amazon and Weights & Biases alongside CoreWeave. Do not count agreement between these entries as independent replication. The English-language public-web emphasis underrepresents private deployments, non-English material, smaller regional providers, and unpublished negative results. Inclusion does not certify leadership, safety, or current employment.

## Find relevant sources

Each linked guide contains ten annotated entries, source frontmatter, keyed attribution, and links to the controls or assessment procedures it informs.

| Research area | Entries | Useful for |
|---|---:|---|
| [Model platforms](research/ai-leaders-model-platforms.md) | 10 corporate | Agent patterns, model evidence, tool access, production ML |
| [AI factory infrastructure](research/ai-leaders-infrastructure.md) | 10 corporate | Compute, network, storage, facilities, operational telemetry |
| [Data and retrieval](research/ai-leaders-data-retrieval.md) | 10 corporate | Retrieval, graph meaning, evaluation data, caching |
| [Agent engineering](research/ai-leaders-agent-engineering.md) | 10 corporate | Persistence, serving, tracing, evaluation, ingestion |
| [Enterprise adoption](research/ai-leaders-enterprise-adoption.md) | 10 corporate | Business processes, industrial systems, human handoffs |
| [Applied AI products](research/ai-leaders-applied-products.md) | 10 corporate | Model variants, coding systems, search, education |
| [Practitioner education](research/ai-leaders-practitioner-education.md) | 10 people | Evaluation, architecture, security, task allocation |
| [Research leadership](research/ai-leaders-research-leadership.md) | 10 people | Research methods, scientific assessment, strategy assumptions |
| [Systems education](research/ai-leaders-systems-education.md) | 10 people | Production ML, representations, evaluation, hardware efficiency |
| [Evaluation and society](research/ai-leaders-evaluation-society.md) | 10 people | Documentation, subgroup evaluation, reproducibility, resource impacts |

## Findings and boundaries

**Choose a system for the task.** Anthropic's agent guidance favors simple compositions and explicit performance/cost tradeoffs.[^agents] The catalog already supports this through [implementation selection](factory-implementation-selection.md) and [task configuration selection](controls/task-configuration-selection.md). A new agent taxonomy would add little here.

**Measure accepted work.** Husain's product evaluation account connects task-specific tests, trace inspection, and product experiments.[^evals] The evaluation guide adds records for coverage, changing rubrics, and comparisons across deployment conditions. It does not replace [outcome verification](controls/outcome-verification.md).

**Connect the two meanings of AI factory.** NVIDIA uses the term for an integrated compute and software platform constrained by data-center conditions.[^factory] This catalog describes systems for producing knowledge-work outcomes. The infrastructure platform can support factory activities, but GPU utilization, token throughput, or a vendor reference design cannot establish that the resulting work is correct, authorized, or valuable. The workload guide connects platform evidence to outcome evidence without redefining the ontology.

**Preserve uncertainty and disagreement.** Research strategy essays offer different forecasts and explanations. Retain them as scenario inputs. Product pages establish what a vendor describes, not achieved savings, compliance, safety, or universal superiority. No numerical productivity, benchmark, environmental, or cost improvement is adopted as a catalog result.

## Apply and maintain the research

1. Select a concrete outcome and an accountable owner using [accepted work definition](controls/accepted-work-definition.md).
2. Follow relevant source entries, distinguish source claims from our proposed application, and inspect deeper material where the review depth is insufficient for the decision.
3. Reuse the linked controls. For adoption, retain their identities, catalog version from the adopted revision, and exact source commit under the [adoption procedure](adoption.md#record-the-adoption).
4. Define local fixtures and acceptance criteria before assessing a candidate. Preserve failed, inconclusive, and missing results.
5. Revisit source applicability after model, data, evaluator, workload, permission, or infrastructure changes. Add new research at its own concept path; generated navigation discovers it without a shared registry.

The catalog comparison used the concept files at `c074a864b457cc2407da6724624bc84133a60fdd`, with targeted reading of relevant controls and guides. The resulting procedures are proposed applications awaiting local assessment. Review should decide whether these guide boundaries are useful and whether deeper primary-method review is needed for a particular adoption. There is no new release baseline or implied authority to merge, deploy, or buy a product.

[^agents]: [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
[^factory]: [NVIDIA: Building AI Factories for the Enterprise](https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html).
[^evals]: [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/).
