---
type: Control
title: "Domain event meaning"
description: "Separate requested actions from evidenced occurrences and define their downstream meaning."
status: draft
tags: [domain-driven-design, knowledge, coordination]
family: workflow-and-coordination
sources:
  - id: evans
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
    title: "Domain-Driven Design Reference, Eric Evans, March 2015"
  - id: eventsourcing
    resource: https://martinfowler.com/eaaDev/EventSourcing.html
    title: "Event Sourcing, Martin Fowler"
---

# Domain event meaning

[Adoption](../adoption.md) · [Domain model selection](../guides/domain-model-selection.md)

## Purpose and applicability

Prevent a planned action, message receipt, or inferred state from being reported as an accomplished domain event. Apply when downstream work depends on something having happened. Evans treats domain events as meaningful occurrences with relevant identities and times.[^evans] The following requirements are a catalog adaptation.

## Requirement

For every event kind in scope, define what occurrence it represents, the evidence needed to assert it, source context, subject identity, occurrence and recording times, and permitted downstream interpretation. Keep requests, observations, inferences, and corrections distinguishable. Do not treat event receipt as authority for a consequential action.

## Implementation

1. Name the occurrence in domain language, such as “submission received.” Define its evidence and distinguish it from “submission requested” and “submission approved.”
2. Record event identity, producer, subject identity, source revision, occurrence time or explicit uncertainty, and recording time. Define how corrections refer to earlier assertions.
3. Define what recipients can conclude, required [translation](context-translation-contracts.md), duplicate recognition, ordering assumptions, and handling of late or contradictory reports.
4. Check evidence before asserting completion. Route downstream actions through their own [authority checks](bounded-external-action.md) and [invariants](domain-invariant-enforcement.md).
5. Keep correction history accessible to affected consumers, with access and retention controls appropriate to the records. Avoid silently rewriting a previously relied-on assertion.

## Expected outcome and assessment

Declare the implementation revision, scope, evaluator, and assessment date. A pass requires complete requirement records and every listed applicable case; a missing requirement or omitted case fails. Explain any conditional case that does not apply. Retain observations rather than expected results alone.

Expected outcome: consumers of the declared event sample distinguish supported occurrences from requests and uncertainty, and do not infer duplicate occurrences from repeated delivery.

Test an evidenced occurrence, a request without completion evidence, duplicate delivery, a late report, and a correction of a prior assertion. For a research workflow, “review requested” cannot establish “claim verified.”

- **Pass:** the supported occurrence is represented correctly; the request remains pending or unknown; duplicates remain one occurrence; the late report preserves the distinction between occurrence and recording; the correction identifies the earlier assertion and affected consumers for reassessment.
- **Fail:** an unsupported completion is accepted, duplication changes the meaning, chronology is fabricated, or a correction is hidden from dependent use.
- **Inconclusive:** source evidence or recipient interpretation cannot be inspected.
- **Evidence:** event definitions and revisions, source artifacts, times, identities, consumer observations, correction links, and reassessment dispositions.

## Dependencies and limitations

Requires [identity rules](domain-identity-and-values.md), evidence access, and recipient cooperation. This control checks event meaning; recognizing repeated delivery as one occurrence does not prevent a repeated external effect. [Reconcile before retry](reconcile-before-retry.md) addresses uncertain effects before repeating a consequential operation. Reliable delivery still needs its own mechanism. Event sourcing rebuilds state from event history and introduces additional design obligations; this control does not require it.[^eventsourcing] No operational effectiveness is claimed.

[^evans]: [Domain-Driven Design Reference, Eric Evans, March 2015](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).
[^eventsourcing]: [Event Sourcing, Martin Fowler](https://martinfowler.com/eaaDev/EventSourcing.html).
