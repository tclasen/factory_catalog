# Candidate adoption walkthroughs

Use these procedures with the generated bundle, recording its full source commit
and VERSION. Give participants the bundle and task brief; contributor documents
must not supply missing adopter instructions. Record participant, date, procedure,
observations, friction, failures, corrections, and unresolved gaps in the release
issue. These are protocols, not completed observations or operational assessments.

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
The participant makes and explains the selection; these suggestions are not a
mandatory minimum for ordinary adoption.

Copy one selected control with its adoption record; reference another at the same
commit. Follow required cross-control dependencies. Declare criteria before writing.
Neither venue currently meets all established requirements: do not invent B's
availability or reduce the headcount. The useful output can be a conditional
recommendation and a request for missing evidence.

Exercise the selected controls' negative fixtures. For evidence traceability,
include a fabricated citation, contradictory claim (A seats 14), and unsupported
claim missing from the claim table (B is available Tuesday). Inspect the full
output. Record detected failures, unknowns, and acceptance decisions separately.
Ask the participant to resume from an incomplete handoff that omits B's source
revision. Observe whether they identify and recover the missing provenance before
claiming a completed adoption. Repeat affected steps after any documentation fix.

## Human with an agent: bounded maintenance

Use a real, authorized repository-maintenance task. The human states the desired
result and boundaries; the agent uses bundle guidance to select and implement
controls. Record what requires human judgment, which effects are authorized, and
how the final evidence reaches the human. Do not assume the repository's own
contribution policy proves the catalog is sufficient for an outside adopter.

Pin reference adoptions and at least one dependency. Introduce a safe fixture with
an unavailable dependency and an interrupted handoff. Stop the predecessor before
resuming; reconstruct scope, current revision, effects, and remaining authority.
Retain an actual failed check and correction, or deliberately inject a safe failure.
Verify that missing evidence stays unknown and failed criteria block acceptance.
Record the human's ability to inspect the final handoff without contributor lore.

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
