---
type: Guide
title: "AI research sources: Agent engineering"
description: "Select and apply relevant learning from ten corporate sources on agent engineering."
status: draft
tags: [ai-research, source-review]
sources:
  - id: langchain
    resource: "https://docs.langchain.com/oss/python/langgraph/persistence"
    title: "Persistence - Docs by LangChain"
  - id: llamaindex
    resource: "https://developers.llamaindex.ai/python/framework/module_guides/evaluating/"
    title: "Evaluating | Developer Documentation"
  - id: arize-ai
    resource: "https://arize.com/docs/phoenix/"
    title: "What is Arize Phoenix? - Phoenix"
  - id: weights-biases
    resource: "https://site.wandb.ai/evaluations/"
    title: "W&B Evaluations"
  - id: anyscale
    resource: "https://docs.ray.io/en/latest/serve/production-guide/index.html"
    title: "Production Guide — Ray 2.58.0"
  - id: modal
    resource: "https://modal.com/docs/guide/cold-start"
    title: "Cold start performance | Modal Docs"
  - id: baseten
    resource: "https://www.baseten.co/blog/driving-model-performance-optimization-2024-highlights/"
    title: "Driving model performance optimization: 2024 highlights"
  - id: together-ai
    resource: "https://www.together.ai/evaluations"
    title: "Evaluations | Together AI"
  - id: fireworks-ai
    resource: "https://docs.fireworks.ai/guides/querying-text-models"
    title: "Text Models - Fireworks AI Docs"
  - id: unstructured
    resource: "https://docs.unstructured.io/api-reference/legacy-api/partition/chunking"
    title: "Chunking strategies - Unstructured"
---

# AI research sources: Agent engineering

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## LangChain

**Selection basis:** Persistence documentation. **Review depth:** Sections.

**Learning:** Distinguishes thread checkpoints from durable cross-thread stores and warns that in-memory checkpoints disappear on restart.[^langchain]

**Catalog use — apply:** Test resumed behavior and persistent state, including unresolved external effects. Use [safe work resumption](../proposals/controls/safe-work-resumption.md).

## LlamaIndex

**Selection basis:** Evaluation framework documentation. **Review depth:** Sections.

**Learning:** Distinguishes response correctness, faithfulness, semantic similarity, and retrieval quality.[^llamaindex]

**Catalog use — guide:** Choose metrics by failure mode and qualify model judges against human labels. Use [agent evaluation coverage](../proposals/guides/agent-evaluation-coverage.md).

## Arize AI

**Selection basis:** Tracing and evaluation documentation. **Review depth:** Sections.

**Learning:** Connects traces, scoring, prompt versions, and experiments on common inputs.[^arize-ai]

**Catalog use — apply:** Protect telemetry while retaining enough context to diagnose tool and retrieval failures. Use [security event traceability](../../catalog/controls/security-event-traceability.md).

## Weights & Biases

**Selection basis:** Experiment and evaluation product education. **Review depth:** Product.

**Learning:** Combines test datasets and scorers with versioned code, evaluation records, and per-example inspection.[^weights-biases]

**Catalog use — apply:** Retain individual results and exact revisions; vendor tooling is not an independent verifier. Use [assessment evidence validity](../../catalog/controls/assessment-evidence-validity.md).

## Anyscale

**Selection basis:** Ray Serve production guide. **Review depth:** Sections.

**Learning:** Describes health checks, recovery, upgrades, and structured deployment configuration.[^anyscale]

**Catalog use — apply:** Test failure recovery against a pinned serving configuration. Use [verified service recovery](../proposals/controls/verified-service-recovery.md).

## Modal

**Selection basis:** Serverless performance guide. **Review depth:** Sections.

**Learning:** Separates cold-start queue delay from initialization work on the first invocation.[^modal]

**Catalog use — guide:** Measure cold and warm workloads separately; a warm average can hide user-visible delays. Use [ai factory workload qualification](../proposals/guides/ai-factory-workload-qualification.md).

## Baseten

**Selection basis:** Inference engineering account. **Review depth:** Sections.

**Learning:** Discusses jointly optimizing latency, throughput, quality, cost, functionality, and deployment efficiency.[^baseten]

**Catalog use — guide:** Use a comparable workload and quality floor before calling one serving stack better. Use [ai factory workload qualification](../proposals/guides/ai-factory-workload-qualification.md).

## Together AI

**Selection basis:** Model-judge evaluation offering. **Review depth:** Product.

**Learning:** Provides pairwise comparison, numeric scoring, and criterion classification.[^together-ai]

**Catalog use — apply:** Require local judge calibration; an automated score is not evidence of production readiness. Use [verifier qualification](../../catalog/controls/verifier-qualification.md).

## Fireworks AI

**Selection basis:** Inference and metrics documentation. **Review depth:** Sections.

**Learning:** Distinguishes server-acknowledged requests from client-observed timeouts and network failures.[^fireworks-ai]

**Catalog use — guide:** Reconcile client and server counts, retries, and failures before calculating reliability. Use [ai factory workload qualification](../proposals/guides/ai-factory-workload-qualification.md).

## Unstructured

**Selection basis:** Document chunking documentation. **Review depth:** Sections.

**Learning:** Uses document structure and metadata to form chunks, including title and page boundaries.[^unstructured]

**Catalog use — apply:** Test extraction/chunking failures; the inspected endpoint is legacy, so verify current APIs separately. Use [data lineage impact](../proposals/controls/data-lineage-impact.md).

[^langchain]: [Persistence - Docs by LangChain](https://docs.langchain.com/oss/python/langgraph/persistence).
[^llamaindex]: [Evaluating | Developer Documentation](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/).
[^arize-ai]: [What is Arize Phoenix? - Phoenix](https://arize.com/docs/phoenix/).
[^weights-biases]: [W&B Evaluations](https://site.wandb.ai/evaluations/).
[^anyscale]: [Production Guide — Ray 2.58.0](https://docs.ray.io/en/latest/serve/production-guide/index.html).
[^modal]: [Cold start performance | Modal Docs](https://modal.com/docs/guide/cold-start).
[^baseten]: [Driving model performance optimization: 2024 highlights](https://www.baseten.co/blog/driving-model-performance-optimization-2024-highlights/).
[^together-ai]: [Evaluations | Together AI](https://www.together.ai/evaluations).
[^fireworks-ai]: [Text Models - Fireworks AI Docs](https://docs.fireworks.ai/guides/querying-text-models).
[^unstructured]: [Chunking strategies - Unstructured](https://docs.unstructured.io/api-reference/legacy-api/partition/chunking).
