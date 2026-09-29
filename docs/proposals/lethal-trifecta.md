---
type: Guide
title: "The lethal trifecta in AI workflows"
description: "Research and design guidance for private data, untrusted content, and external communication in connected AI workflows."
status: draft
tags: [security, privacy, prompt-injection, lethal-trifecta]
sources:
  - id: willison
    resource: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
    title: "The lethal trifecta for AI agents, 16 June 2025"
  - id: indirect-injection
    resource: https://arxiv.org/abs/2302.12173v2
    title: "Greshake et al., Not what you've signed up for, v2"
  - id: slack
    resource: https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private
    title: "PromptArmor, Slack AI data exfiltration, 20 August 2024"
  - id: github-mcp
    resource: https://invariantlabs.ai/blog/mcp-github-vulnerability
    title: "Invariant Labs, GitHub MCP Exploited, 26 May 2025"
  - id: echoleak
    resource: https://www.businesswire.com/news/home/20250611349150/en/Aim-Security-Launches-Aim-Labs-with-Elite-Researchers-from-Google-and-Israels-Unit-8200-to-Advance-AI-Security
    title: "Aim Security announcement of EchoLeak, 11 June 2025"
  - id: patterns
    resource: https://arxiv.org/html/2506.08837v1
    title: "Beurer-Kellner et al., Design Patterns for Securing LLM Agents against Prompt Injections, v1"
  - id: camel
    resource: https://arxiv.org/html/2503.18813v1
    title: "Debenedetti et al., Defeating Prompt Injections by Design, v1"
  - id: rule-of-two
    resource: https://ai.meta.com/blog/practical-ai-agent-security/
    title: "Meta, Agents Rule of Two, 31 October 2025"
  - id: ncsc
    resource: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
    title: "NCSC, Prompt injection is not SQL injection (it may be worse)"
  - id: browser-defenses
    resource: https://www.anthropic.com/research/prompt-injection-defenses
    title: "Anthropic, Mitigating the risk of prompt injections in browser use, 24 November 2025"
  - id: adaptive-attacks
    resource: https://arxiv.org/html/2510.09023v1
    title: "Nasr et al., The Attacker Moves Second, v1"
  - id: agentdojo
    resource: https://arxiv.org/abs/2406.13352v3
    title: "Debenedetti et al., AgentDojo, v3"
---

# The lethal trifecta in AI workflows

[Adoption](../../catalog/adoption.md) · [ATLAS threat assessment](../../catalog/atlas-threat-assessment.md) · [Capability separation](controls/lethal-trifecta-separation.md) · [Assessment procedure](guides/lethal-trifecta-assessment.md) · [Factory example](factories/compartmented-research.md)

## Definition and scope

Simon Willison's June 2025 formulation identifies three capabilities that can combine to enable theft of private information: access to private data, exposure to attacker-controlled content, and external communication. Communication includes HTTP requests and generated links, beyond explicit send or publish tools.[^willison]

The underlying mechanism is indirect prompt injection: an adversary puts instructions into material an application retrieves, so the model may act on that material as instructions. Greshake and colleagues demonstrated this class of attack in 2023, before the trifecta formulation.[^indirect-injection]

Use the trifecta as a **threat-modeling heuristic for confidentiality**. Its presence identifies an attack path to investigate; it does not measure attack probability or prove a particular exploit will succeed. Its absence does not establish overall safety: manipulated decisions, destructive actions, resource exhaustion, and deceptive answers can matter without private-data theft. These scope judgments and the catalog procedures below are catalog synthesis.

Research reviewed **2026-09-28**. The sources span foundational research, original demonstrations, architecture papers, public-sector guidance, and vendor evaluations. Papers are pinned to the editions actually inspected. Reading covered the cited mechanisms, threat models, and limitations; the Greshake and AgentDojo findings were checked at abstract level. No experiments or vendor exploits were reproduced. This is a focused research synthesis, not a systematic review of all prompt-injection literature.

## Identify the three capabilities in context

The following inventory is a proposed catalog application of the heuristic:

| Capability | Inspect | Commonly missed boundary |
|---|---|---|
| Private data | Prompt, conversation history, accessible files, retrieval stores, credentials, browser sessions, memory, private connectors | Data already in context remains available after its read tool is disabled; a confidential research question can itself be sensitive |
| Untrusted content | Web pages, inbound email, documents, issue text, attachments, images/OCR, search snippets, tool results, shared memory | A trusted service can carry text authored by an adversary; internal storage does not make every contribution authoritative |
| External communication | Search queries, URLs, request bodies, uploads, messages, shared records, renderer fetches, logs, telemetry, delegated tools | A read request transmits arguments; an approved service can contain an attacker-controlled account or publicly visible object |

Assess the **connected workflow**, including handoffs and later sessions. Three separate agents can reconnect the same path through shared storage or copied summaries. A reset context helps only when the transferred data, permissions, and persistent state preserve the intended boundary. Treat summaries as derived content whose sensitivity and origin still matter.

An embedded risk record using the existing [ontology](../../catalog/ontology.md) might read:

> An external author plants instructions in a source document consumed by a research activity. The activity can also retrieve internal planning data and construct outbound queries. If that content controls a later request, private planning information may reach an unauthorized recipient, harming the organization and people named in the data. The proposed separation control addresses this path; an assessment must establish the implementation's actual coverage.

This combines the existing scenarios for [retrieved instructions causing actions](../../catalog/risks/retrieved-instruction-action.md) and [disclosure through authorized tools](../../catalog/risks/authorized-tool-data-disclosure.md). Persistent handoffs also warrant assessment against [poisoned memory](../../catalog/risks/poisoned-persistent-memory.md).

## What the evidence establishes

| Source and evidence kind | Finding relevant to the trifecta | Limits of the evidence |
|---|---|---|
| Greshake et al., research paper, 2023[^indirect-injection] | Retrieved adversarial text can redirect application behavior and tool use; impacts include disclosure | Historical application demonstrations and synthetic experiments do not measure today's deployment risk |
| PromptArmor, original Slack AI report, 2024[^slack] | The reported chain combines public-channel instructions with private-channel data to form a link carrying a secret; user click completes disclosure | The report records disagreement during vendor disclosure. Its file-ingestion extension was explicitly untested; neither that extension nor current vulnerability status is established here |
| Invariant Labs, original GitHub MCP demonstration, 2025[^github-mcp] | Public issue text redirected an agent to private repositories and exposed information in a public PR | The demonstrated configuration and approval behavior matter. This is a composition failure using legitimate tools, not evidence that all MCP servers are compromised |
| Aim Security, EchoLeak announcement, 2025[^echoleak] | The discoverer reported an email-triggered disclosure chain in Microsoft 365 Copilot and a coordinated fix associated with CVE-2025-32711 | The original technical page returned HTTP 403 during this review. This row relies on the discoverer's announcement, not independent validation of the detailed chain or current product status |
| Beurer-Kellner et al., architecture paper, 2025[^patterns] | Six patterns restrict how untrusted data can influence actions: action selection, plan then execute, map/reduce, dual LLM, code then execute, and context minimization | Their security arguments depend on the chosen pattern's assumptions and enforced interfaces; they are not a blanket guarantee for general agents |
| Debenedetti et al., CaMeL paper, 2025[^camel] | An interpreter tracks data capabilities and enforces policy while separating a planner from a model that parses untrusted content | The threat model assumes a trusted user query and uncompromised memory. Policy completeness, implementation costs, user burden, and side channels remain concerns; answer manipulation is not generally solved |
| Meta, architecture guidance, 2025[^rule-of-two] | The Agents Rule of Two limits a session to two of untrusted input, sensitive access, and state change/external communication; all three call for supervision or reliable validation | This is broader than the original confidentiality framing because it includes state changes. A session boundary alone is not evidence of secure handoffs |
| NCSC, security guidance[^ncsc] | Prompt/data separation inside an LLM should not be treated as the enforceable separation provided by SQL parameterization | This motivates limiting consequences and evaluating assumptions; it does not imply that every architectural defense is ineffective |
| Anthropic, browser-agent evaluation, 2025[^browser-defenses] | Training, classifiers, and adversarial evaluation improved reported robustness while leaving residual attack success | The vendor's model, harness, and attacker budget bound the result. It is not a local probability estimate or evidence that a filter eliminates the risk |
| Nasr et al., adaptive evaluation, v1[^adaptive-attacks] | Attacks tailored to defenses bypassed protections that appeared stronger under weaker evaluations | Results concern evaluated defenses and threat models across jailbreaks and injection; do not apply an aggregate success rate to every agent |
| AgentDojo, evaluation framework, v3[^agentdojo] | Evaluates tool-using agents on legitimate tasks and security objectives in an extensible environment | Task failure can occur without attacks; utility and security outcomes must be distinguished. A benchmark cannot cover every deployment path |

## Select an architecture

These are design choices proposed for local assessment. They are not claims that the source authors endorsed this catalog's requirements.

| Choice | What it can interrupt | What must be established locally |
|---|---|---|
| Public research compartment with no private access | Removes the private-data leg from browsing | Initial brief, credentials, mounts, cookies, logs, and inherited memory contain no prohibited private data |
| Private analysis compartment without arbitrary outbound channels | Restricts disclosure even if source content redirects the model | Search, renderer fetches, subprocesses, delegates, telemetry, and later output release cannot bypass the boundary |
| Trusted plan with constrained execution | Limits tool selection and destinations that source material can alter | Tool arguments and outputs still meet disclosure rules; a fixed send step can carry an unsafe payload |
| Quarantined extraction with narrow interfaces | Limits content reaching a privileged planner | Free-text fields, errors, summaries, and reparsing cannot become instructions or expand access; valid JSON alone establishes only syntax |
| Enforced information-flow policy | Restricts which data may reach which recipients | Origin and sensitivity survive transformations, and every relevant channel checks the policy |
| Independent release review | Permits a specific intended disclosure | The review covers actual data, recipient, account, artifact revision, and active content; approval cannot silently apply to changed content |

The plan/argument distinction follows the design-pattern paper: fixing action order does not guarantee a safe message body.[^patterns] CaMeL illustrates why an enforced data policy adds something beyond separating two models.[^camel] These approaches trade automation, flexibility, implementation effort, and reviewer workload against the paths they close. Choose a combination based on the actual workflow.

Prompts, delimiters, provenance labels, classifiers, and model training can support the design. Count them as instructions or detection mechanisms unless an independent boundary prevents the prohibited effect. A trusted hostname alone does not identify an authorized recipient. A refusal in the transcript does not show what a renderer, connector, or delegated process actually transmitted.

## Apply the catalog

1. Use [the assessment procedure](guides/lethal-trifecta-assessment.md) to inventory data, influence, and disclosure paths.
2. Select [lethal trifecta separation](controls/lethal-trifecta-separation.md) to require an enforced break or independently authorized release on each path.
3. Apply [approved data processing](controls/approved-data-processing.md) for permitted processing scope and [bounded external action](../../catalog/controls/bounded-external-action.md) for execution authority. A valid action grant still needs a valid disclosure scope.
   Use [sensitive data egress](../../catalog/controls/sensitive-data-egress.md) where a release path remains, and [execution isolation](../../catalog/controls/execution-isolation.md) to enforce compartment boundaries. The separation control adds a workflow-wide check that handoffs and capability changes do not reconnect the three capabilities.
4. Use [evidence traceability](../../catalog/controls/evidence-traceability.md) for claim support, [outcome verification](../../catalog/controls/outcome-verification.md) for legitimate task success, and [controlled dependency change](controls/controlled-dependency-change.md) when tools or models change.
   Maintain the security fixtures and their release dispositions through [adversarial regression assessment](../../catalog/controls/adversarial-regression-assessment.md).
5. Compare the [fictional compartmented research factory](factories/compartmented-research.md) with local constraints. Record adoption by exact commit using [the adoption guide](../../catalog/adoption.md).

Reassess after changes to connectors, retrieval, memory, rendering, model behavior, credentials, sharing settings, delegation, or enforcement. Following suspected disclosure, stop the implicated paths, preserve restricted evidence, identify recipients and affected data, revoke exposed credentials where applicable, and use the local incident process before resuming. Preventing a recurrence does not undo a completed disclosure.

[^willison]: [Willison's original formulation](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
[^indirect-injection]: [Greshake et al., v2 abstract](https://arxiv.org/abs/2302.12173v2).
[^slack]: [PromptArmor's report and disclosure timeline](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private).
[^github-mcp]: [Invariant Labs, setup, demonstration, and scope](https://invariantlabs.ai/blog/mcp-github-vulnerability).
[^echoleak]: [Aim Security's announcement](https://www.businesswire.com/news/home/20250611349150/en/Aim-Security-Launches-Aim-Labs-with-Elite-Researchers-from-Google-and-Israels-Unit-8200-to-Advance-AI-Security).
[^patterns]: [Design Patterns, sections 3 and 4](https://arxiv.org/html/2506.08837v1).
[^camel]: [CaMeL, threat model, design, and limitations](https://arxiv.org/html/2503.18813v1).
[^rule-of-two]: [Meta's Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/).
[^ncsc]: [NCSC's discussion of prompt/data separation](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection).
[^browser-defenses]: [Anthropic's browser evaluation](https://www.anthropic.com/research/prompt-injection-defenses).
[^adaptive-attacks]: [The Attacker Moves Second, v1](https://arxiv.org/html/2510.09023v1).
[^agentdojo]: [AgentDojo, v3 abstract](https://arxiv.org/abs/2406.13352v3).
