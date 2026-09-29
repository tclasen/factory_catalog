---
type: Guide
title: "AI research sources: Systems education"
description: "Select and apply relevant learning from ten individual sources on systems education."
status: draft
tags: [ai-research, source-review]
sources:
  - id: jeremy-howard
    resource: "https://course.fast.ai/"
    title: "Practical Deep Learning for Coders - Practical Deep Learning"
  - id: rachel-thomas
    resource: "https://course.fast.ai/Lessons/lesson8a.html"
    title: "Practical Deep Learning for Coders - Bonus: Data ethics"
  - id: sebastian-ruder
    resource: "https://www.ruder.io/state-of-transfer-learning-in-nlp/"
    title: "The State of Transfer Learning in NLP"
  - id: jay-alammar
    resource: "https://jalammar.github.io/illustrated-transformer/"
    title: "The Illustrated Transformer – Jay Alammar – Visualizing machine learning one concept at a time."
  - id: vicki-boykis
    resource: "https://vickiboykis.com/what_are_embeddings/"
    title: "What are embeddings?"
  - id: goku-mohandas
    resource: "https://madewithml.com/courses/mlops/"
    title: "MLOps Course - Made With ML by Anyscale"
  - id: harrison-chase
    resource: "https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability"
    title: "On Agent Frameworks and Agent Observability"
  - id: jerry-liu
    resource: "https://www.llamaindex.ai/blog/introducing-llama-datasets-aadb9994ad9e"
    title: "Llama Datasets: Benchmark RAG Pipelines Fast | LlamaIndex"
  - id: shreya-shankar
    resource: "https://arxiv.org/abs/2404.12272"
    title: "[2404.12272] Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences"
  - id: tri-dao
    resource: "https://arxiv.org/abs/2307.08691"
    title: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
---

# AI research sources: Systems education

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Jeremy Howard

**Selection basis:** Practical deep-learning curriculum. **Review depth:** Curriculum.

**Learning:** Offers hands-on model training and deployment for people with coding experience.[^jeremy-howard]

**Catalog use — apply:** Use as role training; curriculum coverage does not demonstrate operator competence. Use [accepted work definition](../proposals/controls/accepted-work-definition.md).

## Rachel Thomas

**Selection basis:** Data ethics teaching. **Review depth:** Curriculum.

**Learning:** Uses case studies to examine consequences of choices in data and model development.[^rachel-thomas]

**Catalog use — apply:** Add affected parties and escalation to design reviews; the course overview is not a compliance checklist. Use [decision rights and accountability](../proposals/controls/decision-rights-and-accountability.md).

## Sebastian Ruder

**Selection basis:** Transfer-learning tutorial. **Review depth:** Sections.

**Learning:** Explains transferring knowledge between source and target tasks and domains.[^sebastian-ruder]

**Catalog use — apply:** A source-domain result needs requalification for a different target context. Use [assessment evidence validity](../../catalog/controls/assessment-evidence-validity.md).

## Jay Alammar

**Selection basis:** Transformer education. **Review depth:** Sections.

**Learning:** Explains attention and encoder/decoder architecture visually.[^jay-alammar]

**Catalog use — defer:** Useful background for implementers; architecture explanation supplies no operational control by itself. Review in the context of [required guidance selection](../../catalog/controls/required-guidance-selection.md).

## Vicki Boykis

**Selection basis:** Embedding education. **Review depth:** Hub.

**Learning:** Introduces a generalist learning resource about representations and recommendation systems.[^vicki-boykis]

**Catalog use — defer:** Landing page reviewed; the linked book was not audited, so no algorithm claim is adopted. Review in the context of [semantic mapping validation](../proposals/controls/semantic-mapping-validation.md).

## Goku Mohandas

**Selection basis:** Production ML curriculum. **Review depth:** Curriculum.

**Learning:** Connects design, development, deployment, and iteration using software-engineering practices.[^goku-mohandas]

**Catalog use — apply:** Use exercises to design checks; production implementation and test evidence remain separate. Use [controlled dependency change](../proposals/controls/controlled-dependency-change.md).

## Harrison Chase

**Selection basis:** Agent systems essay. **Review depth:** Sections.

**Learning:** Argues that frameworks evolve with models while observability should remain independent of framework choice.[^harrison-chase]

**Catalog use — apply:** Preserve diagnostics across harness changes and requalify the whole agent system. Use [security event traceability](../../catalog/controls/security-event-traceability.md).

## Jerry Liu

**Selection basis:** Coauthored RAG dataset article. **Review depth:** Sections.

**Learning:** Combines question/answer examples with source context for use-case evaluation.[^jerry-liu]

**Catalog use — guide:** Inspect representativeness and synthetic labels before using community datasets for acceptance. Use [agent evaluation coverage](../proposals/guides/agent-evaluation-coverage.md).

## Shreya Shankar

**Selection basis:** Coauthored evaluator research. **Review depth:** Abstract.

**Learning:** Studies human alignment of generated evaluators and changes in criteria while reviewing outputs.[^shreya-shankar]

**Catalog use — guide:** Version revised rubrics and rerun comparisons; criterion discovery must not silently change a release gate. Use [agent evaluation coverage](../proposals/guides/agent-evaluation-coverage.md).

## Tri Dao

**Selection basis:** Attention implementation research. **Review depth:** Abstract.

**Learning:** FlashAttention-2 studies GPU work partitioning and communication costs.[^tri-dao]

**Catalog use — guide:** Abstract reviewed; kernel performance claims need whole-workload validation. Use [ai factory workload qualification](../proposals/guides/ai-factory-workload-qualification.md).

[^jeremy-howard]: [Practical Deep Learning for Coders - Practical Deep Learning](https://course.fast.ai/).
[^rachel-thomas]: [Practical Deep Learning for Coders - Bonus: Data ethics](https://course.fast.ai/Lessons/lesson8a.html).
[^sebastian-ruder]: [The State of Transfer Learning in NLP](https://www.ruder.io/state-of-transfer-learning-in-nlp/).
[^jay-alammar]: [The Illustrated Transformer – Jay Alammar – Visualizing machine learning one concept at a time.](https://jalammar.github.io/illustrated-transformer/).
[^vicki-boykis]: [What are embeddings?](https://vickiboykis.com/what_are_embeddings/).
[^goku-mohandas]: [MLOps Course - Made With ML by Anyscale](https://madewithml.com/courses/mlops/).
[^harrison-chase]: [On Agent Frameworks and Agent Observability](https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability).
[^jerry-liu]: [Llama Datasets: Benchmark RAG Pipelines Fast | LlamaIndex](https://www.llamaindex.ai/blog/introducing-llama-datasets-aadb9994ad9e).
[^shreya-shankar]: [2404.12272 Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences](https://arxiv.org/abs/2404.12272).
[^tri-dao]: [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691).
