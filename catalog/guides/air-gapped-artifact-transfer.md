---
type: Guide
title: "Transfer artifacts across an air gap"
description: "Package, admit, requalify, and trace artifacts transferred between low-side and air-gapped factories."
status: draft
tags: [air-gap, security, auditability]
---

# Transfer artifacts across an air gap

## Scope and authority

This proposed procedure collects the shared transfer design used by the fictional [software](../factories/government-air-gapped-software.md) and [data science](../factories/government-air-gapped-data-science.md) factories. It applies existing controls to their handoff; it adds no control requirements and reports no operational assessment or certification. The examples retain their domain checks, owners, and integrated assessment fixtures.

Before use, the customer supplies handling rules, transfer channels, trust/key administration, model and dependency admission policy, required reviewers, and evidence retention. “Low side” means approved for the lower-sensitivity work, not unrestricted processing. Use [approved data processing](../controls/approved-data-processing.md) to establish permitted inputs, models, environments, and evidence destinations. Record selected controls through the [adoption procedure](../adoption.md#record-the-adoption).

## Package and admit

1. **Prepare offline continuation.** Assemble approved source material, execution instructions, and the complete dependency set, including required libraries, models, tools, and data snapshots. The receiving factory uses local resources without external inference, telemetry, downloads, or remote rendering. Missing dependencies do not justify a temporary external connection.
2. **Identify and qualify the package.** Record every file, digest, origin, handling label, package identity, relevant configuration, check results, and transfer destination. Preserve source-use permissions. Apply [qualified artifact promotion](../controls/qualified-artifact-promotion.md): qualify the final distributable representation after any packaging transformation. Missing tools, skipped required checks, or security evidence outside the agreed freshness policy block the affected stage.
3. **Authorize and retain custody.** Under [bounded external action](../controls/bounded-external-action.md), the transfer owner authorizes the exact package and destination separately from technical qualification. The custodian uses the customer-approved media or file-transfer procedure and retains custody events and media identity.
4. **Quarantine and inspect.** The receiving service verifies authorization, signatures against locally trusted keys, the complete inventory and hashes, and destination identity. It records content and malware inspection tools, versions, and freshness, and admits only allowed files. Mismatches, unknown handling status, or uncertain destination identity block admission. Hash equality proves correspondence to the manifest, not benign behavior.
5. **Establish execution scope.** Admission does not automatically execute imported scripts, notebooks, model files, or agent instructions. Treat source documents and executable content as untrusted, disable active remote resources during preview, and inspect executable content before authorized execution. Use [execution isolation](../controls/execution-isolation.md) to mediate state import and enforce the permitted workload scope.

## Continue and requalify internally

The receiving factory rebuilds or reruns with admitted tools and dependencies. Repeat the applicable [local quality gates](../controls/local-quality-gates.md) against internal fixtures. Changed code, data, models, or relevant configuration create a new candidate/context requiring affected qualification; a low-side pass does not establish internal acceptance. Keep [protected acceptance](../controls/protected-acceptance.md) separate from production, retain a verdict for the internal candidate, and verify the actual delivered artifact. The examples specify the sensitive software tests and analytical fusion checks for their respective work.

## Preserve audit continuity

Apply [security event traceability](../controls/security-event-traceability.md) and [evidence traceability](../controls/evidence-traceability.md) to connect the original work revision, package, custody, admission, internal changes and runs, verdict, and destination observations. Retain actor/service and grant identities, policy/configuration revisions, model/tool versions, actions, deterministic results, and exception dispositions. Preserve permitted prompts and outputs only when needed under handling policy; private model reasoning is not required.

Evidence stays in approved storage on its originating side; include only approved evidence in the inbound package. The internal record links the stages without exporting sensitive records or connecting a shared external audit service. Use opaque identifiers where descriptive metadata is sensitive. Protect records from producer alteration; define retention, authorized auditor access, causal ordering when clocks differ, and an owner for missing records. In these proposed designs, required logging failure stops transfer, acceptance, and delivery until continuity is restored and affected work is reassessed. Inspect receiving state before retrying a transfer with a missing acknowledgement, and keep completion unresolved until reconciled.

## Separately authorize return transfers

There is no automatic return path. Apply [sensitive data egress](../controls/sensitive-data-egress.md) to the exact outbound payload, audience, and destination, including derived data and removable media. Follow-up work on the low side begins with separately approved material in a fresh context. Removing identifiers or aggregating data does not by itself authorize disclosure. Handle returning media under the customer's rules before reuse; the device itself can be a disclosure route. Each example identifies its domain-specific protected outputs.

## Assessment boundary

Run the selected controls' assessments and the examples' integrated fixtures before claiming effectiveness. The fixtures exercise changed/missing/extra files, custody gaps, prohibited disclosure, internal changes, and legitimate transfers alongside domain failures. Record observed effects and unresolved evidence: failed requirements fail the relevant assessment, while unavailable observations are inconclusive. Passing local documentation checks does not establish secure operation, analytical validity, customer outcomes, or contractual compliance.
