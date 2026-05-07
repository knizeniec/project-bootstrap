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

## Canonical Doc Creation

- When a user asks to create a canonical document, first identify the requested doc type and owning area by checking `docs/00-source-of-truth.md`, `docs/INDEX.md`, the relevant numbered-area `README.md`, and available `*_TEMPLATE.md` files.
- If the user already named the canonical doc type, do not re-decide it. Map that request to the correct canonical area and template.
- Before naming the new file, ask only the minimum kickoff questions needed to create a usable first draft: what the document is about, what scope it covers, and what context-specific title or subject it should use.
- If a matching template exists, copy it into the owning canonical area and rename it to fit the user context.
- If no matching template exists and the document type is reusable, create a new `*_TEMPLATE.md` file in the correct numbered area first, following neighboring template patterns, then create the requested document from that template.
- Keep `docs/adr/` as the only exception to root numbered-area ownership. New ADRs should start from `docs/adr/ADR-000-template.md` and follow `docs/adr/README.md`.
- After creating the file, continue consulting the user to fill it section by section. Aim for a first useful version, not a perfect final version.
- Ask focused follow-up questions that replace the most important placeholders first: summary, scope, goals or decision, constraints or drivers, dependencies or risks, approvals or owners, and related documents.
- Accept partial answers. When information is still unknown, record it explicitly as an assumption, open question, or follow-up item instead of blocking the draft.
- When adding a new reusable canonical template, update the owning area landing page plus `docs/README.md`, `docs/INDEX.md`, and `docs/00-source-of-truth.md` in the same change.

## Information Architecture

- Organize docs by reader need: tutorial, how-to, reference, explanation.
- Prefer links to source files, ADRs, and canonical docs over repeated prose.
- Keep docs consistent with actual behavior and constraints.
- Treat root `docs/` as the canonical source-of-truth tree.
- Treat `docs/adr/` as ADR-only support space.

## Local Routing

- Read `docs/adr/AGENTS.md` before editing `docs/adr/**`.
- Read `docs/superpowers/AGENTS.md` before editing `docs/superpowers/**`.
