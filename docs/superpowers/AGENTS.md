---
name: Superpowers Planning Records
description: Use for work under docs/superpowers/. Covers historical planning-record storage and routing.
applyTo: "docs/superpowers/**"
---

# Superpowers Planning Records

> **Purpose**: route work in `docs/superpowers/` and keep specs and plans in the historical record lane.
> **Audience**: agents and contributors editing planning records under `docs/superpowers/`.
> **When to update**: update when planning-record storage rules or routing expectations change.

This directory stores planning artifacts for agent-driven work.

## Most important rules

- Use [docs/adr/](../adr/README.md) as the primary context for brainstorming and planning.
- Store specs in `docs/superpowers/specs/` and plans in `docs/superpowers/plans/`.
- Treat completed spec and plan files as historical records; create new dated files for later changes instead of rewriting completed ones.
- Keep canonical project rules in root `docs/`, not here.

## Workflow

- Keep planning artifacts concrete, implementation-focused, and easy to execute.
- Match spec and plan scope to a single coherent unit of work.
- Preserve links back to ADRs and other canonical source-of-truth docs in root `docs/`.

## Editing guidance

- Update only the files relevant to the current task.
- Keep entries concise and specific.
- Do not move source-of-truth decisions from [docs/adr/](../adr/README.md) into these historical records.

## Related documents

- [README.md](README.md) — policy for the `docs/superpowers/` area.
- [../00-source-of-truth.md](../00-source-of-truth.md) — canonical ownership map.
- [../adr/README.md](../adr/README.md) — durable implementation decisions.
- [../AGENTS.md](../AGENTS.md) — parent routing rules for the whole docs tree.
