# Factory Catalog

A managed catalog of individually selectable controls for building a knowledge-work factory: repeatable ways for people and AI systems to produce, verify, and improve work. Controls can be used within AI systems, alongside them, or combined into complete systems.

The catalog organizes controls into families and describes each control's purpose, applicability, implementation, assessment, and expected outcomes. A lightweight ontology connects factories, activities, authority, outcomes, controls, and evidence.

**Status: early beta, v0.1.0.** Start at the [catalog entry point](catalog/index.md). See the [versioning and baseline policy](CONTRIBUTING.md#4-classify-the-version-impact).

## Why this exists

The goal is to provide a prioritized selection of reusable controls for building a knowledge-work factory. Adopt the controls your work needs and compose them into a system.

## Catalog format

The catalog is an OKF bundle under `catalog/`, targeting Open Knowledge Format (OKF) **0.2**; this is separate from the catalog version **v0.1.0**. The [vendored specification](vendor/okf/SPEC.md) and [upstream provenance](vendor/okf/UPSTREAM.md) pin the format used here.

The [ontology](catalog/ontology.md) defines concepts and relationships. Browse [work types](catalog/work-types.md), [control families](catalog/control-families.md), [controls](catalog/controls/index.md), and [factory examples](catalog/factories/index.md). The examples are fictional designs, not claims of deployed or effective systems.

## How to use it

Follow the [selection, adoption, and assessment guide](catalog/adoption.md):

1. Describe your intended outcome, operating context, and constraints.
2. Select applicable controls and prioritize them by risk, value, and dependencies.
3. Adopt each control **by reference** (a version-pinned URL) or **by value** (copy and paste its content).
4. Implement the selected controls, run their assessments, and record evidence against their expected outcomes.
5. Review gaps and deliberately update your selection as the work changes.

Every adopted control must retain its identity, catalog version, and exact source revision. For URLs, use `https://github.com/tclasen/factory_catalog/blob/<commit-sha>/<control-path>`; replace the placeholders with an actual commit and file. For copied controls, retain that URL and version alongside the text, and document local adaptations. Avoid moving branch URLs such as `main` for adopted controls.

## Copy and paste into an agent

Replace the bracketed fields:

```text
Use https://github.com/tclasen/factory_catalog to help build a knowledge-work
factory for [project or system] that achieves [outcomes], subject to [constraints].

Read the README and inspect the available controls. Record the exact catalog
commit and version used; the current early-beta version is v0.1.0.
Recommend a prioritized selection of applicable controls with rationale,
dependencies, implementation steps, expected outcomes, and assessment evidence.

Adopt controls by [version-pinned URL / copy and paste], preserving each control's
identity, version, and source commit. Implement and assess the selected controls
within the project's existing instructions and permissions. Report what passed,
what failed, and what remains unverified.

If the catalog lacks the necessary controls, identify the gaps and propose next
steps without presenting invented controls as catalog content.
```

## Contributing

Human and AI contributors should follow [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow, security controls, and SEMVER release policy. AI contributors must also read [AGENTS.md](AGENTS.md). Extend the ontology and vocabulary through explicit design decisions, preserving adopted identities and references.

With [uv](https://docs.astral.sh/uv/guides/scripts/) on your PATH, validate the bundle with `./scripts/validate_catalog.py`. The executable Python validator uses `uv` script mode with an inline PyYAML dependency and checks the pinned OKF structure plus this catalog's metadata, links, and index coverage. It does not assess operational control effectiveness.
