# Universal Repository Template

A governance-first project template. It gives you a clean engineering scaffold, a structured documentation tree, AI-assisted prompts for adoption, and tracked assistant-native integration assets for Claude, Copilot, Codex, and OpenCode.

The core idea is simple: early decisions about purpose, scope, and architecture belong in active documents that the rest of the project refers back to. This template creates that structure upfront so your codebase, docs, and AI agent context stay aligned throughout the project.

The most important part is the documentation curation. The template is designed to produce complete project documentation that supports planning and execution without guesswork or sudden changes to core concepts.

## Project journey

A new project using this template goes through four phases before implementation. Each phase produces active documents that the next phase reads from.

```text
Clone
  │
  ▼
Phase 1 — Intent
  Run prompts/project-bootstrap.md
  Produces: active project brief, active PRD, refreshed README
  Output: docs/00_governance/00_project_brief.md
          docs/02_product/01_prd.md
  │
  ▼
Phase 2 — Specifications
  Run prompts/refine-specs.md
  Refine scope, requirements, goals, and constraints
  until the active documents are robust enough to design against
  Output: ready project brief + PRD, optional early ADRs
  │
  ▼
Phase 3 — Architecture
  Run prompts/architecture-baseline.md
  Reads the active project brief and PRD, guides stack decision conversation,
  proposes 2-3 architectural approaches, generates the active solution design
  Output: docs/03_architecture/01_solution_design.md
          docs/adr/ADR-NNN-*.md (one per durable decision)
  │
  ▼
Phase 4 — Structure
  Run prompts/language-adaptation.md
  The prompt reads the active documents as the source of truth
  and specializes the repo scaffold to match
  Output: language-specific src/, tests/, config/, .gitignore,
          updated AGENTS.md routing, ADRs, docs control spine
  │
  ▼
Implementation planning or deeper documentation work
```

After Phase 4 your repository has a coherent structure, all docs agree on the stack and project shape, and you can move straight into writing specs, planning workstreams, or starting implementation.

## Bootstrap checklist

1. Run [`prompts/project-bootstrap.md`](prompts/project-bootstrap.md) to capture project intent and create the first active project documents.
2. Run [`prompts/refine-specs.md`](prompts/refine-specs.md) until the active brief and PRD are ready for architecture work.
3. Run [`prompts/architecture-baseline.md`](prompts/architecture-baseline.md) to decide the stack and create the active solution design and ADRs.
4. Run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) to specialize the scaffold against the active architecture documents.
5. Replace placeholder ownership metadata in the active docs under `docs/` as you adopt them.
6. Keep only the top-level folders you will actually use.
7. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing.
8. Keep only machine-specific files local; the assistant-native directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are part of the tracked template contract, and Codex also uses tracked repo-native skills under `.agents/skills/`.
9. Commit the bootstrap state as one or two clean commits before starting feature work.

## Minimal adoption path

If you are not using AI prompts, create the active project brief, PRD, and solution design from the starter templates under `docs/`, then adapt the repository structure manually.

## Bootstrap your project

Run [`prompts/project-bootstrap.md`](prompts/project-bootstrap.md) in your AI coding tool of choice (Claude Code, Codex, Cursor, or any tool that accepts Markdown prompt files). The prompt:

- Asks three required questions (project name, what the project needs to achieve, planned product description) and optional follow-ups about users, deployment context, and constraints.
- Proposes two or three approach directions as starting points — not decisions.
- Produces a first-pass project brief and PRD with `[TBD: ...]` markers wherever the answers were incomplete, so iteration is targeted.
- Stays implementation-neutral: no language, framework, or runtime is chosen here.

After bootstrap, spend time on Phase 2. Work through the canonical docs with your AI tool: challenge assumptions, sharpen requirements, resolve TBD markers, and capture any early durable decisions as ADRs. The architecture phase depends on having solid inputs.

## Author the architecture baseline

Run [`prompts/architecture-baseline.md`](prompts/architecture-baseline.md) in your AI coding tool once the project brief and PRD are solid. The prompt:

- Reads the project brief and PRD and summarises what it already knows before asking anything — confirming understanding before driving decisions.
- Asks only what the docs don't already capture: language, primary framework, data storage approach, deployment target, and structural shape (monolith vs. services vs. hybrid).
- Proposes two or three architecture approaches that fit the requirements and constraints, each with explicit trade-offs and risks.
- Generates [`docs/03_architecture/01_solution_design.md`](docs/03_architecture/01_solution_design.md) fully filled in and an ADR for every durable decision made in the conversation.
- Stays implementation-neutral: no code, no version pins, no module names.

The solution design is the single source of truth that [`prompts/language-adaptation.md`](prompts/language-adaptation.md) reads from. If it is missing or still contains template placeholders, the language-adaptation prompt will halt and tell you exactly what is missing.

## Adapt to your stack

Run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) once the architecture baseline is complete. The prompt:

- Reads the project brief, PRD, solution design, and accepted ADRs as the single source of truth. It does not ask you to restate stack facts the docs already capture.
- Halts with a precise list of missing inputs if the architecture or bootstrap docs are not ready.
- Adapts the top-level scaffold, adds language-specific structural directories, updates baseline files (`.gitignore`, `.editorconfig`, `.gitattributes`), updates the documentation control spine, and updates routed `AGENTS.md` files so everything agrees with the canonical docs.
- Stays implementation-neutral: no feature code, no endpoint stubs, no dependency version pins beyond what an accepted ADR explicitly requires.

After adaptation, the repository is structurally ready. You can continue expanding the documentation (interface contracts, delivery plans, security runbooks) or move directly into implementation planning on the adapted template.

See [`prompts/README.md`](prompts/README.md) for the full prompt inventory and workflow detail.

## Top-level layout

| Path | Purpose |
| --- | --- |
| `src/` | Implementation code and reusable modules. |
| `tests/` | Automated verification, ideally mirroring `src/` by scope. |
| `config/` | Environment, runtime, and deployment configuration templates. |
| `scripts/` | Maintainer automation for development, CI, release, and migration tasks. |
| `bin/` | Thin user-facing entrypoints or wrappers for runtime commands. |
| `tools/` | Repository-maintained utilities such as documentation validators and maintenance helpers. |
| `examples/` | Copyable examples for implemented features only. |
| `diagrams/` | Source diagrams that support active architecture docs and ADRs. |
| `.agents/` | Repo-native Codex skill discovery surface. |
| `.claude/` | Tracked Claude Code skills, hooks, and repo-local defaults. |
| `.copilot/` | Tracked Copilot-oriented Superpowers assets kept in parity with other harnesses. |
| `.codex/` | Tracked Codex hook wiring and vendored Superpowers mirror assets. |
| `.opencode/` | Tracked OpenCode skills and plugin bootstrap assets. |
| `prompts/` | Adoption-time prompts that adapt this template to a chosen language stack. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine, the source of truth for how documentation is structured in this project.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records, not canonical guidance.
- `docs/99_archive/` is for retired material, not active guidance.
- `tools/docs_validator/` holds the Python frontmatter validator used by docs-focused local checks and GitHub workflows.

## Assistant-native tooling

The template ships tracked assistant-native assets in `.claude/`, `.copilot/`, `.codex/`, and `.opencode/`.

- Vendored Superpowers assets are synced from `/home/hexaper/.claude/plugins/cache/claude-plugins-official/superpowers/5.1.0`.
- Keep only machine-specific files local, such as `.claude/settings.local.json` and ignored OpenCode workspace files under `.opencode/`.
- GitHub Copilot's actual repository instruction entrypoint remains `.github/copilot-instructions.md`.
- Codex uses root `AGENTS.md`, `.codex/hooks.json`, and `.agents/skills/` as its repo-native runtime surface.
