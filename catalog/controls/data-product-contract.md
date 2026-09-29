---
type: Control
title: "Data product contract"
description: "Agree and check the meaning and delivery conditions of a shared data product."
status: draft
tags: [data-mesh, data-stewardship]
family: intake-and-work-definition
sources:
  - id: odcs
    resource: https://bitol-io.github.io/open-data-contract-standard/latest/
    title: "Open Data Contract Standard"
---

# Data product contract

[Adoption](../adoption.md) · [Data product design](../guides/data-product-design.md)

## Purpose and applicability

Apply to shared files, tables, APIs, streams, statistical releases, or research collections. ODCS provides sections for schema, quality, support, roles, and service agreements.[^odcs]

## Requirement

Before a consumer relies on a product, producer and consumer representatives must agree a versioned contract covering identity, intended use, semantics, access method, quality and delivery expectations, restrictions, change notice, and support. Bind the contract to the served revision and define acceptance checks. A missing or violated required term prevents acceptance for that use.

## Implementation

1. Define what one record represents, keys, units, time basis, inclusion rules, null meanings, refresh behavior, and permitted uses. State unknowns rather than leaving ambiguous blanks.
2. Choose a documented contract format and pin its version. Separate structural validation from checks of actual values and business meaning.
3. Create representative valid and invalid examples with consumer input. Retain the approved contract, checks, exceptions, and release identity.
4. Run checks at publication and relevant ingestion boundaries; route failures to the owner. Changes to meaning require review even when column names and types are unchanged.

Mechanism: documented human procedure, automated checks, or technical restrictions as specified by the local implementation. Record the owner, scope, parameters, and bypass paths before assessment.

## Expected outcome and assessment

Inspect the implementation against every requirement in its declared scope, then run the cases below. A passing fixture alone does not establish operational coverage.

Expected outcome: Consumers can identify the applicable contract and reject products that violate required terms before relying on them.

Use a declared producer-consumer pair. Accept a conforming sample. Supply a missing required field, a changed unit with the same numeric type, and a contract describing a different served revision. Each must be detected and withheld from acceptance.

- **Pass:** the scoped implementation meets the requirement, and the conforming case is usable and each negative case is withheld with a specific failed term.
- **Fail:** a requirement is violated; in particular, a negative case is accepted or the published contract cannot be tied to the served revision.
- **Inconclusive:** required evidence or a necessary assessment case cannot be inspected or completed; do not treat this as a pass.
- **Evidence:** contract and product revisions, party acceptance, fixtures, check results, failure dispositions, and declared coverage.

## Dependencies and limitations

Requires [accountable ownership](data-product-accountability.md). Use [semantic interoperability](data-semantic-interoperability.md) for joins and [service objectives](data-product-service-objectives.md) for ongoing performance. A contract is not an access grant or proof of truthful source data. Adopt using the exact source revision under the [adoption procedure](../adoption.md#record-the-adoption). These are proposed assessment procedures, not executed results.

## Source notes

Sources inspected on 2026-09-28. Requirements and assessment cases are catalog proposals; no operational effectiveness is asserted.

[^odcs]: [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/).
