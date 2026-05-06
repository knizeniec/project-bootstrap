---
name: "Industry Professional Standards"
description: "Use when planning, implementing, testing, documenting, or reviewing repository work. Enforces industry-standard engineering discipline and aligns repository-template outputs with required source-of-truth structure and governance controls."
applyTo: "**"
---

# Industry Professional Standards

Apply these standards to every task unless a user instruction explicitly overrides them.

## 0) Scope and Precedence

- User instructions and repository-specific AGENTS/CLAUDE rules override this file.
- This standard defines the minimum quality bar for engineering, documentation, and repo governance.
- For repository scaffolding/template work, this file is a compatibility contract with `.opencode/prompts/repo-template-prompt.md`.

## 1) Core Operating Principles

- Deliver value in small, reviewable increments.
- Keep agent replies short, straight to the point, and focused on only relevant information while preserving important context, decisions, risks, and verification details.
- Prefer clarity over cleverness.
- Make decisions based on evidence from code, tests, and documentation.
- Keep all changes traceable, testable, and reversible where practical.
- Treat maintainability as a first-class requirement, not a follow-up activity.

## 2) Engineering Quality Baseline

- Define scope before editing; avoid unrelated drive-by changes.
- Prefer root-cause fixes over symptom patches.
- Preserve backward compatibility unless explicitly changing contracts.
- Keep interfaces explicit and stable; document any behavior or API changes.
- Keep dependency usage intentional; avoid adding unnecessary packages/tools.
- Follow secure-by-default patterns and avoid introducing secrets or unsafe defaults.

## 3) Repository Template Compatibility Contract (Mandatory for Scaffolding Work)

When the task is to generate or update a repository template/skeleton, enforce all of the following:

### 3.1 Clarification Gate (Blockers)

- Do not generate a template until primary language/runtime is unambiguous.
- Do not generate a template until repository mode is confirmed (`single-project` or `monorepo`).
- If mode is `monorepo`, require decisions for dependency strategy, release/versioning strategy, and orchestration tool (or clearly state default assumptions).

### 3.2 Mandatory Root Structure

- Always include: `src/`, `bin/`, `scripts/`, `tests/`, `config/`, `examples/`, `diagrams/`, `docs/`.
- In `monorepo` mode also include: `apps/`, `packages/` or `libs/`, and `tools/` when applicable.

### 3.3 Mandatory Baseline Files

- Ensure practical skeletons exist for: `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.gitignore`, `.editorconfig`, `.gitattributes`.
- Ensure governance automation files exist: `.github/CODEOWNERS`, `.github/workflows/ci.yml`.
- License policy: keep `LICENSE` empty unless a specific license is explicitly requested.

### 3.4 Documentation Ownership Model Under `docs/`

- Required entrypoints: `docs/project/Architecture.md`, `docs/project/00-documentation-standards.md`, `docs/project/00-source-of-truth.md`, `docs/project/INDEX.md`.
- ADR canonical path: `docs/project/adr/`.
- Required ADR entrypoints: `docs/project/adr/README.md`, `docs/project/adr/ADR-000-template.md`.
- Active ownership roots are only:
  - `docs/project/00_governance/`
  - `docs/project/01_strategy/`
  - `docs/project/02_product/`
  - `docs/project/03_architecture/`
  - `docs/project/04_ai_governance/`
  - `docs/project/05_testing_acceptance/`
  - `docs/project/06_security_operations/`
  - `docs/project/07_delivery/`
  - `docs/project/08_references/`
- Supporting-only (not active owners): `docs/project/99_archive/`, `docs/superpowers/`.
- Do not create additional active source-of-truth roots.

### 3.5 Monorepo Enforcement Expectations

- Configure workspace discovery at repo root (ecosystem-appropriate manifest/config).
- Prefer single root lock/dependency snapshot when ecosystem supports it.
- Enforce package boundaries: no undeclared cross-project imports.
- Include dependency-graph strategy for affected-task execution.
- Define project taxonomy and machine-enforced dependency constraints.
- Define ownership and branch/ruleset policy requiring code-owner review for protected branches.
- CI must support affected-task execution with cache-aware fallback to full runs.
- Define release/versioning flow for multi-project changes, including changelog behavior and internal dependency bump policy.

### 3.6 Creation Compliance

- If a file is listed in the generated structure, create it with actionable skeleton content.
- Tree-only output is non-compliant.
- Every major folder should include a purpose/ownership `README.md` when part of generated scaffold output.
- For template generation, create documentation skeletons and baseline governance files only by default; do not create runtime/business code files unless explicitly requested.
- Initialize repository bootstrap when creating a new template scaffold:
  - run `git init` if the repository is not initialized,
  - add a best-practice polyglot `.gitignore` baseline (from authoritative public templates),
  - stage generated baseline files,
  - create the first commit with a clear scaffold/bootstrap message.
- Populate baseline files with minimal actionable content (not empty placeholders), except `LICENSE` when no explicit license is selected.
- Ensure `README.md` includes a concise repository overview and a rendered repository tree.
- Ensure `docs/project/00-documentation-standards.md` is initialized with a best-practice baseline (taxonomy, ownership, style, update policy, traceability, review cadence, change log).

### 3.7 Required Output Sections (for Template Generation Responses)

- `Assumptions`
- `Created Structure`
- `Documentation Ownership Model`
- `Branch Management Baseline`
- `Monorepo Enforcement Rules` (monorepo only)
- `CI and Release Strategy` (monorepo only)
- `Quality Gate Results`
- `Adoption Checklist`
- `Open Decisions`

### 3.8 ADR Source-of-Truth Protocol (Mandatory)

- Treat files under `docs/project/adr/` as the primary project source of truth for implementation decisions.
- Update ADRs before implementation begins when a decision changes.
- Do not modify ADR decisions during implementation except for approved factual-error corrections.
- ADRs must contain enough implementation guidance for successful execution without hidden assumptions.
- Other documentation under `docs/` is reference/supporting context (specs, plans, rationale) and must not override ADR decisions.

### 3.9 Superpowers Planning and Brainstorming Protocol (Mandatory)

- Superpowers plugin usage is mandatory for every change.
- Use `docs/project/adr/` as primary context for brainstorming and plan creation.
- Before implementation, create/update implementation specs and plans under:
  - `docs/superpowers/specs/`
  - `docs/superpowers/plans/`
- Default implementation execution mode is `subagent-driven-development` unless explicitly overridden by user instruction.
- `docs/superpowers/` files are historical implementation records; once implementation is complete, do not edit those completed spec/plan files. Create a new dated spec/plan for later changes.

### 3.10 Branch Management Baseline

- Prefer trunk-based development with short-lived branches for review and integration.
- Protect critical branches with rulesets/protection rules: required PR reviews, required checks, code-owner review, no force-push, no deletion.
- Define merge strategy (merge/squash/rebase), linear-history preference, and hotfix/release handling policy.
- For high-throughput repositories, define merge-queue policy and CI behavior for merge-group checks.

## 4) Test and Verification Discipline

- For behavior changes, add or update tests in the same task unless explicitly told not to.
- Run the smallest relevant verification first, then broaden as needed.
- Do not claim success without verification evidence.
- If verification cannot run, state what was not run, why, and the residual risk.
- Keep regression risk visible: call out edge cases, migrations, and compatibility concerns.

## 5) Documentation-as-Code Standard

- Documentation quality is part of done.
- Update docs in the same change when behavior, workflows, architecture, security posture, or operations change.
- Do not duplicate the same truth across multiple docs; keep one canonical owner and link to it.
- In documentation, link to relevant source files, ADRs, standards, and adjacent canonical docs instead of restating the same content.
- In code, when behavior depends on a policy/spec/ADR, add concise comments or docstrings that link to the owning document.
- Prefer concise, actionable docs with explicit assumptions, constraints, and acceptance criteria.
- Keep docs consistent with actual code behavior; if uncertain, verify from code/tests before writing.
- For major features/fixes or architecturally significant changes, create or update the relevant ADR before implementation starts.
- Treat completed files in `docs/superpowers/specs/` and `docs/superpowers/plans/` as immutable historical records.

Documentation template baseline (for major governance/architecture docs):
- Purpose
- Scope
- Owner
- Inputs
- Outputs
- Dependencies
- Review cadence
- Change log

## 6) Documentation Information Architecture

- Organize docs by reader need using a clear structure:
  - Tutorials: learning by doing.
  - How-to guides: task completion.
  - Reference: factual contracts, commands, interfaces.
  - Explanation: design rationale and tradeoffs.
- Keep operational runbooks, architecture decisions, and acceptance criteria easy to discover.
- Record significant architecture decisions in ADR-style format (context, decision, consequences, alternatives) under `docs/project/adr/`, and do this before implementation for major work.
- Use ADRs as the seed for Superpowers brainstorming and planning artifacts.
- Maintain traceability hooks across requirements, decisions, tests, and controls (IDs or equivalent).

## 7) Repository Files That Must Stay Current

When relevant to a change, update these files in the same task:

- README.md: setup, usage, behavior visible to users/operators.
- CHANGELOG.md: notable changes, human-readable release notes for release-ready work.
- CONTRIBUTING.md: contribution workflow or quality expectations.
- SECURITY.md: security policy, reporting, or hardening-relevant changes.
- CLAUDE.md and AGENTS.md: agent workflow rules, commands, constraints, and guardrails.
- docs/codebase/*.md and other architecture docs: current implementation truth.
- docs/project/adr/*: canonical implementation decisions.
- docs/superpowers/specs/* and docs/superpowers/plans/*: historical planning artifacts (append new files; do not rewrite completed ones).
- Update the nearest relevant AGENTS.md when scope-specific commands, constraints, ownership, or workflow guidance changes.

If a file does not need updates, state why.

## 8) Security and Compliance Baseline

- Security requirements must be explicit, testable, and mapped to controls where needed.
- For app-security-sensitive work, map verification to OWASP ASVS requirements (version-pinned references where possible).
- For enterprise/regulatory contexts, map operational controls to NIST SP 800-53 control families as applicable.
- Never commit credentials, keys, or secrets to repository history.

## 9) Changelog and Versioning Discipline

- Apply this section as a hard requirement for release-ready work. For non-release tasks, it is recommended but optional unless requested.
- Maintain a curated changelog for humans.
- Group notable changes consistently (Added, Changed, Deprecated, Removed, Fixed, Security).
- Keep an Unreleased section until release.
- Follow semantic versioning intent for externally visible changes:
  - Major: incompatible changes.
  - Minor: backward-compatible features.
  - Patch: backward-compatible fixes.

## 10) Commit and Review Quality Expectations

- Keep commits and PRs logically scoped and comprehensible.
- Enforce structured commit semantics for release-ready work (for example feat, fix, docs, refactor, test, chore, perf, ci). For non-release tasks, this is recommended unless explicitly required.
- Include clear change rationale and impact in summaries.
- Request review for meaningful implementation milestones.
- Treat critical and important review findings as blocking until resolved or explicitly justified.
- CODEOWNERS rules should map clearly to ownership boundaries and align with branch protection/rulesets.

## 11) Project Management and Execution Hygiene

- Keep plans concrete: objective, scope, constraints, acceptance criteria.
- Maintain transparent progress and decision logs.
- Surface risks, assumptions, and open questions early.
- For major features/fixes, establish decision context and ADR updates before implementation begins.
- For every change, run the Superpowers workflow with ADR context first; default implementation execution skill is `subagent-driven-development` unless user specifies otherwise.
- Define done criteria before implementation and validate against them before completion.
- Prefer sustainable pace and predictable delivery over high-risk batching.
- Use delivery metrics as feedback loops (for example DORA capabilities/metrics) to improve throughput and reliability over time.

## 12) Completion Checklist (Mandatory)

Before marking a task complete, confirm:

- Code changes are minimal, coherent, and aligned with requested scope.
- Tests and verification were run (or explicit gaps and risks are documented).
- Documentation and key repository files were updated or explicitly assessed as no-change.
- Relevant AGENTS.md files were updated when new scope-specific guidance would help future work.
- Security, performance, and compatibility implications were evaluated.
- Remaining risks, tradeoffs, and follow-up actions are clearly listed.
- For repo-template tasks: mandatory structure, docs ownership model, and required baseline files are all present and coherent.

## Standards Basis

These instructions align with established practices and references:

- Diátaxis documentation architecture: https://diataxis.fr/
- ADR guidance and templates: https://adr.github.io/
- Semantic Versioning 2.0.0: https://semver.org/
- Keep a Changelog 1.1.0: https://keepachangelog.com/en/1.1.0/
- GitHub CODEOWNERS guidance: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitHub rulesets guidance: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- GitHub protected branches guidance: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub merge queue guidance: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- Trunk-based development guide: https://trunkbaseddevelopment.com/
- Git branching workflows reference (Pro Git): https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows
- OWASP ASVS project standard: https://owasp.org/www-project-application-security-verification-standard/
- NIST SP 800-53 Rev. 5 control catalog: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- DORA research program: https://dora.dev/
