---
type: Guide
title: "AI research sources: Data and retrieval"
description: "Select and apply relevant learning from ten corporate sources on data and retrieval."
status: draft
tags: [ai-research, source-review]
sources:
  - id: databricks
    resource: "https://docs.databricks.com/aws/en/agents/tutorials/ai-cookbook/evaluate-define-quality"
    title: "Define “quality”: Evaluation sets | Databricks on AWS"
  - id: snowflake
    resource: "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    title: "Cortex Search | Snowflake Documentation"
  - id: hugging-face
    resource: "https://huggingface.co/learn/agents-course/unit0/introduction"
    title: "Welcome to the 🤗 AI Agents Course · Hugging Face"
  - id: mongodb
    resource: "https://www.mongodb.com/docs/vector-search/tutorials/rag/"
    title: "Retrieval-Augmented Generation (RAG) with MongoDB - MongoDB Vector Search - MongoDB Docs"
  - id: elastic
    resource: "https://www.elastic.co/what-is/retrieval-augmented-generation"
    title: "What is Retrieval Augmented Generation (RAG)? | A Comprehensive RAG Guide | Elastic"
  - id: neo4j
    resource: "https://neo4j.com/developer/genai-ecosystem/"
    title: "GraphRAG Developer Guide - Developer Guides"
  - id: pinecone
    resource: "https://www.pinecone.io/learn/retrieval-augmented-generation/"
    title: "Retrieval-Augmented Generation (RAG) | Pinecone"
  - id: weaviate
    resource: "https://weaviate.io/blog/rag-evaluation"
    title: "An Overview on RAG Evaluation | Weaviate"
  - id: qdrant
    resource: "https://qdrant.tech/documentation/search-evaluation/retrieval-relevance/"
    title: "Measuring Retrieval Relevance - Qdrant"
  - id: redis
    resource: "https://redis.io/blog/what-is-semantic-caching/"
    title: "What is semantic caching? Guide to faster, smarter LLM apps"
---

# AI research sources: Data and retrieval

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Databricks

**Selection basis:** Evaluation-set guidance. **Review depth:** Sections.

**Learning:** Recommends representative human-labeled queries, difficult cases, and continued updates as usage changes.[^databricks]

**Catalog use — guide:** Use distinct development and acceptance sets; choose sample sizes for the decision rather than copying a vendor minimum. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Snowflake

**Selection basis:** Hybrid retrieval documentation. **Review depth:** Sections.

**Learning:** Combines semantic and keyword retrieval with managed indexing for enterprise search and agents.[^snowflake]

**Catalog use — apply:** Test current permissions, refresh delay, and retrieval quality with the actual data. Use [retrieval corpus integrity](../../catalog/controls/retrieval-corpus-integrity.md).

## Hugging Face

**Selection basis:** Open agent curriculum. **Review depth:** Curriculum.

**Learning:** Covers tools, actions, observations, libraries, hands-on environments, and an evaluation challenge.[^hugging-face]

**Catalog use — apply:** Use exercises to train implementers; course completion does not qualify a production agent. Use [tool input output validation](../../catalog/controls/tool-input-output-validation.md).

## MongoDB

**Selection basis:** RAG implementation education. **Review depth:** Sections.

**Learning:** Separates ingestion of local data from retrieval and generation to address knowledge and freshness gaps.[^mongodb]

**Catalog use — apply:** Trace changes from source documents to embeddings, retrieved evidence, and answers. Use [data lineage impact](../../catalog/controls/data-lineage-impact.md).

## Elastic

**Selection basis:** Retrieval education. **Review depth:** Sections.

**Learning:** Explains combining external search results with a generator and using semantic or hybrid retrieval.[^elastic]

**Catalog use — apply:** Evaluate retrieval and supported answers separately; retrieval does not guarantee truth. Use [evidence traceability](../../catalog/controls/evidence-traceability.md).

## Neo4j

**Selection basis:** GraphRAG developer resources. **Review depth:** Hub.

**Learning:** Connects knowledge-graph construction, queries, and graph-based retrieval to application examples.[^neo4j]

**Catalog use — apply:** Check extracted entity identities and relationship meaning before using generated graph edges as evidence. Use [semantic mapping validation](../../catalog/controls/semantic-mapping-validation.md).

## Pinecone

**Selection basis:** RAG architecture education. **Review depth:** Sections.

**Learning:** Explains private-domain and freshness limits of model-only answers and the role of retrieval.[^pinecone]

**Catalog use — apply:** Measure source coverage and freshness, including unanswered queries. Use [retrieval corpus integrity](../../catalog/controls/retrieval-corpus-integrity.md).

## Weaviate

**Selection basis:** RAG evaluation article. **Review depth:** Sections.

**Learning:** Separates indexing, retrieval, and generation; discusses model-assisted evaluation.[^weaviate]

**Catalog use — guide:** Calibrate judges and preserve component failures instead of relying on one aggregate score. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Qdrant

**Selection basis:** Retrieval relevance tutorial. **Review depth:** Sections.

**Learning:** Distinguishes relevance to user intent from approximate-neighbor recall and end-to-end answer quality.[^qdrant]

**Catalog use — guide:** Use independently labeled query/document pairs and report rare query classes. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Redis

**Selection basis:** Semantic caching education. **Review depth:** Sections.

**Learning:** Reuses answers for similar queries to reduce repeated model work.[^redis]

**Catalog use — guide:** Similarity alone cannot establish authorization, freshness, or answer equivalence. Use [semantic cache assessment](../../catalog/guides/semantic-cache-assessment.md).

[^databricks]: [Define “quality”: Evaluation sets | Databricks on AWS](https://docs.databricks.com/aws/en/agents/tutorials/ai-cookbook/evaluate-define-quality).
[^snowflake]: [Cortex Search | Snowflake Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview).
[^hugging-face]: [Welcome to the 🤗 AI Agents Course · Hugging Face](https://huggingface.co/learn/agents-course/unit0/introduction).
[^mongodb]: [Retrieval-Augmented Generation (RAG) with MongoDB - MongoDB Vector Search - MongoDB Docs](https://www.mongodb.com/docs/vector-search/tutorials/rag/).
[^elastic]: [What is Retrieval Augmented Generation (RAG)? | A Comprehensive RAG Guide | Elastic](https://www.elastic.co/what-is/retrieval-augmented-generation).
[^neo4j]: [GraphRAG Developer Guide - Developer Guides](https://neo4j.com/developer/genai-ecosystem/).
[^pinecone]: [Retrieval-Augmented Generation (RAG) | Pinecone](https://www.pinecone.io/learn/retrieval-augmented-generation/).
[^weaviate]: [An Overview on RAG Evaluation | Weaviate](https://weaviate.io/blog/rag-evaluation).
[^qdrant]: [Measuring Retrieval Relevance - Qdrant](https://qdrant.tech/documentation/search-evaluation/retrieval-relevance/).
[^redis]: [What is semantic caching? Guide to faster, smarter LLM apps](https://redis.io/blog/what-is-semantic-caching/).
