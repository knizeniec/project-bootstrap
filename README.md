# Universal Repository Template

This repository is a governance-first template for projects that want a clean engineering scaffold plus durable documentation for product, architecture, delivery, and decision tracking.

## Good fit

- backend services and internal tools
- web applications with a real delivery process
- multi-stakeholder or compliance-sensitive projects
- teams that want lightweight code scaffolding with stronger documentation defaults

## Less ideal

- throwaway prototypes
- single-file utilities
- projects that do not want any structured documentation workflow

## Bootstrap checklist

1. Update this `README.md` with your project name, purpose, and operator setup.
2. Replace placeholder ownership metadata in canonical docs under `docs/` as you adopt them.
3. Keep only the top-level folders you will actually use for your project.
4. Record durable technical decisions in `docs/adr/`.
5. Treat `docs/superpowers/` as working history, not canonical guidance.
6. Keep local workspace tooling such as `.opencode/` ignored and untracked.

## Top-level layout

| Path | Purpose |
|---|---|
| `src/` | Implementation code and reusable modules. |
| `tests/` | Automated verification, ideally mirroring `src/` by scope. |
| `config/` | Environment, runtime, and deployment configuration templates. |
| `scripts/` | Maintainer automation for development, CI, release, and migration tasks. |
| `bin/` | Thin user-facing entrypoints or wrappers for runtime commands. |
| `examples/` | Copyable examples for implemented features only. |
| `diagrams/` | Source diagrams that support active architecture docs and ADRs. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records.
- `docs/99_archive/` is for historical evidence, not active guidance.

## Optional local tooling

Repository-local helper tooling is allowed, but it should stay outside the tracked template contract. Keep `.opencode/` and similar workspace directories gitignored so the template remains portable.

## Reference tree

See `REPOSITORY_MAP.md` for the tracked repository tree and quick search reference.
