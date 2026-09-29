---
type: Guide
title: "Factory implementation trade-offs"
description: "Compare prose, code, skills, plugins, extensions, and external gates by their roles, costs, failure modes, and evidence."
status: stable
sources:
  - id: plugins
    resource: https://developers.openai.com/plugins/concepts/plugins
    title: "OpenAI: Plugin architecture"
  - id: mcp-security
    resource: https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices
    title: "MCP security best practices, 2025-11-25 documentation"
  - id: workflows
    resource: https://www.anthropic.com/engineering/building-effective-agents
    title: "Anthropic: Building effective agents"
  - id: replay
    resource: https://docs.temporal.io/workflow-execution
    title: "Temporal Workflow Execution overview"
  - id: idempotency
    resource: https://docs.temporal.io/activity-definition
    title: "Temporal Activity Definition"
  - id: context-effectiveness
    resource: https://arxiv.org/html/2602.11988v2
    title: "Gloaguen et al.: Evaluating AGENTS.md, version 2"
  - id: context-efficiency
    resource: https://arxiv.org/html/2601.20404v1
    title: "Lulla et al.: On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents, version 1"
  - id: evals
    resource: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    title: "OpenAI: Evaluation best practices"
---

# Factory implementation trade-offs

## Recommendation and scope

Choose a mechanism for each activity and control, then assess the composition. A useful starting arrangement is prose for purpose and judgment, skills for reusable procedures, deterministic code for precise operations, optional plugins or extensions for delivery and integration, and protected gates for consequential transitions. A small factory may need only a few of these.

This guide and its linked mechanism notes synthesize primary sources inspected on **2026-09-28**, including two version-pinned empirical papers. Product documentation establishes described behavior; it does not prove a factory's effectiveness. The research was not rerun, and no deployed factory or live security configuration was assessed. Mutable documentation should be checked against the installed product before implementation. The comparisons and recommendations below are catalog inferences; attributed findings are marked with source footnotes.

Use the companion [implementation selection procedure](factory-implementation-selection.md) to apply the findings. This guide specializes the [ontology's Implementation, Assessment, and Evidence concepts](ontology.md#concepts). It adds implementation guidance without changing control requirements or creating new ontology types.

## 1. Separate the choices

These six options overlap. A skill can contain code; a plugin can distribute skills and tools; an extension can invoke a service; GitHub Actions can execute a deterministic validator or a model. Classify the contents and execution boundary as well as the package.

| Design question | What to record | Example |
|---|---|---|
| Where is intent expressed? | Requirements, rationale, exceptions, owner | Prose requirement with examples |
| Who chooses the next step? | Human, model, explicit program, or a mixture | Model chooses research sources; code schedules checks |
| How is capability delivered? | File, skill, plugin, extension, service | Plugin installs a skill and exposes an MCP tool |
| Where does it execute? | Process, host, environment, dependencies | Local script or remote workflow runner |
| What can prevent an effect? | Mandatory boundary, protected configuration, credentials | Destination service rejects an invalid grant |
| What supports acceptance? | Evaluator, target revision, criteria, retained observations | Review plus tests tied to the delivered artifact |

Here, **extension** means an integration into a host such as an editor, browser, or agent runtime. **Plugin** means an installable bundle of capabilities; vendors may use the two words interchangeably. **External gate** means a decision boundary outside the producing agent's effective control. A remotely hosted check is not independent if the agent can rewrite its criteria, forge its result, or bypass it.

Deterministic code has prescribed behavior for specified inputs and state. Code that calls a model or a changing service still contains uncertain results. A deterministic evaluator may consistently enforce the wrong rule. Specify which component is deterministic and which property it establishes.

## 2. Comparison by mechanism

The relative costs below are engineering judgments, not measured rankings. Existing infrastructure, volume, task variability, and consequences can reverse them.

| Mechanism | Best fit | Main benefit | Cost and failure modes | Evidence to seek |
|---|---|---|---|---|
| Prose | Purpose, definitions, judgments, exceptions, changing procedures | Cheap to revise; readable across tools and roles | Repeated context cost; ambiguity, conflicting instructions, missed loading, inconsistent execution | Actual instruction loading and task traces; rubric review; comparisons across representative requests |
| Deterministic code | Parsing, arithmetic, validation, state transitions, bounded retries | Precise interfaces; repeatable checks; efficient repeated operations | Engineering and dependency upkeep; brittle assumptions; systematic bugs; I/O uncertainty | Unit and integration results, adversarial fixtures, revision and environment identities |
| Skills | Recurring recognizable tasks with contextual decisions | Reusable workflow with selective loading and bundled resources | Wrong activation, missing activation, instruction drift, script dependencies, host differences | Activation tests separately from completion quality; script tests and permission tests |
| Plugins | Installable distribution of related workflows and service access | Central packaging and updates; coherent tool interfaces | Installation, authentication, version compatibility, server operations, supply-chain exposure | Installed inventory, component versions, API contracts, permission scope, upgrade/rollback results |
| Extensions and hooks | Host events, inline feedback, specialized UI, tool interception | Timely feedback and access to host context | Host coupling; activation gaps; disabled or absent installation; local/remote mismatch; error semantics | Host/version matrix; real event coverage; bypass, timeout, and disabled-state tests |
| External gates | Merge, publication, deployment, spending, acceptance transitions | Can make prerequisites mandatory across clients | Queue delay, outages, administration, false rejection; writable or optional gates; stale evidence | Valid and invalid transition attempts; effective rules, credential paths, evidence binding, observed effects |

For instruction loading and procedure activation, see [instruction and skill selection](guides/instruction-and-skill-selection.md). For event timing and alternate execution paths, see [extension and hook boundaries](guides/extension-and-hook-boundaries.md). For mandatory transitions and evaluator protection, see [external acceptance gates](guides/external-acceptance-gates.md).

### Code: precise operations and explicit state

Anthropic distinguishes workflows with prescribed code paths from agents that choose their processes dynamically. Its engineering guidance recommends increasing complexity only when task performance justifies the additional cost and latency. This is experience-based guidance, not a controlled comparison of all six mechanisms.[^workflows]

Move stable calculations, schema rules, comparisons, and repetitive transformations into small callable functions. Give them explicit inputs, outputs, errors, and versioned dependencies. Preserve the reason for each rule in prose. Keep a human or model judgment where the acceptance rule cannot be stated adequately; a format validator cannot determine whether a source actually supports an argument.

Durability requires additional design. Temporal, for example, resumes workflow execution by checking generated commands against recorded event history.[^replay] Its activities may retry if a completed effect was not reported; the documentation recommends idempotency, including destination-enforced operation keys.[^idempotency] A loop with retries does not establish one intended external effect. Retain uncertainty after lost responses and reconcile destination state, as described in the [reconcile before retry](controls/reconcile-before-retry.md).

### Plugins: distribution and capability composition

OpenAI describes plugins that can package skills and an MCP server that exposes tools, with lifecycle hooks and optional UI. Capabilities can be surface-specific. The MCP server defines tool schemas, authentication and authorization requirements, and structured results, and can be operated independently of the installed package.[^plugins]

A plugin is useful when multiple users need the same tested components or when a factory needs authenticated service access. Evaluate each component separately: procedural guidance, executable logic, remote service, credentials, and any UI. Record both the installed package revision and the service/API configuration; pinning a local package does not freeze a remote server.

The MCP security guidance forbids token passthrough without proper audience validation and describes how it can bypass controls and obscure accountability.[^mcp-security] For this catalog, the inference is to enforce grants where tools execute, including alternate API paths. Installing a plugin is neither a factory-specific authority grant nor proof of an assessed control. A narrowly scoped CLI may be simpler when distribution and live service integration add no benefit.

## 3. What empirical evidence does and does not establish

| Primary research | Finding in the inspected version | Limits for factory design |
|---|---|---|
| Gloaguen et al., AGENTS.md evaluation | In v2, generated context files had no statistically significant effect on resolution rates and raised inference costs by 20% on SWE-Bench Lite and 23% on CTXBench; developer-provided files improved average resolution by 2.4% (not statistically significant, p = .21) and also increased steps and cost | CTXBench includes 138 Python tasks from 12 repositories, alongside SWE-Bench Lite; the evaluation uses four agent/model settings and does not establish security or performance for every instruction design.[^context-effectiveness] |
| Lulla et al., AGENTS.md efficiency | On 124 PR tasks from 10 repositories, instructions were associated with 28.64% lower median runtime and 16.58% fewer median output tokens | Full semantic correctness was outside scope; a manual sanity check on 50 tasks checked for nontrivial work. Faster termination is not proof of equivalent correctness.[^context-efficiency] |

These findings address different tasks, instruction sets, agent configurations, and measures. They do not establish a universal winner or justify removing required instructions. Our inference is to retain necessary policy, minimize redundant guidance, and measure each proposed change against an unchanged baseline. Separate outcome quality, compliance, runtime, token use, and human rework.

OpenAI's evaluation guidance locates evaluation needs at sources of nondeterminism, including instruction following, model outputs, tool selection, and handoffs.[^evals] Apply that distinction to mixed factories: deterministic unit tests assess precise logic; repeated agent evaluations assess behavior over a defined sample; boundary tests assess enforcement. None substitutes for all the others.

## 4. Can one mechanism implement the whole factory?

The following are conditional design judgments derived from the distinctions above.

| Predominant implementation | When it can be enough | What still has to exist |
|---|---|---|
| Prose and human procedure | Low-volume work with changing judgments and accountable people executing and reviewing each step | People, tools, records, and actual authority restrictions where required; the document is the specification |
| Deterministic application | Inputs, transitions, and acceptable outputs are sufficiently specified | Dependency management, exception handling, observation of external effects, and an owner for changing requirements |
| One skill | A bounded recurring task on an existing capable host | Reliable activation, available tools, state/evidence retention, and separately enforced permissions |
| One plugin | A coherent installable product can package the needed components | Host, service operations, credentials, and assessment of each component and their composition |
| One extension | Work is deliberately confined to a supported host and its interfaces | Host lifecycle support and restrictions covering any out-of-host actions |
| External workflow platform | Work naturally follows event-triggered jobs and managed transitions | Domain logic, judgment where needed, durable records, and destination controls; a gate alone does not produce the work |

A factory can be delivered as one package while using several mechanisms internally. Avoid making “everything in a plugin” an architectural conclusion before identifying which parts are prose, code, services, and enforcement.

## 5. Lifecycle and economic trade-offs

Compare total cost over an agreed horizon: design and migration effort, execution, human review and rework, dependency upgrades, incident recovery, and retirement. Count accepted outcomes as well as attempts. Lower token use can be offset by more review work; cheaper validation can be offset by false rejection and queues. No source inspected supports a universal cost ratio across these mechanisms.

- **Move prose into code** when a rule is precise, repeated, testable, and stable enough to maintain. Keep ambiguous cases explicit rather than silently encoding a weak proxy.
- **Extract a skill** when a recognizable workflow recurs and loading its procedure selectively is useful. Keep always-applicable requirements in the host's reliably loaded instruction path.
- **Package a plugin** when installation, reuse, or service access warrants release management. Separate component versions and credential scopes.
- **Build an extension** when host events or UI measurably improve completion or review. Preserve a usable service or command interface when other clients are required.
- **Add a protected gate** when a transition must be withheld despite producer error or noncompliance. Check availability and exception handling so authorized work can proceed.

Reuse one tested validator across local feedback and remote acceptance where possible. Protect the acceptance revision of that validator independently if the producer can edit the local copy. Avoid duplicating policy logic in prose, scripts, plugins, and workflows without an owner and a reconciliation method. Keep distinct evaluators where correlated errors would defeat the required assurance.

## 6. Connections to the knowledge graph

These are explanatory relationships using the [existing ontology](ontology.md#relationships); they do not assert adoption or a successful assessment.

| Existing concept | Relationship expressed by this guide | Application |
|---|---|---|
| [Bounded external action](controls/bounded-external-action.md) | Implementation choices help realize its enforcement requirement | Put grant checks at covered execution boundaries and inventory alternate paths |
| [Evidence traceability](controls/evidence-traceability.md) | Mechanism selection determines which evidence can be inspected | Link claims to traces, source revisions, validator outputs, and reviewer dispositions |
| [Outcome verification](controls/outcome-verification.md) | Comparison measures instantiate local assessment criteria | Compare accepted outcomes and failures, including unknown outcomes and false rejection |
| [Software delivery factory](factories/software-delivery.md) | Provides an activity context for a mixed implementation | Pair iterative development with checks and separately authorized delivery |
| [Research factory](factories/research.md) | Provides a context where semantic review remains necessary | Code checks citation structure; a qualified reviewer assesses evidential support |
| [Implementation selection](factory-implementation-selection.md) | Applies this research to a local decision | Record mechanisms, ownership, bypasses, assessment plans, and reassessment triggers |

Assess [protected acceptance](controls/protected-acceptance.md) for evaluator independence, [durable work handoff](controls/durable-work-handoff.md) for persisted execution state, and [tool and dependency admission](controls/tool-and-dependency-admission.md) for supply-chain admission. For host compatibility changes, [controlled dependency change](controls/controlled-dependency-change.md) is an optional draft reference, not part of the stable bundle and not required to use this guide. Local mechanisms and evidence remain necessary; selecting an available catalog control does not establish its effectiveness. Follow [adoption](adoption.md#record-the-adoption) before claiming an implementation of a catalog control.

[^plugins]: OpenAI, Plugin architecture; component roles and surface-specific capabilities.
[^mcp-security]: MCP security best practices; token passthrough and trust-boundary risks.
[^workflows]: Anthropic, Building effective agents; workflow/agent distinction and complexity trade-offs. Originally published 2024-12-19; the page notes subsequent tooling changes.
[^replay]: Temporal Workflow Execution overview; replay and recorded event history.
[^idempotency]: Temporal Activity Definition; retries, unreported effects, and destination-enforced idempotency.
[^context-effectiveness]: Gloaguen et al., arXiv:2602.11988v2, sections 3–5; resolution rates, costs, and limitations.
[^context-efficiency]: Lulla et al., arXiv:2601.20404v1, sections 3.1.8 and 4; efficiency measures and correctness limitations.
[^evals]: OpenAI, Evaluation best practices; evaluation at sources of nondeterminism.
