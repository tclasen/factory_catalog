---
type: Guide
title: "Decompose the semantic_search factory"
description: "Map the source factory folder to individually selectable draft controls and supporting guides."
status: draft
sources:
  - id: readme
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/README.md
    title: "Factory overview"
  - id: agents
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/AGENTS.md
    title: "Agent operating contract"
  - id: policies-governance
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md
    title: "Scope, authority and security"
  - id: policies-planning
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md
    title: "Requirements and planning"
  - id: policies-execution
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md
    title: "Ownership, execution and recovery"
  - id: policies-verification
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md
    title: "Verification and review"
  - id: policies-delivery
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md
    title: "Integration, release and completion"
  - id: policies-instructions
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/instructions.md
    title: "Durable instructions and improvement"
  - id: workflows-lifecycle
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/lifecycle.md
    title: "Intent-to-delivery workflow"
  - id: workflows-onboarding
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/onboarding.md
    title: "New-project onboarding interview"
  - id: workflows-operations
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md
    title: "Operations, maintenance and retirement"
  - id: readiness
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/readiness.md
    title: "Adoption and framework readiness"
  - id: templates-project
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md
    title: "Project binding template"
  - id: templates-work-item
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md
    title: "Work-item template"
---

# Decompose the semantic_search factory

[Catalog](index.md) · [Ontology](ontology.md) · [Earlier product lessons](semantic-search-learnings.md)

## Source and design boundary

This decomposition covers all 14 Markdown files in `tclasen/semantic_search/factory/` at `70cfad0de635197f36f14e5276dec145483c5128`, the last commit that changed the folder before its retirement. The source describes a portable set of factory instructions, workflows, policies, and templates; it supplies no orchestration runtime or grants.[^readme]

The folder was marked historical at [e7a16d1](https://github.com/tclasen/semantic_search/commit/e7a16d103c88c3fc4c289e708255da145e6dd739) and removed at [d0b5f56](https://github.com/tclasen/semantic_search/commit/d0b5f56414d65e3cf2746781b860080d393895ac). The pinned materials below support this decomposition; they are not the source project's current operating instructions. Unlike the earlier product-oriented guide, this guide derives its proposed nodes directly from the requested folder.

**Coverage:** 17 controls (15 draft definitions and two stable definitions shared with the Software Factory synthesis) and five supporting guides, using the existing `Control` and `Guide` types and existing control families. This source map is a sixth Guide. A node groups one selectable requirement with its implementation and assessment. File boundaries in the source are not node boundaries: execution policy yields several controls, while related requirements from several files share one node. Each linked definition retains pinned sources and keyed footnotes. The shared evidence-validity and retry definitions combine both source bases. Operational assessments have not been run; lifecycle status records definition maturity, and no `verified` event is asserted.

## Proposed controls

| Control | Existing primary family |
|---|---|
| [Accepted work definition](controls/accepted-work-definition.md) | `intake-and-work-definition` |
| [Planning consistency](controls/planning-consistency.md) | `change-and-dependencies` |
| [Assessment evidence validity](controls/assessment-evidence-validity.md) | `knowledge-and-evidence` |
| [Acceptance coverage](controls/acceptance-coverage.md) | `quality-and-validation` |
| [Local quality gates](controls/local-quality-gates.md) | `quality-and-validation` |
| [Verified delivery](controls/verified-delivery.md) | `release-and-external-action` |
| [Bounded execution](controls/bounded-execution.md) | `reliability-and-recovery` |
| [Safe work resumption](controls/safe-work-resumption.md) | `workflow-and-coordination` |
| [Reconcile before retry](controls/reconcile-before-retry.md) | `reliability-and-recovery` |
| [Isolated parallel work](controls/isolated-parallel-work.md) | `workflow-and-coordination` |
| [Task configuration selection](controls/task-configuration-selection.md) | `workflow-and-coordination` |
| [Instruction change control](controls/instruction-change-control.md) | `monitoring-and-improvement` |
| [Verified service recovery](controls/verified-service-recovery.md) | `reliability-and-recovery` |
| [Independent restoration](controls/independent-restoration.md) | `reliability-and-recovery` |
| [Controlled dependency change](controls/controlled-dependency-change.md) | `change-and-dependencies` |
| [Scoped retirement](controls/scoped-retirement.md) | `information-protection` |
| [Approved data processing](controls/approved-data-processing.md) | `information-protection` |

## Supporting guides

- [Factory project binding](guides/factory-project-binding.md): onboarding and a local context/authority record.
- [Factory work record](guides/factory-work-record.md): durable evidence, ownership, effects, limits, and resumption fields.
- [Factory delivery lifecycle](guides/factory-delivery-lifecycle.md): composition of controls into stages, accountable roles, and exit/failure routes.
- [Factory adoption readiness](guides/factory-adoption-readiness.md): portability and procedure walkthroughs with explicit evidence limits.
- [Optional dispatcher and lead handoff](guides/factory-dispatcher-handoff.md): the source's conditional role arrangement and return protocol.

## Complete source-to-node map

Each row names the destination of its reusable content. Generic repeated rules are linked once; concrete paths, role preferences, and grants remain local binding choices.

| Source file | Decomposition |
|---|---|
| `README.md`[^readme] | [Adoption readiness](guides/factory-adoption-readiness.md), [project binding](guides/factory-project-binding.md); preserve separation between reusable process and host facts. |
| `AGENTS.md`[^agents] | [Delivery lifecycle](guides/factory-delivery-lifecycle.md) composes the operating contract; [dispatcher guide](guides/factory-dispatcher-handoff.md) retains conditional role entry. This is source data, not new repository instructions. |
| `policies/governance.md`[^policies-governance] | [Accepted work definition](controls/accepted-work-definition.md), [approved data processing](controls/approved-data-processing.md), and existing [bounded external action](controls/bounded-external-action.md); exception handling in [instruction change control](controls/instruction-change-control.md). |
| `policies/planning.md`[^policies-planning] | [Accepted work definition](controls/accepted-work-definition.md), [planning consistency](controls/planning-consistency.md), and prerequisite-ready selection/factory-first boundaries in the [lifecycle](guides/factory-delivery-lifecycle.md). |
| `policies/execution.md`[^policies-execution] | [Bounded execution](controls/bounded-execution.md), [safe work resumption](controls/safe-work-resumption.md), [reconcile before retry](controls/reconcile-before-retry.md), [isolated parallel work](controls/isolated-parallel-work.md), [task configuration selection](controls/task-configuration-selection.md), [assessment evidence validity](controls/assessment-evidence-validity.md), plus [work record](guides/factory-work-record.md) and [dispatcher](guides/factory-dispatcher-handoff.md). |
| `policies/verification.md`[^policies-verification] | [Acceptance coverage](controls/acceptance-coverage.md), [local quality gates](controls/local-quality-gates.md), [assessment evidence validity](controls/assessment-evidence-validity.md); existing [evidence traceability](controls/evidence-traceability.md) and [outcome verification](controls/outcome-verification.md) retain their current meanings. |
| `policies/delivery.md`[^policies-delivery] | [Verified delivery](controls/verified-delivery.md), [reconcile before retry](controls/reconcile-before-retry.md), and [verified service recovery](controls/verified-service-recovery.md). Commit style and exact authorized integration endpoint remain host choices. |
| `policies/instructions.md`[^policies-instructions] | [Instruction change control](controls/instruction-change-control.md), with benefit assessment linked to existing [outcome verification](controls/outcome-verification.md). |
| `workflows/lifecycle.md`[^workflows-lifecycle] | [Delivery lifecycle](guides/factory-delivery-lifecycle.md); reusable requirements link to controls instead of being repeated as a second policy. |
| `workflows/onboarding.md`[^workflows-onboarding] | [Project binding](guides/factory-project-binding.md) and [adoption readiness](guides/factory-adoption-readiness.md); reuse known facts and ask only consequential missing questions. |
| `workflows/operations.md`[^workflows-operations] | [Verified service recovery](controls/verified-service-recovery.md), [independent restoration](controls/independent-restoration.md), [controlled dependency change](controls/controlled-dependency-change.md), and [scoped retirement](controls/scoped-retirement.md). Credential rotation is an authorized dependency/security change whose positive and denied paths also use [bounded external action](controls/bounded-external-action.md). |
| `readiness.md`[^readiness] | [Adoption readiness](guides/factory-adoption-readiness.md) and the optional [dispatcher walkthrough](guides/factory-dispatcher-handoff.md); documentation and runtime qualification remain separate. |
| `templates/project.md`[^templates-project] | [Project binding](guides/factory-project-binding.md); copied grant values are excluded and unknowns stay explicit. |
| `templates/work-item.md`[^templates-work-item] | [Work record](guides/factory-work-record.md); local IDs, status, effects, limits, and evidence are records, not new globally registered node types. |

## Graph relationships and composition

An adopter's factory **performs** activities described by the lifecycle. A local implementation **implements** a pinned control revision and **applies within** an activity. An assessment **evaluates** that implementation and **uses** retained evidence. These reuse the existing [ontology relationships](ontology.md#relationships).

For example, a proposed release consumes a candidate artifact, applies evidence validity and acceptance coverage, and then uses verified delivery under bounded external action. An ambiguous destination response invokes reconciliation before retry. Interruption invokes safe work resumption, while a failed installed release may require service recovery. Backup recovery additionally depends on independent restoration. Links specify intended composition, not successful assessment or adoption.

The source's templates become guides for local records. Create separate Actor, Implementation, or Assessment nodes only when there is a concrete subject with reusable identity and real evidence; no fictitious successful assessment is added here.

## Decisions made explicit for review

- **Reuse existing requirements:** permission remains in bounded external action; claim support in evidence traceability; beneficiary success in outcome verification. Related source requirements do not create duplicate controls.
- **Keep distinct failure boundaries:** resumption establishes current scope/ownership, retry reconciliation establishes the outcome of one uncertain mutation, and parallel-work isolation governs simultaneous contributions. Service recovery checks current operation; independent restoration tests whether recovery inputs suffice without the primary.
- **Generalize delivery scope:** the source defaults to main integration. Verified delivery uses the agreed authorized endpoint, so a catalog PR does not grant merge authority. Exact commit style, tool choices, grants, and destinations remain in the host binding.
- **Make structure optional:** fresh-context dispatcher/lead operation is a guide for an explicitly selected arrangement. It does not require this repository to launch agents or adopt an execution framework.
- **Keep configuration choices current:** model and effort selection records available options and uncertainty; no model name, fixed budget, or universal tier ranking is imported. Numerical budget heuristics are local parameters under bounded execution.
- **Preserve provenance without copying the kit:** the source's whole-folder copy instruction becomes selection of pinned controls and required supporting concepts under [catalog adoption](adoption.md).

Review these draft boundaries and requirements before treating their definitions as stable. This proposal changes neither the ontology nor an approved baseline. The next decision is which draft definitions to adopt or refine, followed by assessments of actual local implementations.

[^readme]: [Factory overview](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/README.md).
[^agents]: [Agent operating contract](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/AGENTS.md).
[^policies-governance]: [Scope, authority and security](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md).
[^policies-planning]: [Requirements and planning](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/planning.md).
[^policies-execution]: [Ownership, execution and recovery](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/execution.md).
[^policies-verification]: [Verification and review](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/verification.md).
[^policies-delivery]: [Integration, release and completion](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/delivery.md).
[^policies-instructions]: [Durable instructions and improvement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/instructions.md).
[^workflows-lifecycle]: [Intent-to-delivery workflow](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/lifecycle.md).
[^workflows-onboarding]: [New-project onboarding interview](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/onboarding.md).
[^workflows-operations]: [Operations, maintenance and retirement](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/operations.md).
[^readiness]: [Adoption and framework readiness](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/readiness.md).
[^templates-project]: [Project binding template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md).
[^templates-work-item]: [Work-item template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/work-item.md).
