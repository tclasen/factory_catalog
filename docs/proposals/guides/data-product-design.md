---
type: Guide
title: "Design a shared data product"
description: "Select ownership, contracts, semantics, policy, and delivery controls for a producer-consumer pilot."
status: draft
sources:
  - id: principles
    resource: https://martinfowler.com/articles/data-mesh-principles.html
    title: "Data Mesh Principles and Logical Architecture"
  - id: design
    resource: https://martinfowler.com/articles/designing-data-products.html
    title: "Designing data products"
---

# Design a shared data product

[Adoption](../../../catalog/adoption.md) · [Product records](../data-product-records.md) · [Platform selection](../data-mesh-platform-selection.md)

## Begin with a consumer outcome

Choose a recurring decision and a willing producer-consumer pair. Record the baseline delay, reconciliation effort, cost, and error; name an owner for the combined result. Work backward from the use case to the minimum supported product and service.[^design] Domain ownership, product interfaces, shared services, and governance are linked responsibilities.[^principles]

| Responsibility | Local decision and evidence |
|---|---|
| Producer | Funded owner, supported content, meaning, maintenance, and absence coverage |
| Consumer | Intended use, tolerated delay/error, access scope, and acceptance evidence |
| Platform | Identity, publication, observation, recovery, and operating support |
| Governance | Common rules, delegated decisions, conflicts, exceptions, and enforcement |
| Combined product owner | Mappings, dependencies, downstream commitments, and overall outcome |

## Select controls by failure boundary

Start with [accountability](../controls/data-product-accountability.md), [contracts](../controls/data-product-contract.md), [semantic interoperability](../controls/data-semantic-interoperability.md), and [policy enforcement](../controls/federated-data-policy-enforcement.md). Add [discovery](../controls/data-product-discovery.md) for finding supported products, [service objectives](../controls/data-product-service-objectives.md) for delivery expectations, [lineage](../controls/data-lineage-impact.md) for impact, and [contract evolution](../controls/data-contract-evolution.md) for change. Selection is local; this list is not a universal mandatory package.

## Compare delivery arrangements

Compare shared storage, domain stores with materialized copies, federated queries, batch snapshots, events, and hybrids using the [platform guide](../data-mesh-platform-selection.md). Assess identity on every hop, source outages, consistency, lag, deletion, duplicate events, correction semantics, residency, and recovery for the chosen interfaces. Distributed ownership does not require physically separate storage.

Include platform operation, stewardship, training, duplicate storage, transfers, integration, and governance review in the cost. Explicitly fund work whose benefit accrues to another domain. A small coordination problem may need clearer ownership and contracts on the current platform rather than decentralization.

## Pilot assessment

Have a new consumer use the product without private explanations. Test ambiguous units/keys, stale discovery records, a denied alternate access path, an upstream definition change, late correction, and owner absence. A permitted publication/access request should complete; record elapsed time and manual steps. Run the selected controls' full assessments and compare the beneficiary outcome with the baseline.

Use [regional water evidence](../factories/regional-water-evidence.md) as a fictional example. Similar decisions arise for lab observations, municipal statistics, invoice reconciliation, shipment events, learner summaries, and legal research collections. Use [approved data processing](../controls/approved-data-processing.md) and [scoped retirement](../controls/scoped-retirement.md) for permitted use and copy disposition. Retain required or public-interest outputs through an explicit owner decision rather than a usage-count rule alone.

These are proposed design and assessment procedures; no pilot has been executed. Architecture descriptions and standards metadata do not establish interoperability, compliance, or benefit.

[^principles]: Dehghani, Data Mesh Principles and Logical Architecture; architectural proposal, not controlled outcome evidence.
[^design]: Prakash, Designing data products; practitioner method. Source inspection inherited from the repository's 2026-09-28 research.
