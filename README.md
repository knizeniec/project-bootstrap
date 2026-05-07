# Universal Repository Template

A governance-first project template. It gives you a clean engineering scaffold, a structured documentation tree, AI-assisted prompts for adoption, and tracked assistant-native integration assets for Claude, Copilot, Codex, and OpenCode.

The core idea is simple: early decisions about purpose, scope, and architecture belong in active documents that the rest of the project refers back to. This template creates that structure upfront so your codebase, docs, and AI agent context stay aligned throughout the project.

The most important part is the documentation curation. The template is designed to produce complete project documentation that supports planning and execution without guesswork or sudden changes to core concepts.

## Project journey

A new project using this template goes through seven phases before implementation. Run the commands in order using your AI tool's slash-command interface.

```text
Clone
  │
  ▼
/init-triage   (Phase 0)
  Asks five routing questions, selects a project profile,
  assigns per-artifact modes (interview / confirm / extract),
  and writes the plan file that all subsequent phases read from.
  Output: docs/superpowers/plans/YYYY-MM-DD-project-initialization.md
  │
  ▼
/init-intent   (Phase 1)
  Produces the project brief and optional business case.
  Output: docs/00_governance/00_project_brief.md
          docs/00_governance/01_business_case.md (if activated)
  │
  ▼
/init-spec     (Phase 2)
  Produces PRD, requirements catalog, user journeys, acceptance catalog.
  Output: docs/02_product/01_prd.md + active specification artifacts
  │
  ▼
/init-design   (Phase 3)
  Produces solution design and an ADR per durable decision.
  Output: docs/03_architecture/01_solution_design.md
          docs/adr/ADR-NNN-*.md (one per durable decision)
  │
  ▼
/init-govern   (Phase 4)
  Produces AI use policy, test strategy, security baseline, delivery plan.
  Output: active govern & operate artifacts per profile
  │
  ▼
/init-adapt    (Phase 5)
  Specializes src/, tests/, config/, .gitignore, and entry docs to match.
  Output: language-specific scaffold, updated AGENTS.md and README.md
  │
  ▼
/init-review   (Phase 6)
  Validates cross-doc coherence and declares initialization complete.
  Output: updated plan file; commit suggestion
```

Each command reads the plan file written by `/init-triage` and refuses to run if its prerequisites are unmet.

## Bootstrap checklist

1. Clone this repository.
2. Run `/init-triage` in your AI tool to answer five routing questions and write the initialization plan.
3. Run `/init-intent` through `/init-review` in order. Each command stops when its phase is complete.
4. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing.
5. Keep machine-specific overrides local-only. The assistant directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are part of the tracked template contract; only `settings.local.json` and similar machine-specific files should stay untracked.
6. Commit the bootstrap state as one or two clean commits before starting feature work.

## Initialize your project

Run `/init-triage` in Claude Code, GitHub Copilot Chat, Codex, or any tool that supports per-project slash commands. The command:

- Asks five routing questions: project type, AI involvement, regulatory posture, team shape, and an optional existing description paste.
- Selects a project profile (product, internal tool, library, or platform) and builds a per-artifact roadmap.
- Assigns each artifact a mode: `interview` (full question flow), `confirm` (show extracted content and ask for gaps), or `extract` (draft from pasted content without questions).
- Writes the initialization plan file to `docs/superpowers/plans/` — every subsequent command reads this file.

After triage, run `/init-intent` through `/init-review` in sequence. If you paste a detailed project description at triage, later phases skip questions for content already captured.

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

- Vendored Superpowers assets are synced from `/home/hexaper/.claude/plugins/cache/claude-plugins-official/superpowers/5.1.0`.
- Keep only machine-specific files local, such as `.claude/settings.local.json` and ignored OpenCode workspace files under `.opencode/`.
- GitHub Copilot's actual repository instruction entrypoint remains `.github/copilot-instructions.md`.
- Codex uses root `AGENTS.md`, `.codex/hooks.json`, and `.agents/skills/` as its repo-native runtime surface.
