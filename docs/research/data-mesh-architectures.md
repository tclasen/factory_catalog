---
type: Guide
title: "Data mesh architectures and graph opportunities"
description: "Research synthesis and assessable graph additions for data stewardship across knowledge-work domains."
status: draft
tags: [data-mesh, data-stewardship]
sources:
  - id: principles
    resource: https://martinfowler.com/articles/data-mesh-principles.html
    title: "Data Mesh Principles and Logical Architecture"
  - id: design
    resource: https://martinfowler.com/articles/designing-data-products.html
    title: "Designing data products"
  - id: interviews
    resource: https://arxiv.org/html/2302.01713v2
    title: "Data Mesh: Best Practices to Avoid the Data Mess, v2"
  - id: review
    resource: https://arxiv.org/html/2304.01062v3
    title: "Data Mesh: A Systematic Gray Literature Review, v3"
  - id: platform
    resource: https://arxiv.org/html/2402.04681v1
    title: "Architectural Design Decisions for Self-Serve Data Platforms in Data Meshes, v1"
  - id: odcs
    resource: https://bitol-io.github.io/open-data-contract-standard/latest/
    title: "Open Data Contract Standard"
  - id: lineage
    resource: https://openlineage.io/docs/spec/object-model/
    title: "OpenLineage Object Model"
  - id: dcat
    resource: https://www.w3.org/TR/vocab-dcat-3/
    title: "Data Catalog Vocabulary (DCAT), Version 3"
  - id: fair
    resource: https://www.nature.com/articles/sdata201618
    title: "The FAIR Guiding Principles for scientific data management and stewardship"
  - id: google
    resource: https://docs.cloud.google.com/architecture/data-mesh
    title: "Architecture and functions in a data mesh"
  - id: zalando
    resource: https://engineering.zalando.com/posts/2025/07/direct-data-sharing-using-delta-sharing.html
    title: "Direct Data Sharing using Delta Sharing at Zalando"
  - id: ing
    resource: https://www.thoughtworks.com/en-ca/clients/financial-services/ing-bank
    title: "Data modernization with data mesh at ING"
---

# Data mesh architectures and graph opportunities

Contributor research: use this material to develop controls and task-focused guides. It is outside the distributed OKF bundle; consult current control requirements before reuse.

[Catalog](../../catalog/index.md) · [Ontology](../../catalog/ontology.md) · [Adoption](../../catalog/adoption.md)

## Scope and evidence

This research examines data mesh as an organizational and technical approach to sharing analytical data. It covers ownership, product design, platforms, governance, metadata, lineage, interoperability, economics, and adoption. Applications include scientific research, public-service analysis, finance operations, supply chains, and organizational knowledge stewardship.

The source set combines the original architectural proposal, practitioner guidance, two research syntheses, an interview study, three interoperability specifications, scientific stewardship principles, and two implementation reports. It is a purposive review of twelve public sources inspected on 2026-09-28, not an exhaustive systematic review. Research-paper versions are pinned; mutable documentation needs rechecking before implementation. Source pages and selected method, result, and limitation sections were inspected; no source implementations were executed.

### Evidence map

| Source | Finding used here | Evidence limit |
|---|---|---|
| Dehghani, 2020 architecture | Four connected principles: domain ownership, data as a product, self-service infrastructure, and federated computational governance. A product packages data, metadata, code, and supporting infrastructure. The primary focus is analytical data.[^principles] | An architectural proposal, not a controlled comparison of outcomes |
| Prakash, 2024 product design | Start with a consumer use case, work backward to products, then consider additional uses and service objectives.[^design] | Practitioner method; product boundaries remain context-dependent |
| Bode et al., 2023, v2 | Fifteen expert interviews report difficulties with governance, shifted responsibility, metadata quality, resources, and understanding. Providers may deprioritize work whose benefits accrue elsewhere.[^interviews] | Qualitative evidence; limited quantitative validity, acknowledged by the authors |
| Goedegebuure et al., review v3 | Synthesizes 114 industry gray-literature articles into roles, capabilities, development, and runtime views.[^review] | Repeated practitioner claims are not independent demonstrations of effectiveness |
| Platform architecture study, 2024 v1 | Identifies six main design decisions and 55 options, refined with six expert interviews.[^platform] | A decision catalog, not a benchmark proving one platform best |
| ODCS | Defines a structured data contract with schema, quality, support, team, and service-level sections.[^odcs] | Describes an agreement; actual delivery and enforcement need separate checks |
| OpenLineage | Models datasets, jobs, and runs; design-time metadata and runtime observations are distinct.[^lineage] | Instrumentation coverage determines what can be observed |
| W3C DCAT 3 | Supports catalog exchange, dataset/distribution distinctions, services, and version relationships.[^dcat] | Catalog interoperability does not establish semantic equivalence of the data |
| FAIR principles | Address findability, accessibility, interoperability, and reuse; authentication is compatible with accessibility.[^fair] | Scientific stewardship principles, not a data mesh implementation standard |
| Google architecture guidance | Describes producer, consumer, governance, and platform functions, and coexistence with existing platforms.[^google] | Vendor guidance; product choices and organizational roles are contextual |
| Zalando, 2025 sharing report | Describes partner sharing, manual onboarding constraints in the pilot, and work toward reusable recipient management.[^zalando] | First-party experience; platform expansion and identity federation are described as ongoing work |
| ING / Thoughtworks report | Describes an eight-week proof of concept using a production schema and synthetic data for a customer-service use case.[^ing] | Does not demonstrate production operation or measured bank-wide benefit |

## Architectural interpretation

The four mesh principles are interdependent: distributing ownership creates coordination needs, while shared services and rules make that distribution operable.[^principles] For this catalog, the useful unit is a maintained commitment to consumers: who supplies what, what it means, what evidence accompanies it, and what happens when it changes. This is our synthesis and the basis for the proposed controls below.

### Logical responsibilities

| Responsibility | Decisions to make locally | Failure to assess |
|---|---|---|
| Domain producer | Product boundaries, meaning, support, delivery | Ownership exists on paper but has no capacity |
| Consumer | Intended use, acceptable delay/error, interpretation | Technically readable data cannot answer the decision question |
| Platform | Provisioning, identity integration, publishing, observation | Every domain duplicates infrastructure or waits on tickets |
| Federated governance | Common rules, delegated decisions, conflict and exception handling | Autonomous teams produce incompatible or unauthorized exchanges |
| Cross-domain product owner | Composition, mappings, downstream commitments | Everyone owns an input but nobody owns the combined result |

Google's guide includes central supporting teams; their presence is compatible with distributed product responsibility.[^google] The balance of central and domain decision rights must be explicit. A shared storage service can serve separately owned products; separate storage accounts do not establish independent accountability. Treat these as different design axes.

### Deployment choices to compare

The following is a catalog decision aid, not a ranking established by the sources.

| Choice | Useful when | Costs and checks |
|---|---|---|
| Shared warehouse or lakehouse with domain-owned interfaces | Common tooling and operational support are valuable | Test isolation, noisy-neighbor effects, independent releases, and platform dependency |
| Domain stores with copied or materialized products | Local control or predictable analytical performance matters | Budget duplication; reconcile versions, lag, deletion, and residency constraints |
| Federated query over domain endpoints | Data should remain near its source and queries are feasible | Test source outages, authorization on every hop, consistency, latency, and query costs |
| Batch product exchange | Consumers can tolerate a defined delay and need reproducible snapshots | Specify cutoffs, missing delivery, late corrections, replay, and recipient handling |
| Event-oriented exchange | Consumers need timely changes | Define ordering, deduplication, schema evolution, replay, and correction semantics |
| Hybrid | Different products have different constraints | Keep one clear contract per supported interface and assess transitions between them |

Data mesh concerns responsibilities and product interfaces. Warehouse, lake, and lakehouse decisions concern storage and processing arrangements. Data fabric emphasizes technical integration; the interview paper treats it as related but distinct.[^interviews] A knowledge graph can describe products and relationships, but does not itself operate a mesh. Neither federated query nor a graph database is mandatory for the controls here.

## Graph additions and selection order

Each row links to an independently addressable OKF node. The priorities are proposed adoption order, not universal risk scores. Existing control families and document types are sufficient; these additions establish no new domain schema.

| Priority | Node | Relationship and distinct contribution |
|---|---|---|
| First | [Data product accountability](../proposals/controls/data-product-accountability.md) | Assigns the Actor responsible for product outcomes, support, and continuity |
| First | [Data product contract](../proposals/controls/data-product-contract.md) | Defines acceptance terms for shared Artifacts and their intended use |
| First | [Data semantic interoperability](../proposals/controls/data-semantic-interoperability.md) | Assesses mappings when Activities combine artifacts across domains |
| First | [Federated data policy enforcement](../proposals/controls/federated-data-policy-enforcement.md) | Checks consistent application of policy and Authority grants across routes |
| Next | [Data product discovery](../proposals/controls/data-product-discovery.md) | Makes products and supported distributions findable and reconciles coverage |
| Next | [Data product service objectives](../proposals/controls/data-product-service-objectives.md) | Connects consumer expectations to observations, breach response, and Evidence |
| Next | [Data lineage and impact assessment](../proposals/controls/data-lineage-impact.md) | Traces inputs, transformations, and affected consumers at specific revisions |
| Next | [Data contract evolution](../proposals/controls/data-contract-evolution.md) | Coordinates semantic changes, consumer transitions, and retirement |
| Supporting guide | [Data mesh platform selection](../proposals/data-mesh-platform-selection.md) | Helps select shared capabilities and a bounded pilot |
| Supporting guide | [Data product records](../proposals/data-product-records.md) | Shows how to describe ownership, interfaces, and evidence using existing concepts |
| Application | [Regional water evidence network](../proposals/factories/regional-water-evidence.md) | Fictional non-software example linking producers, consumers, controls, and assessments |

These controls complement [evidence traceability](../../catalog/controls/evidence-traceability.md), which tests support for material claims; [outcome verification](../../catalog/controls/outcome-verification.md), which tests beneficiary outcomes; and [bounded external action](../../catalog/controls/bounded-external-action.md), which tests authority for specific effects. A product can pass structural checks and still be wrong, unauthorized for a use, or unhelpful. These are separate findings.

## Opportunities beyond software factories

The following are proposed transfers of the researched ideas, not claims of deployed systems or sector-specific compliance.

| Domain | Candidate products and owners | Meaning or governance problem to test |
|---|---|---|
| Scientific collaboration | Lab-owned observations, methods, calibration records; consortium-owned synthesis | Units, detection limits, sample identity, reuse terms, corrections, and restricted access |
| Municipal planning | Agency-owned service demand and geographic indicators; planning-owned joined analysis | Boundary changes, denominators, reporting periods, disclosure limits, and missing populations |
| Finance operations | Billing-owned invoices, treasury-owned receipts, accounting-owned reconciliations | Cash versus accrual, currency basis, restatements, period cutoffs, and accountable approval |
| Supply-chain operations | Supplier-owned shipment events, warehouse-owned receipts, planning-owned lead-time indicators | Event time versus arrival time, duplicate events, item identity, and contractual sharing boundaries |
| Education evaluation | Program-owned attendance and assessment summaries | Cohort definitions, score comparability, learner privacy, and misleading cross-program comparisons |
| Legal knowledge stewardship | Matter-owned evidence inventories and approved research collections | Privilege restrictions, jurisdiction, superseded authorities, source revision, and permitted reuse |

FAIR gives a direct conceptual bridge to research stewardship, including provenance and community standards.[^fair] The ING report concerns customer-service analysis and the Zalando report concerns partner data exchange, illustrating application contexts beyond software delivery.[^ing][^zalando] Neither establishes effectiveness of the proposed transfers above.

## Adoption, economics, and failure modes

Start with a decision and willing producer-consumer pair. Establish the current delay, reconciliation effort, incident rate, and cost. Introduce the minimum products and shared services needed for that use; record an owner for the combined result. Expand only after measuring a useful outcome against the baseline. This is a proposed local evaluation strategy informed by use-case-first product design.[^design]

Include platform operations, domain stewardship, training, duplicate storage, cross-boundary transfer, consumer integration, and governance review in the cost model. Explicitly fund work whose benefits occur in another domain. The interview findings motivate examining incentives and resource constraints; they do not supply a universal return-on-investment estimate.[^interviews]

Common failure hypotheses and local probes:

- **Renaming datasets without changing service:** ask a new consumer to use the product without private explanations; inspect support and quality evidence.
- **Domain silos:** combine two products with ambiguous keys and units; verify the mismatch is caught.
- **Central platform bottleneck:** measure actual elapsed time and manual interventions for a permitted publication and access request.
- **Unfunded ownership:** exercise a support request during a planned absence and identify the responsible successor.
- **Governance theater:** try alternate access paths under denied and expired permissions, in an authorized test environment.
- **False confidence in catalogs:** reconcile with the publication inventory and inspect a stale record.
- **Uncontrolled dependencies:** change an upstream definition and verify downstream impact and consumer notice.
- **Product proliferation:** identify unused products, but retain necessary public-interest or mandatory outputs through an explicit owner decision rather than a usage-count rule alone.

A small organization with few producers and no recurring coordination problem may benefit more from clear ownership and contracts on its existing platform. Record the alternative and the measured reason to adopt further decentralization. No source reviewed here establishes a universal organization-size threshold.

## Deferred opportunities and evidence gaps

[Approved data processing](../proposals/controls/approved-data-processing.md) already addresses permitted use and destinations, [scoped retirement](../proposals/controls/scoped-retirement.md) covers resource and copy disposition, and [decision rights and accountability](../proposals/controls/decision-rights-and-accountability.md) covers authority and intervention. Potential later nodes include additional cross-product purpose restrictions, deletion propagation evidence, reference-data stewardship, cross-domain incident coordination, and allocation of shared platform costs. They need clear boundaries against existing or concurrent protection, recovery, dependency, and resource-budget work. Sector-specific legal controls need authoritative jurisdiction-specific research. Attested metric computations need actual sanctioned code, executor instructions, and deterministic attesters under pinned OKF §10; a metric description alone is insufficient.

This contribution intentionally keeps those opportunities as proposals. The delivered guides and controls are draft definitions. Local bundle checks establish structure and links, not operational effectiveness. Next review decisions are whether the boundaries are useful and which real producer-consumer pilot should exercise the proposed assessments. Adoption must pin identities and source revisions under the [adoption guide](../../catalog/adoption.md#record-the-adoption).

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^principles]: [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html).
[^design]: [Designing data products](https://martinfowler.com/articles/designing-data-products.html).
[^interviews]: [Data Mesh: Best Practices to Avoid the Data Mess, v2](https://arxiv.org/html/2302.01713v2).
[^review]: [Data Mesh: A Systematic Gray Literature Review, v3](https://arxiv.org/html/2304.01062v3).
[^platform]: [Architectural Design Decisions for Self-Serve Data Platforms in Data Meshes, v1](https://arxiv.org/html/2402.04681v1).
[^odcs]: [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/).
[^lineage]: [OpenLineage Object Model](https://openlineage.io/docs/spec/object-model/).
[^dcat]: [Data Catalog Vocabulary (DCAT), Version 3](https://www.w3.org/TR/vocab-dcat-3/).
[^fair]: [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618).
[^google]: [Architecture and functions in a data mesh](https://docs.cloud.google.com/architecture/data-mesh).
[^zalando]: [Direct Data Sharing using Delta Sharing at Zalando](https://engineering.zalando.com/posts/2025/07/direct-data-sharing-using-delta-sharing.html).
[^ing]: [Data modernization with data mesh at ING](https://www.thoughtworks.com/en-ca/clients/financial-services/ing-bank).
