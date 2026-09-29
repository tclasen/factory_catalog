---
type: Guide
title: "AI research sources: AI factory infrastructure"
description: "Select and apply relevant learning from ten corporate sources on ai factory infrastructure."
status: draft
tags: [ai-research, source-review]
sources:
  - id: nvidia
    resource: "https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html"
    title: "Building AI Factories for the Enterprise"
  - id: amd
    resource: "https://rocm.docs.amd.com/en/latest/"
    title: "AMD ROCm — AMD ROCm 10.0.0"
  - id: intel
    resource: "https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html"
    title: "Intel® Distribution of OpenVINO™ Toolkit"
  - id: dell-technologies
    resource: "https://www.dell.com/en-us/blog/how-dell-makes-the-ai-factory-real/"
    title: "How Dell Makes the AI Factory Real | Dell"
  - id: hewlett-packard-enterprise
    resource: "https://www.hpe.com/psnow/downloadDoc/HPE%20Private%20Cloud%20AI%20QuickSpecs-a50009216enw.pdf?contentDisposition=attachment&deepLink=&form=false&hf=regular&id=a50009216enw.pdf&isFutureVersion=true&isLinearized=false&originalObjectName=&prelaunchSection=&preview=false&print=&r=&section=&softrollSection=&ver=1"
    title: "HPE Private Cloud AI QuickSpecs"
  - id: cisco
    resource: "https://blogs.cisco.com/datacenter"
    title: "Data Center - Cisco Blogs"
  - id: schneider-electric
    resource: "https://www.se.com/ww/en/work/solutions/data-centers-and-networks/"
    title: "Data Center Solutions and Networks | Schneider Electric"
  - id: vertiv
    resource: "https://www.vertiv.com/en-us/solutions/ai-hub/"
    title: "Vertiv AI Hub: Transforming Modern Data Centers To Support AI and HPC Demands"
  - id: supermicro
    resource: "https://www.supermicro.com/solutions/validated-design/NVIDIA-Enterprise-AI-Factory-Reference-Architecture-SMCI-Spectro-Cloud.pdf"
    title: "NVIDIA Enterprise AI Factory reference architecture for Supermicro, revision 1.0.1"
  - id: coreweave
    resource: "https://docs.coreweave.com/observability/managed-grafana/cks/cluster-resource"
    title: "Cluster Resource Overview - CoreWeave Docs"
---

# AI research sources: AI factory infrastructure

[Research method and priorities](../ai-leaders-research.md) · [Adoption](../adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](../ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## NVIDIA

**Selection basis:** AI factory architecture guidance. **Review depth:** Sections.

**Learning:** Connects compute, networking, storage, data pipelines, software, security, and facility constraints.[^nvidia]

**Catalog use — guide:** Qualify the combined stack with the intended workload; a reference design is a starting point. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

## AMD

**Selection basis:** GPU software and operations documentation. **Review depth:** Sections.

**Learning:** Distinguishes runtime and libraries from driver, deployment, monitoring, and cluster operations.[^amd]

**Catalog use — apply:** Record supported hardware/software combinations and reassess upgrades. Use [controlled dependency change](../controls/controlled-dependency-change.md).

## Intel

**Selection basis:** Inference optimization education. **Review depth:** Product.

**Learning:** Describes model conversion and optimization across deployment environments and Intel hardware.[^intel]

**Catalog use — apply:** Measure quality after conversion or quantization along with latency and throughput. Use [task configuration selection](../controls/task-configuration-selection.md).

## Dell Technologies

**Selection basis:** AI factory adoption explanation. **Review depth:** Sections.

**Learning:** Starts with business use cases and combines data, infrastructure, software, and deployment services.[^dell-technologies]

**Catalog use — guide:** Separate outcome selection from procurement and require a workload acceptance record. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

## Hewlett Packard Enterprise

**Selection basis:** Private-cloud AI engineering specifications. **Review depth:** Sections.

**Learning:** QuickSpecs describes a pre-integrated private AI system, its component roles, lifecycle management, and capacity monitoring.[^hewlett-packard-enterprise]

**Catalog use — apply:** Overview and feature sections reviewed. Product claims and internal comparisons require local acceptance evidence. Use [architecture decision traceability](../controls/architecture-decision-traceability.md).

## Cisco

**Selection basis:** Data-center engineering blog collection. **Review depth:** Hub.

**Learning:** Surfaces fabric deployment, distributed clusters, heterogeneous GPUs, and tenant isolation topics.[^cisco]

**Catalog use — guide:** Treat article summaries as discovery leads; individual network designs need deeper review. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

## Schneider Electric

**Selection basis:** Facility planning resources. **Review depth:** Hub.

**Learning:** Offers power sizing, power-usage effectiveness, monitoring, and pre-engineered data-center resources.[^schneider-electric]

**Catalog use — guide:** Bring facility capacity assumptions into workload acceptance; this page is not a design calculation. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

## Vertiv

**Selection basis:** AI infrastructure education and designs. **Review depth:** Hub.

**Learning:** Organizes retrofit and new-build reference designs around density, scale, and cooling choices.[^vertiv]

**Catalog use — guide:** Retain design boundaries and involve qualified facilities owners before production changes. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

## Supermicro

**Selection basis:** Joint reference architecture hosted by Supermicro. **Review depth:** Sections.

**Learning:** The Spectro Cloud document specifies component versions, sizing, and network/storage configuration for Supermicro systems.[^supermicro]

**Catalog use — apply:** Record the January 2026 revision and local deviations; vendor validation does not transfer automatically. Use [architecture decision traceability](../controls/architecture-decision-traceability.md).

## CoreWeave

**Selection basis:** Cluster observability documentation. **Review depth:** Sections.

**Learning:** Shows workload health and resource capacity, requests, limits, and utilization at cluster and node levels.[^coreweave]

**Catalog use — guide:** Correlate capacity telemetry with accepted jobs and queue latency. Use [ai factory workload qualification](../guides/ai-factory-workload-qualification.md).

[^nvidia]: [Building AI Factories for the Enterprise](https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html).
[^amd]: [AMD ROCm — AMD ROCm 10.0.0](https://rocm.docs.amd.com/en/latest/).
[^intel]: [Intel® Distribution of OpenVINO™ Toolkit](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html).
[^dell-technologies]: [How Dell Makes the AI Factory Real | Dell](https://www.dell.com/en-us/blog/how-dell-makes-the-ai-factory-real/).
[^hewlett-packard-enterprise]: [HPE Private Cloud AI QuickSpecs](https://www.hpe.com/psnow/downloadDoc/HPE%20Private%20Cloud%20AI%20QuickSpecs-a50009216enw.pdf?contentDisposition=attachment&deepLink=&form=false&hf=regular&id=a50009216enw.pdf&isFutureVersion=true&isLinearized=false&originalObjectName=&prelaunchSection=&preview=false&print=&r=&section=&softrollSection=&ver=1).
[^cisco]: [Data Center - Cisco Blogs](https://blogs.cisco.com/datacenter).
[^schneider-electric]: [Data Center Solutions and Networks | Schneider Electric](https://www.se.com/ww/en/work/solutions/data-centers-and-networks/).
[^vertiv]: [Vertiv AI Hub: Transforming Modern Data Centers To Support AI and HPC Demands](https://www.vertiv.com/en-us/solutions/ai-hub/).
[^supermicro]: [NVIDIA Enterprise AI Factory reference architecture for Supermicro, revision 1.0.1](https://www.supermicro.com/solutions/validated-design/NVIDIA-Enterprise-AI-Factory-Reference-Architecture-SMCI-Spectro-Cloud.pdf).
[^coreweave]: [Cluster Resource Overview - CoreWeave Docs](https://docs.coreweave.com/observability/managed-grafana/cks/cluster-resource).
