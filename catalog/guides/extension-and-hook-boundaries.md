---
type: Guide
title: "Extension and hook boundaries"
description: "Assess host events, execution paths, and failure behavior before relying on extensions or hooks."
status: stable
sources:
  - id: extension-host
    resource: https://code.visualstudio.com/api/advanced-topics/extension-host
    title: "VS Code extension host"
  - id: workspace-trust
    resource: https://code.visualstudio.com/api/extension-guides/workspace-trust
    title: "VS Code Workspace Trust extension guide"
  - id: hooks
    resource: https://code.claude.com/docs/en/hooks
    title: "Claude Code hooks reference"
---

# Extension and hook boundaries

This note develops the [factory implementation comparison](../factory-implementation-tradeoffs.md). The cited product documentation was inspected on **2026-09-28**; it describes behavior and does not establish factory effectiveness. No deployed factory or live security configuration was assessed. Check mutable documentation against the installed product before implementation. Recommendations are catalog inferences.

## Extensions and hooks: close to the work, limited by the host

VS Code distinguishes local, remote, and browser extension hosts with different runtimes and installation locations.[^extension-host] Its Workspace Trust guide warns that hiding a command in the UI does not prevent invocation; execution must also be checked or left unregistered.[^workspace-trust]

Hooks require equally precise treatment. Claude Code documents blocking behavior for `PreToolUse`, while `PostToolUse` runs after the tool has executed. It also distinguishes blocking exit codes and timeout behavior: a timed-out command hook continues through the normal permission flow.[^hooks] These are host-specific examples, not universal hook contracts.

Use extensions to make the right action convenient and to expose review evidence at the point of work. A synchronous hook may reject a covered operation, but first establish event coverage, configuration protection, and failure behavior. A post-action notification can detect an unwanted effect; it cannot prevent the effect already observed. Test direct API and shell paths as well as the integrated UI. Move indispensable restrictions to a boundary that all those paths must traverse.

Use the [implementation selection procedure](../factory-implementation-selection.md) to record the choice and test the composed system. For restrictions shared across clients, assess [external acceptance gates](external-acceptance-gates.md) and the [bounded external action control](../controls/bounded-external-action.md).

[^extension-host]: VS Code extension host; execution locations and runtime requirements.
[^workspace-trust]: VS Code Workspace Trust extension guide; command invocation and execution checks.
[^hooks]: Claude Code hooks reference; per-event decision control, exit codes, and timeouts.
