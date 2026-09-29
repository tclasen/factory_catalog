---
type: Control
title: "Qualified artifact promotion"
description: "Verify that the published object is the artifact whose acceptance evidence was qualified."
status: stable
family: release-and-external-action
sources:
  - id: software-factory
    resource: https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/artifact-promotion.md
    title: "Software Factory: Qualified artifact promotion basis"
---

# Qualified artifact promotion

[Controls](./) · [Adoption](../adoption.md) · [Families](../control-families.md)

## Purpose and applicability

Apply when publishing a package, document set, model artifact, or other deliverable, or promoting it between environments. Prevent qualification of one object from being used to justify delivery of another.

## Requirement

Bind acceptance evidence to an immutable candidate identity and relevant build inputs. Promote that object through the authorized delivery path and verify the actual destination object before claiming delivery. Version environment configuration separately and verify compatibility. Rebuilding, substitution, or a relevant configuration change creates a changed candidate/context requiring affected qualification. A matching branch name or successful upload is insufficient.

## Implementation

1. Assign a release owner and define the complete artifact boundary, including attachments, manifests, and required files.
2. Record source revision, build inputs, artifact digest or complete file inventory, configuration identity, and acceptance evidence.
3. Use the qualified object for promotion. If packaging transforms it, qualify and identify the final distributable representation before release.
4. Inspect the installed/downloaded object at the destination. Compare digests or the complete file set and contents, including unexpected additions.
5. Block completion on mismatch; quarantine or recover within existing authority. Keep unresolved destination observations visible.

## Expected outcome and assessment

Expected outcome: every claimed delivery matches a qualified artifact and compatible configuration.

Test a matching object, changed file, missing file, extra file, different rebuild, incompatible configuration, and successful upload with unavailable destination verification. Include every alternate authorized publication path.

- **Pass:** the matching object completes verification; every mismatch or unknown destination prevents a delivery claim and triggers the documented disposition; changed candidates obtain affected qualification before promotion.
- **Fail:** upload success substitutes for identity verification, a mismatched object is declared qualified, or an alternate path bypasses the check. Any other unmet mandatory requirement is also a failure; missing evidence cannot override an observed failure.
- **Inconclusive:** candidate/destination identity or compatibility cannot be inspected.
- **Evidence:** build and manifest identities, qualified results, destination observations, configuration checks, mismatch dispositions, release owner, and time.

## Dependencies and limitations

Use [assessment evidence validity](assessment-evidence-validity.md) for qualification reuse and [bounded external action](bounded-external-action.md) for publication authority. Requires trustworthy build and destination inspection. Matching bytes do not establish runtime correctness or beneficiary outcomes; [outcome verification](outcome-verification.md) remains separate. Confidential artifacts need protected evidence access.

## Source and adoption

This catalog requirement is adapted from Software Factory guidance.[^software-factory] Its assessment cases are proposed catalog procedures, not reported operational results. Before adoption by reference or copying, retain this identity, catalog version, and the exact published catalog commit URL; pin cross-control references to that same revision using the [adoption procedure](../adoption.md#record-the-adoption).

[^software-factory]: [Pinned Software Factory source](https://github.com/tclasen/software-factory/blob/0a429827a595712ce1fa3069528565c72da2a549/skills/software-factory/references/artifact-promotion.md).
