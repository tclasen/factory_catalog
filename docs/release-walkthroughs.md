# Candidate adoption exercises

Use the generated bundle and record its full source commit and VERSION. The
release exercises are an agent-only task simulation and a programmatic consumer
check; no human participant is required. Record the evaluator/agent role, date,
procedure, task brief, selected concepts and rationale, outputs, friction,
failures, unknowns, corrections, repeats, and unresolved gaps. For simulated
adoption, distinguish the agent's reported experience from an observed human
outcome. These exercises do not establish operational control effectiveness.

## Agent-only: a meeting recommendation

Use only the bundle and this supplied fictional evidence; do not use online
research:

- Venue A: 12 seats, price 120 units, available Tuesday; supplier sheet revision 1.
- Venue B: 16 seats, price 150 units; availability is absent from supplier sheet revision 2.
- The group has 14 people, a 160-unit budget, and needs Tuesday availability.

Independently select applicable controls, state criteria before drafting, and
prepare a one-page recommendation. Read the selected controls' implementation,
assessment, dependencies, and in-bundle fixtures. Resolve mandatory dependencies;
for other linked controls, record whether their trigger applies and why. Record
whether adoption is by reference or by value and preserve the candidate commit
and VERSION. A programmatic adoption record may be used for copied content; keep
local adaptations distinct from source text.

Neither venue currently meets all established requirements. Do not invent
Venue B's availability or reduce the group size. A conditional recommendation
and request for missing evidence are valid outcomes.

Run only negative cases specified by selected controls. Record when an
assessment has no executable negative case rather than inventing a fixture. For
evidence traceability, if selected, check a fabricated citation, a contradictory
claim (A seats 14), and an unsupported claim missing from the claim table (B is
available Tuesday). If the control is not selected, record that fact without
retroactively changing the initial selection; consider applicability only in a
separate review.

Resume from an incomplete handoff that omits Venue B's source revision. Do not
supply the missing revision. Record whether completion remains withheld until
supported provenance is recovered. Retain failures and corrections, and repeat
affected steps after a documentation fix.

Report this as an agent simulation. It is not a human usability observation, a
real purchase or booking, or evidence that a control is operationally effective.

## Programmatic consumer

From an extracted bundle:

1. Recursively scan Markdown concepts excluding reserved index/log names. Parse
   YAML, derive identities from paths, and compare discovered identities with
   the complete generated navigation. Do not infer completeness from curated
   indexes.
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
consumer walkthrough against the actual candidate. Neither this check nor an
agent simulation establishes empirical human usability.
