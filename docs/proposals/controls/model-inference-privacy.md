---
type: Control
title: "Model inference privacy"
description: "Gate access to models using sensitive training data on scoped privacy and utility assessments."
status: draft
family: information-protection
sources:
  - id: atlas
    resource: https://github.com/mitre-atlas/atlas-data/blob/3259f388d19cbcca11bacf12a0ef97f4198f711b/dist/v6/ATLAS-2026.09.yaml#L2053
    title: "AML.T0024: Exfiltration via AI Inference API"
  - id: membership
    resource: https://arxiv.org/abs/1610.05820v2
    title: "Membership Inference Attacks against Machine Learning Models"
  - id: extraction
    resource: https://arxiv.org/abs/2012.07805v2
    title: "Extracting Training Data from Large Language Models"
---

# Model inference privacy

[Adoption](../../../catalog/adoption.md) · [ATLAS assessment](../../../catalog/atlas-threat-assessment.md)

## Purpose and applicability

Apply when a model trained or adapted on sensitive records is served to callers who are not entitled to those records or their membership in the training set. Include classification scores, embeddings, generated text, and downloadable model artifacts where available. Unknown training provenance is an explicit assessment limitation.

## Requirement

Before exposure, record protected information, permitted callers, model/data revisions, attacker access and query budget, privacy acceptance criteria, utility criteria, and the disposition for missing evidence. Enforce caller access and query/output restrictions outside the model. Assess applicable training-data extraction and membership-inference risks against the declared threat model. Block the assessed release or restrict its audience when a criterion fails or material evidence is missing; repeat affected assessments after model, data, or serving changes.

## Implementation

1. Assign a data owner and a privacy evaluator. Inventory training/fine-tuning data classes, serving routes, confidence outputs, exports, and caller privileges.
2. Choose data minimization, audience restrictions, output reduction, and training/privacy mechanisms appropriate to the risk. Record their assumptions; rate limits and redaction alone do not prove privacy.
3. Predeclare attack families, baselines, repetitions, sample construction, metrics, uncertainty, and thresholds. Use authorized synthetic or controlled records; keep members and nonmembers comparable to avoid trivial distribution cues.
4. Enforce admission, per-caller and aggregate query limits where required, and access revocation. Protect test evidence and prevent evaluation from exposing real sensitive records.
5. Retain the release decision, residual risk, and reassessment triggers. A deployment authority may accept risk separately; it cannot relabel a failed control assessment as passed.

## Expected outcome and assessment

Expected outcome: exposure is limited to callers and configurations with the declared privacy and utility evidence.

Test permitted useful inference, a denied/revoked caller, every supported alternate serving/export route, and exhaustion of configured limits. In an authorized environment, run extraction and membership probes on a controlled fixture; assess attack success/advantage against the predeclared baseline with uncertainty. Use decision fixtures with failed privacy, failed utility, missing provenance, and a changed model after qualification.

- **Pass:** authorized utility meets criteria; access and limit cases behave as required; every applicable privacy criterion meets its declared bound; failed, missing, or stale evidence blocks the affected release.
- **Fail:** prohibited access, a privacy/utility threshold failure, or release despite a known failed or missing required gate.
- **Inconclusive:** insufficient data provenance, attack coverage, sample evidence, or observations to decide. No measured extraction in a small probe is not proof of privacy.
- **Evidence:** data/model/serving identities, access policy, threat model, attack and utility plans, member/nonmember construction, all results and uncertainty, release disposition, evaluator, and time.

## Dependencies and limitations

[Approved data processing](approved-data-processing.md) governs lawful organizational scope and permitted destinations; this control addresses leakage through inference even when callers use the intended interface. [Sensitive data egress](../../../catalog/controls/sensitive-data-egress.md) alone cannot establish resistance to membership inference. Requires specialist evaluation and observable serving boundaries. Empirical tests provide bounded evidence, not a formal privacy guarantee; a claimed formal guarantee needs its own reviewed assumptions and accounting.

ATLAS identifies inference-API exfiltration.[^atlas] Published work demonstrates membership inference and extraction of training examples; their abstracts were inspected for this addition, and experiments were not reproduced.[^membership][^extraction] The requirement and assessment above are catalog proposals.

[^atlas]: Pinned ATLAS 2026.09, AML.T0024; scenario attribution retained from the existing guide.
[^membership]: Shokri et al., Membership Inference Attacks against Machine Learning Models, v2; abstract inspected 2026-09-29.
[^extraction]: Carlini et al., Extracting Training Data from Large Language Models, v2; abstract inspected 2026-09-29.
