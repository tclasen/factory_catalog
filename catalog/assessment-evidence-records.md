---
type: Guide
title: "Assessment evidence records"
description: "Record an assessment’s target, method, observations, limits, and conditions for reuse."
catalog_version: "v0.1.0"
status: stable
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/verification.md
    title: "Software Factory: Assessment evidence records basis"
---

# Assessment evidence records

[Catalog](index.md) · [Ontology](ontology.md) · [Adoption](adoption.md)

## Use

Use an existing issue, report, or evidence store to implement [assessment evidence validity](controls/assessment-evidence-validity.md) and support [evidence traceability](controls/evidence-traceability.md). One record can cover related checks if each result remains attributable to its inputs. Separate artifact acceptance, control assessment, and beneficiary outcome claims.

## Suggested record

| Field | Content |
|---|---|
| Identity and owner | Record ID/revision, accountable owner, assessor identity and role, observation time with timezone |
| Target and scope | Artifact/implementation identity, immutable revision or digest, environment, included and excluded behaviors |
| Adoption | Control identity, catalog version, exact catalog commit, pinned source URL, and local adaptations for each adopted control |
| Criteria | Accepted criterion revisions, thresholds, mandatory gates, and disposition for failure or absent evidence |
| Method | Executable command or review procedure, evaluator version, fixture identity, configuration and relevant dependencies |
| Observations | Raw output or protected references, contrary evidence, execution times, and observed effects |
| Execution state | Passed, failed, blocked, or unrun for each check, with reasons; these describe checks, not the whole control assessment |
| Assessment result | `not-assessed`, `pass`, `fail`, or `inconclusive`, with explicit criterion-to-observation reasoning |
| Validity | Bound inputs, dependency map, freshness conditions, changes that reopen checks, and decision on proposed reuse |
| Follow-up | Outstanding gates, remediation, owner and review trigger; source access and retention restrictions |

## Procedure

1. Record target and criteria before running checks. Select normal, boundary, denied, and recovery cases where relevant.
2. Capture observations with their actual input identities; distinguish reports by the producer from independently observed evidence.
3. Compare observations with criteria and preserve failures. A blocked check cannot supply passing evidence; a control may nevertheless pass a test that requires it to detect and report a blocked outcome.
4. Before reuse, apply [assessment evidence validity](controls/assessment-evidence-validity.md). Preserve the original result and explain invalidation rather than rewriting history.
5. For consequential acceptance, link the boundary evidence for [protected acceptance](controls/protected-acceptance.md) and qualification evidence for the [verifier](controls/verifier-qualification.md).

## Illustrative record fragment

A report-export check passed for candidate A and fixture F. Candidate B changes authorization logic. The A result remains a historical observation, but cannot close B's authorization gate. Record that gate as unrun until the affected checks execute. A passing style check on B does not replace it.

## Review the record

A reviewer should be able to locate the exact assessed object, reproduce or inspect the method, resolve each material claim to observations, and explain whether the result applies now. Missing evidence yields an explicit gap. Avoid storing credentials, unnecessary personal data, or unrestricted copies of sensitive fixtures.

## Source and scope

Adapted from the pinned Software Factory procedure.[^software-factory] The tables are suggested local record fields, not new required OKF frontmatter. Store actual records with their owning project and appropriate access and retention controls. A populated record is not evidence that its claimed observations are true. No operational assessment is asserted here.

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/policies/verification.md).
