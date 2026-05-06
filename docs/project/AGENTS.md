---
name: Project Source of Truth Docs
description: Use for work under docs/project/. Covers ADRs, governance docs, template structure rules, and architecture ownership.
applyTo: "docs/project/**"
---

# Project Source Of Truth Docs

This directory holds active project documentation and architecture decisions.

## Most Important Rules

- Treat `docs/project/adr/` as the primary source of truth for implementation decisions.
- Update ADRs before implementation when a decision changes.
- Do not create new active source-of-truth roots outside the approved `docs/project/` structure.

## Required Structure

- Keep required entrypoints present: `Architecture.md`, `00-documentation-standards.md`, `00-source-of-truth.md`, `INDEX.md`.
- Keep ADR canonical files in `docs/project/adr/`.
- Active ownership roots are limited to `00_governance/`, `01_strategy/`, `02_product/`, `03_architecture/`, `04_ai_governance/`, `05_testing_acceptance/`, `06_security_operations/`, `07_delivery/`, and `08_references/`.
- `99_archive/` is supporting-only, not an active owner.

## Template And Governance Rules

- For template work, keep mandatory root structure and baseline files aligned with the repository contract.
- `README.md` must stay a concise overview; the directory tree lives in `REPOSTORY_MAP.md`.
- Keep governance, branch-management, changelog, security, and documentation standards aligned with actual repo behavior.

## Quality Rules

- Keep guidance concise and executable.
- Preserve traceability across requirements, decisions, tests, and controls.
- Do not restate broad repo rules already covered by root or parent `AGENTS.md` files.
