---
name: "Create Full Repository Template"
description: "Use when you need a complete repository template with baseline governance files, source-of-truth architecture controls, and initialized git scaffolding."
argument-hint: "Provide project name, domain, template profile (language-agnostic or language-specific), repository mode (monorepo or single-project), optional language/runtime, deployment target, and non-negotiable constraints (license optional)"
agent: "agent"
---

Create a complete repository template skeleton focused on documentation and governance, ready for project initiation without generating runtime/business code.

Use the user arguments as hard requirements.

Mandatory clarification gate:
- Template profile selection is required input: `language-agnostic` or `language-specific`.
- Repository mode selection is required input (`monorepo` or `single-project`).
- If template profile is `language-specific`, one primary language/runtime must be explicitly confirmed before generation.
- If template profile is `language-agnostic`, do not require language/runtime and do not generate language/framework-specific files.
- If input is vague, broad, or lists alternatives, ask follow-up questions and block generation until resolved.
- If repository mode is missing or ambiguous, ask and block generation until mode is confirmed.
- If repository mode is `monorepo`, require explicit decisions for:
  - dependency strategy (`single-version policy` or `independently maintained dependencies`)
  - release/versioning strategy (`fixed`, `independent`, or `hybrid`)
  - preferred monorepo orchestration tool (or choose a sensible default for the selected ecosystem and state the assumption)
- Preserve the mandatory top-level structure while keeping generated content language-neutral unless `language-specific` is explicitly requested.
- You may ask up to 5 concise clarification questions for other critical gaps.

Primary objective:
- Generate a repository skeleton with strong separation of concerns across directories, baseline governance files, and source-of-truth documentation.
- Ensure documentation is complete enough to guide implementation planning and execution.
- Do not generate project-specific runtime code files unless explicitly requested by the user.
- Default behavior for all template profiles is documentation-first scaffolding with baseline files only (no implementation code).
- Initialize repository bootstrap state (`git init`, baseline `.gitignore`, initial commit) as part of scaffold setup.

Mandatory top-level structure:
- `src/`
- `bin/`
- `scripts/`
- `tests/`
- `config/`
- `examples/`
- `diagrams/`
- `docs/`

Monorepo structural requirements (mandatory when repository mode is `monorepo`):
- Preserve the mandatory top-level structure above, and also add:
  - `apps/` for deployable applications/services
  - `packages/` or `libs/` for shared modules/libraries (choose ecosystem-appropriate naming)
  - `tools/` for repo-wide tooling where applicable
- Define a clear project discovery/workspace mechanism at repo root (ecosystem-appropriate workspace manifest/config).
- Create a single root lock/dependency snapshot file when the ecosystem supports it.
- Ensure each project unit has explicit metadata/manifests and task entrypoints.
- Prevent ambiguous nested project definitions unsupported by selected tooling.
- Enforce package boundaries: no cross-project `../` imports; only declared public APIs/exports and declared dependencies.
- Include a dependency graph strategy (native tool graph or equivalent metadata) to support affected-task computation.

Mandatory top-level baseline files (create practical skeleton versions):
- `README.md`
- `REPOSTORY_MAP.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `AGENTS.md`
- `.gitignore`
- `.editorconfig`
- `.gitattributes`

Mandatory governance/automation files:
- `.github/CODEOWNERS`
- `.github/workflows/ci.yml`

License policy:
- Always create a `LICENSE` file.
- Default: keep `LICENSE` intentionally empty.
- Only populate `LICENSE` content if the user explicitly selects a license type.

Documentation system requirements:

1) Required documentation entrypoints:
- `docs/project/Architecture.md`
- `docs/project/00-documentation-standards.md`
- `docs/project/00-source-of-truth.md`
- `docs/project/INDEX.md`
- `docs/project/adr/README.md`
- `docs/project/adr/ADR-000-template.md`

2) Active documentation tree rooted under `docs/project/`:
- `docs/project/00_governance/` (governance, project control, traceability ownership)
- `docs/project/01_strategy/` (strategy and tooling direction)
- `docs/project/02_product/` (product scope, journeys, requirements, acceptance)
- `docs/project/03_architecture/` (architecture, contracts, workflows, design decisions)
- `docs/project/04_ai_governance/` (scenario, approval, safety, quality governance)
- `docs/project/05_testing_acceptance/` (evaluation and acceptance baselines)
- `docs/project/06_security_operations/` (security, privacy, access, operating controls)
- `docs/project/07_delivery/` (delivery plan, rollout, handoff readiness)
- `docs/project/08_references/` (external references and due diligence)

Active ownership boundary:
- Only `docs/project/00_governance/` through `docs/project/08_references/` are active source-of-truth ownership folders.
- `docs/project/99_archive/` and `docs/superpowers/` are supporting-only and must not be treated as active source-of-truth owners.
- Do not create additional active source-of-truth ownership roots under `docs/project/`.

3) Supporting folders:
- `docs/project/99_archive/` (historical evidence only)
- `docs/superpowers/` (working history only)

4) Source-of-truth guardrail:
- Retired hyphen-named runtime folders and legacy nested enterprise-pack paths are not active source-of-truth owners after the reset.

5) Superpowers planning lifecycle:
- Treat `docs/project/adr/` as the input context for brainstorming and implementation planning.
- Store generated implementation specs/plans in `docs/superpowers/specs/` and `docs/superpowers/plans/`.
- Completed files in `docs/superpowers/` are historical references and must not be rewritten; create new dated files for later iterations.

Execution requirements:
- Build a complete directory and file skeleton, including `README.md` files inside major folders to explain purpose, ownership, and update rules.
- Create all required files physically/content-wise in the output scope. Do not provide only a proposed tree.
- If you mention a file in the generated structure, create it with at least a minimal actionable skeleton.
- Do not create language/framework-specific source code, executable scripts, or app/business logic by default.
- Create only documentation skeletons, baseline governance files, and folder/readme scaffolding unless user explicitly asks for concrete code/config implementations.
- Under `src/`, `bin/`, `scripts/`, `tests/`, `config/`, `examples/`, `diagrams/` (and `apps/`, `packages|libs`, `tools` in monorepos), create only folder-level `README.md` placeholders by default.
- Populate `README.md` with a concise repository overview and a pointer to `REPOSTORY_MAP.md`.
- Populate `REPOSTORY_MAP.md` with the repository directory tree as a quick search/reference map.
- Populate baseline files with minimal, actionable starter content (not empty placeholders), except `LICENSE` when no license is selected.
- `docs/project/00-documentation-standards.md` must be initialized with a best-practice baseline at minimum covering:
  - documentation taxonomy (Diátaxis: tutorial/how-to/reference/explanation),
  - ownership and source-of-truth rules,
  - style and formatting conventions,
  - docs update policy tied to code changes,
  - traceability expectations,
  - review cadence and change log.
- Initialize git repository state:
  - run `git init` if repository is not initialized,
  - create `.gitignore` using a best-practice polyglot baseline,
  - stage generated scaffold files,
  - create initial commit with a clear bootstrap message.
- Creation compliance rule:
  - If workspace file tools are available, create every listed file in the workspace.
  - If file tools are unavailable, provide full content for every listed file path directly in the response.
  - Tree-only output is non-compliant.
- If repository mode is `monorepo`, enforce these additional implementation requirements:
  - Create root orchestration and workspace discovery config files appropriate to the selected ecosystem.
  - Define project type taxonomy (for example feature/ui/data-access/util or equivalent) and machine-enforce dependency constraints between project types.
  - Generate a code ownership map in `.github/CODEOWNERS` aligned to directory boundaries and ownership responsibilities.
  - Define branch/ruleset policy documentation that requires code-owner review for protected branches.
  - Implement CI to run affected tasks by default, with cache-aware execution and safe fallback to full runs when affected detection is unavailable.
  - Define dependency governance for the chosen strategy (single-version or independent), including lockfile/update policy.
  - Define release/versioning workflow for multi-project changes, including changelog generation and internal dependency bump behavior.
  - Define shared-vs-app-local code placement rules and promotion criteria for moving app-local code into shared packages.
  - Define binary artifact handling policy (for example Git LFS or external artifact/object storage) to avoid degrading monorepo performance.
- Enforce separation of concerns: no mixed ownership between strategy, product, architecture, testing, security, delivery, and references.
- Avoid duplicated documentation content. Prefer canonical ownership + links to the owning document.
- Standardize document templates with consistent sections (purpose, scope, owner, inputs, outputs, dependencies, review cadence, change log).
- Create scoped `AGENTS.md` files using context routing instead of putting all agent guidance in root.
- Root `AGENTS.md` must stay minimal and contain only repo-wide guidance such as reply style, repository structure, global workflow, git/safety rules, and a routing map to deeper `AGENTS.md` files.
- Add the closest relevant `AGENTS.md` files for scoped rules when directories justify them. For this template, create at minimum:
  - `docs/AGENTS.md`
  - `docs/project/AGENTS.md`
  - `docs/superpowers/AGENTS.md`
  - `.github/AGENTS.md`
  - `.opencode/AGENTS.md`
  - `.opencode/instructions/AGENTS.md`
  - `src/AGENTS.md`
- Put the most important instructions first in each `AGENTS.md` file.
- `src/AGENTS.md` should hold coding best practices and implementation quality rules for source files.
- Root and scoped `AGENTS.md` files must preserve these expectations where relevant: concise-response style, ambiguity clarification when needed, context preservation, targeted file reads, tool-use discipline, and adherence to approved specs/plans.
- Root `AGENTS.md` must state that `AGENTS.md` files should be kept up to date when workflow or context-management guidance changes, or when new instructions would materially improve future work.
- Include traceability hooks across docs (for example IDs for requirements, architecture decisions, tests, and controls).
- Provide decision records under `docs/project/adr/` (ADR-compatible skeletons).
- Every ADR must explicitly state:
  - ADRs are the main project source of truth for implementation decisions.
  - ADRs must be updated before implementation begins when a decision changes.
  - ADRs are not modified mid-implementation except for pre-approved correction of factual errors.
  - ADR content must be sufficient for implementation to succeed without hidden assumptions.
  - Other `docs/` files are supporting references for context, specs, and plans, and must not override ADR decisions.
- Create a references index in `docs/project/08_references/` that captures standards, regulations, and external sources used.
- Ensure every key workflow and control has an owning document and an acceptance criterion.

Branch management baseline requirements:
- Default to trunk-based development with short-lived branches for review/integration.
- If explicit versioned-release workflows are requested, document release/hotfix branch policy and merge-back rules.
- Define protected-branch/ruleset policy for critical branches (required PR reviews, required checks, code-owner review, no force push, no deletion).
- Define merge strategy (merge/squash/rebase) and linear-history preference.
- For high-throughput repos, define merge queue policy and CI requirements for `merge_group` checks.

Research requirement:
- Apply recognized industry documentation practices (for example: architecture decision records, traceability matrices, verification gates, operational runbooks, security control mapping, and acceptance criteria alignment).
- If web/research tools are available, gather authoritative references and include them in `docs/project/08_references/` with short rationale for inclusion.
- Branch-management references should include at least one platform control source and one workflow model source.
- For `.gitignore`, prefer recognized public template sources (for example `github/gitignore` and/or gitignore.io) and document assumptions for the selected baseline.
- If tools are unavailable, use established best-practice patterns already known and mark assumptions explicitly.

Quality gates before finishing:
- Internal links are coherent and point to owning documents.
- No critical documentation domains are missing from the required tree.
- No direct contradictions between `docs/project/00-source-of-truth.md` and folder ownership.
- Skeleton content is actionable, not placeholder-only boilerplate.
- Generated template can be used immediately for real project initiation.
- Git repository is initialized and initial commit exists unless user explicitly opts out.
- In monorepo mode, verify all of the following:
  - Workspace discovery config, lockfile policy, and orchestration config are present and coherent.
  - Dependency boundaries are enforced by tooling (not just documented).
  - CODEOWNERS coverage exists for key paths and governance docs define protected-branch owner review requirements.
  - CI includes affected-task strategy and caching strategy with documented fallback behavior.
  - Release/versioning workflow is explicit and executable for multi-project changes.
  - Shared code rules prevent accidental cross-team coupling via undeclared/internal APIs.
  - Branch-management policy is explicit, enforceable, and aligned to CODEOWNERS/rulesets.

Output expectations:
1. Show the final repository tree.
2. Create all required files and folder readmes with concise but complete skeleton content.
3. Summarize source-of-truth ownership model and anti-duplication strategy.
4. Provide a short "adoption checklist" for teams using the template.
5. List assumptions and any user decisions still needed.
6. In monorepo mode, include dependency boundary rules and project taxonomy.
7. In monorepo mode, include ownership and branch protection summary.
8. In monorepo mode, include CI affected-task/caching model and release/versioning model.
9. Include branch management baseline summary.
10. Include git bootstrap summary (`git init`, `.gitignore` source strategy, initial commit message).

Response format:
- `Assumptions`
- `Created Structure`
- `Documentation Ownership Model`
- `Branch Management Baseline`
- `Monorepo Enforcement Rules` (required in monorepo mode)
- `CI and Release Strategy` (required in monorepo mode)
- `Quality Gate Results`
- `Adoption Checklist`
- `Open Decisions`

Non-goals:
- Do not add unrelated runtime code unless explicitly requested.
- Do not generate language/framework-specific code files by default.
- Do not introduce alternate documentation trees that conflict with the required schema.
