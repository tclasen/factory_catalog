---
type: Taxonomy
title: "Control families"
description: "Control families and contextual questions for selecting controls."
status: stable
---

# Control families

[Catalog](index.md) · [Ontology](ontology.md) · [Controls](controls/)

Each control has one primary family and can have several cross-cutting tags. Families classify purpose; they do not imply that a family has complete control coverage.

## Families

| Family | Value | Governs |
|---|---|---|
| Purpose and accountability | `purpose-and-accountability` | Objectives, ownership, scope, exceptions |
| Intake and work definition | `intake-and-work-definition` | Inputs, requirements, triage, acceptance criteria |
| Knowledge and evidence | `knowledge-and-evidence` | Sources, provenance, freshness, memory admission |
| Workflow and coordination | `workflow-and-coordination` | Dependencies, handoffs, escalation, stopping rules |
| Authority and access | `authority-and-access` | Permissions, delegation, separation of duties |
| Quality and validation | `quality-and-validation` | Tests, review, uncertainty, acceptance |
| Information protection | `information-protection` | Sensitivity, confidentiality, retention, deletion |
| Release and external action | `release-and-external-action` | Publication, commitments, transactions, rollout |
| Reliability and recovery | `reliability-and-recovery` | Budgets, retries, fallback, rollback |
| Change and dependencies | `change-and-dependencies` | Changes to tools, models, instructions, suppliers |
| Monitoring and improvement | `monitoring-and-improvement` | Operational observations, incidents, reassessment |

Add cross-cutting tags where useful: quality, security, privacy, safety, efficiency, accountability; prevent, detect, respond, recover; human procedure, instructions, automated check, technical restriction. Classification does not establish effectiveness.

## Context questions that change control selection

| Condition | Concern to investigate | Candidate response beyond or within this catalog |
|---|---|---|
| External or adversarial inputs | Deceptive evidence, prompt injection | Provenance, separation of source content from instructions, enforced permissions |
| Sensitive data | Disclosure, inappropriate reuse | Access limits, destination restrictions, minimization, retention rules |
| Code execution or dependencies | Compromise, credential theft | Sandboxing, dependency verification, isolated credentials |
| External actions | Unauthorized commitments, duplicate actions | Bounded external action, idempotency, recovery |
| Multiple users or tenants | Cross-user disclosure | Isolation in storage, retrieval, caches, and memory |
| Persistent memory | Poisoned or stale information | Admission review, provenance, expiration, correction |
| Delegation | Expanded authority, lost constraints | Explicit delegated scope, constrained credentials, handoff evidence |
| Continuous or large-scale operation | Runaway costs, cascading failure | Budgets, rate limits, bounded retries, shutdown |
| Self-modification | Changed or bypassed controls | Protected configuration, independent authorization, regression assessment |
| Consequential human outcomes | Poor advice, inequitable treatment, misplaced reliance | Outcome measures, expert review, contestability, context-specific obligations |

The catalog controls cover only part of this space. Record gaps explicitly; their presence must not be interpreted as a complete security or compliance program.
