---
name: Adoption Prompt Rules
description: Use for work under prompts/. Covers adoption-time prompts that adapt this template to a chosen language stack.
applyTo: "prompts/**"
---

# Adoption Prompt Rules

Apply these rules when editing files under `prompts/`.

## Most Important Rules

- Prompts are tooling-agnostic Markdown that adopters paste into their AI coding tool of choice. Do not couple them to a specific agent or vendor.
- Prompts must be implementation-neutral. They may direct structural and documentation changes, but never generate business logic, feature code, or version-pinned dependencies.
- Prompts may reference only paths that exist in the current tracked tree. Do not reintroduce references to the retired `docs/project/` prefix or to the previously-misspelled repository map filename — both are guarded by CI.

## Structure Rules

- Each prompt is a single self-contained Markdown file at the top of `prompts/`.
- Each prompt opens with YAML frontmatter: `name`, `description`, `argument-hint`, `agent`.
- Each prompt declares mandatory clarification gates that block adaptation until the adopter resolves required inputs.
- Each prompt declares explicit non-goals that prevent scope creep into implementation.

## Quality Rules

- Before committing a prompt change, verify that every directory or file path referenced in the prompt exists in the current tree.
- Bump `Last updated` in [README.md](README.md) when prompt inventory or behavior changes.
- Keep the most important instructions first and avoid duplicating rules that belong in scoped `AGENTS.md` files elsewhere in the repo.

## Routing

- Repo-wide rules live in the root [AGENTS.md](../AGENTS.md).
- Documentation rules live in [docs/AGENTS.md](../docs/AGENTS.md).
- Source-of-truth ownership for this directory is recorded in [docs/00-source-of-truth.md](../docs/00-source-of-truth.md).
