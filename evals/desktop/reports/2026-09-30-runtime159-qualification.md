# Desktop runtime 0.159.2 qualification

**Decision: revise before another pilot.** One task and its evaluator completed,
but frozen-prompt validation rejected scoring. No catalog-effectiveness result is
available. [Issue #80](https://github.com/tclasen/factory_catalog/issues/80) remains
the work record; [PR #82](https://github.com/tclasen/factory_catalog/pull/82) contains
the reader adaptation and correction.

## Configuration and observations

The new experiment used app 26.928.21956 (12404), desktop runtime 0.159.2,
`gpt-6-astra` / `high`, seed 20260930, and the unchanged catalog at
`f4c6f53679248f3330a6724b8458fe0e49cd0999`. Its configuration hash was
`93453ca16fdfa845d5e4d89b13818882e271e361384959f9404bb8c4dbbd196f`.
Task/evaluator time thresholds were reporting-only, with serial natural completion.

| Observation | Count |
|---|---:|
| Planned tasks | 48 |
| Task attempts / natural completions | 1 / 1 |
| Evaluator attempts / natural completions | 1 / 1 |
| Accepted scores | 0 |
| Unattempted tasks | 47 |

The first randomized cell was the minimal-prompting uncertain-effect fixture.
Task session capture passed identity, model/effort, completion and tool pairing
checks, with no detected contamination. Native duration was 39.591 seconds for
the task and 53.338 seconds for its evaluator. These are single-run observations,
not comparative performance estimates.

The desktop encodes the initial prompt inside a creation envelope. The initial
adapter recognized that envelope but did not decode its character entities.
The evaluator's input contained XML markup from the blinded evidence, so the
captured prompt failed exact comparison with the frozen prompt. The scoring gate
rejected it, and further dispatch halted. No scores were invented or repaired.

## Correction and limitations

The corrected adapter decodes entities once. Replaying the retained evaluator log
for adapter validation recovers the exact frozen prompt and a complete session.
Regression coverage includes literal entities, malformed/repeated/late envelopes,
unknown output sources, final-answer normalization and scoring from an encoded
creation envelope. This replay does not score or alter the frozen experiment.

The raw task/evaluator logs, artifacts, ledger and generated all-cell report remain
local. The prior runtime-mismatch experiment also retains its separate one task
attempt and zero evaluator attempts. Cumulatively, these qualification attempts
used two task chats and one evaluator chat. Neither experiment is reset or pooled.

Pass rates, silent-error rates and paired differences remain unknown. Automated
checks do not establish effectiveness. Recommendation: retain the halted records
and validate a separately authorized new frozen pilot with the corrected reader.
