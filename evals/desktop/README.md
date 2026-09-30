# Automated Codex desktop pilot

This pilot adds concrete fixtures and evidence handling to the [evaluation suite](../README.md).
The coordinator is a Codex desktop chat using native app tools. The Python utility
prepares files, records operations, validates evidence and generates reports; it
never invokes Codex CLI or a model API. Keep the coordinating chat and desktop open.

The fixed design is eight synthetic mixed-work tasks, three conditions (`bare`,
`minimal`, `catalog-full`), two repetitions, seed `20260930`, and
`gpt-6-astra` with `high` reasoning. The limits are 48 task chats and 48 evaluator
chats, serially. Task and evaluator deadlines are 600 and 180 seconds respectively.
Reservations count even if dispatch becomes uncertain. There are no replacement
runs, automatic retries, model substitutions or recurring jobs.

## Qualification comes before dispatch

The [initial preflight report](reports/2026-09-30-preflight.md) records a stop-control
blocker. It is not an evaluation result. The current Computer Use tool rejects
access to Codex, and the available native tools do not expose an arbitrary-chat
stop operation. Do not start a batch while this gate is unresolved. Moving a chat,
closing a window, archiving a chat, asking the evaluated agent to stop, killing the
app, or switching to CLI execution is not a qualified replacement.

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

`preflight.json` starts with four unavailable capabilities: `native_chat_tools`,
`stop_action`, `session_logs`, and `separate_workspaces`. A coordinator may record
`available: true` only with an actual supporting observation and its evidence
reference. Keep failed observations in the canonical issue. These records are
attestations, not a technical permission system. `reserve` refuses dispatch if any
capability is unavailable. No command here manufactures or grants a stop capability.

Confirm that a supported stop action targets the exact chat and that cessation can
be observed. Confirm that full local session logs can be located by the returned
chat ID. The reader currently qualifies only desktop runtime
`0.158.0-alpha.2.1`, observed on this host; the installed CLI version is irrelevant.
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
   timeout accounting at dispatch, not at the later response receipt.
5. Use native `wait_threads` with the returned cursor and waits of at most 60
   seconds. Check `deadline <run-id> task` between waits. Inspect relevant results
   using `read_thread`, but do not use its truncated summaries as complete evidence.
6. For the missing-date fixture only, when the participant actually asks for the
   approved date, call `oracle <run-id>` and send its exact frozen response to that
   participant using the native message tool. No hints, remediation, or other
   steering is permitted. A uncertain oracle delivery requires reconciliation;
   never resend blindly. Its time remains part of the original task deadline.
7. On a timeout, use the qualified stop action and independently confirm cessation.
   Then record `timed_out` with `cessation_observed: true` and a reason. This halts
   further dispatch. If cessation cannot be established, record `blocked` with
   the uncertainty and stop dispatch immediately. Do the same for account-limit
   failures. Do not purchase capacity or change models.
8. On actual completion, record `completed` with `cessation_observed: true`, then
   `collect <run-id> <session-jsonl-path>`. Capture the full correct session only.
   A capture error halts the experiment. Preserve the original log locally;
   encrypted reasoning and account metadata are never evaluator or public inputs.
9. Generate `evaluator-prompt <run-id>`, reserve the evaluator, and create one fresh
   projectless scoring chat with the same model/effort and the exact prompt. Record
   its identity as above. No workspace access, external tools or follow-up repair
   prompts are permitted for the scorer. Apply the 180-second deadline.
10. On scorer completion, record its terminal receipt and call
    `score <run-id> <evaluator-session-jsonl-path>`. This checks the actual scorer
    session, model/effort, received prompt, JSON response and cited evidence. Missing
    or malformed scoring stays unscored; it is not replaced by invented values.
11. After the first three task runs and their evaluators, run `qualify`. This requires
    complete, uncontaminated scoring, not success on the task itself. Only then may
    the second block begin. Continue serially; run `report` at checkpoints and before
    handoff. Keep all evaluation chats available through handoff.

The coordinator calls the app tools; there is no undocumented Python endpoint that
starts desktop chats. The ledger is serialized with an OS file lock and chained
hashes. This prevents cooperative duplicate dispatch and detects accidental edits;
it is not protection against an actor with permission to rewrite all files.

## Evidence and scoring

The reader checks session identity, desktop cwd, model, effort, supported runtime,
turn completion, paired tool calls/results, inherited-context hashes and final
response. Unknown record types, pending calls, compaction or possible truncation
stop dependent scoring. Cumulative usage snapshots are not added together. Missing
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

Reports compare full catalog with bare and minimal, matching task/repetition and
requiring matching environment identities. Cluster intervals resample task means,
weighting each task equally; they are descriptive with only eight tasks. Unmatched
runs remain in summaries and the all-cell report. Task and evaluator resource
observations are reported separately, including their missingness.

The predeclared decision is to **stop** on qualification/harness failure, **revise**
on incomplete or contaminated evidence, and consider a separately authorized larger
experiment only after a fully qualified pilot. This pilot never authorizes adoption
on speed alone. Report quality regressions regardless of latency or token savings.
No retries, fixture repairs, rubric tuning or model changes may be silently mixed
into a frozen experiment. Preserve it and request a new bounded experiment instead.

Run `./scripts/test_desktop_eval.py` for offline regressions. These also run through
`./scripts/check_catalog.py --github`. Synthetic tests establish tooling behavior,
not successful desktop integration or catalog effectiveness.
