---
type: Guide
title: "Data mesh platform selection"
description: "Select shared platform services and evaluate a bounded cross-domain data pilot."
status: draft
tags: [data-mesh, data-stewardship]
sources:
  - id: platform
    resource: https://arxiv.org/html/2402.04681v1
    title: "Architectural Design Decisions for Self-Serve Data Platforms in Data Meshes, v1"
  - id: google
    resource: https://docs.cloud.google.com/architecture/data-mesh
    title: "Architecture and functions in a data mesh"
  - id: zalando
    resource: https://engineering.zalando.com/posts/2025/07/direct-data-sharing-using-delta-sharing.html
    title: "Direct Data Sharing using Delta Sharing at Zalando"
---

# Data mesh platform selection

[Data product design](guides/data-product-design.md) · [Adoption](adoption.md)

## Basis and applicability

Use this procedure when several teams need to produce or consume maintained data products. The platform study organizes design choices across infrastructure, product experience, and mesh experience; it offers alternatives rather than a single mandatory stack.[^platform] Google's guidance recommends business use cases with ready consumers and continued funding for the platform.[^google]

The procedure below is a proposed catalog adaptation. It can be used for research repositories, recurring financial analysis, public statistics, and supply-chain reporting. Platform functionality can combine staffed services and automation; document the actual mechanism.

## 1. Establish readiness and an alternative

Name a decision owner, a producer, a consumer, and the owner of the composed result. Describe the current bottleneck with observations. Confirm data rights, staffing, operating budget, and an escalation route. Record the simpler alternative, such as improving contracts on the current shared warehouse.

Stop expansion when ownership, authority, or consumer demand remains unresolved. A small pilot may still investigate those uncertainties if its scope and outputs remain explicit.

## 2. Select capabilities by consumer journey

| Journey | Minimum candidate capabilities | Evidence to collect |
|---|---|---|
| Produce | Standard storage/processing options, versioned publication, contract checks | Producer completes a release and detects an invalid contract |
| Find and understand | Search, identity, supported distributions, glossary and examples | New consumer locates and interprets a suitable product |
| Obtain authorized access | Identity, request route, policy application, revocation | Allowed request succeeds; denied and revoked requests fail |
| Operate | Quality indicators, service status, incident routing, cost visibility | Stale delivery is detected and reaches the responsible owner |
| Combine | Semantic mappings, lineage, consumer dependency records | Cross-domain fixture produces reconciled results |
| Change and retire | Version transition, consumer notice, recovery, disposition of copies | Breaking change and retirement rehearsals preserve agreed commitments |

For each capability, decide whether to reuse, buy, build, or provide a temporary human service. Assign an owner, supported interface, service target, failure behavior, and escape route. Evaluate technology choices against isolation, skills, accessibility, portability, transfer costs, and observed workload.

Separate central product discovery from data location. Avoid copying restricted data into the metadata catalog for convenience. Test metadata access as well as data access.

## 3. Make the operating model concrete

Evaluate [accountability](controls/data-product-accountability.md), [contracts](controls/data-product-contract.md), and [federated policy enforcement](controls/federated-data-policy-enforcement.md) for applicability; record the selection rationale and any gaps. This guide does not make every linked control mandatory. State which decisions domains can make independently and which need shared approval. Give producers access to a supported path for ordinary tasks and document exceptions.

Zalando's report describes manual token onboarding during its sharing pilot and subsequent work on recipient management.[^zalando] The local lesson is to measure actual manual intervention and support effort before describing a capability as self-service. Do not assume that the same authentication arrangement is appropriate elsewhere.

## 4. Run a bounded pilot

Before starting, specify duration, spending limit, intended population, acceptable defect rates, consumer completion target, and stop conditions. Include at least two products with one meaningful cross-domain dependency; one may already exist. Use synthetic data for destructive or denial tests, and authorized representative data for usefulness checks.

Measure time from request to usable data, reconciliation effort, agreed quality indicators, support workload, and total incremental cost. Record sample sizes, exclusions, missing measurements, and the baseline. Use [service objectives](controls/data-product-service-objectives.md) for delivery and [outcome verification](controls/outcome-verification.md) for the actual decision task.

Run a successful consumer journey, a semantic mismatch, a policy denial, a stale feed, and an upstream correction. Retain observed effects and failures. A prototype passing synthetic tests does not establish production reliability.

## 5. Decide whether to expand

Compare results to the predeclared criteria and simpler alternative. Expand, revise, or stop with a named decision maker and rationale. Count the continuing cost of domain stewardship, platform operations, training, consumer integration, and exception handling. Avoid using product count as a substitute for consumer benefit.

The next increment should add a distinct consumer or operating constraint that tests reuse. Rerun affected assessments when the architecture or policies change. Record local implementations and evidence separately from this guide; pin adopted control revisions.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^platform]: [Architectural Design Decisions for Self-Serve Data Platforms in Data Meshes, v1](https://arxiv.org/html/2402.04681v1).
[^google]: [Architecture and functions in a data mesh](https://docs.cloud.google.com/architecture/data-mesh).
[^zalando]: [Direct Data Sharing using Delta Sharing at Zalando](https://engineering.zalando.com/posts/2025/07/direct-data-sharing-using-delta-sharing.html).
