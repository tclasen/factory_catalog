---
type: Guide
title: "Integrate knowledge sources"
description: "Resolve source identity, reconcile existing concepts, and retain inspectable evidence for knowledge updates."
status: draft
sources:
  - id: intake
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-source-intake/SKILL.md
    title: "classwork: Source intake procedure"
  - id: synthesis
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/.agents/skills/okf-knowledge-synthesis/SKILL.md
    title: "classwork: Knowledge synthesis procedure"
  - id: provenance
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/information-systems/information-provenance-and-trust.md
    title: "classwork: Information provenance and trust"
  - id: assurance
    resource: https://github.com/tclasen/classwork/blob/12d29b3ae730c565135604f027b502b87b225758/bundle/assurance/assurance-case.md
    title: "classwork: Assurance case"
---

# Integrate knowledge sources

[Adoption](../adoption.md) · [Evidence traceability](../controls/evidence-traceability.md) · [Source corroboration](../controls/source-corroboration.md)

## When to use this procedure

Use when admitting new material into a research collection, shared knowledge base, or decision record. It implements claim review and corpus admission without requiring a particular graph technology. Intake and synthesis procedures inform this adaptation.[^intake][^synthesis] The fixtures below are proposed, not executed.

## Intake and reconcile

1. Identify the exact source, edition/revision, access date, relevant passage, and intended use. Record suitability and copying rights; link rather than retain a copy when appropriate. Secondary summaries establish what the summary says, not independent review of its cited originals.
2. Search existing titles, definitions, aliases, and incoming relationships. For each material claim, record whether it confirms, qualifies, contradicts, or supersedes current knowledge. Reuse a canonical concept where meaning matches; keep distinct identities where scope differs.
3. Preserve conflicts, uncertain entity matches, and reviewer rationale. Explain each relationship as evidence, prerequisite, example, or limitation. A resolving link proves neither correct meaning nor independent support.
4. Stage the update under [retrieval corpus integrity](../controls/retrieval-corpus-integrity.md). Review affected links and consumers before activating it. Keep corrections independent of rebuildable indexes under [data-preserving migration](../controls/data-preserving-migration.md).
5. Check that evidence applies to the current target through [assessment evidence validity](../controls/assessment-evidence-validity.md). Record the argument from observation to claim, including assumptions and rebuttals.[^provenance][^assurance]

## Working record

Keep source/revision/location; claim and evidence status; existing concept and scope; proposed change; affected consumers; conflict and disposition; reviewer; accepted revision; and correction history. Restrict private observations to their authorized workspace. Shared reusable knowledge should not absorb individual learner or customer records merely because it links to their workflow.

## Review fixtures

| Fixture | Required observation |
|---|---|
| Two editions change a material claim | Accepted content names the actual edition and does not silently combine incompatible claims |
| New source contradicts the current conclusion | Conflict and reviewer rationale remain visible; unsupported certainty is withheld |
| A synonym duplicates an existing concept | Reuse the identity or explain the substantive scope difference; repair affected references |
| Authentic evidence describes an earlier target revision | Reuse needs a reasoned applicability decision or new evidence |
| Approved correction followed by index rebuild | Correction survives and the active result points to the accepted revision |

Retain before/after content, source passages, affected references, review decisions, and fixture results. A known hidden conflict, lost correction, or unsupported accepted claim fails the procedure; unavailable evidence is inconclusive. A pass requires the valid update to remain usable as well as the defective cases to be withheld. Assess each selected control against its own complete criteria.

[^intake]: Pinned classwork source intake procedure.
[^synthesis]: Pinned classwork knowledge synthesis procedure.
[^provenance]: Pinned classwork information provenance concept.
[^assurance]: Pinned classwork assurance-case concept; underlying publications were not independently reviewed for this adaptation.
