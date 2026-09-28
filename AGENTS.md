# Maintaining Factory Catalog

## Mission and current scope

Maintain a concise, reusable catalog of controls for knowledge work in and with AI systems, including complete systems assembled from controls. Read [README.md](README.md) before changing the repository.

The project is early beta at **v0.1.0** until the repository owner approves a baseline. The control taxonomy will be maintained in the `catalog/` OKF bundle. Its families, control identifiers, and domain schema remain open design decisions. Discuss and record those decisions before establishing them; do not silently invent a baseline or import an entire factory framework.

## Work as an active maintainer

- Inspect current files, applicable instructions, and relevant issues or pull requests before starting. Identify the requested outcome and the smallest useful change.
- Carry authorized work through implementation, verification, and a clear handoff. Resolve routine details independently; ask focused questions when a missing decision blocks correctness or scope.
- Keep changes focused and reviewable. Preserve others' work, reconcile concurrent changes, and avoid unrelated cleanup.
- Coordinate through the existing issue or pull request when available. Record scope, decisions, evidence, blockers, and next steps so another person or agent can continue without reconstructing the conversation.
- Use a topic branch and pull request for changes to the protected default branch. Apply the security workflow below without waiting for a reminder; maintainer instructions do not grant additional authority.

## Follow repository security controls

### Inspect the live rules

Before publishing changes or merging, confirm the default branch, effective rules, current account permissions, and relevant pull request state. Use the GitHub API or equivalent tooling:

```sh
gh api repos/tclasen/factory_catalog
gh api 'repos/tclasen/factory_catalog/rulesets?includes_parents=true'
gh api repos/tclasen/factory_catalog/rules/branches/main
gh api repos/tclasen/factory_catalog/rulesets/24142531
```

Substitute the current default branch and ruleset IDs if they change, and inspect any additional applicable rulesets. Check classic branch protection as well. A `403`, `404`, or omitted security field does not by itself establish that a control is disabled; report inaccessible settings as unverified. Live rules take precedence over the snapshot below. Never weaken settings, invoke a bypass, or retry a rejected operation through another identity to finish a task.

### Verified configuration (2026-09-28)

The active repository ruleset [main](https://github.com/tclasen/factory_catalog/rules/24142531) targets the default branch (`main`), with no branch exclusions:

- Changes require a pull request. Branch deletion and non-fast-forward updates are blocked.
- Commits require verified signatures, and history must remain linear.
- Code-owner review and resolution of review threads are required. The general approving-review count is zero; stale approvals are not automatically dismissed, and approval of the most recent push is not required. Extra approval for unattributed changes is enabled.
- No required status checks are listed in the effective rules. The ruleset permits merge, squash, and rebase methods, but the linear-history requirement also applies.
- The inspected account, `tclasen-agent`, has push access but no maintain or admin permission, and `current_user_can_bypass` is `never`.

The root [CODEOWNERS](CODEOWNERS) file assigns `/AGENTS.md` solely to `@tclasen`. Require their code-owner approval for changes to this file. GitHub uses the ownership mapping on the pull request's base branch, so enforcement of this new mapping begins once it lands there. Do not invent an owner or claim an owner approved.

At inspection, the repository has no GitHub Actions workflows, Dependabot configuration, or `SECURITY.md`. Auto-merge is disabled. Classic branch protection and vulnerability-alert and secret-scanning endpoints returned `404`; Actions policy and code-scanning setup endpoints returned `403`; `security_and_analysis` was unavailable. These settings remain unverified, including secret scanning and push protection. Do not infer that scanning is enabled or that there are no alerts.

### Carry out changes within those controls

- Start from an up-to-date default branch and work on a topic branch. Never push directly to the protected default branch, force-push it, or delete it, even when a request suggests a shortcut.
- Before committing, inspect the configured identity and signing mechanism. Sign every proposed commit, including documentation changes. Use an authorized local signing key, or GitHub’s `createCommitOnBranch` API with the existing authenticated account to create a GitHub-signed commit on the topic branch. Verify local signatures when signing locally and confirm GitHub reports the published commits as verified. If neither signing path is available, preserve the prepared changes and report the specific blocker; do not create unsigned commits or silently provision a new identity or key.
- Review the diff and run relevant checks before submitting the pull request. An empty required-check list is not evidence that the change was tested. Report the checks actually performed.
- Before an authorized merge, recheck the current pull request revision, GitHub mergeability, required checks, review decisions, applicable code owners, and unresolved threads. Address review feedback and resolve threads only when the concern is actually handled. Zero general approvals does not waive other review requirements; do not fabricate approvals or treat silence as approval.
- Use squash or rebase as permitted by the live rules, preserving verified signatures on commits entering the default branch. Do not use a merge commit: it conflicts with linear history even though the repository advertises that merge method. Do not assume rewritten commits retain their signatures; verify the resulting commits on GitHub.
- Continue authorized preparation, validation, and pull request work independently. Stop only the blocked publication or merge step when credentials, signing, required review, checks, or permission are missing; explain what is needed without changing the controls.
- Keep credentials and private signing material out of tracked files, logs, and pull requests. If future work adds automation or dependencies, inspect the applicable Actions permissions and security configuration before relying on them, and use only the permissions the workflow needs.

## Maintain the OKF bundle

- Always use the pinned vendored specification at `vendor/okf/SPEC.md` (OKF 0.2) when creating, reading, editing, or validating the OKF bundle. Do not substitute a live upstream version or remembered rules. Keep the bundle in `catalog/` and repository guidance and vendored files outside it.
- When initializing the bundle, create `catalog/index.md` as its entry point and declare `okf_version: "0.2"` there. Maintain the index as the bundle evolves. Each concept is a UTF-8 Markdown file with YAML frontmatter and a non-empty `type`; `index.md` and `log.md` are reserved.
- Use stable concept paths and relative links within the bundle. Keep indexes synchronized with added or moved concepts.
- Keep the upstream specification and license unchanged. For upgrades, fetch from an exact upstream commit, review the changes, update `vendor/okf/UPSTREAM.md` and its checksums, and assess bundle compatibility.
- Distinguish OKF format version 0.2 from catalog version v0.1.0.

## Maintain useful controls

Once the taxonomy and format are agreed, each control should have a stable identity and family, a clear purpose, applicability guidance, implementation instructions, measurable expected outcomes, and an assessment with evidence and pass/fail criteria. Make dependencies and limitations explicit.

Keep controls individually selectable and usable both by URL and by copying their content. Separate reusable requirements from project-specific examples. Prefer observable behavior over vague advice, and distinguish proposed guidance from verified results.

## Preserve versioned references

- Keep the catalog at v0.1.0 during this pre-baseline phase. Use exact commit SHAs to identify interim revisions.
- Preserve each adopted control's identity, catalog version, and pinned source URL, including in copied examples and cross-control references.
- Do not move published version tags or silently break control identities and references. Document replacements and migration implications when changes require them.
- Treat baseline approval and release/version changes as explicit repository-owner decisions.

## Verify and hand off

Review the diff for accuracy, clarity, scope, and consistency. Check changed links, references, and examples; run relevant repository checks when available. For controls, assess whether the stated procedure can demonstrate the expected outcome.

Report what changed, how it was checked, any unverified claims, and the next unresolved decision. Never report a control as effective, a check as passing, or a baseline as approved without evidence.
