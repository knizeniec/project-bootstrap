---
name: Superpowers Planning Records
description: Use for work under docs/superpowers/. Covers specs, plans, and historical implementation records.
applyTo: "docs/superpowers/**"
---

# Superpowers Planning Records

This directory stores planning artifacts for agent-driven work.

## Most Important Rules

- Use `docs/adr/` as the primary context for brainstorming and planning.
- Store specs in `docs/superpowers/specs/` and plans in `docs/superpowers/plans/`.
- Treat completed spec and plan files as historical records; create new dated files for later changes instead of rewriting completed ones.
- Keep canonical project rules in root `docs/`, not here.

## Workflow

- Keep planning artifacts concrete, implementation-focused, and easy to execute.
- Match spec and plan scope to a single coherent unit of work.
- Preserve links back to ADRs and other canonical source-of-truth docs in root `docs/`.

## Editing Guidance

- Update only the files relevant to the current task.
- Keep entries concise and specific.
- Do not move source-of-truth decisions from `docs/adr/` into these historical records.
