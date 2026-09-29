---
type: Guide
title: "Assess workflow trace coverage"
description: "Reconstruct quality, latency, and cost across child work, retries, queues, and resumed operations."
status: draft
sources:
  - id: ap-traces
    resource: https://github.com/agentpatterns-ai/website/blob/7d655a99fdebfa373ceacfcb3a6171c53da1b883/observability/subagent-otel-trace-correlation.md
    title: "Agent Patterns: Subagent trace correlation"
---

# Assess workflow trace coverage

[Adoption](../adoption.md) · [Security event traceability](../controls/security-event-traceability.md)

## Procedure

Use for a workflow whose quality or cost depends on several actors or services. Apply security event traceability to required boundary events and extend its correlation record to operational diagnosis. Agent Patterns' trace guidance informs this adaptation.[^ap-traces]

1. Inventory work item, actor, parent, attempt, tool, input/output revision, queue/resume transition, and observed outcome. Define required events and coverage before collecting data.
2. Propagate correlation references across each supported boundary; distinguish a retry from a new logical operation. Record missing events explicitly rather than joining by similar timestamps alone.
3. Use [approved data processing](../controls/approved-data-processing.md) for telemetry destinations and retention. Keep private payloads out of shared traces; use protected references. Do not use unbounded per-run IDs as metric dimensions.
4. Reconstruct a successful workflow, a missing child event, a retry, and an interrupted/resumed trace. Reconcile totals with independent destination and resource observations where available.

## Assessment and limits

Pass when the complete case reconstructs correctly and the missing/interrupted cases show their coverage gaps; fail when a missing branch becomes a false completion or duplicate attempts distort reported totals. Required unavailable observations are inconclusive. Retain the inventory, event/configuration revisions, synthetic fixtures, reconstruction, totals, evaluator, time, and dispositions.

Correlation does not establish evidence authenticity or full instrumentation coverage. These fixtures have not been executed and do not prescribe a trace-storage product.

[^ap-traces]: Agent Patterns, subagent trace correlation; rewritten adaptation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
