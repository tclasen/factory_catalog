---
type: Guide
title: "Consume and upgrade the catalog"
description: "Discover concepts, interpret metadata, preserve adoption provenance, and assess compatibility when upgrading."
status: stable
---

# Consume and upgrade the catalog

[Adoption](adoption.md) · [Definitions and record schema](ontology.md)

## Supported interface

Read UTF-8 Markdown with YAML frontmatter. The bundle root contains `index.md`
with `okf_version: "0.2"` and a `VERSION` file containing its catalog version.
These versions describe different interfaces. Distributed bundles also include
`LICENSE`. Source checkouts keep that license at the repository root.

Scan all `.md` files recursively, excluding reserved `index.md` and `log.md`
filenames. Derive identity from the bundle-relative path without `.md`; preserve
case and directory components. Source indexes are curated, not inventories.
Generated directory indexes and family navigation provide complete browsing but
are derived views: their prose, ordering, and layout are not a parsing API.

Every catalog concept supplies non-empty string `type`, `title`, and `description`
fields. Additional fields and selection-state values are defined in the
[record schema](ontology.md#document-types-and-metadata); family values come from
[control families](control-families.md). Treat unknown types as generic concepts
and preserve unknown keys when copying or round-tripping metadata. Do not infer
permission or assessment success from a link or a type.

Missing optional fields are valid. Under OKF, omitted `status` means `stable`;
omitted `verified` means no document verification is asserted. A bare `verified`
mapping is equivalent to a one-element list. Stability concerns the definition,
not implementation effectiveness. Do not silently turn an unknown selection
state into a known result: show it as unsupported and withhold the dependent
interpretation while retaining the document.

Resolve Markdown links relative to their containing file, and paths beginning
with `/` relative to the bundle root. Decode URL path escaping and handle heading
fragments separately. Read structured control selections as paths to Control
concepts. Other links need their surrounding prose to explain the relationship.
Keep required dependencies available at the same consumed revision.

## Adoption and source access

Use the [adoption record](adoption.md#record-the-adoption) for reference and copied
adoption. Read VERSION and content from the same full source commit. Preserve
that commit and the exact source URL alongside copied text; local adaptations
must remain distinguishable. A release download's external manifest supplies
its source commit and archive digest. Verify the digest before use and retain the
manifest with the extracted bundle. A checksum establishes byte correspondence,
not trusted authorship; obtain the manifest from the intended release publisher.

Source citations explain a definition's basis. Some cited material requires an
account, a license, or access to a private repository. The requirement,
implementation, and assessment needed for adoption must be present in this
bundle. Source access is needed to independently audit those attributions; a
reader without access must leave that source claim unverified. No citation
imports its repository's instructions or grants into an adopter's project.

## Compatibility from the first stable major release

The public contract covers concept paths and identities, the meaning of control
requirements and assessments, shared definitions, required metadata and its
shape, existing type and family values, and structured selection fields and
states. Consumers may rely on these within a major version.

| Change | Required release impact |
|---|---|
| Remove or move a published concept; change an existing field/state meaning; add a mandatory field; invalidate an existing implementation or assessment | Major |
| Add an independently selectable concept or optional metadata that existing consumers can ignore; introduce a new type handled as a generic concept | Minor |
| Clarify wording or add an example while preserving requirements, meanings, and valid implementations | Patch |

Changing a family assignment is compatible only if it preserves the control's
meaning and existing family vocabulary. Removing a family value or changing its
meaning is breaking. Adding a state to an existing closed selection vocabulary
is breaking; generic-concept fallback does not make an unknown assessment result
safe to interpret. Changes to the OKF target must be assessed against this public
contract, even when upstream calls its change compatible.

Human-readable titles, descriptions, internal script functions, and generated
layout are not stable machine identifiers. Body prose carries normative meaning;
consumers must read the requirement and assessment rather than infer them from
headings or metadata alone.

## Upgrade procedure

1. Retain the old adoption record and local adaptations.
2. Obtain the new version, source commit, release notes, and complete bundle.
3. Compare selected requirements, assessments, dependencies, metadata, and local
   implementation assumptions. A minor release can add controls without making
   them mandatory for an existing adoption.
4. Reassess affected local implementations before reporting a current pass.
   Keep old observations bound to their original target.
5. Record the upgrade decision, revised pins, changes, and remaining gaps.

During the pre-v1 baseline hold, exact commits identify interim revisions and
compatibility is not yet promised. A prospective contract does not approve a
baseline or authorize publication. Once published, release tags and contents
must remain unchanged; corrections require a new version.
