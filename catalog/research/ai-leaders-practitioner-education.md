---
type: Guide
title: "AI research sources: Practitioner education"
description: "Select and apply relevant learning from ten individual sources on practitioner education."
status: draft
tags: [ai-research, source-review]
sources:
  - id: chip-huyen
    resource: "https://huyenchip.com/2024/07/25/genai-platform.html"
    title: "Building A Generative AI Platform"
  - id: hamel-husain
    resource: "https://hamel.dev/blog/posts/evals/"
    title: "Your AI Product Needs Evals – Hamel’s Blog"
  - id: lilian-weng
    resource: "https://lilianweng.github.io/posts/2023-06-23-agent/"
    title: "LLM Powered Autonomous Agents | Lil'Log"
  - id: andrej-karpathy
    resource: "https://karpathy.github.io/2019/04/25/recipe/"
    title: "A Recipe for Training Neural Networks"
  - id: andrew-ng
    resource: "https://www.deeplearning.ai/the-batch/issue-242/"
    title: "The Batch, issue 242: Andrew's letter on reflection"
  - id: ethan-mollick
    resource: "https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged"
    title: "Centaurs and Cyborgs on the Jagged Frontier"
  - id: simon-willison
    resource: "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/"
    title: "The lethal trifecta for AI agents: private data, untrusted content, and external communication"
  - id: sebastian-raschka
    resource: "https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches"
    title: "Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)"
  - id: eugene-yan
    resource: "https://eugeneyan.com/writing/llm-evaluators/"
    title: "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)"
  - id: jason-liu
    resource: "https://python.useinstructor.com/"
    title: "Instructor: Structured LLM outputs"
---

# AI research sources: Practitioner education

[Research method and priorities](../ai-leaders-research.md) · [Adoption](../adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](../ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Chip Huyen

**Selection basis:** Practitioner platform architecture. **Review depth:** Sections.

**Learning:** Adds context, guardrails, routing, caching, and actions as needs arise.[^chip-huyen]

**Catalog use — guide:** Evaluate each added component and its interactions; this is a design synthesis, not a universal stack. Use [semantic cache assessment](../guides/semantic-cache-assessment.md).

## Hamel Husain

**Selection basis:** Product evaluation case study. **Review depth:** Sections.

**Learning:** Builds a loop of task-specific tests, trace inspection, human/model evaluation, and online comparisons.[^hamel-husain]

**Catalog use — guide:** Use failures from real tasks and keep changes separate from final acceptance evidence. Use [agent evaluation coverage](../guides/agent-evaluation-coverage.md).

## Lilian Weng

**Selection basis:** Agent architecture tutorial. **Review depth:** Sections.

**Learning:** Explains planning, memory, and tools with research examples and limitations.[^lilian-weng]

**Catalog use — apply:** Treat reflection and memory as hypotheses to test, not independent evidence of correctness. Use [planning consistency](../controls/planning-consistency.md).

## Andrej Karpathy

**Selection basis:** Neural-network training recipe. **Review depth:** Sections.

**Learning:** Advocates inspecting data and building a controlled, incremental training process.[^andrej-karpathy]

**Catalog use — apply:** Keep a simple baseline and investigate silent data or implementation errors. Use [measured process improvement](../controls/measured-process-improvement.md).

## Andrew Ng

**Selection basis:** Practitioner letter on reflection. **Review depth:** Sections.

**Learning:** Describes iterative critique and revision, including tests and external feedback.[^andrew-ng]

**Catalog use — apply:** Self-critique can assist revision; qualify acceptance with independent task evidence. Use [verifier qualification](../controls/verifier-qualification.md).

## Ethan Mollick

**Selection basis:** Author account of a work experiment. **Review depth:** Sections.

**Learning:** Reports task-dependent gains and limits from AI assistance on consulting tasks.[^ethan-mollick]

**Catalog use — apply:** Use the existing guide to allocate work by task class; do not extrapolate a study average to every job. Use [human ai authority](../human-ai-authority.md).

## Simon Willison

**Selection basis:** Agent security analysis. **Review depth:** Sections.

**Learning:** Identifies the combination of private data, untrusted content, and external communication as an exfiltration risk.[^simon-willison]

**Catalog use — apply:** Already covered in the catalog; reuse its enforcement and assessment rather than add another slogan. Use [lethal trifecta separation](../controls/lethal-trifecta-separation.md).

## Sebastian Raschka

**Selection basis:** LLM evaluation tutorial. **Review depth:** Sections.

**Learning:** Explains major evaluation approaches and how their results differ.[^sebastian-raschka]

**Catalog use — guide:** Keep benchmark, preference, judge, and task evidence distinct. Use [agent evaluation coverage](../guides/agent-evaluation-coverage.md).

## Eugene Yan

**Selection basis:** Evaluator literature review. **Review depth:** Sections.

**Learning:** Examines where model judges help and where their validity needs scrutiny.[^eugene-yan]

**Catalog use — apply:** Use as discovery guidance; inspect underlying experiments before adopting quantitative findings. Use [verifier qualification](../controls/verifier-qualification.md).

## Jason Liu

**Selection basis:** Creator's structured-output project. **Review depth:** Sections.

**Learning:** Instructor documents schema-based extraction, validation, and retries; Liu's own site identifies him as its creator.[^jason-liu]

**Catalog use — apply:** A schema-valid value can still be wrong; test semantic content and bound retries. The linked RAG course was unavailable. Use [tool input output validation](../controls/tool-input-output-validation.md).

[^chip-huyen]: [Building A Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html).
[^hamel-husain]: [Your AI Product Needs Evals – Hamel’s Blog](https://hamel.dev/blog/posts/evals/).
[^lilian-weng]: [LLM Powered Autonomous Agents | Lil'Log](https://lilianweng.github.io/posts/2023-06-23-agent/).
[^andrej-karpathy]: [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/).
[^andrew-ng]: [The Batch, issue 242: Andrew's letter on reflection](https://www.deeplearning.ai/the-batch/issue-242/).
[^ethan-mollick]: [Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged).
[^simon-willison]: [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
[^sebastian-raschka]: [Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches).
[^eugene-yan]: [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/).
[^jason-liu]: [Instructor: Structured LLM outputs](https://python.useinstructor.com/).
