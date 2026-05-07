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

1. Run [`prompts/project-bootstrap.md`](prompts/project-bootstrap.md) against this fresh clone to capture project intent and produce a first-pass canonical documentation baseline. See [Bootstrap your project](#bootstrap-your-project) below.
2. Iterate on the bootstrap canonical docs ([`docs/00_governance/00_project_brief.md`](docs/00_governance/00_project_brief_TEMPLATE.md), [`docs/02_product/01_prd.md`](docs/02_product/01_prd_TEMPLATE.md)) until project specifications, requirements, and goals are robust enough to plan against.
3. Author the architecture baseline by copying [`docs/03_architecture/01_solution_design_TEMPLATE.md`](docs/03_architecture/01_solution_design_TEMPLATE.md) to `docs/03_architecture/01_solution_design.md` and filling in the chosen language stack, primary technologies, building blocks, runtime and deployment view, and the basic application plan. Record durable decisions as ADRs in [`docs/adr/`](docs/adr/).
4. Run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) to specialize the structural baseline against those architecture docs. The prompt reads the canonical docs as the source of truth and halts if they are missing or still contain placeholders. See [Adapt to your stack](#adapt-to-your-stack) below.
5. Replace placeholder ownership metadata in canonical docs under `docs/` as you adopt them.
6. Keep only the top-level folders you will actually use for your project.
7. Treat `docs/superpowers/` as working history, not canonical guidance.
8. Replace the placeholder [`LICENSE`](LICENSE) with your chosen license before publishing the repository.
9. Keep local workspace tooling such as `.opencode/` ignored and untracked.
10. Continue with deeper documentation work or move into implementation planning on the adapted template.

## Bootstrap your project

This is the first step against a fresh clone. Run [`prompts/project-bootstrap.md`](prompts/project-bootstrap.md) in your AI coding tool of choice. The prompt:

- Asks three required questions (project name, what the project needs to achieve, planned product description) and a small set of optional follow-ups about users, deployment context, and constraints.
- Proposes two or three approach directions with non-binding tech-stack options for the user to consider — proposals are starting points, not decisions.
- Produces a first-pass canonical documentation baseline: an active project brief at `docs/00_governance/00_project_brief.md`, an active PRD at `docs/02_product/01_prd.md`, a refreshed root README, and an optional initial ADR if the user committed to a durable decision during the conversation.
- Stays implementation-neutral. It does not pick a language, framework, or runtime. Those choices happen in the next step.

## Adapt to your stack

After bootstrap and after the architecture docs ([`docs/03_architecture/01_solution_design.md`](docs/03_architecture/01_solution_design_TEMPLATE.md) plus any accepted ADRs) are filled in with the chosen language stack and basic application plan, run [`prompts/language-adaptation.md`](prompts/language-adaptation.md) to specialize the structural baseline. The prompt:

- Reads the canonical docs as the single source of truth: project brief, PRD, and the solution design. It does not ask the adopter to restate stack facts that the docs already capture.
- Halts with a precise list of missing or unfilled inputs if the architecture or bootstrap docs are not yet ready, instead of guessing.
- Adapts the top-level scaffold to the language stack and project shape recorded in the docs and adds language-specific structural directories where they are durable.
- Updates the documentation control spine, ADRs when the adaptation itself crystallizes a durable decision, baseline files (`.gitignore`, `.editorconfig`, `.gitattributes`), and routed `AGENTS.md` files so they all agree with the canonical docs.
- Stays implementation-neutral. It does not generate feature code, endpoints, or dependency version pins beyond what an accepted ADR or the solution design already requires.

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
