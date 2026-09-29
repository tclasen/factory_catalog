---
okf_version: "0.2"
---

# Factory Catalog

Reusable controls and a lightweight ontology for knowledge-work factories: repeatable systems in which people, software, and optionally AI turn inputs into useful artifacts, decisions, or actions, with explicit ways to judge and improve the results.

The catalog version is recorded in [VERSION](VERSION). The OKF format version is declared in this entry point’s frontmatter and is independent of the catalog version. Use exact commit references for interim revisions. Check each concept’s lifecycle status before use: `draft` definitions are proposals that need review, while `stable` definitions are ready for consumption. Neither status establishes operational effectiveness; the catalog does not claim that any local implementation has passed an assessment or that a release baseline has been approved.

## Understand and use the catalog

- [Definitions and record schema](ontology.md) — Shared meanings and metadata needed to use controls.
- [Control families](control-families.md) — Control families and contextual questions for selecting controls.
- [Select, adopt, and assess controls](adoption.md) — Describe a factory, select contextual controls, and preserve pinned adoption and assessment records.

## Build and assess a factory

- [Implementation selection](factory-implementation-selection.md) — Allocate human procedures, software, and AI to activities.
- [Implementation and assessment guides](guides/) — Concrete procedures and local records.
- [Controls](controls/) — Individually selectable requirements with implementation and assessment procedures.
- [Factory examples](factories/) — Optional fictional applications illustrating distinct domains and operating constraints; select an example relevant to the factory being built.

## Browse all concepts

This is a curated entry point. Browse [this directory](./) for current files; agents should scan Markdown files and read their frontmatter. Complete indexes are generated for distribution by `./scripts/build_catalog.py` from the repository root. Adding a concept does not require editing this page.
