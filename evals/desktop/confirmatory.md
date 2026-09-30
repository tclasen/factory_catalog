# Objective desktop benchmark

This revision follows the [pilot report](reports/2026-09-30-pilot.md) and
[tracking issue #87](https://github.com/tclasen/factory_catalog/issues/87).
It measures task completion on the fixed eight synthetic fixtures. It does not
measure general catalog usefulness or replace human evaluation.

## What changed and why

The pilot conflated additional adoption records with changed protected inputs,
lost most full-catalog scores to evaluator citation/unknown judgments, and had
almost no accepted matched comparisons. Schema 3 expressly permits `adoption/`
and `scratch/` for every condition, checks original inputs separately, and
replaces subjective evaluator ratings with observable checks and `completion.json`.
No evaluator chats are dispatched. Older schema 2 preparation and analysis remain
available; historical experiments must use their frozen source revision.

Every run receives the same task permissions and completion interface. Bare has
no condition prompt; minimal adds the existing one-sentence instruction; full
receives the pinned catalog and onboarding procedure, with adoption records
confined to the permitted directory. This tests that entire prompted package.
Baseline workspaces contain no catalog files. Filesystem separation does not
prove access isolation. Detected contamination blocks inference.

A completed, fully captured task passes only if **every frozen objective check is
true**. Missing deliverables fail. Missing operational capture is unknown and
halts dependent execution. The declaration requires a boolean artifact status,
one required-check status, and one external-effect status. It must match the
actual requested outcome. `structured_false_completion` counts an affirmative
artifact declaration when an objective core check did not pass. This narrow
metric does not assess all claims in prose, all instruction-following behavior,
or artifact usefulness. Simulated-service logs and string-based process checks
are observable proxies, not a security boundary against a malicious participant.

## Frozen sampling and decisions

- Model: `gpt-6-astra`, reasoning `high`, native desktop projectless chats only.
- Seed: `20261001`. Draw 128 task IDs uniformly **with replacement** from the
  eight fixtures; independently shuffle the three condition orders per block.
- Planned cumulative looks: 64 blocks / 192 chats, then 128 blocks / 384 chats.
  Fresh workspaces, no replacement attempts, zero evaluator chats.
- Primary endpoint: paired difference in pass probability, full minus bare and
  full minus minimal. Practical margin: **10 percentage points**.
- For each contrast, count paired wins and losses. Bound each probability by
  exact binomial CDF inversion, then subtract bounds:
  `[lower(win) - upper(loss), upper(win) - lower(loss)]`.
- Use `0.05 / 32` per tail: two contrasts × two looks × (four quality tails +
  two native-time overhead tails + two total-token overhead tails). A union bound
  gives at least 95% simultaneous coverage under the sampling assumptions.
- Classify superiority if the quality interval lies above +0.10, inferiority if
  below -0.10, practical equivalence if entirely within [-0.10,+0.10], otherwise
  unresolved. Stop at a planned look only when **both** contrasts are classified.
  At the second look, report unresolved findings honestly. Do not change the
  margin, endpoint, or sample maximum after observing results.
- Secondary overhead: exact bounds for the probability that full consumes more
  than 1.2 times baseline native elapsed time or total input-plus-output tokens.
  A lower bound above 0.5 establishes overhead for a majority of these draws.
  Missing usage remains unknown; tokens are not monetary cost.

The exact binomial bounds follow the conservative Clopper–Pearson construction
[documented by statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html).
The subtraction and multiple-tail allocation are this experiment's conservative
construction. They assume independent stationary draws from this finite task
mixture. Repeated fixtures, temporal dependence, model nondeterminism and native
instruction variants limit that interpretation. All assigned variants remain in
the analysis; inspect their condition distribution. App/runtime/model/tool or
permission drift halts dispatch. There is no inference to a population of new
tasks, and equivalence within 10 points is not proof of identical performance.
Objective task-specific checks follow
[OpenAI's evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices),
but these automated checks have no independent human validation.

## Execution and recovery

```sh
./scripts/desktop_eval.py --experiment build/evals/NEW prepare \
  --catalog-ref COMMIT --app-version 'OBSERVED VERSION (BUILD)' --confirmatory
```

Inspect the frozen config, manifest, fixtures, source hashes and app version.
Record actual preflight evidence in `preflight.json`. For each manifest row:

1. `stage RUN /absolute/separate/workspace`, then `reserve RUN task`.
2. Create the native desktop chat with the exact prompt and frozen model/effort.
   Immediately persist its receipt and `transition RUN task started --receipt FILE`.
3. Monitor with native desktop tools. Deliver the one frozen `oracle RUN` response
   only after the task requests the missing date. Preserve its native delivery.
4. When cessation is observed, record `transition RUN task completed --receipt FILE`.
5. `collect RUN SESSION_JSONL`, then `objective-score RUN`.
6. After the first three runs, `qualify`; continue only when capture and scoring
   are usable. Qualification does not require successful task outcomes.
7. At each planned look, `report`. The reservation guard enforces the stopping
   decision before starting the next stage.

`objective-score` can recover an identical score file written before its ledger
receipt; it never overwrites a different result. A reserved chat without a receipt
requires native-state reconciliation before any further dispatch. Other capture,
configuration and ledger errors halt. Diagnose and preserve failed setups before
any explicitly distinct corrected experiment; never pool incompatible revisions.
No runtime cancellation, scheduled automation, CLI model invocation or API model
invocation is provided. Thresholds are reported after completion. Account limits
halt new dispatch. Raw logs remain ignored and private; public reports contain
aggregate results, sanitized checks and references. The coordinator must remain
active. Statistical conclusiveness is a possible outcome, not a guarantee.

Run `./scripts/test_desktop_eval_objective.py` and
`./scripts/check_catalog.py --github` before publication or live dispatch.
