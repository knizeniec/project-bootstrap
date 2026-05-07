# Documentation Architecture

Status: Active
Owner: Documentation maintainers
Purpose: define the structure of the active documentation system and the role of each documentation surface
Last updated: 2026-05-06

This repository keeps one active documentation system rooted under `docs/`. Canonical content lives in the control spine plus the numbered areas from `00_governance/` through `08_references/`.

`docs/adr/` stores durable architecture decisions. `superpowers/` stores working history. `99_archive/` stores evidence and retired material.

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
|- adr/
`- superpowers/
```

## Document classes

| Class | Surface | Role |
|---|---|---|
| Control spine | [README.md](README.md), [Architecture.md](Architecture.md), [00-documentation-standards.md](00-documentation-standards.md), [00-source-of-truth.md](00-source-of-truth.md), [INDEX.md](INDEX.md) | Entry, structure, standards, ownership, and navigation for the active docs system. |
| Active domain docs | [00_governance/](00_governance/README.md) through [08_references/](08_references/README.md) | Canonical documentation by domain. |
| Starter templates | Named `_TEMPLATE.md` files in canonical areas | Reusable project bootstrap surfaces for governance, product, architecture, and delivery documentation. |
| ADRs | [adr/](adr/README.md) | Durable implementation and architecture decisions. |
| Working history | [superpowers/](superpowers/README.md) | Specs, plans, and other tracked work records that do not define the active baseline. |
| Archive/evidence | [99_archive/](99_archive/README.md) | Historical evidence and retired material kept for traceability only. |

## Anchoring

The numbered domain folders (`00_governance/` through `08_references/` plus `99_archive/`) are a custom convention chosen for this template. They are not a one-to-one mapping to a published standard.

Adopters who must align with arc42 can map the folders as follows:

| Folder | arc42 alignment |
|---|---|
| `00_governance/` | Quality goals, stakeholders, constraints (arc42 §1, §2) |
| `01_strategy/` | Strategic context (arc42 §1) |
| `02_product/` | Requirements and quality goals (arc42 §1, §10 quality scenarios) |
| `03_architecture/` | Solution strategy, building blocks, runtime, deployment, crosscutting (arc42 §4-§8) |
| `04_ai_governance/` | Quality requirements and risks specific to AI (arc42 §10, §11) |
| `05_testing_acceptance/` | Quality scenarios and verification evidence (arc42 §10) |
| `06_security_operations/` | Crosscutting concepts and runtime view for operations (arc42 §8, §6) |
| `07_delivery/` | Deployment view and risk/technical debt (arc42 §7, §11) |
| `08_references/` | Glossary and external references (arc42 §12) |
| `adr/` | Architecture decisions (arc42 §9) |

Adopters who prefer to keep this template's numbered taxonomy without arc42 alignment can ignore the table above.

## Change rules

- If the documentation structure changes, update [README.md](README.md), [Architecture.md](Architecture.md), [00-documentation-standards.md](00-documentation-standards.md), [00-source-of-truth.md](00-source-of-truth.md), and [INDEX.md](INDEX.md) together.
- If canonical ownership changes, update [00-source-of-truth.md](00-source-of-truth.md) in the same patch.
- If a durable implementation decision changes, update the relevant ADR in [adr/](adr/README.md).
- If archive or working-history handling changes, update the matching README in [99_archive/](99_archive/README.md) or [superpowers/](superpowers/README.md).
