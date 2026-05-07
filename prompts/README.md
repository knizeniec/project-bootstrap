# Adoption Prompts

Status: Active
Owner: Template maintainers
Purpose: hold adoption-time prompts that adapt this language-agnostic template to a specific language, stack, or project type
Last updated: 2026-05-06

This directory is the canonical home for prompts that an adopter runs against a fresh clone of the template to specialize it. Prompts here are tooling-agnostic Markdown with YAML frontmatter and can be pasted into any AI coding tool that supports prompt-style instructions.

## Inventory

| Prompt | Purpose | Run order |
|---|---|---|
| [project-bootstrap.md](project-bootstrap.md) | Capture project intent and produce a first-pass canonical documentation baseline (project brief, PRD, refreshed root README, optional initial ADR). | First |
| [language-adaptation.md](language-adaptation.md) | Specialize the structural baseline to the language stack already recorded in the canonical architecture docs. Reads the docs as the source of truth and refuses to run if they are missing or unfilled. | After bootstrap and architecture docs are filled in |

## How adopters use this directory

1. Clone the template into your new project directory.
2. Open [project-bootstrap.md](project-bootstrap.md) and paste it into your AI coding tool (Claude Code, Codex, Cursor, or another agent that supports prompt instructions). Answer the required questions (project name, what the project needs to achieve, planned product description), review the proposed approach options, and accept the generated first-pass canonical docs.
3. Iterate on the bootstrap canonical docs ([docs/00_governance/00_project_brief.md](../docs/00_governance/00_project_brief_TEMPLATE.md) and [docs/02_product/01_prd.md](../docs/02_product/01_prd_TEMPLATE.md)) until project specifications, requirements, and goals are robust enough to plan against.
4. Author the architecture baseline by copying [docs/03_architecture/01_solution_design_TEMPLATE.md](../docs/03_architecture/01_solution_design_TEMPLATE.md) to `docs/03_architecture/01_solution_design.md` and filling in the chosen language stack, primary technologies, building blocks, runtime and deployment view, and the basic application plan. Add ADRs under [docs/adr/](../docs/adr/) when the design crystallizes durable decisions.
5. Open [language-adaptation.md](language-adaptation.md) and paste it into the same tool. The prompt reads the canonical docs as authoritative input and halts if the architecture baseline is missing or still contains placeholders. Review the structural changes before accepting them.
6. Follow the remaining steps in the bootstrap checklist in the root [README.md](../README.md) (set the LICENSE, replace placeholder ownership metadata, etc.).
7. Commit the bootstrap state as one or two clean commits before starting feature work, and continue with deeper documentation work or implementation planning on the adapted template.

## What adoption prompts may modify

- Top-level scaffold (`src/`, `tests/`, `config/`, `scripts/`, and similar) to match the chosen ecosystem.
- Documentation control spine: [docs/Architecture.md](../docs/Architecture.md), [docs/00-source-of-truth.md](../docs/00-source-of-truth.md), [docs/00-documentation-standards.md](../docs/00-documentation-standards.md), [docs/INDEX.md](../docs/INDEX.md).
- ADRs under [docs/adr/](../docs/adr/) when language, technology direction, or repository mode become baseline decisions.
- Baseline files: `.gitignore`, `.editorconfig`, `.gitattributes`, [CONTRIBUTING.md](../CONTRIBUTING.md), [SECURITY.md](../SECURITY.md).
- Routed `AGENTS.md` files, especially [src/AGENTS.md](../src/AGENTS.md) and the root [AGENTS.md](../AGENTS.md).

## What adoption prompts must not do

- Generate business logic, feature code, endpoints, or domain models.
- Pin framework or dependency versions unless the adopter explicitly required them.
- Replace the repository governance model with language-specific shortcuts.
- Introduce alternate documentation trees that conflict with the active control spine.

## Editing prompts

- Each prompt is a single self-contained Markdown file with frontmatter (`name`, `description`, `argument-hint`, `agent`).
- Reference only paths that exist in the current tracked tree.
- Bump `Last updated` in this README and in any prompt you change.
- Keep prompts implementation-neutral and tooling-agnostic.
- Read [AGENTS.md](AGENTS.md) before editing prompt files.

## Source of truth

This directory is owned by the template maintainers and tracked in [docs/00-source-of-truth.md](../docs/00-source-of-truth.md).
