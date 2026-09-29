---
type: Control
title: "Protected acceptance"
description: "Keep consequential acceptance criteria and evaluation outside the producer’s effective write authority."
catalog_version: "v0.1.0"
status: stable
family: quality-and-validation
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/independent-acceptance.md
    title: "Software Factory: Protected acceptance basis"
---

# Protected acceptance

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

**Identity:** `controls/protected-acceptance` · **Catalog:** v0.1.0 · **Family:** `quality-and-validation`

## Purpose and applicability

Apply when the host requires independent acceptance or when changes affect money movement, authority across a trust boundary, or irreversible acknowledged data. Scope protection to the affected behavior. The purpose is to prevent a producer from approving its own incorrect work by altering the acceptance mechanism.

## Requirement

Protect canonical criteria, expected results, fixtures, evaluator code, and acceptance records from the implementing actor's effective write authority. Evaluate candidate behavior without exposing evaluator credentials to candidate code. Only the authorized acceptance owner may change the protected criteria, and such changes invalidate affected results. A second reviewer or agent with the same mutable acceptance assets does not establish this boundary.

## Implementation

1. Inventory producer identities, tools, credentials, evaluator inputs, and every route that can change or replace them.
2. Assign a separate acceptance owner. Use a protected CI job, service identity, or host-enforced equivalent; document the actual permissions and bypass paths.
3. Run candidate code in an isolated environment without evaluator secrets. Compare observed output against expected results held on the evaluator side.
4. Bind the evaluator and fixture identities to the assessed candidate. Authenticate records from the trusted evaluation path.
5. Handle legitimate criterion changes through the acceptance owner's existing authority and rerun affected checks.

## Expected outcome and assessment

Expected outcome: producer-controlled changes cannot cause wrong work to earn protected acceptance.

From the producer's actual execution identity, attempt fixture edits, evaluator replacement, forged verdict submission, credential access, and alternate-path bypasses in an authorized test environment. Test a valid alternative implementation and a wrong candidate whose own tests have been weakened. Exercise an authorized criterion update separately.

- **Pass:** valid work passes; wrong work fails despite weakened local tests; all unauthorized alterations and forged verdicts are rejected; authorized updates invalidate affected results and are reassessed.
- **Fail:** producer-controlled changes alter protected acceptance, a false verdict is accepted, or required isolation is bypassed. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** an effective permission or execution path cannot be inspected or tested.
- **Evidence:** boundary inventory, permission revisions, producer/evaluator identities, attempted alterations, observed effects, candidate/fixture/evaluator revisions, and owner update records.

## Dependencies and limitations

Requires enforceable permissions and trustworthy evaluation infrastructure. A worktree or directory name is not a security boundary. Use [verifier qualification](verifier-qualification.md) to test correctness: protection cannot make a wrong evaluator accurate. [Bounded external action](bounded-external-action.md) separately governs execution authority. Human judgment may remain necessary for properties that cannot be reliably automated.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/independent-acceptance.md).
