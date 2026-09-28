# Proposed browsing vocabulary

[MVP overview](index.md) · [Model](model.md)

These are labels for discussion, not stable catalog identifiers or mutually exclusive categories. Domain, work type, workflow, autonomy, and authority are separate dimensions.

## Work types

| Work type | Distinguishing outcome |
|---|---|
| Research and discovery | Findings, evidence, or answers to open questions |
| Knowledge organization and stewardship | Structured, findable, maintained information |
| Analysis and diagnosis | Explanations of conditions, causes, and significance |
| Forecasting and simulation | Estimates of possible future outcomes |
| Strategy and planning | Objectives, priorities, and courses of action |
| Design and specification | Descriptions of what should be built or changed |
| Software and computational development | Executable systems and computational capabilities |
| Content and media production | Material that informs, explains, entertains, or persuades |
| Translation and adaptation | Material made useful for another audience or context |
| Evaluation and assurance | Evidence about quality, correctness, conformity, or readiness |
| Decision-making and adjudication | Selected options or dispositions with rationale |
| Advice and professional guidance | Recommendations tailored to a situation |
| Teaching and capability development | Improved understanding or ability |
| Case and transaction processing | Completed cases or updated operational records |
| Coordination and relationship work | Shared understanding, commitments, and agreements |
| Monitoring and operational response | Awareness of changes and appropriate interventions |

Research gathers evidence; analysis interprets it. Forecasting estimates what could happen; planning chooses what to do. Assurance checks criteria; adjudication decides what follows. Content creation produces teaching material; teaching aims to improve ability.

Combined labels such as monitoring and response are convenient for browsing. Describe constituent activities separately whenever authority, consequence, or validation differs. The examples should help determine which labels need splitting.

## Candidate control families

| Primary family | Governs |
|---|---|
| Purpose and accountability | Objectives, ownership, scope, exceptions |
| Intake and work definition | Inputs, requirements, triage, acceptance criteria |
| Knowledge and evidence | Sources, provenance, freshness, memory admission |
| Workflow and coordination | Dependencies, handoffs, escalation, stopping rules |
| Authority and access | Permissions, delegation, separation of duties |
| Quality and validation | Tests, review, uncertainty, acceptance |
| Information protection | Sensitivity, confidentiality, retention, deletion |
| Release and external action | Publication, commitments, transactions, rollout |
| Reliability and recovery | Budgets, retries, fallback, rollback |
| Change and dependencies | Changes to tools, models, instructions, suppliers |
| Monitoring and improvement | Operational observations, incidents, reassessment |

Add cross-cutting tags where useful: quality, security, privacy, safety, efficiency, accountability; prevent, detect, respond, recover; human procedure, instructions, automated check, technical restriction. Classification does not establish effectiveness.

## Context questions that change control selection

| Condition | Concern to investigate | Candidate response beyond or within this MVP |
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

The three MVP controls cover only part of this space. Record gaps explicitly; their presence must not be interpreted as a complete security or compliance program.
