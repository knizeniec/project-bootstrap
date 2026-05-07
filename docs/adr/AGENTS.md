---
name: Project ADR Records
description: Use for work under docs/project/. Covers ADR authoring and durable implementation decision records.
applyTo: "docs/project/**"
---

# Project ADR Records

This directory is reserved for Architecture Decision Records.

## Most Important Rules

- Treat `docs/adr/` as the primary source of truth for implementation decisions.
- Update ADRs before implementation when a decision changes.
- Do not place active root documentation here outside `docs/adr/`.

## Required Structure

- Keep ADR canonical files in `docs/adr/`.
- Keep canonical area docs in root `docs/`.

## Authoring Rules

- Keep ADRs concise, dated, and explicit about the decision, context, and consequences.
- Link ADRs back to canonical root docs when they refine an active area.
- Use the ADR template as the default starting point for new records.

## Quality Rules

- Keep guidance concise and executable.
- Preserve traceability across requirements, decisions, tests, and controls.
- Do not restate broad repo rules already covered by root or parent `AGENTS.md` files.
