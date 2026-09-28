---
okf_version: "0.2"
---

# Factory Catalog

Reusable controls and a lightweight ontology for knowledge-work factories: repeatable systems in which people, software, and optionally AI turn inputs into useful artifacts, decisions, or actions, with explicit ways to judge and improve the results.

Catalog version **v0.1.0**, early beta. OKF format version **0.2** is independent of the catalog version. Use exact commit references for interim revisions. Definitions are ready to use; the catalog does not claim that any local implementation has passed an assessment or that a release baseline has been approved.

## Understand and use the catalog

- [Factory ontology](ontology.md) — Concepts, relationships, and record conventions for describing factories and their controls.
- [Knowledge work types](work-types.md) — Sixteen non-exclusive work labels classified by their intended outcome.
- [Control families](control-families.md) — Eleven control families and contextual questions for selecting controls.
- [Select, adopt, and assess controls](adoption.md) — Describe a factory, select contextual controls, and preserve pinned adoption and assessment records.
- [Apply classwork learnings](classwork-learnings.md) — Apply source intake, graph reconciliation, learning assessment, and action evidence to existing catalog controls.

## Controls and factories

- [Controls](controls/index.md) — Individually selectable requirements with implementation and assessment procedures.
- [Factory examples](factories/index.md) — Research, learning, and contract workflows connecting outcomes, authority, risks, and controls.

## History

- [Historical catalog log](log.md) — Earlier changes; subsequent history is recorded in Git and pull requests.

## Browse all concepts

This is a curated entry point. Browse [this directory](./) for current files; agents should scan Markdown files and read their frontmatter. Complete indexes are generated for distribution by `./scripts/build_catalog.py` from the repository root. Adding a concept does not require editing this page.
