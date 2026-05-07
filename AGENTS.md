---
name: Repository Agent Routing
description: Global instructions for all work in this repository. Keep this file minimal and route detailed rules to the closest subdirectory AGENTS.md.
applyTo: "**"
---

# Repository Agent Routing

Use this file for repo-wide rules only. Read the closest deeper `AGENTS.md` before editing files in that area.

## Reply Style

- Keep replies short, straight to the point, and limited to relevant information.
- Preserve important context, decisions, risks, and verification details.
- Put the most important information first.

## Repository Structure

- Root purpose: repository scaffold and governance baseline.
- Main directories: `docs/`, `.github/`, `.opencode/`, `bin/`, `config/`, `diagrams/`, `examples/`, `scripts/`, `src/`, `tests/`.
- Reference tree: `REPOSTORY_MAP.md`.

## Global Workflow

- Define scope before editing and avoid unrelated changes.
- Prefer root-cause fixes and explicit, simple changes.
- Keep `AGENTS.md` files up to date when workflow or context-management guidance changes, or when new instructions would materially improve future work.
- Update documentation in the same task when behavior, workflow, or structure changes.
- Do not claim success without verification evidence.
- If verification cannot run, state what was not run, why, and the residual risk.

## Git And Safety

- Never commit credentials, keys, or secrets.
- Keep commits and PRs logically scoped.
- Do not use destructive git actions unless explicitly requested.
- Preserve backward compatibility unless the task explicitly changes the contract.

## Routing Map

- `docs/AGENTS.md` — documentation rules and doc update expectations.
- `docs/project/AGENTS.md` — ADR authoring and durable implementation decision rules.
- `docs/superpowers/AGENTS.md` — specs, plans, and historical implementation record rules.
- `.github/AGENTS.md` — CI, CODEOWNERS, and branch protection guidance.
- `.opencode/AGENTS.md` — OpenCode local tooling and prompt/instruction assets.
- `.opencode/instructions/AGENTS.md` — instruction file ownership and standards documents.
- `src/AGENTS.md` — coding practices and implementation rules for source files.
