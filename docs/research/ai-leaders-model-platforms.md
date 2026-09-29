---
type: Guide
title: "AI research sources: Model platforms"
description: "Select and apply relevant learning from ten corporate sources on model platforms."
status: draft
tags: [ai-research, source-review]
sources:
  - id: anthropic
    resource: "https://www.anthropic.com/engineering/building-effective-agents"
    title: "Building Effective AI Agents \\ Anthropic"
  - id: openai
    resource: "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/"
    title: "A practical guide to building agents | OpenAI"
  - id: google
    resource: "https://developers.google.com/machine-learning/guides/rules-of-ml"
    title: "Rules of Machine Learning:  |  Google for Developers"
  - id: microsoft
    resource: "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns"
    title: "AI Agent Orchestration Patterns - Azure Architecture Center | Microsoft Learn"
  - id: meta
    resource: "https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md"
    title: "Llama 3.1 evaluation details"
  - id: amazon-web-services
    resource: "https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html"
    title: "Machine Learning Lens - AWS Well-Architected Framework - Machine Learning Lens"
  - id: ibm
    resource: "https://www.ibm.com/think/topics/ai-governance"
    title: "What is AI Governance? | IBM"
  - id: cohere
    resource: "https://docs.cohere.com/docs/retrieval-augmented-generation-rag"
    title: "Retrieval Augmented Generation (RAG) | Cohere"
  - id: mistral-ai
    resource: "https://docs.mistral.ai/studio/agents/introduction"
    title: "Agents Introduction | Mistral Docs"
  - id: deepseek
    resource: "https://github.com/deepseek-ai/DeepSeek-R1"
    title: "DeepSeek-R1 model documentation"
---

# AI research sources: Model platforms

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Anthropic

**Selection basis:** Agent architecture guidance. **Review depth:** Sections.

**Learning:** Separates fixed workflows from agents that choose actions; recommends increasing complexity only when evaluation supports the tradeoff.[^anthropic]

**Catalog use — apply:** Use its patterns as comparison candidates; vendor experience does not prove a local benefit. Use [task configuration selection](../proposals/controls/task-configuration-selection.md).

## OpenAI

**Selection basis:** Agent implementation guidance. **Review depth:** Sections.

**Learning:** Organizes agent design around model decisions, tools, instructions, failure handling, and human handoff.[^openai]

**Catalog use — apply:** Test permissions and the stop/handoff path independently of output quality. Use [bounded external action](../../catalog/controls/bounded-external-action.md).

## Google

**Selection basis:** Production ML engineering guidance. **Review depth:** Sections.

**Learning:** Emphasizes simple baselines and robust pipelines before adding model complexity.[^google]

**Catalog use — apply:** Record a baseline and infrastructure failures before attributing gains to a model. Use [measured process improvement](../../catalog/controls/measured-process-improvement.md).

## Microsoft

**Selection basis:** Agent orchestration reference. **Review depth:** Sections.

**Learning:** Compares direct calls, a single agent, workflows, and multiple agents with coordination costs.[^microsoft]

**Catalog use — apply:** Choose a pattern from task dependencies and measured outcomes. Use [planning consistency](../proposals/controls/planning-consistency.md).

## Meta

**Selection basis:** Published evaluation methodology. **Review depth:** Sections.

**Learning:** Documents benchmark prompts, shot counts, output parsing, and generation limits for Llama 3.1.[^meta]

**Catalog use — apply:** Preserve evaluation settings; a benchmark score alone cannot select a factory configuration. Use [assessment evidence validity](../../catalog/controls/assessment-evidence-validity.md).

## Amazon Web Services

**Selection basis:** Operational architecture guidance. **Review depth:** Sections.

**Learning:** Links model operation to data quality, monitoring, and lifecycle improvement.[^amazon-web-services]

**Catalog use — apply:** Translate broad architecture advice into owned service objectives and recovery evidence. Use [data product service objectives](../proposals/controls/data-product-service-objectives.md).

## IBM

**Selection basis:** Governance education. **Review depth:** Sections.

**Learning:** Discusses oversight, stakeholders, data risks, and lifecycle governance.[^ibm]

**Catalog use — apply:** Use as an intake checklist; broad governance claims do not establish compliance or effectiveness. Use [decision rights and accountability](../proposals/controls/decision-rights-and-accountability.md).

## Cohere

**Selection basis:** Grounded generation documentation. **Review depth:** Sections.

**Learning:** Demonstrates generating answers from supplied documents with inline citations.[^cohere]

**Catalog use — apply:** Check whether each citation supports its claim and whether the source is authorized and current. Use [evidence traceability](../../catalog/controls/evidence-traceability.md).

## Mistral AI

**Selection basis:** Agent platform documentation. **Review depth:** Sections.

**Learning:** Introduces agents that plan, use tools, and collaborate to pursue goals.[^mistral-ai]

**Catalog use — apply:** Translate capabilities into an explicit tool inventory and scoped grants before use. Use [tool and dependency admission](../../catalog/controls/tool-and-dependency-admission.md).

## DeepSeek

**Selection basis:** Reasoning-model release and technical material. **Review depth:** Sections.

**Learning:** Describes reinforcement learning, cold-start data, distillation, and observed failure modes such as repetition.[^deepseek]

**Catalog use — apply:** Reassess smaller or distilled models on local tasks; release benchmarks remain supplier reports. Use [task configuration selection](../proposals/controls/task-configuration-selection.md).

[^anthropic]: [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents).
[^openai]: [A practical guide to building agents | OpenAI](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
[^google]: [Rules of Machine Learning:  |  Google for Developers](https://developers.google.com/machine-learning/guides/rules-of-ml).
[^microsoft]: [AI Agent Orchestration Patterns - Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns).
[^meta]: [Llama 3.1 evaluation details](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md).
[^amazon-web-services]: [Machine Learning Lens - AWS Well-Architected Framework - Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html).
[^ibm]: [What is AI Governance? | IBM](https://www.ibm.com/think/topics/ai-governance).
[^cohere]: [Retrieval Augmented Generation (RAG) | Cohere](https://docs.cohere.com/docs/retrieval-augmented-generation-rag).
[^mistral-ai]: [Agents Introduction | Mistral Docs](https://docs.mistral.ai/studio/agents/introduction).
[^deepseek]: [DeepSeek-R1 model documentation](https://github.com/deepseek-ai/DeepSeek-R1).
