---
type: Guide
title: "Lessons from Software Factory"
description: "Apply source-backed lessons about scope, evidence, recovery, and process improvement to knowledge-work factories."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: overview
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/README.md
    title: "Software Factory overview"
  - id: planning
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/planning.md
    title: "Requirements and planning"
  - id: governance
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/governance.md
    title: "Scope, authority and security"
  - id: verification
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/verification.md
    title: "Verification and review"
  - id: acceptance
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/independent-acceptance.md
    title: "Protected independent acceptance"
  - id: verifiers
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verifiers.md
    title: "Verifier quality"
  - id: promotion
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/artifact-promotion.md
    title: "Promote the qualified artifact"
  - id: resumption
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/durable-resumption.md
    title: "Durable resumption"
  - id: context
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/progressive-disclosure.md
    title: "Select the context needed for the next action"
  - id: measurement
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/measurement.md
    title: "Measure a factory experiment"
  - id: instructions
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/instructions.md
    title: "Maintain instructions from observed evidence"
  - id: validation
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/docs/validation.md
    title: "Validation record"
  - id: routing-trial
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/evaluations/results/sf-r040-trial1.json
    title: "SF-R040 trial record"
  - id: selective-trial
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/evaluations/results/sf-r048-selective-reading.json
    title: "SF-048 selective-reading trial record"
---

# Lessons from Software Factory

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md) · [Software delivery example](factories/software-delivery.md)

## Source and scope

This guide synthesizes selected guidance from `tclasen/software-factory` at commit `0a429827a595712ce1fa3069528565c72da2a549`, inspected on 2026-09-28. The source is a demonstration instruction package.[^overview] Its reported evaluations concern particular fixtures and package identities; they are not assessments of this catalog's controls. We inspected the guidance and cited records, without rerunning its agent trials.[^validation]

The applications below are catalog interpretations of that guidance. They use the existing ontology, families, and three controls. Additional mechanisms remain proposals for local design or future catalog controls; linking them does not establish adoption or permission.

## Lessons and applications

### 1. Bind reusable guidance to the local decision

The source separates reusable procedures from project scope, acceptance criteria, and authority. It sizes planning to the next useful increment and treats missing permission as a block on the dependent action.[^planning][^governance]

**Apply:** In the [factory description](adoption.md#describe-the-factory), connect each activity to its outcome, accountable actor, constraints, and authority. Keep local settings in the implementation record. A copied procedure or available credential does not expand a grant. [Bounded external action](controls/bounded-external-action.md) supplies the existing requirement for enforcing external authority; instructions alone cannot implement it.

### 2. Verify the beneficiary's observable result

Verification is selected from accepted outcomes, affected boundaries, and consequences. The source distinguishes failed, blocked, and unrun checks and requires evidence to match the candidate and relevant configuration.[^verification]

**Apply:** Use [outcome verification](controls/outcome-verification.md) to separate an artifact's acceptance from the intended benefit. For an export feature, producing a file is artifact behavior; the beneficiary completing the intended reporting task is a separate outcome. Declare the measure and observation period first. A missing required tool leaves the check blocked, not passed. These check execution states are recorded in evidence; they do not replace the catalog's assessment-result vocabulary.

### 3. Test the evaluator and protect consequential acceptance

The source calls for valid alternatives and plausible wrong candidates when qualifying a verifier. Its protected-acceptance profile places criteria and fixtures outside the implementer's effective write scope when consequences or host rules require it. A second agent sharing mutable tests is insufficient.[^verifiers][^acceptance]

**Apply:** Treat the evaluator as a dependency of an assessment. Check both false acceptance and false rejection, including a convincing success report accompanying wrong output. [Evidence traceability](controls/evidence-traceability.md) makes supporting records inspectable; it does not itself enforce evaluator independence. Record the actual protection mechanism and its bypass paths before claiming independence.

### 4. Carry evidence with the artifact it qualifies

The source records immutable artifact identity and build inputs, checks the object actually installed, and reopens affected qualification after a rebuild or relevant configuration change.[^promotion]

**Apply:** Connect an assessment to the artifact revision it evaluated and connect publication to the destination artifact. For documents, compare the approved content and attachments; for software, compare the package digest or complete file set. [Bounded external action](controls/bounded-external-action.md) checks authority and any action-specific approval. Artifact matching is an additional release mechanism, and successful upload alone does not establish it.

### 5. Reconcile uncertain effects before retrying

The source's restart record retains intent, ownership, revisions, obligations, cumulative limits, and external operation identity/status. Resumption checks actual local and recipient state. A saved checkpoint neither restarts an agent nor guarantees a single external effect.[^resumption]

**Apply:** Distinguish a failed request from an unknown effect. After a lost publication response, query the destination before resubmitting. Preserve attempts and limits across handoffs. [Bounded external action](controls/bounded-external-action.md) still governs permission; duplicate prevention and recovery remain separate gaps. If the recipient cannot resolve uncertainty, block the retry and record the missing evidence.

### 6. Retrieve by the next action, retain unfinished obligations

The source uses task triggers and exit conditions to select relevant guidance. Completed procedures become evidence pointers; pending effects, limits, failures, and recovery duties remain visible. Missing required guidance blocks dependent work while other work can continue.[^context]

**Apply:** Scan the catalog's concept files or use its generated complete indexes to select controls based on [context](control-families.md#context-questions-that-change-control-selection). Selection must still discover every applicable requirement. For a routing change, review a routine correction, a consequential migration, a missing reference, and a stage transition. Link reachability demonstrates discoverability, not correct selection or lower context use.

### 7. Improve the process through bounded comparisons

The source preserves baseline and treatment, fixed acceptance criteria, task context, failures, review effort, and resource measurements. It keeps project corrections in their canonical owner and requires authority for shared instruction changes.[^measurement][^instructions]

**Apply:** Use [outcome verification](controls/outcome-verification.md) for improvement claims and [evidence traceability](controls/evidence-traceability.md) for their support. Compare representative tasks under declared limits; keep unknown telemetry explicit. A faster run that fails required acceptance does not establish an improvement. Record a keep, revise, or revert decision and a reconsideration trigger. Generalize a local lesson only after checking whether its assumptions transfer.

## What the source evidence supports

These are reports in the pinned source, not trials performed for this catalog:

| Record | Reported observation | Limit to carry forward |
|---|---|---|
| SF-R040 | Three functional cases passed, but reading beyond metadata violated the selection protocol; the overall trial remained failed.[^routing-trial] | No pure metadata selection or automatic discovery qualification; the record lacks complete audit and exact model/build details. |
| SF-048 | Four explicit-path cases report successful artifact review, including missing-reference handling and resumption.[^selective-trial] | No matched old/new comparison or measured total tokens, cost, or latency; read lists are self-reported, and the recovery fixture only permits queries. |
| SF-048 package identities | The record distinguishes the tested package from a final package containing a later caller-trigger correction.[^selective-trial] | That correction received static review, without repeated behavioral trials; do not transfer every behavioral result to the final package unchanged. |

The transferable lesson is to preserve negative results, protocol deviations, and evidence boundaries alongside successes. Document structure, consistent records, and operational effectiveness require different evidence.

## Candidate controls for discussion

These proposed topics have no assigned control identities or adopted requirements. The order prioritizes false acceptance and unsafe repetition before workflow optimization; adopters should reprioritize for their risks.

| Proposed topic | Existing family | Evidence a future assessment should demand |
|---|---|---|
| Verifier qualification and protected acceptance | Quality and validation | Valid alternatives accepted; plausible wrong outputs rejected; candidate edits cannot alter protected acceptance where required |
| Reconciliation before retry | Reliability and recovery | Lost-response case resolves against recipient state; no duplicate effect; cumulative limits survive interruption |
| Qualified artifact promotion | Release and external action | Destination identity matches the assessed object; substituted or rebuilt artifacts reopen affected checks |
| Guidance selection and evidence invalidation | Knowledge and evidence | Required procedures remain discoverable and selected; changed inputs reopen affected assessments |
| Measured process improvement | Monitoring and improvement | Fixed criteria, comparable baseline, retained failures and costs, explicit adoption/reversion decision |

Discuss scope, identities, measurable requirements, dependencies, and pass/fail criteria before promoting any topic into a control. The [software delivery example](factories/software-delivery.md) exercises the current controls and makes these coverage gaps explicit. The catalog remains v0.1.0; baseline approval is a separate owner decision.

[^overview]: [Software Factory overview](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/README.md).
[^planning]: [Requirements and planning](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/planning.md).
[^governance]: [Scope, authority and security](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/governance.md).
[^verification]: [Verification and review](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/verification.md).
[^acceptance]: [Protected independent acceptance](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/independent-acceptance.md).
[^verifiers]: [Verifier quality](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/verifiers.md).
[^promotion]: [Promote the qualified artifact](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/artifact-promotion.md).
[^resumption]: [Durable resumption](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/durable-resumption.md).
[^context]: [Select the context needed for the next action](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/progressive-disclosure.md).
[^measurement]: [Measure a factory experiment](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/measurement.md).
[^instructions]: [Maintain instructions from observed evidence](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/instructions.md).
[^validation]: [Validation record](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/docs/validation.md).
[^routing-trial]: [SF-R040 trial record](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/evaluations/results/sf-r040-trial1.json).
[^selective-trial]: [SF-048 selective-reading trial record](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/evaluations/results/sf-r048-selective-reading.json).
