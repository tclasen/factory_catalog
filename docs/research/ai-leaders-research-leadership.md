---
type: Guide
title: "AI research sources: Research leadership"
description: "Select and apply relevant learning from ten individual sources on research leadership."
status: draft
tags: [ai-research, source-review]
sources:
  - id: yoshua-bengio
    resource: "https://yoshuabengio.org/en/blog/how-rogue-ais-may-arise"
    title: "How Rogue AIs may Arise | Yoshua Bengio"
  - id: yann-lecun
    resource: "https://arxiv.org/abs/2301.08243v3"
    title: "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"
  - id: geoffrey-hinton
    resource: "https://arxiv.org/abs/1503.02531"
    title: "Distilling the Knowledge in a Neural Network"
  - id: fei-fei-li
    resource: "https://cs231n.stanford.edu/"
    title: "Stanford University CS231n: Deep Learning for Computer Vision"
  - id: demis-hassabis
    resource: "https://deepmind.google/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/"
    title: "AlphaFold: a solution to a 50-year-old grand challenge in biology — Google DeepMind"
  - id: dario-amodei
    resource: "https://darioamodei.com/essay/machines-of-loving-grace"
    title: "Dario Amodei — Machines of Loving Grace"
  - id: sam-altman
    resource: "https://blog.samaltman.com/three-observations"
    title: "Three Observations - Sam Altman"
  - id: ilya-sutskever
    resource: "https://ssi.inc/"
    title: "Safe Superintelligence Inc."
  - id: richard-sutton
    resource: "http://www.incompleteideas.net/IncIdeas/BitterLesson.html"
    title: "The Bitter Lesson"
  - id: michael-i-jordan
    resource: "https://rise.cs.berkeley.edu/blog/michael-i-jordan-artificial-intelligence%E2%80%8A-%E2%80%8Athe-revolution-hasnt-happened-yet/"
    title: "Michael I. Jordan: Artificial Intelligence — The Revolution Hasn’t Happened Yet - RISE Lab"
---

# AI research sources: Research leadership

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Yoshua Bengio

**Selection basis:** Author risk analysis. **Review depth:** Sections.

**Learning:** Uses explicit definitions and hypotheses to examine conditions for dangerous autonomous behavior.[^yoshua-bengio]

**Catalog use — apply:** Record assumptions and exposure paths; the essay does not supply measured local probabilities. Use [risk estimate assumptions](../../catalog/controls/risk-estimate-assumptions.md).

## Yann LeCun

**Selection basis:** Coauthored representation-learning research. **Review depth:** Abstract.

**Learning:** I-JEPA studies predicting image representations from context without hand-crafted augmentations.[^yann-lecun]

**Catalog use — defer:** Abstract reviewed; useful for model alternatives, but it supplies no reusable factory control by itself. Review in the context of [task configuration selection](../../catalog/controls/task-configuration-selection.md).

## Geoffrey Hinton

**Selection basis:** Coauthored distillation research. **Review depth:** Abstract.

**Learning:** Explores transferring ensemble knowledge into a model that is easier to deploy.[^geoffrey-hinton]

**Catalog use — apply:** Qualify the distilled model separately; this abstract does not prove preservation of all behaviors. Use [task configuration selection](../../catalog/controls/task-configuration-selection.md).

## Fei-Fei Li

**Selection basis:** Computer-vision teaching. **Review depth:** Curriculum.

**Learning:** CS231n teaches task setup, model implementation, training, and projects; Li is listed among its instructors.[^fei-fei-li]

**Catalog use — apply:** Curriculum supports practitioner education; individual lessons and assignments were not audited. Use [accepted work definition](../../catalog/controls/accepted-work-definition.md).

## Demis Hassabis

**Selection basis:** Associated team's scientific AI account. **Review depth:** Sections.

**Learning:** DeepMind's AlphaFold account explains blind domain assessment through CASP.[^demis-hassabis]

**Catalog use — apply:** Retain an independent test boundary. Team material is not attributed solely to Hassabis. Use [protected acceptance](../../catalog/controls/protected-acceptance.md).

## Dario Amodei

**Selection basis:** Author strategy essay. **Review depth:** Position.

**Learning:** Explores possible benefits from advanced AI and explicitly frames predictions as uncertain.[^dario-amodei]

**Catalog use — defer:** Use as scenario input; do not convert forecasts into accepted outcomes or investment evidence. Review in the context of [risk estimate assumptions](../../catalog/controls/risk-estimate-assumptions.md).

## Sam Altman

**Selection basis:** Author strategy essay. **Review depth:** Position.

**Learning:** Offers views about scaling resources, declining use costs, and economic effects.[^sam-altman]

**Catalog use — defer:** Treat these as dated claims; measure current task economics independently. Review in the context of [measurement basis validation](../../catalog/controls/measurement-basis-validation.md).

## Ilya Sutskever

**Selection basis:** Co-signed research mission. **Review depth:** Position.

**Learning:** SSI's founding statement links safety and capability development as its mission.[^ilya-sutskever]

**Catalog use — defer:** Mission intent supplies no inspectable implementation or assessment procedure. Review in the context of [autonomy change gates](../../catalog/controls/autonomy-change-gates.md).

## Richard Sutton

**Selection basis:** Author research strategy essay. **Review depth:** Position.

**Learning:** Argues that scalable search and learning have repeatedly outperformed hand-built domain approaches.[^richard-sutton]

**Catalog use — apply:** Compare scalable and specialized methods empirically; the essay does not waive domain constraints. Use [task configuration selection](../../catalog/controls/task-configuration-selection.md).

## Michael I. Jordan

**Selection basis:** Author systems essay. **Review depth:** Position.

**Learning:** Argues for engineering data-driven systems and intelligence augmentation in their social and operational context.[^michael-i-jordan]

**Catalog use — apply:** Specify effects on people and processes, including changed data or measurement conditions. Use [outcome verification](../../catalog/controls/outcome-verification.md).

[^yoshua-bengio]: [How Rogue AIs may Arise | Yoshua Bengio](https://yoshuabengio.org/en/blog/how-rogue-ais-may-arise).
[^yann-lecun]: [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243v3).
[^geoffrey-hinton]: [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531).
[^fei-fei-li]: [Stanford University CS231n: Deep Learning for Computer Vision](https://cs231n.stanford.edu/).
[^demis-hassabis]: [AlphaFold: a solution to a 50-year-old grand challenge in biology — Google DeepMind](https://deepmind.google/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/).
[^dario-amodei]: [Dario Amodei — Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace).
[^sam-altman]: [Three Observations - Sam Altman](https://blog.samaltman.com/three-observations).
[^ilya-sutskever]: [Safe Superintelligence Inc.](https://ssi.inc/).
[^richard-sutton]: [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).
[^michael-i-jordan]: [Michael I. Jordan: Artificial Intelligence — The Revolution Hasn’t Happened Yet - RISE Lab](https://rise.cs.berkeley.edu/blog/michael-i-jordan-artificial-intelligence%E2%80%8A-%E2%80%8Athe-revolution-hasnt-happened-yet/).
