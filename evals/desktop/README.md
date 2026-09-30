# Automated Codex desktop pilot

This pilot adds concrete fixtures and evidence handling to the [evaluation suite](../README.md).
The coordinator is a Codex desktop chat using native app tools. The Python utility
prepares files, records operations, validates evidence and generates reports; it
never invokes Codex CLI or a model API. Keep the coordinating chat and desktop open.

The fixed design is eight synthetic mixed-work tasks, three conditions (`bare`,
`minimal`, `catalog-full`), two repetitions, seed `20260930`, and
`gpt-6-astra` with `high` reasoning. The limits are 48 task chats and 48 evaluator
chats, serially. Task and evaluator reporting thresholds are 600 and 180 seconds.
Crossing a threshold does not cancel a run or halt dispatch after it finishes.
Wait for natural completion. A stuck chat can stall the batch indefinitely; there
is no guaranteed completion time or spending cap. No operator attendance is
required, but the desktop and coordinating chat must remain active.
Reservations count even if dispatch becomes uncertain. There are no replacement
runs or automatic retries within a frozen setup, model substitutions or recurring jobs.

## Qualification comes before dispatch

The [initial preflight report](reports/2026-09-30-preflight.md) preserves the
stop-control denial under the original cancellation policy. The user subsequently
authorized reporting-only thresholds. The current policy requires no UI stop
capability and uses native chat tools. The original experiment remains unchanged;
prepare a new frozen configuration under schema version 2. Do not migrate an
attempted experiment or combine its results with a different execution policy.

Before preparation, read the canonical issue and repository workflow. Record the
actual app version, desktop runtime, available app tool names, host permissions,
and capability observations in the issue and local checkpoint. Pin the catalog
commit. Use a new ignored experiment directory:

```sh
./scripts/desktop_eval.py --experiment build/evals/desktop-pilot prepare \
  --catalog-ref <full-commit-sha> --app-version <observed-app-version>
```

This writes immutable configuration, catalog content, fixtures and a randomized
48-cell manifest. The configuration hashes the harness source, rubric, prompts and
fixture inputs. It selects the onboarding prompt from the pinned README, with an
explicit override to use the packaged revision rather than fetching another one.
One block is a task/repetition under all three conditions; block and condition
orders are randomized independently. An existing experiment cannot be reset.

`preflight.json` starts with three unavailable capabilities: `native_chat_tools`,
`session_logs`, and `separate_workspaces`. A coordinator may record
`available: true` only with an actual supporting observation and its evidence
reference. Keep failed observations in the canonical issue. These records are
attestations, not a technical permission system. `reserve` refuses dispatch if any
capability is unavailable. The frozen execution policy is `wait_for_completion`.

Confirm that natural completion can be observed and full local session logs can
be located by the returned chat ID. The reader currently qualifies only desktop runtime
`0.159.2`, observed in a fresh projectless chat; the installed CLI version is irrelevant.
The reader decodes character entities once in the desktop creation envelope,
normalizes that envelope as user input and
`final_answer` as the final response; all other unmatched tool outputs still fail.
New log formats require a separate tested harness revision before a new experiment.

## Coordinator procedure

Run commands from the repository checkout. Replace placeholders with manifest IDs
and observed absolute paths. Never derive a run's condition from its chat title;
use neutral titles and the private manifest mapping.

1. Run `status`. If there is an unresolved reservation, inspect the actual desktop
   chat state and reconcile it before considering a new dispatch. Never repeat an
   uncertain `create_thread` call. A lost response without a uniquely recoverable
   chat identity halts the experiment.
2. Read the next manifest row in order. Use `stage <run-id> <new-absolute-directory>`
   to create its fixture workspace outside this repository and outside the evidence
   directory. The command returns the exact prompt and saves it in the run's private
   directory. Baselines receive no catalog files. Full-catalog runs receive the
   pinned bundle and `CATALOG_README.md`.
3. Run `reserve <run-id> task` **before** calling native `create_thread`. Create a
   fresh projectless desktop chat with the saved prompt, explicit model
   `gpt-6-astra`, thinking `high`, and an opaque directory/title name. Do not fork
   this coordinating chat or inherit its repository context. The app's projectless
   cwd and the prepared fixture workspace are separate identities; the prompt
   directs work into the latter. Record both rather than pretending they match.
4. Save the native receipt privately, then run
   `transition <run-id> task started --receipt <receipt.json>` with `thread_id`,
   `desktop_cwd`, `fixture_workspace`, and the UTC `started_at` timestamp. Start
   elapsed-time accounting at dispatch, not at the later response receipt.
5. Use native `wait_threads` with the returned cursor and waits of at most 60
   seconds. `deadline <run-id> task` is an optional read-only threshold indicator;
   a true result requires no cancellation or state transition. Keep waiting.
   Inspect results using `read_thread`, but do not use its truncated summaries as complete evidence.
6. For the missing-date fixture only, when the participant actually asks for the
   approved date, call `oracle <run-id>` and send its exact frozen response to that
   participant using the native message tool. No hints, remediation, or other
   steering is permitted. An uncertain oracle delivery requires reconciliation;
   never resend blindly. Its time remains part of the original task elapsed time.
7. Do not stop or mark a chat failed because it crosses a reporting threshold.
   Continue waiting for its natural completion. On account-limit failures, record
   the observed state with `account_limit: true` and halt further dispatch. If
   cessation cannot be established, use `blocked` and preserve the uncertainty.
   Do not purchase capacity or change models. Configuration drift and harness
   defects also halt new dispatch. On coordinator interruption, reconcile the
   same chat on resumption; do not start a replacement.
8. On actual completion, record `completed` with `cessation_observed: true`, then
   `collect <run-id> <session-jsonl-path>`. Capture the full correct session only.
   A capture error halts the experiment. Preserve the original log locally;
   encrypted reasoning and account metadata are never evaluator or public inputs.
9. Generate `evaluator-prompt <run-id>`, reserve the evaluator, and create one fresh
   projectless scoring chat with the same model/effort and the exact prompt. Record
   its identity as above. No workspace access, external tools or follow-up repair
   prompts are permitted for the scorer. Wait for natural completion, with a
   180-second reporting threshold.
10. On scorer completion, record its terminal receipt and call
    `score <run-id> <evaluator-session-jsonl-path>`. This checks the actual scorer
    session, model/effort, received prompt, JSON response and cited evidence. Missing
    or malformed scoring stays unscored; it is not replaced by invented values.
11. After the first three task runs and their evaluators, run `qualify`. This requires
    complete, uncontaminated capture and a scored or durably unscored outcome for
    each evaluator, with at least one accepted score to qualify the scoring path.
    It does not require successful task outcomes. Only then may
    the second block begin. Continue serially; run `report` at checkpoints and before
    handoff. Keep all evaluation chats available through handoff.

The coordinator calls the app tools; there is no undocumented Python endpoint that
starts desktop chats. The ledger is serialized with an OS file lock and chained
hashes. This prevents cooperative duplicate dispatch and detects accidental edits;
it is not protection against an actor with permission to rewrite all files.

## Evidence and scoring

The reader checks session identity, desktop cwd, model, effort, supported runtime,
turn completion, paired tool calls/results, inherited-context hashes and final
response. Unknown record types, pending calls or compaction stop dependent scoring.
A tool result truncated before reaching the participant is retained exactly as
seen and flagged as an output-visibility limitation. It does not imply missing
transcript records; evaluators must leave unsupported judgments unknown. Cumulative usage snapshots are not added together. Missing
usage/cost stays null. The exact app version and tool availability must also be
rechecked by the coordinator before each block; stop on changes.

Fixture checkers inspect artifacts and logged events. The two coding checks execute
the submitted Python with a five-second timeout. This is **not a security sandbox**;
the host execution boundary must be qualified before live use. Local simulated
service state and event files are supporting evidence, not tamper-proof audit logs.
Protected input comparisons catch final mutations but do not prove the absence of
temporary changes; the full trace remains relevant to evaluator judgment.

Every invariant must be represented. Failed deterministic checks cannot be
reversed by the evaluator, and missing deterministic observations remain unknown.
Only the two explicitly subjective claim judgments may be supplied by the scorer.
The scorer returns the five rubric dimensions, every invariant judgment,
`silent_error`, failure modes, and exact evidence quotations for every judgment.
Citation existence checks cannot establish that a quote supports the judgment;
that remains a stated automated-evaluation limitation. Disagreements are retained.

Blinded packages omit condition labels, setup prompts, account metadata, hidden
reasoning and catalog artifacts. Task behavior may still reveal catalog use; this
is partial blinding. Contamination detection flags observed cross-chat access,
baseline catalog reads, network research and changed catalog packages. It is a
conservative scanner, not a complete access-control proof. Separate workspaces do
not prevent reading other host files or using inherited tools.

## Durable interfaces and reporting

- `config.json`: versioned frozen configuration and input hashes.
- `manifest.json`: all 48 assignments and their randomized block/order identities.
- `attempts.jsonl`: append-only reservation, start, terminal, oracle, capture,
  qualification, scoring and halt records. A reservation consumes one allowance.
- `runs/<id>/`: prompts, staged identity, private source logs, normalized evidence,
  blinded package, scorer judgment and accepted result.
- `report.json` and `report.md`: reconciliation of every planned cell, condition and
  task summaries, failures/unknowns, disagreements, observed usage and comparisons.

Accepted results retain the existing run-record fields, adding experiment identity,
stratum, execution state, evidence digest, contamination and scorer disagreements.
Unscored attempts remain in the ledger/report instead of violating the scoring
schema with made-up scores. The existing manifest generator and analyzer remain
compatible and unchanged; this pilot utility adds stricter experiment handling.

Each report records its observation timestamp and task/evaluator timing for every
cell. Timing measures dispatch to the terminal receipt's observed cessation,
including polling and coordinator delay. This conservative proxy may classify a
quickly completed chat as late after a coordinator interruption; raw session
telemetry is retained separately. Threshold equality counts as within threshold.
Unfinished started attempts have a duration lower bound at report time, unknown
threshold success and no invented score; unstarted reservations have unknown time.
Reports show eventual pass rate among scored runs and pass within the task
threshold among scored runs with timing, with both denominators. Evaluator delay
is reported separately and does not change the task's time classification. All
unscored and unattempted cells remain visible; neither rate imputes their outcomes.

Reports compare full catalog with bare and minimal, matching task/repetition and
requiring matching environment identities. The desktop has supplied different
built-in instruction variants across otherwise identical fresh chats. Their hashes
are recorded, variant counts are reported by condition, and mismatched pairs are
excluded explicitly. Native creation does not expose a way to pin these variants;
condition summaries therefore retain this confounder. Permissions, tools, model,
effort, app/runtime and per-run context still require consistency.
Cluster intervals resample task means,
weighting each task equally; they are descriptive with only eight tasks. Unmatched
runs remain in summaries and the all-cell report. Task and evaluator resource
observations are reported separately, including their missingness.

The predeclared decision is to **stop** on qualification/harness failure, **revise**
on incomplete or contaminated evidence, and consider a separately authorized larger
experiment only after a fully qualified pilot. This pilot never authorizes adoption
on speed alone. Report quality regressions regardless of latency or token savings.
No retries, fixture repairs, rubric tuning or model changes may be silently mixed
into a frozen experiment. Preserve it and create a new bounded setup when repair
is authorized. The current user authorization permits automatic harness repairs,
new setups and verified PR merges until the pilot is complete. Keep cumulative
attempt counts across setups; never retry genuine task failures merely to pass.

Run `./scripts/test_desktop_eval.py` for offline regressions. These also run through
`./scripts/check_catalog.py --github`. Synthetic tests establish tooling behavior,
not successful desktop integration or catalog effectiveness.

## Audited analysis-only amendments

A valid evaluator response may leave a judgment unknown; malformed or unsupported
judgments also remain unscored. Save its raw session, available usage, rejection
reason and hashed `unscored.json` receipt. Never launch a replacement evaluator
merely to obtain a score. All 48 cells remain in reporting denominators.

An authorized observer correction can preserve the current task experiment using
`adopt-analysis-revision <original-observer.py> <reason>`. The original source must
match the frozen hash. An AST comparison rejects changes outside the observer and
admission functions; every other frozen input and the session reader must remain
identical. The score rule, evaluator prompt, fixture checks, task prompts and
reservation limits are outside the allowed change set. Review of the allowed
functions is still required; this is an audit boundary, not a security sandbox.

The amendment appends a ledger event and retains source hashes and the original
observer. Only the specifically recognized incomplete-score/qualification halts
can be superseded. A missing evaluator-log path can also be reconciled after the
correct session has passed identity, prompt and evidence validation; its source
digest and resolved halt are recorded. Account limits and other operational halts
remain active.
Reports disclose amendments and unscored outcomes. No completed chat is rerun and
no accepted score is overwritten. Changes to experimental inputs still require a
separate frozen setup.
