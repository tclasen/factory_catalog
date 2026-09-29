---
type: Guide
title: "AI research sources: Applied AI products"
description: "Select and apply relevant learning from ten corporate sources on applied ai products."
status: draft
tags: [ai-research, source-review]
sources:
  - id: apple
    resource: "https://machinelearning.apple.com/research/introducing-apple-foundation-models"
    title: "Introducing Apple’s On-Device and Server Foundation Models - Apple Machine Learning Research"
  - id: alibaba
    resource: "https://qwenlm.github.io/blog/qwen3/"
    title: "Qwen3: Think Deeper, Act Faster | Qwen"
  - id: tencent
    resource: "https://github.com/Tencent-Hunyuan/Hunyuan-A13B"
    title: "Hunyuan-A13B model documentation"
  - id: baidu
    resource: "https://github.com/PaddlePaddle/ERNIE"
    title: "ERNIE model and toolkit documentation"
  - id: bytedance
    resource: "https://github.com/bytedance/deer-flow"
    title: "DeerFlow harness documentation"
  - id: perplexity
    resource: "https://docs.perplexity.ai/docs/agent-api/tools/web-search"
    title: "Web Search - Perplexity"
  - id: cursor
    resource: "https://cursor.com/blog/shadow-workspace"
    title: "Iterating with shadow workspaces · Cursor"
  - id: replit
    resource: "https://replit.com/blog/evaluating-and-improving-agent-at-scale"
    title: "Closing the loop: Evaluating and improving Replit | Replit"
  - id: cognition
    resource: "https://cognition.com/blog/introducing-devin"
    title: "Introducing Devin, the first AI software engineer | Cognition"
  - id: deeplearning-ai
    resource: "https://www.deeplearning.ai/courses/evaluating-ai-agents"
    title: "Evaluating AI Agents"
---

# AI research sources: Applied AI products

[Research method and priorities](../ai-leaders-research.md) · [Adoption](../adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](../ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Apple

**Selection basis:** Task-adapted model research account. **Review depth:** Sections.

**Learning:** Describes specialized on-device and server models for user tasks.[^apple]

**Catalog use — apply:** Record where each task's data is processed and qualify local/cloud routing. Use [approved data processing](../controls/approved-data-processing.md).

## Alibaba

**Selection basis:** Open-model release documentation. **Review depth:** Sections.

**Learning:** Distinguishes thinking and non-thinking modes and multiple model sizes.[^alibaba]

**Catalog use — apply:** Treat reasoning mode as part of the tested configuration and measure its cost and latency. Use [task configuration selection](../controls/task-configuration-selection.md).

## Tencent

**Selection basis:** Mixture-of-experts model documentation. **Review depth:** Sections.

**Learning:** Describes active versus total parameters and inference optimizations.[^tencent]

**Catalog use — apply:** Do not substitute active-parameter counts for measured memory, quality, or serving cost. Use [measurement basis validation](../controls/measurement-basis-validation.md).

## Baidu

**Selection basis:** Multimodal model and toolkit documentation. **Review depth:** Sections.

**Learning:** Presents ERNIE variants and training/deployment tooling across text and visual tasks.[^baidu]

**Catalog use — apply:** Qualify each modality and supported runtime; release results do not establish local acceptance. Use [controlled dependency change](../controls/controlled-dependency-change.md).

## ByteDance

**Selection basis:** Long-running agent harness documentation. **Review depth:** Sections.

**Learning:** Combines tools, memory, sandboxes, skills, and delegated work; identifies a major rewrite boundary.[^bytedance]

**Catalog use — apply:** Pin the harness version and review permissions across its extensions. Use [tool and dependency admission](../controls/tool-and-dependency-admission.md).

## Perplexity

**Selection basis:** Web-search tool documentation. **Review depth:** Sections.

**Learning:** Provides live web retrieval as an agent tool and search-result metadata.[^perplexity]

**Catalog use — apply:** Retain actual source URLs and claim support; a search result is not proof of comprehensive coverage. Use [evidence traceability](../controls/evidence-traceability.md).

## Cursor

**Selection basis:** Coding environment engineering account. **Review depth:** Sections.

**Learning:** Uses background workspaces so AI can inspect feedback and iterate without disrupting user edits.[^cursor]

**Catalog use — apply:** Isolate mutable work and test promotion into the intended checkout. Use [isolated parallel work](../controls/isolated-parallel-work.md).

## Replit

**Selection basis:** Production evaluation engineering account. **Review depth:** Sections.

**Learning:** Combines offline tasks, online tests, and production traces in an improvement loop.[^replit]

**Catalog use — guide:** Measure user-visible behavior and retain failures before and after release. Use [agent evaluation coverage](../guides/agent-evaluation-coverage.md).

## Cognition

**Selection basis:** Software-agent release account. **Review depth:** Sections.

**Learning:** Describes planning, sandboxed developer tools, progress feedback, and benchmark tasks.[^cognition]

**Catalog use — apply:** Verify the delivered artifact and its environment; demonstrations do not prove broad autonomy. Use [verified delivery](../controls/verified-delivery.md).

## DeepLearning.AI

**Selection basis:** Agent evaluation curriculum. **Review depth:** Curriculum.

**Learning:** Covers component and trajectory evaluation, traces, evaluator choices, and structured experiments.[^deeplearning-ai]

**Catalog use — guide:** Course outline reviewed; videos, labs, and claimed learning outcomes were not independently assessed. Use [agent evaluation coverage](../guides/agent-evaluation-coverage.md).

[^apple]: [Introducing Apple’s On-Device and Server Foundation Models - Apple Machine Learning Research](https://machinelearning.apple.com/research/introducing-apple-foundation-models).
[^alibaba]: [Qwen3: Think Deeper, Act Faster | Qwen](https://qwenlm.github.io/blog/qwen3/).
[^tencent]: [Hunyuan-A13B model documentation](https://github.com/Tencent-Hunyuan/Hunyuan-A13B).
[^baidu]: [ERNIE model and toolkit documentation](https://github.com/PaddlePaddle/ERNIE).
[^bytedance]: [DeerFlow harness documentation](https://github.com/bytedance/deer-flow).
[^perplexity]: [Web Search - Perplexity](https://docs.perplexity.ai/docs/agent-api/tools/web-search).
[^cursor]: [Iterating with shadow workspaces · Cursor](https://cursor.com/blog/shadow-workspace).
[^replit]: [Closing the loop: Evaluating and improving Replit | Replit](https://replit.com/blog/evaluating-and-improving-agent-at-scale).
[^cognition]: [Introducing Devin, the first AI software engineer | Cognition](https://cognition.com/blog/introducing-devin).
[^deeplearning-ai]: [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents).
