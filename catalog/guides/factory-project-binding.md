---
type: Guide
title: "Factory project binding"
description: "Bind reusable controls to confirmed project intent, authority, environment, and acceptance."
status: draft
sources:
  - id: workflows-onboarding
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/onboarding.md
    title: "New-project onboarding interview"
  - id: templates-project
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md
    title: "Project binding template"
  - id: policies-governance
    resource: https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md
    title: "Scope, authority and security"
---

# Factory project binding

[Delivery lifecycle](factory-delivery-lifecycle.md) · [Adoption](../adoption.md)

## Purpose and trigger

Use when adopting a factory process for a new project or when its existing context record is missing or materially stale. This guide adapts the source onboarding interview and project template into a project-owned binding.[^workflows-onboarding][^templates-project] The binding records local facts and decisions; it is not an authority grant.

## Owner and inputs

One accountable adopter gathers the user request, current repository instructions and state, existing requirements, known grants, and environment facts. Keep the reusable catalog unchanged by project-specific answers. Use actual authority sources rather than inferring permissions from tools or credentials.[^policies-governance]

## Procedure

1. Inspect existing evidence and conversation before asking questions. Reuse current confirmed facts and preserve existing work.
2. Fill the applicable fields below. Mark each material answer as observed, owner-confirmed, unknown, deferred, or not applicable, with its source. Do not turn a hypothetical future activity into accepted scope.
3. Ask focused questions in short batches only when missing intent, authority, or consequential choices affect the next work. Allow unknown/deferred answers; block only dependent actions or claims.
4. Select applicable controls with rationale under the [adoption guide](../adoption.md), preserving exact catalog commit URLs and local adaptations. Record mechanisms separately from selected requirements.
5. Reconcile root instructions with the binding and selected controls. Keep one canonical location for each local rule; record authorized exceptions with scope, reason, owner, risk, and review/expiry condition.
6. Perform the [adoption readiness review](factory-adoption-readiness.md). Report the prepared binding, unresolved dependencies, and next authorized work.

## Binding fields

| Section | Record locally |
|---|---|
| Purpose | Intended users, outcome, success criteria, owner, current priority |
| Scope | Current authorized phase, work and exclusions; source of each material decision |
| Canonical records | Requirements, roadmap, architecture, source/tests, evidence, agent instructions, operations |
| Authority | Actual grants for reads, writes, data processing, providers, spending, publication, deployment, and delegation; approval conditions and unknowns |
| Environment | Available tools, platforms, limitations, repository protections, credential references only |
| Controls | Selected identity/version/pinned URL, applicability rationale, local mechanism/owner, adaptations, assessment state |
| Coordination | Lead, edit boundaries, concurrency/resource limits, handoff location, optional dispatcher choice |
| Quality | Applicable criteria, pinned tools/settings, actual commands, test layers, exceptions, unavailable checks |
| Delivery | Authorized endpoint, integration/publication stages, installed checks where relevant, explicit inapplicability |
| Operations | Health, recovery/backup objectives, maintenance and retirement owners and scope where services exist |
| Unknowns | Missing fact/decision, affected activity or claim, responsible owner and resume condition |

## Relationships and walkthrough

The binding supplies local context for [accepted work definition](../controls/accepted-work-definition.md), [approved data processing](../controls/approved-data-processing.md), [bounded external action](../controls/bounded-external-action.md), and [verified delivery](../controls/verified-delivery.md). A reference to a control does not prove its implementation or grant authority.

Walk a second unrelated project: generic requirements remain unchanged, its own grants and paths are used, and unknown commands remain unknown. Then remove a deployment grant: authorized planning can continue while deployment remains blocked. Completion means the binding and unknowns are reviewable; product readiness and control effectiveness still require their own assessments.

The cited onboarding, project-template, and governance pages support the interview, binding fields, and authority boundary described above. The catalog-control mapping and ordered procedure are proposed catalog synthesis; this guide grants no authority and reports no adoption or effectiveness result.

[^workflows-onboarding]: [New-project onboarding interview](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/workflows/onboarding.md).
[^templates-project]: [Project binding template](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/templates/project.md).
[^policies-governance]: [Scope, authority and security](https://github.com/tclasen/semantic_search/blob/70cfad0de635197f36f14e5276dec145483c5128/factory/policies/governance.md).
