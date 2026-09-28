# Maintaining Factory Catalog

## Mission and current scope

Maintain a concise, reusable catalog of controls for knowledge work in and with AI systems, including complete systems assembled from controls. Read [README.md](README.md) before changing the repository.

The project is early beta at **v0.1.0** until the repository owner approves a baseline. The taxonomy, control identifiers, and schema remain open design decisions. Discuss and record those decisions before establishing them; do not silently invent a baseline or import an entire factory framework.

## Work as an active maintainer

- Inspect current files, applicable instructions, and relevant issues or pull requests before starting. Identify the requested outcome and the smallest useful change.
- Carry authorized work through implementation, verification, and a clear handoff. Resolve routine details independently; ask focused questions when a missing decision blocks correctness or scope.
- Keep changes focused and reviewable. Preserve others' work, reconcile concurrent changes, and avoid unrelated cleanup.
- Coordinate through the existing issue or pull request when available. Record scope, decisions, evidence, blockers, and next steps so another person or agent can continue without reconstructing the conversation.
- Use a branch and pull request for proposed changes unless direct commits are authorized. Follow repository permissions and review rules; maintainer instructions do not grant additional authority.

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
