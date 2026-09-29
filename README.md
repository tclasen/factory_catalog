# Factory Catalog

A managed catalog of individually selectable controls for building a knowledge-work factory: repeatable ways for people and AI systems to produce, verify, and improve work. Controls can be used within AI systems, alongside them, or combined into complete systems.

The catalog organizes controls into families and describes each control's purpose, applicability, implementation, assessment, and expected outcomes. A lightweight ontology connects factories, activities, authority, outcomes, controls, and evidence.

See the [catalog version](catalog/VERSION) and [baseline status](CONTRIBUTING.md#4-classify-the-version-impact). Start at the [catalog entry point](catalog/index.md).

## Why this exists

The goal is to provide a prioritized selection of reusable controls for building a knowledge-work factory. Adopt the controls your work needs and compose them into a system.

The bundle is organized around the adopter's decisions. Supporting content earns its place by helping someone select, implement, or assess controls. Research surveys and contributor vocabulary live outside the bundle; useful findings become controls or practical guidance with their provenance retained. Contributions follow the [bundle admission rules](CONTRIBUTING.md#bundle-admission-rules).

## Catalog format

The catalog is an OKF bundle under `catalog/`, targeting Open Knowledge Format (OKF) **0.2**; this is separate from the [catalog version](catalog/VERSION). The [vendored specification](vendor/okf/SPEC.md) and [upstream provenance](vendor/okf/UPSTREAM.md) pin the format used here.

The [ontology](catalog/ontology.md) defines concepts and relationships. Browse [control families](catalog/control-families.md), [controls](catalog/controls/), and [factory examples](catalog/factories/). The examples are fictional designs, not claims of deployed or effective systems.

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
commit and the value of catalog/VERSION at that same commit.
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

The [knowledge work types](docs/work-types.md) describe the full domain scope for contributors. [Research inputs](docs/research/) stay outside the OKF bundle. The bundle contains controls and the procedures, records, scenarios, and examples needed to build and assess a factory.

Human and AI contributors should follow [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow, security controls, and SEMVER release policy. AI contributors must also read [AGENTS.md](AGENTS.md). Extend the ontology and vocabulary through explicit design decisions. Before v1, paths and definitions may change without compatibility shims; pin adoption to an exact commit.

With [uv](https://docs.astral.sh/uv/guides/scripts/) on your PATH, validate the bundle with `./scripts/validate_catalog.py`. The executable Python validator uses `uv` script mode with inline PyYAML and Markdown parser dependencies and checks the pinned OKF structure plus this catalog's metadata and links. It does not assess operational control effectiveness.

Before pushing, run `./scripts/check_catalog.py --github` for the same regression tests, validation, temporary build, content review scan, and whitespace checks used in CI. Live PR-state review requires authenticated `gh`; omit `--github` for offline checks. Unavailable live checks are explicitly reported. Advisory findings require human review and do not fail the command.

See [verification](CONTRIBUTING.md#5-verify-and-open-a-pull-request) for check coverage and limits. Individual scripts remain available for focused checks.

## Repository layout and parallel work

`catalog/` holds the authored OKF concepts at stable paths. Its root index is a curated entry point; directory listings are generated. For a complete inventory, scan all concept files or generate a browsable bundle with `./scripts/build_catalog.py --output build/catalog`. The output directory must be new; `build/` is ignored. The build creates complete directory indexes from frontmatter and validates their coverage. Run `./scripts/build_catalog.py` without arguments to check a temporary build.

Independent PRs add or edit their own concept files without maintaining a shared inventory or changelog. Keep change history in Git and PRs. See [parallel contributions](CONTRIBUTING.md#parallel-contributions) for agent isolation, shared-schema coordination, and checks before merge.
