# Contributing to Factory Catalog

This workflow applies to human and AI contributors. Read [README.md](README.md) for the project's purpose and usage, and follow applicable [agent instructions](AGENTS.md) when working with an AI contributor.

## 1. Define the change

- Inspect current files, applicable instructions, and relevant issues or pull requests. Identify the requested outcome and the smallest useful change.
- Discuss and record changes to control families, identifiers, and the domain schema before establishing them. The [catalog ontology](catalog/ontology.md) records the initial design. Do not silently replace it, invent a release baseline, or import an entire factory framework.
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

### Parallel contributions

Use one topic branch and a separate checkout or worktree per agent. Never share a mutable checkout between concurrent tasks. Start independent branches from the default branch; use an explicit dependency when one PR needs another's content.

- Scope ordinary content PRs to their concept files. Add a control at `catalog/controls/<descriptive-slug>.md`, an example at `catalog/factories/<descriptive-slug>.md`, or a guide at a unique descriptive path. The path is its identity; do not allocate sequential IDs or register every addition in a shared file.
- Discover concepts by scanning `catalog/**/*.md`, excluding the reserved `index.md` and `log.md` filenames. Frontmatter supplies titles, descriptions, types, and family membership. Never treat the curated source indexes as exhaustive inventories.
- Do not update source indexes, the README, taxonomies, ontology, or a shared log just to announce a concept addition. Record the scope, rationale, version impact, and validation evidence in that PR. Git history records subsequent changes; `catalog/log.md` preserves historical entries only.
- Put relationships and supporting evidence in the affected concept. When adding a guide or example, link from it to the existing controls, taxonomies, and guides it uses. Do not append reciprocal “related guidance” links to every existing target just to advertise the addition; discover incoming relationships by scanning links. Edit an existing target when its requirements, explanation, or assessment actually need to change. Change shared schema or vocabulary only when the meaning actually changes. Coordinate overlapping concept edits and schema changes through the relevant issues/PRs; merge a shared prerequisite first and then update dependent branches.
- Do not commit generated bundles, inventories, build timestamps, or per-PR version bumps. Generate navigation from the combined tree during checks and distribution.
- Before merge, update against the current default branch and rerun validation and build checks on the combined content. A clean text merge does not prove semantic compatibility. Never use union merge drivers or automatic “ours/theirs” resolution to discard competing edits.

The [design decision](docs/decisions/parallel-okf-authoring.md) records the format basis and compatibility tradeoffs. This layout removes mandatory shared-file edits for independent additions. Concurrent changes to the same requirements, identities, or schema still need review and coordination.

### Scripts

Write scripts in Python with a `#!/usr/bin/env -S uv run --script` shebang and an executable Git file mode. Declare Python requirements and dependencies in inline script metadata so `uv` can manage the script environment. Document direct invocation, such as `./scripts/validate_catalog.py`, without requiring an explicit Python launcher.

### Maintain the OKF bundle

- Always use the pinned vendored specification at `vendor/okf/SPEC.md` (OKF 0.2) when creating, reading, editing, or validating the OKF bundle. Do not substitute a live upstream version or remembered rules. Keep the bundle in `catalog/` and repository guidance and vendored files outside it.
- Keep `catalog/index.md` as a stable entry point declaring `okf_version: "0.2"`. Source indexes provide curated navigation; update them only for deliberate navigation changes. Each concept is a UTF-8 Markdown file with YAML frontmatter and a non-empty `type`; `index.md` and `log.md` are reserved.
- Use stable concept paths and relative links within the bundle. Complete directory indexes are derived by `./scripts/build_catalog.py` from concept frontmatter, following OKF §8. New directories need no handwritten index. The build preserves existing index prose and appends a sorted inventory in a separate copy.
- Run `./scripts/build_catalog.py` to build and validate in a temporary directory. To retain a browsable copy, use `./scripts/build_catalog.py --output build/catalog` with a new output directory; choose a fresh path for subsequent builds. `build/` is ignored. Distribute this generated bundle when consumers need complete progressive-disclosure indexes. Consumers of the source tree must scan files for a complete inventory.
- Keep the historical `catalog/log.md` and existing concept paths for compatibility. OKF §9 makes logs optional; use Git and PR history for new changes rather than appending to a shared log. Archives without Git retain only the historical log, not a complete change history.
- Keep the upstream specification and license unchanged. For upgrades, fetch from an exact upstream commit, review the changes, update `vendor/okf/UPSTREAM.md` and its checksums, and assess bundle compatibility.
- Distinguish OKF format version 0.2 from catalog version v0.1.0.

### Write useful controls

Each control should have a stable identity and family, a clear purpose, applicability guidance, implementation instructions, measurable expected outcomes, and an assessment with evidence and pass/fail criteria. Follow the [catalog ontology](catalog/ontology.md) and [control families](catalog/control-families.md). Make dependencies and limitations explicit.

Keep controls individually selectable and usable both by URL and by copying their content. Separate reusable requirements from project-specific examples. Prefer observable behavior over vague advice, and distinguish proposed guidance from verified results.

### Preserve adoption references

Follow the [README's adoption guidance](README.md#how-to-use-it) for control identities, catalog versions, and pinned source URLs, including in copied examples and cross-control references. Document replacements and migration implications whenever changes affect existing identities or references.

## 4. Classify the version impact

Use **Semantic Versioning (SEMVER)** in `MAJOR.MINOR.PATCH` form, following [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) with these catalog-specific change categories:

| Release | When to use it | Example |
| --- | --- | --- |
| **Major** | Breaking changes, including re-organizations that change published control paths, identities, or the meaning of existing requirements. | Move controls into a new hierarchy that requires adopters to update their references. |
| **Minor** | Add new content or controls while preserving compatibility with existing definitions and references. | Add a new control or a new guide. |
| **Patch** | Clarify or extend existing definitions without changing their requirements or invalidating existing implementations or assessments. | Explain an ambiguous term or add an example to an existing definition. |

Classify by the effect on adopters. An extension that introduces an incompatible requirement is a major change even if it edits only one definition. For changes spanning categories, use the highest required level. A major release resets minor and patch to zero; a minor release resets patch to zero.

**Current baseline hold:** the project remains early beta at **v0.1.0** until the repository owner explicitly approves a baseline. Use exact commit SHAs to identify interim revisions. Describe the intended version impact in pull requests, but do not bump the version or publish a release during this hold. Baseline approval and all release/version changes require explicit repository-owner decisions; this guide does not approve them. Never move published version tags or alter an already released version's contents.

## 5. Verify and open a pull request

Before submitting:

- Review the complete diff for accuracy, clarity, scope, and consistency; run `git diff --check`.
- Check changed links, references, and examples. For bundle changes, validate against the pinned specification and ensure the generated indexes cover the concepts present.
- Run `./scripts/validate_catalog.py` for bundle or schema changes. It uses `uv` script mode with inline PyYAML and Markdown parser dependencies to check OKF structure, catalog metadata and local links; passing it does not establish control effectiveness. Source indexes are curated and do not require exhaustive coverage.
- Run `./scripts/build_catalog.py` and `./scripts/test_validate_catalog.py` for bundle or tooling changes. The build checks complete index coverage in its generated output. The regression suite checks independent additions, generated discovery, and validation failures.
- Run relevant repository checks when available. For controls, assess whether the procedure can demonstrate the expected outcome and record evidence against its pass/fail criteria.
- Explain the problem and resulting change in the pull request. Include scope, version impact, compatibility or migration notes, checks actually performed, unverified claims, and the next unresolved decision. Link the relevant issue or prior discussion when available.

Never report a control as effective, a check as passing, or a baseline as approved without evidence. An absence of automated checks is not a passing test result.

## 6. Address review and hand off

Address review feedback and validate any resulting changes. Follow the [security controls](#2-prepare-a-branch-and-follow-security-controls) before an authorized merge. Report what changed, how it was checked, and any remaining blockers or decisions. If work cannot be published or merged, preserve the prepared changes and state what is needed to continue.
