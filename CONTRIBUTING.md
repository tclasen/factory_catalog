# Contributing to Factory Catalog

This workflow applies to human and AI contributors. Read [README.md](README.md) for the project's purpose and usage, and follow applicable [agent instructions](AGENTS.md) when working with an AI contributor.

## Local maintenance factory

For each maintenance request, use the [factory binding](factory/README.md),
[workflow](factory/workflow.md), and [work record](factory/work-record.md). Keep
intent, criteria, current state, and evidence in the task’s issue/PR, with a local
checkpoint before publication. The binding applies selected catalog controls to
this repository; the policies below remain authoritative.

## 1. Define the change

- Inspect current files, applicable instructions, and relevant issues or pull requests. Identify the requested outcome and the smallest useful change.
- Discuss and record changes to control families, identifiers, and the domain schema before establishing them. The [catalog ontology](catalog/ontology.md) defines the current model. Do not silently replace it, invent a release baseline, or import an entire factory framework.
- Coordinate through an existing issue or pull request when available. Record scope, decisions, evidence, blockers, and next steps so another contributor can continue without reconstructing the conversation.
- Keep changes focused and reviewable. Preserve others' work, reconcile concurrent changes, and avoid unrelated cleanup.

## 2. Prepare a branch and follow security controls

- Start from an up-to-date default branch and work on a topic branch. Never push directly to the protected default branch, force-push it, or delete it, even when a request suggests a shortcut.
- Before committing, inspect the configured identity and signing mechanism. Sign every proposed commit, including documentation changes. Use an authorized local signing key, or GitHub’s `createCommitOnBranch` API with the existing authenticated account to create a GitHub-signed commit on the topic branch. Verify local signatures when signing locally and confirm GitHub reports the published commits as verified. If neither signing path is available, preserve the prepared changes and report the specific blocker; do not create unsigned commits or silently provision a new identity or key.
- Review the diff and run relevant checks before submitting the pull request. An empty required-check list is not evidence that the change was tested. Report the checks actually performed.
- Before an authorized merge, recheck the current pull request revision, GitHub mergeability, required checks, review decisions, applicable code owners, and unresolved threads. Address review feedback and resolve threads only when the concern is actually handled. Zero general approvals does not waive other review requirements; do not fabricate approvals or treat silence as approval.
- Use squash or rebase as permitted by the live rules, preserving verified signatures on commits entering the default branch. Do not use a merge commit: it conflicts with linear history even though the repository advertises that merge method. Do not assume rewritten commits retain their signatures; verify the resulting commits on GitHub.
- Continue authorized preparation, validation, and pull request work independently. Stop only the blocked publication or merge step when credentials, signing, required review, checks, or permission are missing; explain what is needed without changing the controls.
- Keep credentials and private signing material out of tracked files, logs, and pull requests. If future work adds automation or dependencies, inspect the applicable Actions permissions and security configuration before relying on them, and use only the permissions the workflow needs.

## 3. Author the contribution

### Bundle admission rules

The product is a reusable control catalog. Every bundle concept must help an adopter select, understand, implement, compose, or assess controls for a concrete factory decision. Apply these rules before adding or expanding content; a valid OKF document is not automatically suitable catalog content.

| Content | Home and admission rule |
|---|---|
| Reusable requirement | `catalog/controls/`: independently selectable, with a distinct failure or outcome boundary and an assessable requirement |
| Implementation or assessment procedure, record, risk scenario, or example | `catalog/`: identify the adopter's task, the controls it supports, and the usable procedure, record fields, or observable assessment it adds |
| Shared definitions and control families | Existing ontology and taxonomy: add only what actual controls or consumers need; explain the requirement for a schema change |
| Source surveys, literature reviews, organization/person lists, source-by-source lessons, candidate ideas | `docs/research/`: contributor inputs, with sources and evidence limits; extract usable content before publishing it in the bundle |
| Knowledge-work vocabulary | `docs/work-types.md`: contributor scope guidance; never a required lookup for a distributed bundle |
| Contribution policy, design discussion, change history | Repository guidance and the relevant issue/PR; keep maintenance narratives outside the bundle |

**Choose by meaning, not file type.** Calling a survey a Guide, marking it draft, or renaming it after a task does not satisfy admission. Supporting content must do useful work beyond summarizing a source or listing links. Keep source attribution and relevant evidence limits with the resulting control or procedure; those are part of its basis, not research clutter.

### Turn research into usable content

1. Read [knowledge work types](docs/work-types.md) and identify the beneficiary, activity, decision, and failure being addressed. Consider human procedures and non-software settings. A specialized control can remain domain-specific; do not generalize beyond its evidence or create an example for every work type.
2. Search the current concept files, requirements, assessments, and incoming links for existing coverage. Compare meanings and failure cases, not just titles. Reuse an existing control; extend it when the same requirement needs clarification; create another only when it addresses a separately selectable and assessable concern. Record the boundary in the PR.
3. Decompose findings by the adopter's task. Put normative requirements and their pass/fail criteria in controls. Use supporting guides for mechanisms, composition, records, and worked assessments. A guide must not silently add mandatory conditions to a linked control; change that control explicitly or propose a separate one.
4. Preserve exact source revisions where available, attribution, reviewed scope, and uncertainty. A source recommendation, draft definition, or successful repository check is not evidence that a local implementation works. Keep unsupported proposals in research or an issue until a useful requirement or procedure can be stated.
5. For moved or removed material, identify useful requirements, procedures, examples, and provenance before deleting it. Incorporate distinct useful content, link existing coverage, or explain why it is deferred or unnecessary. Record that disposition in the PR, without adding a permanent migration map or shared inventory to the bundle.

A research request authorizes the requested research; it does not make every finding a bundle addition. Deliver research in its appropriate home and publish only the usable concepts within the authorized scope. Do not copy an entire source framework, taxonomy, or actor directory into the catalog.

### Keep the adopter's bundle sufficient and focused

- The distributed bundle must work without `docs/`, repository instructions, research surveys, or an external work-type taxonomy. Keep operational definitions and required procedures inside it. External primary sources may substantiate a requirement; identify any source access actually needed to implement or assess it.
- Factory examples describe actual work in free-text `activities`, following the [record schema](catalog/ontology.md#document-types-and-metadata). Do not restore `work_types` vocabulary references or copy the contributor taxonomy into the bundle.
- Keep an example only when it teaches a distinct selection, implementation, composition, or assessment decision. Prefer a focused section or fixture over another full factory profile when it communicates the same lesson. Examples stay optional and must distinguish invented design from observed results.
- Keep the ontology limited to meanings and records used by controls and their consumers. Families organize existing requirements; they do not establish coverage or require a control for every category. Avoid speculative schema expansion.
- Apply the same admission test to edits and research imports as to new files. Remove obsolete duplication when replacing guidance, repair affected references, and preserve adoption provenance under the rules below. Do not add historical stubs solely to keep removed research inside the bundle.

### Parallel contributions

Use one topic branch and a separate checkout or worktree per agent. Never share a mutable checkout between concurrent tasks. Start independent branches from the default branch; use an explicit dependency when one PR needs another's content.

- Scope ordinary content PRs to their concept files. Add a control at `catalog/controls/<descriptive-slug>.md`, an example at `catalog/factories/<descriptive-slug>.md`, or a guide at a unique descriptive path. The path is its identity; do not allocate sequential IDs or register every addition in a shared file.
- Discover concepts by scanning `catalog/**/*.md`, excluding the reserved `index.md` and `log.md` filenames. Frontmatter supplies titles, descriptions, types, and family membership. Never treat the curated source indexes as exhaustive inventories.
- Do not update source indexes, the README, taxonomies, ontology, or a shared log just to announce a concept addition. Record the scope, rationale, version impact, and validation evidence in that PR. Keep change history in Git and PRs, not in catalog logs or repository retrospectives.
- Put relationships and supporting evidence in the affected concept. When adding a guide or example, link from it to the existing controls, taxonomies, and guides it uses. Do not append reciprocal “related guidance” links to every existing target just to advertise the addition; discover incoming relationships by scanning links. Edit an existing target when its requirements, explanation, or assessment actually need to change. Change shared schema or vocabulary only when the meaning actually changes. Coordinate overlapping concept edits and schema changes through the relevant issues/PRs; merge a shared prerequisite first and then update dependent branches.
- Do not commit generated bundles, inventories, build timestamps, or per-PR version bumps. Generate navigation from the combined tree during checks and distribution.
- Before merge, update against the current default branch and rerun validation and build checks on the combined content. A clean text merge does not prove semantic compatibility. Never use union merge drivers or automatic “ours/theirs” resolution to discard competing edits.

This layout removes mandatory shared-file edits for independent additions. Concurrent changes to the same requirements, identities, or schema still need review and coordination.

### Keep changes local

Before adding metadata, boilerplate, or a new requirement, identify its authoritative source and which files a future change would touch. A release, taxonomy label change, repository move, or policy clarification should not require rewriting unrelated concepts.

- Store the catalog version only in `catalog/VERSION`, as one `vMAJOR.MINOR.PATCH` value (optional SemVer prerelease/build suffixes). Read it at the consumed commit; the build carries the file unchanged. Version changes still require owner authorization under the baseline policy. Do not hardcode the current value in concepts, examples, prompts, documentation, validators, or fixtures.
- Derive concept identity from its path and family from its frontmatter. Do not duplicate these in authored summary headers. Keep paths independent of mutable family labels. Generate display metadata, counts, inventories, and reverse links from the combined tree.
- Link to shared adoption and contribution procedures instead of restating their full policy in every item. Preserve control-specific requirements, assessment criteria, limitations, and source attribution so controls remain individually usable.
- Keep license text at the repository root and copy it into distributions. Do not add per-concept copies of bundle-wide owners, release dates, repository URLs, schema versions, or build information. Use relative internal links; derive distribution details when building or consuming the bundle.
- Keep actual evidence local: lifecycle status, source revisions, inspection dates, verification events, and historical adoption records describe a particular concept or observation. Never bulk-refresh them for a release or centralize them into a mutable value that rewrites their meaning.
- Treat required schema changes as migrations: first consider an optional field, a derived value, or a consumer default with an explicit meaning. If an incompatible change is necessary, document why and its affected consumers in the PR. Do not weaken meaningful requirements just to avoid edits.
- Add regression coverage when tooling can enforce these boundaries. Test that changing the bundle version needs only its one file and that independent additions need no shared edits. Review prose for duplicated policy and stale counts; automated checks cannot prove every statement has one authority.

### Scripts

Write scripts in Python with a `#!/usr/bin/env -S uv run --script` shebang and an executable Git file mode. Declare Python requirements and dependencies in inline script metadata so `uv` can manage the script environment. Document direct invocation, such as `./scripts/validate_catalog.py`, without requiring an explicit Python launcher.

### Maintain the OKF bundle

- Always use the pinned vendored specification at `vendor/okf/SPEC.md` (OKF 0.2) when creating, reading, editing, or validating the OKF bundle. Do not substitute a live upstream version or remembered rules. Keep the bundle in `catalog/` and repository guidance and vendored files outside it.
- Keep `catalog/index.md` as a stable entry point declaring `okf_version: "0.2"`. The root index provides curated navigation; generate directory listings rather than maintaining nested indexes. Each concept is a UTF-8 Markdown file with YAML frontmatter and a non-empty `type`; `index.md` and `log.md` are reserved.
- Use descriptive concept paths and relative links within the bundle. Complete directory indexes are derived by `./scripts/build_catalog.py` from concept frontmatter, following OKF §8. New directories need no handwritten index. The build preserves existing index prose and appends a sorted inventory in a separate copy.
- Run `./scripts/build_catalog.py` to build and validate in a temporary directory. To retain a browsable copy, use `./scripts/build_catalog.py --output build/catalog` with a new output directory; choose a fresh path for subsequent builds. `build/` is ignored. Distribute this generated bundle when consumers need complete progressive-disclosure indexes. Consumers of the source tree must scan files for a complete inventory.
- OKF §9 makes logs optional. Do not add historical logs, compatibility placeholders, or migration narratives to the bundle. Retain source provenance and evidence limits that support current guidance.
- Keep the upstream specification and license unchanged. For upgrades, fetch from an exact upstream commit, review the changes, update `vendor/okf/UPSTREAM.md` and its checksums, and assess bundle compatibility.
- Distinguish the pinned OKF format version from the catalog version in `catalog/VERSION`.

### Write useful controls

Apply the [bundle admission rules](#bundle-admission-rules) and [research decomposition procedure](#turn-research-into-usable-content) before authoring a control or supporting concept.

Each control should have a stable identity and family, a clear purpose, applicability guidance, implementation instructions, measurable expected outcomes, and an assessment with evidence and pass/fail criteria. Follow the [catalog ontology](catalog/ontology.md) and [control families](catalog/control-families.md). Make dependencies and limitations explicit.

Keep controls individually selectable and usable both by URL and by copying their content. Separate reusable requirements from project-specific examples. Prefer observable behavior over vague advice, and distinguish proposed guidance from verified results.

### Preserve adoption references

Follow the [README's adoption guidance](README.md#how-to-use-it) for control identities, catalog versions, and pinned source URLs, including in copied examples and cross-control references. Before v1, remove obsolete paths and content directly and update current references in the same PR; do not retain aliases, stubs, or historical files solely for compatibility. Describe breaking changes in the PR. Exact-commit adoption records remain useful for identifying the content actually adopted.

## 4. Classify the version impact

Use **Semantic Versioning (SEMVER)** in `MAJOR.MINOR.PATCH` form, following [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) with these catalog-specific change categories after v1:

| Release | When to use it | Example |
| --- | --- | --- |
| **Major** | Breaking changes, including re-organizations that change published control paths, identities, or the meaning of existing requirements. | Move controls into a new hierarchy that requires adopters to update their references. |
| **Minor** | Add new content or controls while preserving compatibility with existing definitions and references. | Add a new control or a new guide. |
| **Patch** | Clarify or extend existing definitions without changing their requirements or invalidating existing implementations or assessments. | Explain an ambiguous term or add an example to an existing definition. |

**Before v1:** backwards compatibility is not required. Breaking changes are permitted; describe their effect in the PR and repair links in the current tree. For a future pre-v1 release, classify breaking or additive changes as minor and corrections as patch. The baseline hold below still applies.

**From v1:** classify by the effect on adopters. An extension that introduces an incompatible requirement is a major change even if it edits only one definition. For changes spanning categories, use the highest required level. A major release resets minor and patch to zero; a minor release resets patch to zero.

**Current baseline hold:** the project remains early beta at the version declared in [catalog/VERSION](catalog/VERSION) until the repository owner explicitly approves a baseline. Use exact commit SHAs to identify interim revisions. Describe the intended version impact in pull requests, but do not bump the version or publish a release during this hold. Baseline approval and all release/version changes require explicit repository-owner decisions; this guide does not approve them. Never move published version tags or alter an already released version's contents.

## 5. Verify and open a pull request

Before submitting, run `./scripts/check_catalog.py --github`. CI runs this same command. It fails on regression failures, invalid structure or provenance, broken local links or heading anchors, incomplete generated navigation, missing distribution license, and whitespace errors. Duplicate YAML keys are rejected at every mapping level. Footnotes must have definitions and matching source IDs. Source entries must supply a resource; explicit relative or absolute bundle paths and whitespace-free resources containing `/` or `.` are checked as local paths. URI resources and scope descriptions remain valid; use `./` for an otherwise ambiguous local filename.

The generated bundle includes the source VERSION and repository LICENSE unchanged, control maturity and family labels, and a complete family view. These are derived from files and metadata; authors do not maintain an inventory.

Whitespace checks cover the full tracked working tree, including committed content in a clean or shallow CI checkout, plus staged and unstaged changes. The full-tree scan excludes only `vendor/okf/SPEC.md` and `vendor/okf/LICENSE.md`, whose upstream whitespace must remain unchanged. Stage new files before running the final check so Git includes them. No base branch or network fetch is needed for this scan.

Generated links encode special characters in filenames, and coverage checks decode those links. Per pinned OKF §5.4, a missing lifecycle status is displayed as `stable`. The standalone advisory reviewer validates its input before inspecting prose; malformed metadata fails with validation diagnostics.

`review_catalog.py` emits advisory findings for similar control titles within a family, blanket readiness claims alongside drafts, selected blanket implementation claims inconsistent with metadata, and proposal/pending wording around PR links. `--github` uses authenticated, read-only `gh api` calls to check this repository's referenced PR states. Offline mode and failed live lookups explicitly report that state was not checked. Warnings do not fail CI: title similarity cannot establish duplication, and a merged PR can still be discussed legitimately. Arbitrary prose contradictions, evidence quality, control effectiveness, and policy decisions still need human review. These heuristics are deliberately narrow and are not a complete semantic audit.

Individual checks and review requirements:

- Review the complete diff for accuracy, clarity, scope, and consistency; run `git diff --check`.
- For bundle content, state in the PR the adopter task, why existing content is insufficient, and the contribution's distinct requirement or practical support. For removals or moves, include the useful-content disposition. Scale this explanation to the change; do not maintain another registry.
- Review admission separately from automated validity: check for source-oriented surveys, duplicated requirements, hidden requirements in guides, unnecessary examples, external contributor-document dependencies, and speculative schema. Resolve these findings before submission; passing checks do not waive the admission rules.
- The required check command also runs `./scripts/check_guidance_links.py` over root Markdown files and recursively over `docs/` and `factory/`. It checks local Markdown links and images, including reference links, repository-root paths, URL-encoded paths, and Markdown heading fragments in destinations such as `catalog/`. Queries are ignored for filesystem lookup. External URLs, raw HTML links/anchors, code examples, and non-Markdown fragments are not checked; review those manually when changed. Generated output and vendored documents are not scanned as guidance sources. This check does not impose OKF metadata rules on repository guidance.
- Check changed links, references, and examples. For bundle changes, validate against the pinned specification and ensure the generated indexes cover the concepts present.
- Run `./scripts/validate_catalog.py` for bundle or schema changes. It uses `uv` script mode with inline PyYAML and Markdown parser dependencies to check OKF structure, catalog metadata and local links; passing it does not establish control effectiveness. Source indexes are curated and do not require exhaustive coverage.
- Run `./scripts/build_catalog.py` and `./scripts/test_validate_catalog.py` for bundle or tooling changes. The build checks complete index coverage in its generated output. The regression suite checks independent additions, generated discovery, and validation failures.
- Run relevant repository checks when available. For controls, assess whether the procedure can demonstrate the expected outcome and record evidence against its pass/fail criteria.
- Explain the problem and resulting change in the pull request. Include scope, version impact, breaking-change notes, checks actually performed, unverified claims, and the next unresolved decision. Link the relevant issue or prior discussion when available.

Never report a control as effective, a check as passing, or a baseline as approved without evidence. An absence of automated checks is not a passing test result.

## 6. Address review and hand off

Address review feedback and validate any resulting changes. Follow the [security controls](#2-prepare-a-branch-and-follow-security-controls) before an authorized merge. Report what changed, how it was checked, and any remaining blockers or decisions. If work cannot be published or merged, preserve the prepared changes and state what is needed to continue.
