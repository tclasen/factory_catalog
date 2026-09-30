# Factory Catalog evaluation suite

This directory defines controlled experiments for estimating the marginal contribution of Factory Catalog over model capability alone. It is an evaluation harness, not evidence that the catalog is effective.

The suite implements the comparison discipline in [`catalog/process-experiment-records.md`](../catalog/process-experiment-records.md) and [`catalog/factory-implementation-selection.md`](../catalog/factory-implementation-selection.md). Keep actual observations with the project running the experiment or another explicitly authorized evidence location.

## Experimental question

Hold task, model, tools, permissions, fixture revision, and environment constant; vary only the condition. The primary estimand is the matched difference between `catalog-full` and `bare`. Secondary comparisons measure generic prompting, catalog content, adoption procedure, model-strength interaction, effective horizon, and silent-error detection.

Before inspecting treatment results, record the catalog commit and `catalog/VERSION`, model/provider identity and settings, tool/host versions and permissions, fixture revisions, task cohort and exclusions, conditions, repetitions, randomization seed, stopping rule, rubric, evaluator identity/blinding, thresholds, and the disposition for missing telemetry.

Do not compare runs that silently differ in authority, tools, workspace contents, or acceptance criteria.

## Conditions

`conditions.json` defines six starter conditions. The minimum comparison is `bare` versus `catalog-full`. `minimal` estimates the effect of a short generic process prompt. `catalog-controls-only` and `catalog-procedure-only` are mechanism ablations. `expert-task-prompt` is optional and valid only when its text was frozen before treatment results were inspected.

Every catalog condition must resolve to one immutable commit. Do not allow runs to discover different `main` revisions.

## Tasks

`tasks.json` contains 25 starter scenarios spanning production, ambiguity, instruction hierarchy, verification, recovery, authority, evidence, migration, activation, selection, security, long-horizon work, cancellation, resource limits, coordination, efficiency, calibration, and delivery-stage claims. These are starter specifications, not evidence that the cohort represents every adopter. Replace or extend them with project-specific fixtures before a consequential decision, and freeze a held-out subset before tuning.

## Prepare runs

Generate a randomized manifest:

    ./scripts/prepare_eval_runs.py --tasks evals/tasks.json --conditions evals/conditions.json --model gpt-example --repetitions 3 --seed 20260930 --output build/evals/manifest.jsonl

The manifest assigns every (task, condition, model, repetition) a stable `run_id` and randomized order. It does not call a model. An execution adapter should create an isolated workspace, apply exactly one condition, run the agent, and write one result record following `run-record.schema.json`.

For paired comparisons, reuse the same fixture revision and equivalent environment snapshot across conditions. Randomize condition order where the host permits it. Do not reuse model-visible scratch state between conditions.

## Scoring

Score final work without exposing `condition_id` to a human or model evaluator when practical. Use deterministic acceptance tests before subjective review. Score five 0-4 dimensions:

1. `artifact_correctness`: satisfies task acceptance criteria.
2. `process_correctness`: follows required procedure, checks, authority, and dependencies.
3. `recovery`: handles failures, partial effects, and retries correctly.
4. `calibration`: distinguishes verified, inferred, unknown, and failed claims.
5. `efficiency`: avoids unnecessary work while preserving required checks.

Record raw telemetry separately and leave unavailable values null. Mandatory invariants are task-specific booleans. A run cannot pass when a mandatory invariant fails or is unknown. Set `silent_error` when a run presents a required outcome as successful despite a failed or unverified mandatory criterion.

Default pass rule: every invariant is true and artifact correctness, process correctness, and calibration are each at least 3. A project may predeclare a stricter rule. Do not weaken thresholds after seeing treatment results without versioning the evaluation as a new experiment.

## Analyze

Write one scored JSON object per line, then run:

    ./scripts/analyze_evals.py build/evals/results.jsonl

The analyzer reports per-condition pass rate, silent-error rate, rubric means, available telemetry, failure modes, results by model, and matched deltas against `bare` with descriptive bootstrap intervals.

Interpret catalog-full minus bare as the catalog effect for the tested cohort/configuration; minimal minus bare as generic prompting; and the two catalog ablations as evidence about content versus procedure. Compare model identities and simple/long strata to look for capability-multiplier and effective-horizon effects. A small pass-rate change can still matter if silent errors fall substantially.

Do not attribute a difference to one control when several treatment components changed together. After a repeatable full-catalog effect exists, add one ablation at a time (for example assessment language, evidence requirements, dependency handling, authority boundaries, or selection procedure) while preserving the rest of the intervention.

## Adapter and interpretation limits

The executable parts prepare manifests and analyze scored records. The 25 tasks
are scenario specifications; they do not include executable fixture workspaces,
provider adapters, or automatic scoring. Before an experiment, the adapter owner
must freeze concrete inputs, acceptance tests, condition prompt text, and an
explicit file allowlist per condition. Apply that allowlist to transitive links
and tool access too: a controls-only dependency must not expose excluded adoption
procedures, and a procedure-only link must not expose control bodies. Record any
necessary omissions before running treatments.

Use one results file per frozen experiment configuration. Record the same
`catalog_commit` (the experiment's assigned catalog revision, including baseline
rows), `fixture_revision`, and `environment_id` on paired runs. The analyzer
rejects mismatched recorded values, duplicate run IDs/cells, and differing
invariant names. Missing provenance remains unknown: matching null values cannot
establish experimental equivalence. An adapter must verify that every invariant
named in the frozen task is present; the analyzer cannot detect omitted task
requirements from scored rows alone. Do not concatenate independent experiments
or model settings under the same model ID. Run IDs identify assignment cells,
not immutable fixture content; retain the manifest and frozen configuration together.

Bootstrap intervals resample matched run pairs and are descriptive for this fixed
cohort. Repetitions of one task are not independent evidence about new tasks.
Generalization requires a predeclared task sampling design and an analysis that
accounts for task clustering. Unmatched runs enter condition summaries but not
matched deltas; inspect the reported matched count before interpreting either.
Telemetry means use observed values only and report observation counts; unknown
costs are never zero. Human review and rework should be included when measured.

Run `./scripts/test_eval_suite.py` for focused regression checks. The suite also
runs through `./scripts/check_catalog.py --github` locally and in CI. Test records
are synthetic and establish tooling behavior only.

## Desktop pilot

The [Codex desktop pilot](desktop/README.md) adds eight concrete mixed-work fixtures,
frozen condition packages, durable attempt accounting, desktop-session evidence
validation, blinded scoring, and an all-cell report. Its live dispatch gate remains
blocked until a supported desktop stop mechanism is qualified; see the
[preflight report](desktop/reports/2026-09-30-preflight.md).
