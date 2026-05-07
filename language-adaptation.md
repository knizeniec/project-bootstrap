---
name: "Adapt Language-Agnostic Template To Language Stack"
description: "Use when you need to adapt an existing language-agnostic repository template to one or more specific languages and technologies without starting implementation."
argument-hint: "Provide target language(s), primary technologies, optional deployment target, optional short project description, and constraints that affect baseline structure."
agent: "agent"
---

Adapt an already-created language-agnostic repository template into a language-aware project baseline without generating implementation code.

Use the user arguments as hard requirements.

Mandatory clarification gate:
- Ask concise follow-up questions and block adaptation until all required decisions below are explicit.
- Required questions:
  - What language or languages should this repository support?
  - What primary technologies, frameworks, runtimes, or platforms will be used for each language?
- Optional but recommended questions:
  - What deployment target or runtime environment is expected?
  - Give a short project description so the baseline can include the always-needed structure for this project type.
  - Is this repository `single-project` or `monorepo` if the current structure does not make that unambiguous?
  - If multiple languages are selected, which directories, apps, packages, or responsibilities belong to each language?
  - Is the project mainly a library, service, web app, CLI, worker, data pipeline, mobile app, desktop app, infrastructure project, or a hybrid?
  - Are there durable top-level needs that should exist from day one, such as API surface docs, migrations, assets, infrastructure, SDKs, jobs, schemas, or public/static content?
  - Are there organization constraints that affect baseline structure, such as package registry choice, container use, CI platform, compliance requirements, or internal deployment conventions?
- If the project description is omitted, add only the structural baseline that is necessary regardless of project type and state assumptions clearly.
- Keep clarification focused on structure and documentation readiness, not implementation details.

Primary objective:
- Adapt the repository so it is structurally ready for the selected language stack.
- Keep the repository documentation-first and implementation-neutral.
- Make the repository ready to start project documentation and later implementation without needing another baseline restructure.
- Do not generate business logic, feature code, or implementation-specific application behavior.

Adaptation rules:
- Preserve the existing repository governance model, documentation ownership model, and routed `AGENTS.md` structure.
- Add only directories and files that are durable for the chosen language stack or project type.
- Do not choose dependency versions, framework versions, or implementation-layer libraries unless the user explicitly provides them and they are required for a baseline contract.
- Do not generate endpoints, components, services, domain models, or concrete runtime workflows.
- Prefer clear ownership boundaries and future-proof structure over convenience placeholders.

Repository structure updates:
- Keep the required top-level scaffold unless the user explicitly changes repository mode.
- Add language-specific structural directories only when they will clearly remain useful through implementation.
- For single-language projects, adapt `src/`, `tests/`, `config/`, `scripts/`, `examples/`, and other baseline directories to match ecosystem expectations without adding feature code.
- For multi-language projects, create explicit boundaries for each language and for shared assets, tools, or interface contracts.
- If the project description implies durable architectural areas, add only the empty structural folders and folder-level `README.md` files needed to support that project type.
- If deployment information is provided and it affects long-lived structure, add only stable deployment-facing placeholders such as infrastructure, deployment config, container, or environment documentation folders.

Documentation updates:
- Update `README.md` with a concise overview of the selected language stack and keep it pointing to `REPOSTORY_MAP.md`.
- Update `REPOSTORY_MAP.md` so it reflects the adapted repository tree and remains a quick reference for search.
- Update `docs/project/Architecture.md` with the selected language/languages, major technology choices, structural boundaries, and deployment assumptions if provided.
- Update `docs/project/00-source-of-truth.md` with where language, tooling, and project-structure decisions live.
- Update `docs/project/00-documentation-standards.md` with naming, layout, and documentation expectations introduced by the selected language stack.
- Update `docs/project/INDEX.md` so the new stack- or structure-relevant docs are discoverable.
- Create or update ADRs under `docs/project/adr/` when language, technology direction, repository mode, or structural ownership decisions become part of the project baseline.
- If deployment or operations details are provided, update the relevant docs under `docs/project/06_security_operations/` and `docs/project/07_delivery/` with baseline ownership and assumptions.

Baseline file updates:
- Update `.gitignore`, `.editorconfig`, and `.gitattributes` to fit the selected language stack.
- Add ecosystem baseline files only when they are long-lived structural contracts and not premature implementation choices.
- Keep baseline config files minimal, actionable, and free of implementation-specific dependencies where possible.
- Update `CONTRIBUTING.md`, `SECURITY.md`, and other operator-facing baseline files when the selected stack changes workflow expectations.
- Do not introduce concrete application dependencies or version pinning unless the user explicitly requires them for the baseline.

`AGENTS.md` adaptation requirements:
- Preserve context routing: keep root `AGENTS.md` minimal and place scoped rules in the closest relevant directory.
- Update root `AGENTS.md` with high-level project facts that matter repo-wide, including selected language/languages, concise project description if provided, and routing to any new scoped `AGENTS.md` files.
- Update `src/AGENTS.md` with language-specific coding best practices, structural conventions, and quality expectations for the selected language/languages.
- If multiple languages or major subdomains justify it, add deeper scoped `AGENTS.md` files for those directories instead of crowding root or `src/AGENTS.md`.
- Ensure relevant `AGENTS.md` files include project-specific information that improves workflow and context management, including selected languages, project description when provided, and best-practice guidance for the chosen stack.
- Keep the most important instructions first in every `AGENTS.md` file.
- Keep `AGENTS.md` files up to date whenever new workflow or context-management guidance would materially improve future work.

Language adaptation quality gate:
- The final tree reflects the selected language stack and project type without implementation code.
- Docs, ADRs, baseline files, and `AGENTS.md` files all agree on the selected language/languages and technology direction.
- The repository remains documentation-first and does not force premature framework or feature decisions.
- New directories and baseline files are durable and justified by the selected stack or project description.
- The adapted repository can move directly into project documentation and implementation planning without another baseline rewrite.

Output expectations:
1. Show the final repository tree.
2. Create or update all required files with concise, actionable baseline content.
3. Summarize what changed in structure, documentation, baseline files, and `AGENTS.md` routing.
4. List assumptions and open decisions that still need user input.
5. Call out any intentional deferrals that were avoided because they would start implementation too early.

Response format:
- `Assumptions`
- `Adapted Structure`
- `Documentation Updates`
- `Baseline File Updates`
- `AGENTS.md Routing Updates`
- `Quality Gate Results`
- `Open Decisions`

Non-goals:
- Do not create feature code or business logic.
- Do not lock framework or dependency versions unless explicitly required.
- Do not make implementation-level architecture decisions that belong in later specs or plans.
- Do not replace the repository governance model with language-specific shortcuts.
