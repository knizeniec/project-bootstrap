# Documentation Architecture

Status: Active
Owner: [Role or team responsible for documentation]
Purpose: define the structure of the active documentation system and the role of each documentation surface
Last updated: YYYY-MM-DD

This repository keeps one active documentation system rooted under `docs/`. Canonical content lives in the control spine plus the numbered areas from `00_governance/` through `08_references/`.

`docs/project/adr/` stores durable architecture decisions. `superpowers/` stores working history. `99_archive/` stores evidence and retired material.

## Active model

```text
docs/
|- README.md
|- Architecture.md
|- 00-documentation-standards.md
|- 00-source-of-truth.md
|- INDEX.md
|- 00_governance/
|- 01_strategy/
|- 02_product/
|- 03_architecture/
|- 04_ai_governance/
|- 05_testing_acceptance/
|- 06_security_operations/
|- 07_delivery/
|- 08_references/
|- 99_archive/
|- project/
|  `- adr/
`- superpowers/
```

## Document classes

| Class | Surface | Role |
|---|---|---|
| Control spine | [README.md](README.md), [Architecture.md](Architecture.md), [00-documentation-standards.md](00-documentation-standards.md), [00-source-of-truth.md](00-source-of-truth.md), [INDEX.md](INDEX.md) | Entry, structure, standards, ownership, and navigation for the active docs system. |
| Active domain docs | [00_governance/](00_governance/README.md) through [08_references/](08_references/README.md) | Canonical documentation by domain. |
| Starter templates | Named `_TEMPLATE.md` files in canonical areas | Reusable project bootstrap surfaces for governance, product, architecture, and delivery documentation. |
| ADRs | [project/adr/](project/adr/README.md) | Durable implementation and architecture decisions. |
| Working history | [superpowers/](superpowers/README.md) | Specs, plans, and other tracked work records that do not define the active baseline. |
| Archive/evidence | [99_archive/](99_archive/README.md) | Historical evidence and retired material kept for traceability only. |

## Change rules

- If the documentation structure changes, update [README.md](README.md), [Architecture.md](Architecture.md), [00-documentation-standards.md](00-documentation-standards.md), [00-source-of-truth.md](00-source-of-truth.md), and [INDEX.md](INDEX.md) together.
- If canonical ownership changes, update [00-source-of-truth.md](00-source-of-truth.md) in the same patch.
- If a durable implementation decision changes, update the relevant ADR in [project/adr/](project/adr/README.md).
- If archive or working-history handling changes, update the matching README in [99_archive/](99_archive/README.md) or [superpowers/](superpowers/README.md).
