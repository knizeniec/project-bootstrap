---
name: "Adapt Language-Agnostic Template To Language Stack"
description: "Use when an adopter has filled in the canonical project, product, and architecture docs and now needs the language-agnostic repository scaffold specialized to the chosen stack without writing implementation code."
argument-hint: "No user-supplied stack inputs. The prompt reads the chosen language stack and project shape from the canonical docs under docs/. Run only after bootstrap and the architecture docs are filled in."
agent: "agent"
---

Adapt an already-bootstrapped repository template into a language-aware project baseline by reading the canonical docs as the single source of truth. Do not generate implementation code.

The adopter has already run [project-bootstrap.md](project-bootstrap.md) and authored the architecture documents. The chosen language stack, primary technologies, deployment direction, and project shape are recorded in those docs. Treat the docs as authoritative input. Do not ask the adopter to restate stack facts that the docs already capture.

Canonical input documents (read before doing anything else):

- [docs/00_governance/00_project_brief.md](../docs/00_governance/00_project_brief_TEMPLATE.md) — project name, problem, goals, scope, stakeholders, constraints.
- [docs/02_product/01_prd.md](../docs/02_product/01_prd_TEMPLATE.md) — product scope, users, journeys, functional and non-functional requirements.
- [docs/03_architecture/01_solution_design.md](../docs/03_architecture/01_solution_design_TEMPLATE.md) — chosen language stack, primary technologies and frameworks, building blocks, runtime and deployment view, basic application plan. This file is the primary source for stack decisions.
- [docs/03_architecture/README.md](../docs/03_architecture/README.md) and any other active files under [docs/03_architecture/](../docs/03_architecture/) — supporting architecture context, interface contracts, and quality concerns.
- [docs/adr/](../docs/adr/) — accepted ADRs that lock in language, framework, repository mode, or structural ownership decisions.

Preflight gate (halt before adapting if any of the following hold):

- [docs/03_architecture/01_solution_design.md](../docs/03_architecture/01_solution_design_TEMPLATE.md) does not exist as an active instance file.
- The active solution design file is empty or still contains template placeholder text in the sections that name language(s), primary technologies, building blocks, or runtime and deployment view.
- The bootstrap canonical docs ([docs/00_governance/00_project_brief.md](../docs/00_governance/00_project_brief_TEMPLATE.md), [docs/02_product/01_prd.md](../docs/02_product/01_prd_TEMPLATE.md)) are missing or still contain template placeholders for project name, problem, goals, or scope.
- The architecture and bootstrap docs disagree on project name, scope, or stack direction.

If any halt condition holds, do not adapt. Instead, list the missing or inconsistent inputs precisely (file path, section, what is missing or contradicting), point the adopter to [project-bootstrap.md](project-bootstrap.md) for missing bootstrap content and to [docs/03_architecture/01_solution_design_TEMPLATE.md](../docs/03_architecture/01_solution_design_TEMPLATE.md) for the architecture template, and stop. Do not infer stack facts.

Stack and project-shape extraction (when preflight passes):

- Extract from the canonical docs: target language(s), primary technologies and frameworks per language, runtime and deployment target, repository mode (single-project or monorepo), project type (library, service, web app, CLI, worker, data pipeline, mobile app, desktop app, infrastructure project, or hybrid), durable top-level needs (API surface, migrations, assets, infrastructure, SDKs, jobs, schemas, public/static content), and any organization or compliance constraints that affect baseline structure.
- If the docs are silent on an optional dimension (for example, no deployment target named), record that explicitly under `Assumptions` and add only the structural baseline that is necessary regardless.
- Never invent a language, framework, or deployment choice that the docs do not state. If a structural decision is forced by an unstated input, list it under `Open Decisions` and stop instead of guessing.

Primary objective:

- Adapt the repository so it is structurally ready for the language stack and project shape recorded in the canonical docs.
- Keep the repository documentation-first and implementation-neutral.
- Make the repository ready to expand documentation or move into implementation planning without needing another baseline restructure.
- Do not generate business logic, feature code, or implementation-specific application behavior.

Adaptation rules:

- Preserve the existing repository governance model, documentation ownership model, and routed `AGENTS.md` structure.
- Add only directories and files that are durable for the language stack and project shape recorded in the canonical docs.
- Do not choose dependency versions, framework versions, or implementation-layer libraries unless an accepted ADR or the solution design file explicitly fixes them and they are required for a baseline contract.
- Do not generate endpoints, components, services, domain models, or concrete runtime workflows.
- Prefer clear ownership boundaries and future-proof structure over convenience placeholders.

Repository structure updates:

- Keep the required top-level scaffold unless the canonical docs explicitly change repository mode.
- Add language-specific structural directories only when they will clearly remain useful through implementation as described in the solution design.
- For single-language projects, adapt `src/`, `tests/`, `config/`, `scripts/`, `examples/`, and other baseline directories to match ecosystem expectations without adding feature code.
- For multi-language projects, create explicit boundaries for each language and for shared assets, tools, or interface contracts, matching the partitioning described in the solution design.
- If the solution design implies durable architectural areas, add only the empty structural folders and folder-level `README.md` files needed to support that project type.
- If the solution design or an accepted ADR fixes a deployment shape that affects long-lived structure, add only stable deployment-facing placeholders such as infrastructure, deployment config, container, or environment documentation folders.

Documentation updates:

- Treat [docs/03_architecture/01_solution_design.md](../docs/03_architecture/01_solution_design_TEMPLATE.md) and accepted ADRs as the source of truth for stack and architecture facts. Do not rewrite or summarize their content elsewhere; link to them.
- Update [README.md](../README.md) with a concise overview of the selected language stack that points to the solution design as the authoritative source.
- Update [docs/Architecture.md](../docs/Architecture.md) only with structural and ownership changes the adaptation introduced into the docs control spine. Do not duplicate stack facts that already live in `03_architecture/01_solution_design.md`.
- Update [docs/00-source-of-truth.md](../docs/00-source-of-truth.md) so any new active instance docs introduced by the adaptation have a canonical owner row, and so existing rows still resolve to the correct owner after structural changes.
- Update [docs/00-documentation-standards.md](../docs/00-documentation-standards.md) with naming, layout, and documentation expectations introduced by the language stack named in the solution design.
- Update [docs/INDEX.md](../docs/INDEX.md) so newly active stack-relevant docs are discoverable.
- Create or update ADRs under [docs/adr/](../docs/adr/) when the adaptation itself crystallizes a durable decision (for example, repository mode, structural ownership) that the solution design implies but does not yet record as an ADR.
- If the solution design names operational or delivery details, update the relevant docs under [docs/06_security_operations/](../docs/06_security_operations/) and [docs/07_delivery/](../docs/07_delivery/) with baseline ownership and assumptions, again linking back to the solution design rather than restating it.

Baseline file updates:

- Update `.gitignore`, `.editorconfig`, and `.gitattributes` to fit the language stack named in the solution design.
- Add ecosystem baseline files only when they are long-lived structural contracts and not premature implementation choices.
- Keep baseline config files minimal, actionable, and free of implementation-specific dependencies where possible.
- Update [CONTRIBUTING.md](../CONTRIBUTING.md), [SECURITY.md](../SECURITY.md), and other operator-facing baseline files when the chosen stack changes workflow expectations.
- Do not introduce concrete application dependencies or version pinning unless the solution design or an accepted ADR explicitly requires them for the baseline.

`AGENTS.md` adaptation requirements:

- Preserve context routing: keep root [AGENTS.md](../AGENTS.md) minimal and place scoped rules in the closest relevant directory.
- Update root [AGENTS.md](../AGENTS.md) with high-level project facts that matter repo-wide, including selected language(s), a concise project description sourced from the project brief and PRD, and routing to any new scoped `AGENTS.md` files.
- Update [src/AGENTS.md](../src/AGENTS.md) with language-specific coding best practices, structural conventions, and quality expectations for the language(s) named in the solution design.
- If multiple languages or major subdomains in the solution design justify it, add deeper scoped `AGENTS.md` files for those directories instead of crowding root or `src/AGENTS.md`.
- Ensure relevant `AGENTS.md` files include project-specific information that improves workflow and context management, including selected languages, project description sourced from the canonical docs, and best-practice guidance for the chosen stack.
- Keep the most important instructions first in every `AGENTS.md` file.
- Keep `AGENTS.md` files up to date whenever new workflow or context-management guidance would materially improve future work.

Language adaptation quality gate:

- The final tree reflects the language stack and project shape recorded in the canonical docs without implementation code.
- Docs, ADRs, baseline files, and `AGENTS.md` files all agree with the solution design and the bootstrap canonical docs.
- The repository remains documentation-first and does not force premature framework or feature decisions beyond what the solution design or an accepted ADR already fixes.
- New directories and baseline files are durable and justified by the solution design and project shape.
- The adapted repository can move directly into deeper documentation work or implementation planning without another baseline rewrite.

Output expectations:

1. Show the final repository tree.
2. Create or update all required files with concise, actionable baseline content sourced from the canonical docs.
3. Summarize what changed in structure, documentation, baseline files, and `AGENTS.md` routing.
4. List assumptions made when the canonical docs were silent on optional dimensions.
5. List open decisions that the canonical docs do not yet resolve and that adaptation refused to guess about.
6. Call out any intentional deferrals that were avoided because they would start implementation too early.

Response format:

- `Canonical Inputs Read`
- `Preflight Result`
- `Assumptions`
- `Adapted Structure`
- `Documentation Updates`
- `Baseline File Updates`
- `AGENTS.md Routing Updates`
- `Quality Gate Results`
- `Open Decisions`

Non-goals:

- Do not ask the adopter for stack inputs that the canonical docs already capture.
- Do not infer or invent stack, framework, or deployment choices when the canonical docs are silent.
- Do not create feature code or business logic.
- Do not lock framework or dependency versions unless an accepted ADR or the solution design explicitly requires it.
- Do not make implementation-level architecture decisions that belong in later specs or plans.
- Do not replace the repository governance model with language-specific shortcuts.
