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

1. Run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) against this fresh clone to specialize the template to your language stack and project type. See [Adapt to your stack](#adapt-to-your-stack) below.
2. Update this `README.md` with your project name, purpose, and operator setup.
3. Replace placeholder ownership metadata in canonical docs under `docs/` as you adopt them.
4. Keep only the top-level folders you will actually use for your project.
5. Record durable technical decisions in `docs/adr/`.
6. Treat `docs/superpowers/` as working history, not canonical guidance.
7. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing the repository.
8. Keep local workspace tooling such as `.opencode/` ignored and untracked.

## Adapt to your stack

This template ships language-agnostic. Before populating canonical docs or writing code, run the adaptation prompt at [`prompts/language-adaptation.md`](prompts/language-adaptation.md) in your AI coding tool of choice. The prompt:

- Asks the minimum questions needed to specialize the baseline (target language(s), primary technologies, optional deployment target and project description).
- Adapts the top-level scaffold to the chosen ecosystem and adds language-specific structural directories where they are durable.
- Updates the documentation control spine, ADRs as needed, baseline files (`.gitignore`, `.editorconfig`, `.gitattributes`), and routed `AGENTS.md` files so they all agree on the chosen stack.
- Stays implementation-neutral. It does not generate feature code, endpoints, or dependency version pins.

See [`prompts/README.md`](prompts/README.md) for the full inventory and adoption workflow.

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
| `prompts/` | Adoption-time prompts that adapt this template to a chosen language stack. |
| `docs/` | Canonical documentation tree and governance structure. |

## Documentation model

- `docs/README.md`, `docs/Architecture.md`, `docs/00-documentation-standards.md`, `docs/00-source-of-truth.md`, and `docs/INDEX.md` form the control spine.
- `docs/adr/` holds durable architecture and implementation decisions.
- `docs/superpowers/` holds dated specs and plans as historical working records.
- `docs/99_archive/` is for historical evidence, not active guidance.

## Optional local tooling

Repository-local helper tooling is allowed, but it should stay outside the tracked template contract. Keep `.opencode/` and similar workspace directories gitignored so the template remains portable.
