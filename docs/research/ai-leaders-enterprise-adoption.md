---
type: Guide
title: "AI research sources: Enterprise adoption"
description: "Select and apply relevant learning from ten corporate sources on enterprise adoption."
status: draft
tags: [ai-research, source-review]
sources:
  - id: salesforce
    resource: "https://developer.salesforce.com/blogs/2025/11/automate-multi-turn-agent-testing-with-conversation-history-in-agentforce"
    title: "Automate Multi-Turn Agent Testing with Conversation History in Agentforce | Salesforce Developers Blog"
  - id: servicenow
    resource: "https://www.servicenow.com/products/ai-control-tower.html"
    title: "AI Control Tower - ServiceNow"
  - id: sap
    resource: "https://www.sap.com/products/artificial-intelligence/ai-ethics.html"
    title: "Responsible AI | SAP"
  - id: oracle
    resource: "https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm"
    title: "Overview of Generative AI Agents Service"
  - id: siemens
    resource: "https://www.siemens.com/en-us/company/insights/generative-ai-industrial-copilot/"
    title: "Siemens Industrial Copilot"
  - id: abb
    resource: "https://new.abb.com/process-automation/genix/abb-genix-copilot"
    title: "ABB Genix™ Copilot | Unlocks the power of GenAI@scale enabling industries to outrun leaner and cleaner - ABB Genix™ Industrial IoT and AI Suite Genix™ Industrial IoT and AI Suite | ABB"
  - id: palantir
    resource: "https://www.palantir.com/docs/foundry/aip/overview"
    title: "Overview • AIP • Palantir"
  - id: uipath
    resource: "https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/overview?fallbackReason=invalidTopic&isFallback=true&fallbackCount=1"
    title: "Maestro - Overview"
  - id: intercom
    resource: "https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/"
    title: "From resolutions to outcomes: Evolving how Fin delivers value - The Intercom Blog"
  - id: thomson-reuters
    resource: "https://www.thomsonreuters.com/en/artificial-intelligence/ai-principles"
    title: "AI Principles | Thomson Reuters"
---

# AI research sources: Enterprise adoption

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Research method and priorities](ai-leaders-research.md) · [Adoption](../../catalog/adoption.md)

## How to use these sources

This is an annotated selection from the 100-entry research set, inspected on **2026-09-28 (America/Los_Angeles)**. Choose a source for the problem in its entry, inspect its stated limits, then apply the linked catalog guidance. Order is thematic, not a rank. The [research method](ai-leaders-research.md#selection-and-review-method) defines review depth and selection limits.

“Learning” summarizes the cited material; “Catalog use” is our interpretation. Links indicate supporting material or applicability, not endorsement, adoption, or a successful assessment. Papers are credited to the named contributor and coauthors; company/team material is not assumed to have been personally written by a leader. Historical material remains dated evidence, and mutable documentation must be rechecked before implementation.

## Salesforce

**Selection basis:** Multi-turn testing tutorial. **Review depth:** Sections.

**Learning:** Replays conversation history and evaluates subsequent turns against expected behavior.[^salesforce]

**Catalog use — guide:** Include corrections and topic switches, and inspect actual tool effects alongside answers. Use [agent evaluation coverage](../proposals/guides/agent-evaluation-coverage.md).

## ServiceNow

**Selection basis:** AI governance product overview. **Review depth:** Product.

**Learning:** Describes an inventory of AI assets linked to owners, services, runtime monitoring, and business value.[^servicenow]

**Catalog use — apply:** Treat inventory as an implementation input; advertised complete visibility requires local testing. Use [decision rights and accountability](../proposals/controls/decision-rights-and-accountability.md).

## SAP

**Selection basis:** Responsible AI policy resources. **Review depth:** Product.

**Learning:** Organizes responsible AI around ethics, security, compliance, and governance responsibilities.[^sap]

**Catalog use — apply:** Map actual data flows and owners; principles alone cannot enforce processing restrictions. Use [approved data processing](../proposals/controls/approved-data-processing.md).

## Oracle

**Selection basis:** Enterprise agent service documentation. **Review depth:** Sections.

**Learning:** Describes context retention, retrieval, SQL tools, guardrails, and agent orchestration.[^oracle]

**Catalog use — apply:** Separate permission to read from permission to execute database changes. Use [bounded external action](../../catalog/controls/bounded-external-action.md).

## Siemens

**Selection basis:** Industrial copilot education. **Review depth:** Product.

**Learning:** Illustrates code generation, troubleshooting, digital twins, and integration with production systems.[^siemens]

**Catalog use — apply:** Keep simulation and engineering evidence distinct from authorization to change physical operations. Use [qualified artifact promotion](../../catalog/controls/qualified-artifact-promotion.md).

## ABB

**Selection basis:** Industrial data and AI product explanation. **Review depth:** Product.

**Learning:** Combines shop-floor, enterprise, and unstructured data with role-specific interfaces.[^abb]

**Catalog use — apply:** Validate units, asset identity, and domain meaning before acting on combined data. Use [context translation contracts](../proposals/controls/context-translation-contracts.md).

## Palantir

**Selection basis:** Operational AI platform documentation. **Review depth:** Sections.

**Learning:** Connects agents and workflows to an ontology, evaluation tools, security, and audit infrastructure.[^palantir]

**Catalog use — apply:** Model object relationships and permissions explicitly; importing a platform does not validate local semantics. Use [domain model boundaries](../proposals/controls/domain-model-boundaries.md).

## UiPath

**Selection basis:** Business-process orchestration documentation. **Review depth:** Sections.

**Learning:** Combines automation, agents, people, process models, and business rules.[^uipath]

**Catalog use — apply:** Identify the owner, required evidence, and authority at each actor transition. Use [durable work handoff](../../catalog/controls/durable-work-handoff.md).

## Intercom

**Selection basis:** Customer-support operating-model account. **Review depth:** Sections.

**Learning:** Explains why agent value can include work completed before a required human handoff.[^intercom]

**Catalog use — apply:** Define customer outcomes beyond autonomous resolution or conversation closure. Use [outcome verification](../../catalog/controls/outcome-verification.md).

## Thomson Reuters

**Selection basis:** Data and AI ethics principles. **Review depth:** Product.

**Learning:** States expectations for privacy, security, accountable use, and trustworthy products.[^thomson-reuters]

**Catalog use — apply:** In professional work, retain source support and competent review; policy statements are not performance evidence. Use [evidence traceability](../../catalog/controls/evidence-traceability.md).

[^salesforce]: [Automate Multi-Turn Agent Testing with Conversation History in Agentforce | Salesforce Developers Blog](https://developer.salesforce.com/blogs/2025/11/automate-multi-turn-agent-testing-with-conversation-history-in-agentforce).
[^servicenow]: [AI Control Tower - ServiceNow](https://www.servicenow.com/products/ai-control-tower.html).
[^sap]: [Responsible AI | SAP](https://www.sap.com/products/artificial-intelligence/ai-ethics.html).
[^oracle]: [Overview of Generative AI Agents Service](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm).
[^siemens]: [Siemens Industrial Copilot](https://www.siemens.com/en-us/company/insights/generative-ai-industrial-copilot/).
[^abb]: [ABB Genix™ Copilot | Unlocks the power of GenAI@scale enabling industries to outrun leaner and cleaner - ABB Genix™ Industrial IoT and AI Suite Genix™ Industrial IoT and AI Suite | ABB](https://new.abb.com/process-automation/genix/abb-genix-copilot).
[^palantir]: [Overview • AIP • Palantir](https://www.palantir.com/docs/foundry/aip/overview).
[^uipath]: [Maestro - Overview](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/overview?fallbackReason=invalidTopic&isFallback=true&fallbackCount=1).
[^intercom]: [From resolutions to outcomes: Evolving how Fin delivers value - The Intercom Blog](https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/).
[^thomson-reuters]: [AI Principles | Thomson Reuters](https://www.thomsonreuters.com/en/artificial-intelligence/ai-principles).
