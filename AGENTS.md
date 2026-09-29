# Maintaining Factory Catalog

Read [README.md](README.md) for the project's mission and current scope before changing the repository.

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the shared human and AI contribution workflow, including design decisions, security controls, OKF maintenance, control quality, versioning, verification, and handoff. These requirements apply to every agent contribution.

## Work as an active maintainer

Carry authorized work through implementation, verification, and a clear handoff. Resolve routine details independently; ask focused questions when a missing decision blocks correctness or scope. Maintainer instructions do not grant additional authority.

## Start from the latest main commit

Before starting any work, fetch `origin/main` and create the task's topic branch from its latest commit. When continuing an existing branch, fetch and incorporate the latest `origin/main` before making further changes. Do not rely on a stale local `main` or remote-tracking ref. Preserve existing work and follow the signing and branch protection requirements in [CONTRIBUTING.md](CONTRIBUTING.md).

## Completion requires local tests and a remote pull request

No work is considered done until all of the following are complete, in order:

1. Test the final changes locally with the checks required by [CONTRIBUTING.md](CONTRIBUTING.md) and any additional checks relevant to the change. Review the diff and run `git diff --check`, including for documentation-only changes. Fix failures and rerun affected checks after any further edits.
2. Push the tested changes as signed commits on the topic branch to the remote and open or update a pull request targeting `main`. Confirm the PR contains the tested revision and GitHub reports the commits as verified.
3. Hand off the PR URL and the local checks actually run, their results, and any remaining review decisions.

If local tests, signing, credentials, permissions, or PR publication are blocked, preserve the work and report the specific blocker. The task remains incomplete until local verification and remote PR publication succeed. Merging requires separate authorization under [CONTRIBUTING.md](CONTRIBUTING.md).

## Parallel work

Follow [Parallel contributions](CONTRIBUTING.md#parallel-contributions). Use an isolated checkout and topic branch per concurrent task. Ordinary concept additions must not require edits to shared indexes, logs, registries, or version files. Discover content from files and frontmatter, and run `./scripts/build_catalog.py` to check generated navigation. Coordinate edits to the same concept or shared schema before merging.

## Avoid catalog-wide maintenance

Follow [Keep changes local](CONTRIBUTING.md#keep-changes-local). Keep bundle facts in one authoritative location, derive navigation and display metadata, and preserve concept-specific evidence. Before adding a field or repeated instruction, check whether changing it would force unrelated files to be rewritten.
