---
type: Guide
title: "Instruction and skill selection"
description: "Choose prose and reusable skills with explicit checks for instruction loading, activation, and execution."
status: stable
sources:
  - id: agents-md
    resource: https://learn.chatgpt.com/docs/agent-configuration/agents-md
    title: "OpenAI: Custom instructions with AGENTS.md"
  - id: skills
    resource: https://agentskills.io/specification
    title: "Agent Skills specification"
---

# Instruction and skill selection

This note develops the [factory implementation comparison](../factory-implementation-tradeoffs.md). The cited product documentation was inspected on **2026-09-28**; it describes behavior and does not establish factory effectiveness. No deployed factory or live security configuration was assessed. Check mutable documentation against the installed product before implementation. Recommendations are catalog inferences.

## Prose: expressive policy, variable execution

Codex documents a discovery chain for `AGENTS.md`, with scope and precedence rules and a configured size limit. Merely storing instructions somewhere in a repository does not establish that a particular run loaded them.[^agents-md]

Use concise prose where interpretation is useful: intended beneficiaries, acceptable trade-offs, source quality, and escalation under uncertainty. Put frequently changing project facts in authoritative records with clear references. Duplicating the same requirement in several instruction files adds reconciliation work.

Prose can describe an entire human-operated factory. In an agent-operated factory it relies on the model, tools, and host to execute that description. It cannot itself remove a credential or prevent an unauthorized effect. The existing [bounded external action control](../controls/bounded-external-action.md) explicitly requires enforcement at execution paths.

## Skills: reusable procedures with a discovery dependency

The Agent Skills specification combines metadata and instructions in `SKILL.md` with optional scripts, references, and assets. It describes progressive loading from metadata to instructions to resources; its experimental `allowed-tools` support varies by implementation.[^skills]

This makes a skill useful for recurring work such as evidence review or preparing a release record. Evaluate two separate questions: did the correct procedure activate, and was it executed correctly? Test explicit invocation, indirect requests, similar tasks that should not activate it, and unavailable dependencies. Packaging a validator in a skill does not make invoking it mandatory. Authority still comes from the host and service configuration.

Prefer one coherent procedure over a skill containing every factory activity. A large skill can recreate the context and ambiguity costs of a large instruction file. Conversely, many tiny skills can make selection and handoffs harder. Choose the boundary through observed activation and task performance.

Use the [implementation selection procedure](../factory-implementation-selection.md) to record the choice and test the composed system. Compare task quality and cost using the [empirical evidence and its limits](../factory-implementation-tradeoffs.md#3-what-empirical-evidence-does-and-does-not-establish).

[^agents-md]: OpenAI, Custom instructions with AGENTS.md; discovery and instruction-chain behavior.
[^skills]: Agent Skills specification; directory structure, progressive disclosure, and experimental allowed-tools field.
