# Universal Repository Template

A governance-first project template. It gives you a clean engineering scaffold, a structured documentation tree, and a set of AI-assisted prompts that walk you from a blank clone through requirements, architecture, and language specialization — before you write a single line of implementation code.

The core idea: decisions made early (what the project is for, what it needs to achieve, which stack and why) should be recorded in canonical documents that the rest of the project refers back to. This template creates that structure upfront, so your codebase, docs, and AI agent context stay in sync throughout the project's life.

The most important part is the documentation curation. This template aims to enable producing robust and complete project documentation that allows for planning and executing an implementation without any guesswork and sudden changes of the core concepts.

## Project journey

A new project using this template goes through four phases before implementation. Each phase produces canonical documents that the next phase reads from.

```text
Clone
  │
  ▼
Phase 1 — Intent
  Run prompts/project-bootstrap.md
  Produces: project brief, PRD, refreshed README
  Output: docs/00_governance/00_project_brief.md
          docs/02_product/01_prd.md
  │
  ▼
Phase 2 — Specifications
  Iterate on the canonical docs with your AI tool
  Refine scope, requirements, goals, and constraints
  until they are robust enough to design against
  Output: solid project brief + PRD, optional early ADRs
  │
  ▼
Phase 3 — Architecture
  Run prompts/architecture-baseline.md
  Reads project brief and PRD, guides stack decision conversation,
  proposes 2-3 architectural approaches, generates solution design
  Output: docs/03_architecture/01_solution_design.md
          docs/adr/ADR-NNN-*.md (one per durable decision)
  │
  ▼
Phase 4 — Structure
  Run prompts/language-adaptation.md
  The prompt reads your canonical docs as the source of truth
  and specializes the repo scaffold to match
  Output: language-specific src/, tests/, config/, .gitignore,
          updated AGENTS.md routing, ADRs, docs control spine
  │
  ▼
Implementation planning or deeper documentation work
```

After Phase 4 your repository has a coherent structure, all docs agree on the stack and project shape, and you can move straight into writing specs, planning workstreams, or starting implementation.

## Bootstrap checklist

1. Run [`prompts/project-bootstrap.md`](prompts/project-bootstrap.md) — capture intent, produce first-pass canonical docs.
2. Iterate on [`docs/00_governance/00_project_brief.md`](docs/00_governance/00_project_brief_TEMPLATE.md) and [`docs/02_product/01_prd.md`](docs/02_product/01_prd_TEMPLATE.md) until specifications, requirements, and goals are solid.
3. Run [`prompts/architecture-baseline.md`](prompts/architecture-baseline.md) — guides the stack and architecture decision conversation, then generates the solution design and ADRs.
4. Run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) — specializes the scaffold against the architecture docs.
5. Replace placeholder ownership metadata in canonical docs under `docs/` as you adopt them.
6. Keep only the top-level folders you will actually use.
7. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing.
8. Keep local workspace tooling such as `.opencode/` gitignored and untracked.
9. Commit the bootstrap state as one or two clean commits before starting feature work.

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
- Generates [`docs/03_architecture/01_solution_design.md`](docs/03_architecture/01_solution_design_TEMPLATE.md) fully filled in and an ADR for every durable decision made in the conversation.
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
| `examples/` | Copyable examples for implemented features only. |
| `diagrams/` | Source diagrams that support active architecture docs and ADRs. |
| `prompts/` | Adoption-time prompts that adapt this template to a chosen language stack. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine — the source of truth for how documentation is structured in this project.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records, not canonical guidance.
- `docs/99_archive/` is for retired material, not active guidance.

## Optional local tooling

Repository-local helper tooling is allowed but should stay outside the tracked template contract. Keep `.opencode/` and similar workspace directories gitignored so the template remains portable.
