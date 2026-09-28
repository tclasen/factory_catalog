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

### Scripts

Write scripts in Python with a `#!/usr/bin/env -S uv run --script` shebang and an executable Git file mode. Declare Python requirements and dependencies in inline script metadata so `uv` can manage the script environment. Document direct invocation, such as `./scripts/validate_catalog.py`, without requiring an explicit Python launcher.

### Maintain the OKF bundle

- Always use the pinned vendored specification at `vendor/okf/SPEC.md` (OKF 0.2) when creating, reading, editing, or validating the OKF bundle. Do not substitute a live upstream version or remembered rules. Keep the bundle in `catalog/` and repository guidance and vendored files outside it.
- When initializing the bundle, create `catalog/index.md` as its entry point and declare `okf_version: "0.2"` there. Maintain the index as the bundle evolves. Each concept is a UTF-8 Markdown file with YAML frontmatter and a non-empty `type`; `index.md` and `log.md` are reserved.
- Use stable concept paths and relative links within the bundle. Keep indexes synchronized with added or moved concepts.
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
- Check changed links, references, and examples. For bundle changes, validate against the pinned specification and ensure indexes match the concepts present.
- Run `./scripts/validate_catalog.py` for bundle or schema changes. It uses `uv` script mode with an inline PyYAML dependency to check OKF structure, catalog metadata, local links, and index coverage; passing it does not establish control effectiveness.
- Run relevant repository checks when available. For controls, assess whether the procedure can demonstrate the expected outcome and record evidence against its pass/fail criteria.
- Explain the problem and resulting change in the pull request. Include scope, version impact, compatibility or migration notes, checks actually performed, unverified claims, and the next unresolved decision. Link the relevant issue or prior discussion when available.

Never report a control as effective, a check as passing, or a baseline as approved without evidence. An absence of automated checks is not a passing test result.

## 6. Address review and hand off

Address review feedback and validate any resulting changes. Follow the [security controls](#2-prepare-a-branch-and-follow-security-controls) before an authorized merge. Report what changed, how it was checked, and any remaining blockers or decisions. If work cannot be published or merged, preserve the prepared changes and state what is needed to continue.

## CI and merge enforcement

[Catalog CI](.github/workflows/validate.yml) runs on every pull request, pushes to
`main`, merge queue groups, and manual dispatch. The **Catalog validation** job
runs the validator regression tests and checks the complete catalog. It uses a
GitHub-hosted Ubuntu runner, read-only repository permission, no saved checkout
credentials, and actions pinned to full commit SHAs. Python and uv versions are
pinned in the workflow; Python dependencies are pinned in both executable scripts.
Update both scripts together when changing their shared dependencies.

Run the same checks locally with uv on PATH:

```sh
./scripts/test_validate_catalog.py
./scripts/validate_catalog.py
```

The validator checks catalog structure, metadata, Markdown navigation links,
index coverage, and required control sections with content. It does not establish
control effectiveness or compatibility with prior revisions, validate all optional
OKF fields, check external URLs or repository documentation links, or verify the
vendored specification checksums. Human review remains necessary. Undefined
Markdown reference labels render as plain text; only resolved Markdown links are
checked. Heading anchors use the validator's existing simplified heading rules.

### Enable the workflow

1. Publish this branch and open a pull request. In **Settings → Actions → General**,
   confirm Actions is enabled and policy allows `actions/checkout` and
   `astral-sh/setup-uv` at the pinned revisions. Keep default workflow permissions
   read-only; this workflow needs no secrets or write access.
2. Let **Catalog CI / Catalog validation** complete successfully on the pull
   request. A first-time fork contributor may need a maintainer to approve the run.
   Review workflow changes before granting that approval.
3. Merge through the normal signed-commit and review process. Manual dispatch is
   available from the Actions tab once the workflow is on the default branch.

### Require a passing check before merging

A workflow file does not make its result mandatory. A repository administrator
must configure enforcement separately:

1. Open **Settings → Rules → Rulesets** and edit the active ruleset targeting
   `main` (or create an active branch ruleset targeting the default branch).
2. Keep the existing pull request, code owner review, signature, linear history,
   conversation resolution, deletion, and force-push protections.
3. Enable **Require status checks to pass** and add the exact check name
   **Catalog validation**. Select **GitHub Actions** as its expected source when
   offered. If the check is absent from the picker, first run the workflow
   successfully on a PR and refresh the settings page.
4. Enable **Require branches to be up to date before merging**. If using a merge
   queue, the workflow already handles `merge_group` events.
5. Keep enforcement **Active** and review bypass entries: anyone allowed to bypass
   the rule can merge without the check. Avoid bypasses if universal enforcement
   is intended. Save the ruleset.
6. Verify with a temporary PR that introduces a broken catalog link: the check
   should fail and merging should be blocked. Fix the link, rerun, and confirm
   the status-check requirement is satisfied. Other review rules may still block
   merging.

For repositories using classic branch protection, add **Catalog validation**
under **Settings → Branches → main protection → Require status checks to pass
before merging**, require an up-to-date branch, and apply protection to bypass
actors as appropriate. Do not remove existing protections to add this check.

Keep the job name stable after making it required. Run on every PR without path
filters, and do not add `continue-on-error` or job conditions that let validation
be skipped. Review changes to the workflow, validator, and tests as changes to the
merge gate; CODEOWNERS includes these paths.

See GitHub's [ruleset setup instructions](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
and [available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
