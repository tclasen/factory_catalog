# Desktop pilot preflight — 2026-09-30

Historical observation under the original cancellation policy. The user later
authorized reporting-only thresholds; see the [current runbook](../README.md).
The stop denial below is preserved and no longer blocks admission under the
revised policy. It does not establish fresh-chat or session-log qualification.

**Decision: stop before live dispatch.** The required desktop stop capability is
unavailable. No catalog-effectiveness conclusion can be drawn.

Canonical work record: [issue #80](https://github.com/tclasen/factory_catalog/issues/80).
The [pilot procedure](../README.md) describes the implementation and resume conditions.

## Frozen intended comparison

Eight synthetic coding, document and analytical tasks; bare, minimal prompting and
full catalog; two repetitions; 48 task chats and up to 48 scorer chats. Model:
`gpt-6-astra`, reasoning `high`. Serial execution; 600-second task and 180-second
scorer deadlines. Seed: `20260930`.

Catalog source: `f4c6f53679248f3330a6724b8458fe0e49cd0999`, version `v1.0.0`.
Observed desktop application version: `26.924.51851`, build `12111`.
Observed desktop session runtime: `0.158.0-alpha.2.1`.
Frozen configuration hash: `beaa97121f5e2e021248e847d628298d9e05f0db5b1e4af06c9aec762d880a8c`.

## Observations

- The callable native tools provide create, read, wait and message operations for
  desktop chats. They provide no arbitrary-chat stop operation.
- Attempting `cua.getApp("Codex")` returned: “Computer Use is not allowed to use the
  app 'com.openai.codex' for safety reasons.” No further UI-control method was tried.
- The existing coordinator session shows identity, context, tool events, completion
  and usage records. This supports implementation of a format-specific reader;
  it does not qualify evidence collection from a newly dispatched experiment chat.
- The prepared manifest contains all 48 cells. Staging the first fixture outside the
  repository succeeded. The actual `reserve` command refused dispatch with the
  recorded stop-action gap, before writing any attempt reservation. The generated
  report independently reconciled 48 unattempted cells and zero scorer attempts.
- Moving a chat is a different operation and was not used as a cancellation
  workaround. No CLI or API model execution was substituted.

## All-cell reconciliation

| Condition | Planned | Task attempts | Scored | Pass rate | Silent-error rate |
|---|---:|---:|---:|---|---|
| bare | 16 | 0 | 0 | unknown | unknown |
| minimal | 16 | 0 | 0 | unknown | unknown |
| catalog-full | 16 | 0 | 0 | unknown | unknown |

All 48 task cells remain unattempted. Evaluator attempts: 0 of 48. No reservations
or uncertain live effects exist. Task-level effects, confidence intervals,
performance, model usage, evaluator disagreements and monetary cost are unknown.
There are no representative model successes or failures to inspect.

The local frozen experiment and generated all-cell report retain each assignment,
capability failure and input hash. Raw host/session evidence stays local; this
public report contains no account metadata or unrelated chat content.

## Resume condition

A supported, authorized mechanism must be able to stop the exact desktop chat and
verify cessation. Qualify that capability and the remaining preparation/evidence
gates, preserving this failed observation. Recheck the application, model, runtime
format and frozen harness identities before reserving any run. If those identities
changed, create a separately tracked configuration; do not rewrite this observation.
The first three-condition block must then qualify before the remaining blocks run.

This is an incomplete live pilot with a delivered software harness and a recorded
preflight outcome. Offline synthetic regressions do not establish desktop behavior,
benefit to adopters, or any operational control pass.
