---
name: Documentation Rules
description: Use for work under docs/. Covers documentation update discipline and information architecture.
applyTo: "docs/**"
---

# Documentation Rules

Apply these rules when editing anything under `docs/`.

## Priorities

- Keep the canonical source of truth in one place and link instead of duplicating.
- Keep docs concise, actionable, and easy to scan.
- Verify doc claims against code or commands before writing them.

## Update Rules

- Update docs in the same task when behavior, workflows, architecture, or operations change.
- If a file does not need updates, state why in the final response.
- Keep operational runbooks, architecture decisions, and acceptance criteria easy to discover.

## Information Architecture

- Organize docs by reader need: tutorial, how-to, reference, explanation.
- Prefer links to source files, ADRs, and canonical docs over repeated prose.
- Keep docs consistent with actual behavior and constraints.

## Local Routing

- Read `docs/project/AGENTS.md` before editing `docs/project/**`.
- Read `docs/superpowers/AGENTS.md` before editing `docs/superpowers/**`.
