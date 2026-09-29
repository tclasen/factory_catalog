---
type: Guide
title: "Qualify AI factory infrastructure against workloads"
description: "Connect infrastructure capacity, reliability, cost, and energy measurements to accepted factory work."
status: draft
tags: [ai-factory, infrastructure, assessment]
sources:
  - id: nvidia-factory
    resource: https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html
    title: "Building AI Factories for the Enterprise"
  - id: supermicro-ra
    resource: https://www.supermicro.com/solutions/validated-design/NVIDIA-Enterprise-AI-Factory-Reference-Architecture-SMCI-Spectro-Cloud.pdf
    title: "NVIDIA Enterprise AI Factory reference architecture for Supermicro, revision 1.0.1"
  - id: cold-start
    resource: https://modal.com/docs/guide/cold-start
    title: "Cold start performance"
  - id: request-metrics
    resource: https://docs.fireworks.ai/guides/querying-text-models
    title: "Text Models: Response metadata and metrics"
  - id: energy
    resource: https://arxiv.org/abs/2311.16863
    title: "Power Hungry Processing: Watts Driving the Cost of AI Deployment?"
---

# Qualify AI factory infrastructure against workloads

[Research basis](../ai-leaders-research.md) · [Implementation selection](../factory-implementation-selection.md) · [Adoption](../adoption.md)

## Purpose and boundary

Use when choosing or changing hosted inference, a private AI platform, an accelerator stack, or infrastructure shared by several knowledge-work factories. Apply [task configuration selection](../controls/task-configuration-selection.md), [architecture decision traceability](../controls/architecture-decision-traceability.md), [workflow resource budgets](../controls/workflow-resource-budgets.md), and [verified service recovery](../controls/verified-service-recovery.md).

NVIDIA describes an AI factory as an integrated platform whose workload choices interact with compute, storage, networking, software, and facility constraints.[^nvidia-factory] A joint Supermicro/Spectro Cloud reference design specifies versions and component configuration and explicitly allows evaluated alternatives.[^supermicro-ra] These provide design evidence. Local qualification must establish the intended service and work outcomes.

This is an assessment guide for platform owners and factory owners. It does not prescribe hardware purchases or authorize experiments on live facilities. Physical power, cooling, and safety changes require their existing engineering and operating authority.

## Define the qualification envelope

| Area | Record |
|---|---|
| Accepted work | Task classes, quality criteria, authorized outcomes, accountable factory owner |
| Workload | Model and precision, input/output lengths, context distribution, concurrency, arrivals and bursts, retrieval sizes, training or checkpoint traffic if applicable |
| Placement | Hosted, private, or hybrid; tenant boundaries; permitted data and telemetry destinations |
| Platform revision | Accelerators, memory, drivers, runtime, serving framework, scheduler, network topology, storage, quotas, and vendor design deviations |
| Service objectives | Deadline, queue delay, response latency distribution, throughput at the required quality, error rate, and recovery objectives |
| Capacity | Limiting resource, reservations, utilization, spare capacity, overload behavior, and measured or contractual facility limits |
| Accounting | Included costs, currency and measurement date, reservation/idle costs, retries, failed jobs, human review, energy boundary, and missing meters |
| Evidence | Instrumentation coverage, client/server reconciliation, load generator, fixture revision, repeated runs, evaluator, and decision |

For managed services, record provider evidence and unavailable infrastructure details rather than inventing telemetry. Undocumented capacity or recovery behavior remains an uncertainty in the selection.

## Procedure

1. **Start with a feasible baseline.** Compare a suitable existing service or smaller deployment to the proposed platform. Hold work quality, data permission, and accounting boundaries constant. Keep claims of local measurement separate from supplier estimates.
2. **Test the complete path.** Include ingestion or retrieval, orchestration, model execution, tool calls, verification, and delivery. Measure component timings to diagnose bottlenecks, while using accepted end-to-end completion as the outcome. High token throughput can coexist with slow or incorrect work.
3. **Exercise workload variation.** Include short and long contexts, expected bursts, mixed task types, concurrent tenants where applicable, and cold starts. Modal distinguishes queue delay from first-invocation initialization, which motivates recording both cold and warm cases.[^cold-start] State arrival schedules and duration so another evaluator can repeat the comparison.
4. **Bound overload.** Exercise admission and shared-budget limits in an authorized test environment. Inspect whether rejected or queued work is explicit, whether retries amplify load, and whether an interrupted job can resume without resetting consumption. Connect this to [cumulative execution limits](../controls/cumulative-execution-limits.md).
5. **Reconcile observations.** Connect work IDs, attempts, client timeouts, provider responses, and final effects. Fireworks documents that provider dashboards exclude some client/network failures.[^request-metrics] A healthy dashboard therefore needs corroboration from the client and delivered work.
6. **Test recovery and change.** Use controlled dependency failure or retained equivalent evidence for the permitted scope. Verify restoration, queue handling, duplicate prevention, and data integrity. Requalify after model, precision, runtime, scheduler, topology, or workload changes using [controlled dependency change](../controls/controlled-dependency-change.md).
7. **Decide within the measured envelope.** Keep throughput, latency, quality, failure, cost, and energy results together. Reject a claim of superiority when comparable conditions or a required measure are missing. Record a provisional decision where appropriate and identify the evidence needed to revisit it.

## Cost and energy records

Use **cost per accepted work item** only with a visible denominator: total in-scope cost divided by the number of items meeting the unchanged acceptance criteria. Show rejected, failed, timed-out, and human-repaired items separately, and state whether repair is included. If none are accepted, the ratio is undefined; retain the total cost and failure count. Report sample size and variation instead of presenting one small run as a stable operating rate.

Luccioni and coauthors compare inference energy across tasks and model types.[^energy] This motivates local measurement, not adoption of their ratios as current platform facts. Record device-only versus whole-system energy, interval, workload, idle allocation, and whether cooling or network costs are included. Convert energy to emissions only with a stated, dated factor and system boundary; absent data remains unknown. Do not infer energy savings from token prices or GPU utilization.

## Assessment design

These are proposed fixtures; no platform benchmark or disruption test was executed for this guide.

| Fixture | Expected observation |
|---|---|
| Normal authorized workload within the declared envelope | Accepted items meet quality and service objectives; all relevant consumption is counted. |
| Bursty arrivals with cold workers | Queue and initialization delays remain visible; the configured admission or overload disposition occurs. |
| A high-throughput setting produces lower-quality work | It fails the unchanged quality floor even if raw tokens per second increase. |
| Client timeouts occur while the provider shows successful requests | Client, provider, retry, and destination records reconcile or show an explicit unresolved gap. |
| Shared capacity is saturated by another permitted job | Reservations, scheduling, and isolation meet the declared tenant objectives or qualification fails for that mix. |
| A worker or dependency fails after an external effect | Recovery reconciles the effect before retrying; duplicate completion is prevented. |
| A reference-design component is substituted | The deviation is recorded and relevant combined-path checks rerun. |
| Energy or facility measurements are unavailable | The report withholds the affected energy or facility-capacity claim. |

**Pass:** complete records demonstrate all required objectives for the declared workload and revision, including bounded overload and recovery. **Fail:** a required objective is violated or a known measurement gap is concealed by an aggregate. **Inconclusive:** required effects or measures cannot be inspected. An objective can pass for one task class and fail for another; record both.

Retain the workload/configuration record, raw client and platform measurements, accepted/rejected item counts, instrument coverage, recovery observations, design deviations, and owner disposition. Store sanitized references rather than sensitive prompt payloads when possible.

## Limits and adoption

The study covers selected vendor guidance and an energy paper abstract, without reproducing benchmarks or commissioning a facility. These fixtures test a local implementation within its scope; they are not a complete data-center safety, cybersecurity, or compliance program. Use [supplier assurance records](supplier-assurance-records.md) for externally supplied evidence and [approved data processing](../controls/approved-data-processing.md) for every telemetry destination.

Adopt linked controls using the [adoption procedure](../adoption.md#record-the-adoption). Record guide adaptations and unresolved measures alongside the assessment.

[^nvidia-factory]: [NVIDIA enterprise AI factory guidance](https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/building-ai-factories-for-the-enterprise.html).
[^supermicro-ra]: [Reference architecture, revision 1.0.1](https://www.supermicro.com/solutions/validated-design/NVIDIA-Enterprise-AI-Factory-Reference-Architecture-SMCI-Spectro-Cloud.pdf), overview and component sections reviewed.
[^cold-start]: [Modal: Cold start performance](https://modal.com/docs/guide/cold-start).
[^request-metrics]: [Fireworks: Text model request metrics](https://docs.fireworks.ai/guides/querying-text-models).
[^energy]: [Luccioni and coauthors: Power Hungry Processing](https://arxiv.org/abs/2311.16863), abstract reviewed.
