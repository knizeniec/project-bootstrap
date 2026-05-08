# Universal Repository Template

A governance-first project template. It gives you a clean engineering scaffold, a structured documentation tree, AI-assisted prompts for adoption, and tracked assistant-native integration assets for Claude, Copilot, Codex, and OpenCode.

The core idea is simple: early decisions about purpose, scope, and architecture belong in active documents that the rest of the project refers back to. This template creates that structure upfront so your codebase, docs, and AI agent context stay aligned throughout the project.

The most important part is the documentation curation. The template is designed to produce complete project documentation that supports planning and execution without guesswork or sudden changes to core concepts.

## Project journey

A new project using this template goes through seven phases before implementation, but the user only needs to remember one command: `/init`.

```text
Clone
  │
  ▼
/init
  Starts Phase 0 (Triage) if no plan exists.
  Otherwise shows status, resumes the next phase,
  or lets the user revisit a completed phase or artifact.
  State lives in docs/superpowers/plans/YYYY-MM-DD-project-initialization.md
```

`/init` routes into these phases:

| Phase | Routed target | Output |
| --- | --- | --- |
| 0 | `project-initialization/phases/0-triage.md` | plan file in `docs/superpowers/plans/` |
| 1 | `project-initialization/phases/1-intent.md` | `docs/00_governance/00_project_brief.md` and optional `01_business_case.md` |
| 2 | `project-initialization/phases/2-specification.md` | active specification artifacts |
| 3 | `project-initialization/phases/3-design.md` | `docs/03_architecture/01_solution_design.md`, ADRs, optional C4 views |
| 4 | `project-initialization/phases/4-govern-operate.md` | govern and operate artifacts per profile |
| 5 | `project-initialization/phases/5-adapt.md` | language-specific scaffold and repository sync updates |
| 6 | `project-initialization/phases/6-review.md` | final review pass and completed plan |

## Bootstrap checklist

1. Clone this repository.
2. Run `/init` in your AI tool to start Phase 0 (Triage) and write the initialization plan.
3. Run `/init` again whenever you want to continue; it will resume the next incomplete phase automatically.
4. Use `/init <phase-or-artifact-name>` if you need to revisit a completed phase or artifact directly.
5. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing.
6. Keep machine-specific overrides local-only. The assistant directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are part of the tracked template contract; only `settings.local.json` and similar machine-specific files should stay untracked.
7. Commit the bootstrap state as one or two clean commits before starting feature work.

## Initialize your project

Run `/init` in Claude Code, GitHub Copilot Chat, Codex, or any tool that supports per-project slash commands. The command:

- Starts triage if no plan exists.
- Reads the existing plan file and shows a status block when initialization is already in progress.
- Lets the user continue, revisit completed work, or print the plan path and resume context.
- Supports direct jumps with `/init <phase-or-artifact-name>`.

See [`project-initialization/README.md`](project-initialization/README.md) for the full phase catalog and shared contract.

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
| `project-initialization/` | Phase orchestration content, artifact rubrics, and profiles for the init workflow. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine, the source of truth for how documentation is structured in this project.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records, not canonical guidance.
- `docs/99_archive/` is for retired material, not active guidance.
- `tools/docs_validator/` holds the Python frontmatter validator used by docs-focused local checks and GitHub workflows.

## Assistant-native tooling

The template ships tracked assistant-native assets in `.claude/`, `.copilot/`, `.codex/`, and `.opencode/`.


