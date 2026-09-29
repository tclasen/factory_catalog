---
type: Guide
title: "Select, adopt, and assess controls"
description: "Describe a factory, select contextual controls, and preserve pinned adoption and assessment records."
status: stable
---

# Select, adopt, and assess controls

[Catalog](index.md) · [Ontology](ontology.md) · [Controls](controls/)

## Describe the factory

Record its intended outcome, beneficiaries, accountable owner, and exclusions. Describe the actual activities, domain, actors, inputs, outputs, workflow, knowledge sources, and persistent state. Activities can include research, teaching, analysis, negotiation, publication, or software delivery. Record autonomy and authority for each activity, including escalation and stopping conditions.

Describe data sensitivity, external exposure, scale, obligations, consequences, and reversibility. Unknown context stays explicit. The [factory examples](factories/) show how to connect these fields.

## Select controls

1. Identify desired outcomes and risk scenarios: cause or threat, enabling condition, unwanted outcome, and affected parties.
2. Use [control families](control-families.md) to find relevant requirements. Actual context determines applicability; family membership alone does not require adoption.
3. Record `applicable`, `not-applicable`, or `undetermined`, with rationale, assumptions, decision owner, and a reassessment date or trigger. Do not equate missing implementation with non-applicability.
4. Prioritize controls by consequence, exposure, expected benefit, dependencies, and implementation cost. Record gaps where the catalog has no adequate control.
5. Check composition: shared credentials, memory, handoffs, and combined authority can introduce risks not visible in isolated components.

## Record the adoption

An adoption is an explicit decision to apply a particular control revision. A relative link in a factory example only selects a control within that bundle revision. Before implementation or copying, record:

| Field | Required content |
|---|---|
| Control identity | Bundle-relative concept path without `.md`, such as `controls/evidence-traceability` |
| Catalog version | Value of [VERSION](VERSION) at the source revision actually adopted |
| Source revision | Full commit SHA of the catalog revision actually read |
| Pinned source URL | `https://github.com/tclasen/factory_catalog/blob/` + that SHA + `/catalog/` + the control identity + `.md` |
| Scope and owner | Factory/activity coverage and person accountable for implementation |
| Applicability | Decision, rationale, assumptions, owner, reassessment trigger |
| Local implementation | Mechanism, parameters, dependencies, adaptations, and current state |
| Assessment record | Target revision, criteria, evaluator, time, evidence references, result, limitations, and follow-up |

To obtain a source revision from a checkout, use `git rev-parse HEAD` and confirm that the selected files have no local edits with `git status --short -- catalog`. Confirm the commit and file exist on the published repository before using its URL. A SHA identifies the committed contents, not unstaged edits. For a downloaded bundle, obtain the distributor's exact source revision rather than guessing it.

For by-reference adoption, retain the identity, version, and pinned URL in the local record. For by-value adoption, retain those fields alongside the copied control, preserve the reusable requirement and assessment, and distinguish local adaptations from source text. Resolve any relative cross-control references against the same source revision and retain their identities, versions, and pinned URLs too. Do not substitute moving branch URLs.

Read the version once per adopted bundle revision. A local adoption record may share that version and SHA across controls from the same revision; keep separate records when revisions differ. For a copied control, retain the adoption record alongside the text. Never refresh historical adoption versions just because a newer catalog exists.

## Implement and assess

Set the implementation state independently from applicability: `not-planned`, `proposed`, `implemented`, or `retired`. Identify whether the mechanism is instructions, a human procedure, an automated check, or a technical restriction. Record incomplete coverage and bypass paths.

Execute the control's assessment in the declared scope, using safe test environments where actions have external effects. Retain positive and negative results. Report `not-assessed`, `pass`, `fail`, or `inconclusive`; a pass is limited to the tested method, scope, revision, and time. Record exceptions and remediation instead of hiding failed criteria.

Keep artifact acceptance, factory outcome attainment, and control assessment separate. A control can pass by correctly detecting an unmet factory outcome. Documentation checks do not establish operational control effectiveness.


## Reassess and evolve

Reassess when assumptions, data, actors, tools, authority, workflow, or consequences change. Preserve the prior adoption record when updating to a new source revision. Document changed requirements, local adaptations, and any migration before claiming the new control is implemented or assessed.

The catalog does not cover every security, privacy, quality, or operational concern; the examples explicitly identify remaining gaps.
