# Factory Catalog

A managed catalog of individually selectable controls for building a knowledge-work factory: repeatable ways for people and AI systems to produce, verify, and improve work. Controls can be used within AI systems, alongside them, or combined into complete systems.

The catalog will organize controls into families and centralize each control's purpose, when to apply it, how to implement it, how to assess whether it works, and the outcomes to expect.

**Status: early beta, v0.1.0.** The taxonomy and initial controls are still to be defined. See the [versioning and baseline policy](CONTRIBUTING.md#4-classify-the-version-impact).

## Why this exists

The goal is to provide a prioritized selection of reusable controls for building a knowledge-work factory. Adopt the controls your work needs and compose them into a system.

## Catalog format

A [review MVP of the proposed ontology](docs/ontology-mvp/index.md) describes factories, work types, controls, and assessment evidence through three worked examples. It is a design proposal, not an approved taxonomy or catalog baseline.

The control taxonomy will be maintained in an OKF bundle under `catalog/`. It targets Open Knowledge Format (OKF) **0.2**; this is separate from the catalog version **v0.1.0**. The [vendored specification](vendor/okf/SPEC.md) and [upstream provenance](vendor/okf/UPSTREAM.md) pin the format used here. The bundle and its control families will be built out after the taxonomy discussion.

## How to use it

Once controls are available:

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

Human and AI contributors should follow [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow, security controls, and SEMVER release policy. AI contributors must also read [AGENTS.md](AGENTS.md). The next design step is agreeing on the control taxonomy.
