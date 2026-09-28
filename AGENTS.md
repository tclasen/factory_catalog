# Maintaining Factory Catalog

Read [README.md](README.md) for the project's mission and current scope before changing the repository.

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the shared human and AI contribution workflow, including design decisions, security controls, OKF maintenance, control quality, versioning, verification, and handoff. These requirements apply to every agent contribution.

## Work as an active maintainer

Carry authorized work through implementation, verification, and a clear handoff. Resolve routine details independently; ask focused questions when a missing decision blocks correctness or scope. Maintainer instructions do not grant additional authority.

## Parallel work

Follow [Parallel contributions](CONTRIBUTING.md#parallel-contributions). Use an isolated checkout and topic branch per concurrent task. Ordinary concept additions must not require edits to shared indexes, logs, registries, or version files. Discover content from files and frontmatter, and run `./scripts/build_catalog.py` to check generated navigation. Coordinate edits to the same concept or shared schema before merging.
