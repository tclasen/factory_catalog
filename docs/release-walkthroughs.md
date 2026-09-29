# Candidate adoption walkthroughs

Use these procedures with the generated bundle, recording its full source commit
and VERSION. Give participants the bundle and task brief; contributor documents
must not supply missing adopter instructions. Record participant, evaluator and
independence, date, procedure, task brief, selections and rationale, outputs,
observations, friction, failures and unknowns, corrections and repeats, and
unresolved gaps in the release issue. For repository maintenance, also record
the repository revision, human/agent roles, tools, allowed effects, isolation,
fixture state, and cleanup. These are protocols, not completed observations or
operational assessments.

## Human-only: a meeting recommendation

A human prepares a one-page recommendation choosing between two fictional meeting
venues. Use this supplied evidence, without online research:

- Venue A: 12 seats, price 120 units, available Tuesday; supplier sheet revision 1.
- Venue B: 16 seats, price 150 units; availability absent from supplier sheet revision 2.
- The group has 14 people, a 160-unit budget, and needs Tuesday availability.

Using only the bundle, identify applicable controls, record selections and
provenance, implement the chosen procedures, and assess the recommendation.
Suggested starting points are [adoption](../catalog/adoption.md),
[evidence traceability](../catalog/controls/evidence-traceability.md), and
[outcome verification](../catalog/controls/outcome-verification.md).
The participant makes and explains the initial selection without being shown
these suggestions or the negative fixtures. They are facilitator references,
not required selections for ordinary adoption.

Copy one selected control with its adoption record; reference another at the same
commit. Follow required cross-control dependencies. Declare criteria before writing.
Neither venue currently meets all established requirements: do not invent B's
availability or reduce the headcount. The useful output can be a conditional
recommendation and a request for missing evidence.

After recording the initial recommendation, inspect each selected control's
assessment and run an in-bundle negative case when one is specified. Do not invent
a substitute fixture; record when an assessment has no executable negative case.
For evidence traceability, if selected, include a fabricated citation,
contradictory claim (A seats 14), and unsupported claim missing from the claim
table (B is available Tuesday). Inspect the full output and record detected
failures, unknowns, and acceptance decisions separately. If evidence
traceability was not selected, record that omission and its rationale, then
present it as a separate applicability challenge after the first recommendation;
do not silently add it to the participant's original adoption.

Ask the participant to resume from an incomplete handoff that omits B's source
revision. Do not provide the missing revision in the handoff. Observe whether the
participant withholds completion until they recover supported provenance. Repeat
affected steps after any documentation fix.

## Human with an agent: bounded maintenance

Before the session, the human supplies a real authorized maintenance task and
states its desired result, boundaries, and allowed effects. Record the repository
and starting commit, the disposable worktree or copy used, the human, agent and
evaluator roles, and the tools available. The agent uses bundle guidance to
select and implement controls. Do not assume the repository's own contribution
policy proves the catalog is sufficient for an outside adopter.

Run the task in an isolated disposable worktree or copy. Limit effects to that
checkout and local checks; do not push, merge, deploy, contact external parties,
or use production data. Put failure injection and unavailable-dependency fixtures
in a separate scratch area of that disposable checkout. Use a deliberately absent
local fixture dependency and a safe failing check, not a disabled real service or
broken shared branch. Record the fixture setup and remove it after the session;
verify the shared repository and external systems were not changed.

Pin reference adoptions and at least one dependency to the candidate revision.
Create an interrupted handoff that records scope, current revision, attempted
effects, evidence, unresolved dependency, and remaining authority. Stop the
predecessor before resuming. Observe whether the successor agent reconstructs
those facts and whether the human can inspect them without contributor lore.
Retain the actual or injected failed check and correction. Verify missing evidence
stays unknown and failed criteria block acceptance. Record the final local diff
and cleanup disposition; do not treat isolated test effects as repository changes.

## Programmatic consumer

From an extracted bundle:

1. Recursively scan Markdown concepts excluding reserved index/log names. Parse
   YAML, derive identities from paths, and compare discovered identities with the
   complete generated navigation. Do not infer completeness from curated indexes.
2. Resolve every structured control selection to a Control at the same revision.
   Distinguish applicability, implementation state, and assessment result.
3. Read VERSION and the external provenance manifest; retain the full commit and
   pinned source URLs for reference adoption. Copy a control and its dependencies,
   preserving metadata, source text, and provenance alongside local adaptations.
4. Exercise an unknown optional key, omitted optional status, malformed YAML,
   broken dependency, unknown selection state, and missing source provenance.
   Document which inputs can be preserved generically and which interpretations
   must be withheld. A successful parser is not a successful control assessment.
5. Interrupt after copying but before recording provenance. Resume by verifying
   source correspondence and filling only supported fields; otherwise leave the
   adoption incomplete. Verify an upgrade preserves the old adoption record.

The [release regression suite](../scripts/test_release_catalog.py) covers many
mechanical failure cases with a synthetic stable fixture. Its status substitutions
are test setup only; they do not approve catalog concepts or replace this complete
consumer walkthrough against the actual candidate.
