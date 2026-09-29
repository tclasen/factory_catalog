---
type: Guide
title: "AI research sources: Evaluation and society"
description: "Select and apply relevant learning from ten individual sources on evaluation and society."
status: draft
tags: [ai-research, source-review]
sources:
  - id: margaret-mitchell
    resource: "https://arxiv.org/abs/1810.03993"
    title: "[1810.03993] Model Cards for Model Reporting"
  - id: timnit-gebru
    resource: "https://arxiv.org/abs/1803.09010"
    title: "[1803.09010] Datasheets for Datasets"
  - id: joy-buolamwini
    resource: "https://proceedings.mlr.press/v81/buolamwini18a.html"
    title: "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification"
  - id: rumman-chowdhury
    resource: "https://humane-intelligence.org/"
    title: "Home - Humane Intelligence Humane Intelligence"
  - id: arvind-narayanan
    resource: "https://www.normaltech.ai/p/ai-as-normal-technology"
    title: "AI as Normal Technology"
  - id: sayash-kapoor
    resource: "https://reproducible.cs.princeton.edu/"
    title: "Leakage and the Reproducibility Crisis in ML-based Science"
  - id: percy-liang
    resource: "https://arxiv.org/abs/2211.09110"
    title: "Holistic Evaluation of Language Models"
  - id: sarah-hooker
    resource: "https://arxiv.org/abs/2009.06489"
    title: "The Hardware Lottery"
  - id: emily-m-bender
    resource: "https://aclanthology.org/2020.acl-main.463/"
    title: "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data - ACL Anthology"
  - id: sasha-luccioni
    resource: "https://arxiv.org/abs/2311.16863"
    title: "[2311.16863] Power Hungry Processing: Watts Driving the Cost of AI Deployment?"
---

# AI research sources: Evaluation and society

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Margaret Mitchell

**Selection basis:** Coauthored model documentation research. **Review depth:** Abstract.

**Learning:** Model Cards records intended use, evaluation conditions, and performance across relevant groups.[^margaret-mitchell]

**Catalog use — guide:** Attach conditions and limitations to model-selection evidence. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Timnit Gebru

**Selection basis:** Coauthored dataset documentation research. **Review depth:** Abstract.

**Learning:** Datasheets records why and how data was collected and its recommended uses.[^timnit-gebru]

**Catalog use — apply:** Carry collection context into evaluation and retrieval-data records. Use [data product contract](../../catalog/controls/data-product-contract.md).

## Joy Buolamwini

**Selection basis:** Coauthored empirical audit. **Review depth:** Abstract.

**Learning:** Gender Shades reports intersectional differences in classification performance for its evaluated systems.[^joy-buolamwini]

**Catalog use — guide:** Test relevant subgroups; do not transplant historical error rates to current systems. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Rumman Chowdhury

**Selection basis:** Organization's evaluation methods. **Review depth:** Hub.

**Learning:** Humane Intelligence describes contextual evaluations, red teaming, and participation by impacted communities.[^rumman-chowdhury]

**Catalog use — guide:** Team material supplies a participation lead; local evaluator expertise and coverage still need evidence. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Arvind Narayanan

**Selection basis:** Coauthored technology-governance essay. **Review depth:** Position.

**Learning:** Argues for understanding AI through deployment, diffusion, and human institutions.[^arvind-narayanan]

**Catalog use — apply:** Use the existing authority-allocation guide; distinguish this perspective from competing forecasts. Use [human ai authority](../../catalog/human-ai-authority.md).

## Sayash Kapoor

**Selection basis:** Coauthored reproducibility research resource. **Review depth:** Sections.

**Learning:** Documents data-leakage failures and separates scientific claims from other ML evaluation settings.[^sayash-kapoor]

**Catalog use — guide:** Check train/test separation and temporal leakage before accepting evidence. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Percy Liang

**Selection basis:** Coauthored evaluation framework. **Review depth:** Abstract.

**Learning:** HELM evaluates multiple metrics across scenarios and explicitly identifies coverage gaps.[^percy-liang]

**Catalog use — guide:** Report missing scenarios and tradeoffs rather than one universal ranking. Use [agent evaluation coverage](../../catalog/guides/agent-evaluation-coverage.md).

## Sarah Hooker

**Selection basis:** Author hardware-systems essay. **Review depth:** Abstract.

**Learning:** The Hardware Lottery explains how available software and hardware can shape which research ideas succeed.[^sarah-hooker]

**Catalog use — guide:** Separate hardware fit from model merit when comparing alternatives. Use [ai factory workload qualification](../../catalog/guides/ai-factory-workload-qualification.md).

## Emily M. Bender

**Selection basis:** Coauthored position paper. **Review depth:** Abstract.

**Learning:** Distinguishes language form from meaning and cautions against unsupported understanding claims.[^emily-m-bender]

**Catalog use — apply:** Test task-specific interpretation and consequences instead of inferring correctness from fluency. Use [contextual domain language](../../catalog/controls/contextual-domain-language.md).

## Sasha Luccioni

**Selection basis:** Coauthored inference-cost research. **Review depth:** Abstract.

**Learning:** Compares energy and emissions across task-specific and general-purpose inference systems.[^sasha-luccioni]

**Catalog use — guide:** Measure a stated workload and accounting boundary; paper results are not current procurement estimates. Use [ai factory workload qualification](../../catalog/guides/ai-factory-workload-qualification.md).

[^margaret-mitchell]: [1810.03993 Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993).
[^timnit-gebru]: [1803.09010 Datasheets for Datasets](https://arxiv.org/abs/1803.09010).
[^joy-buolamwini]: [Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](https://proceedings.mlr.press/v81/buolamwini18a.html).
[^rumman-chowdhury]: [Home - Humane Intelligence Humane Intelligence](https://humane-intelligence.org/).
[^arvind-narayanan]: [AI as Normal Technology](https://www.normaltech.ai/p/ai-as-normal-technology).
[^sayash-kapoor]: [Leakage and the Reproducibility Crisis in ML-based Science](https://reproducible.cs.princeton.edu/).
[^percy-liang]: [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110).
[^sarah-hooker]: [The Hardware Lottery](https://arxiv.org/abs/2009.06489).
[^emily-m-bender]: [Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data - ACL Anthology](https://aclanthology.org/2020.acl-main.463/).
[^sasha-luccioni]: [2311.16863 Power Hungry Processing: Watts Driving the Cost of AI Deployment?](https://arxiv.org/abs/2311.16863).
