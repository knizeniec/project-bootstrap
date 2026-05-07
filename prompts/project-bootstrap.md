---
name: "Bootstrap A New Project's Documentation Baseline"
description: "Use as the very first action against a fresh clone of this template. Captures project intent and produces a first-pass set of canonical documents (project brief, PRD, refreshed root README, optional initial ADR) that later prompts and implementation work refine."
argument-hint: "Provide project name, what the project needs to achieve in one or two sentences, and a short description of the planned product. Optional: target users, deployment context, known constraints, explicit non-goals."
agent: "agent"
---

Bootstrap a new project's canonical documentation baseline.

This prompt runs against a fresh, unspecialized clone of the template **before** [`language-adaptation.md`](language-adaptation.md). It captures the project's intent and generates first-pass canonical documents that later prompts and implementation work will refine. It does not pick a language stack, framework, runtime, or implementation approach.

Use the user arguments as hard requirements.

Mandatory clarification gate:

- Block document generation until all required inputs below are explicit. Never invent answers; ask one targeted question per gap if the user's input is vague.
- Required questions:
  - What is the project name?
  - In one or two sentences, what does the project need to achieve?
  - In two to four sentences, what is the planned product? Cover what it does, who uses it, and what the user experience looks like.
- Recommended follow-up questions (ask only the ones still unclear after the required answers):
  - Who are the primary users or stakeholders, and which of them are accountable owners?
  - What is the deployment context (web service, CLI tool, mobile app, internal tool, library, data pipeline, infrastructure project, hybrid)?
  - Are there hard constraints (compliance, performance, regulatory, vendor, internal platform, deadline) that affect scope?
  - Are there explicit non-goals or out-of-scope items the team has already excluded?
  - Is there an existing system being replaced or extended?
  - What is the rough scale of expected usage at launch (orders of magnitude, not exact numbers)?
- Keep the conversation focused on intent, scope, and outcome. Do not ask about implementation details, frameworks, or runtimes during this gate.

Approach proposal:

- After the required answers are gathered, propose two or three reasonable directions the project could take. Each proposal must include:
  - a one-sentence summary of the approach,
  - the trade-off it favors (for example: speed-of-delivery vs. extensibility, monolith vs. service-oriented, batteries-included vs. minimal, on-premises vs. managed),
  - a non-binding indication of which tech-stack family typically fits the approach, framed explicitly as "options to consider" — never as a decision,
  - at least one alternative the user might prefer instead.
- Make it explicit in the conversation and in any document you write that these proposals are starting points, not chosen directions. The chosen direction is recorded later in [`language-adaptation.md`](language-adaptation.md) and in ADRs under [`docs/adr/`](../docs/adr/README.md).
- If the project description is too narrow or specific to admit alternatives, ask one clarifying question first instead of forcing alternatives.
- If the user explicitly commits to a durable direction during this conversation (for example: open-source vs proprietary release, single-tenant vs multi-tenant, regulated environment), record that decision in an ADR per the document creation rules below. Do not record decisions the user did not make.

Primary objective:

- Produce a first-pass canonical documentation baseline that captures intent, scope, and requirements.
- Keep all documents implementation-neutral. No language pinning, no framework choice, no version locks.
- Make it easy for the user to iterate on these documents later as scope sharpens.
- Use explicit `[TBD: <what is unknown>]` markers in every spot the user did not answer, so future iteration is targeted and greppable.

Document creation rules:

- Always create or overwrite the following first-pass files using the matching `_TEMPLATE.md` as the starting point:
  - [`docs/00_governance/00_project_brief.md`](../docs/00_governance/00_project_brief_TEMPLATE.md) from [`docs/00_governance/00_project_brief_TEMPLATE.md`](../docs/00_governance/00_project_brief_TEMPLATE.md). Fill project name, sponsor, problem statement, target outcome, goals, success measures, in-scope and out-of-scope items, stakeholders and roles, constraints, assumptions, risks, dependencies, governance and approval model.
  - [`docs/02_product/01_prd.md`](../docs/02_product/01_prd_TEMPLATE.md) from [`docs/02_product/01_prd_TEMPLATE.md`](../docs/02_product/01_prd_TEMPLATE.md). Fill problem and opportunity, target outcome, primary and secondary users, stakeholders, goals, non-goals, in-scope and out-of-scope items, an initial functional requirements table (use sequential `FR-001`, `FR-002` IDs even if some rows are TBD), an initial non-functional requirements table (`NFR-001`, `NFR-002`), user journeys, acceptance criteria, dependencies and risks.
- Update the root [`README.md`](../README.md):
  - Replace the H1 (`# Universal Repository Template`) with `# <project name>`.
  - Replace the lead paragraph with the product description gathered from the user.
  - Drop the template-only `## Good fit` and `## Less ideal` sections.
  - Preserve the `## Bootstrap checklist`, `## Adapt to your stack`, `## Top-level layout`, `## Documentation model`, and `## Optional local tooling` sections so the adopter still has the next-step pointers and structural reference.
  - Do not invent a quick-start, status, or installation section. Those are added later, language-specific, and belong to the adaptation step.
- Update [`docs/00_governance/README.md`](../docs/00_governance/README.md) and [`docs/02_product/README.md`](../docs/02_product/README.md):
  - Add a `## Project documents` subsection that lists the new instance file(s) for that area, alongside the existing `## Starter templates` list.
  - Do not remove or rename the starter-template entries; templates remain available for reuse.
- Update [`docs/INDEX.md`](../docs/INDEX.md):
  - Add the new instance files under the Active tree, listed below the area landing pages they belong to. Use the same row format already in the file.
  - Leave the Bootstrap starter templates section unchanged.
- Update [`docs/00-source-of-truth.md`](../docs/00-source-of-truth.md):
  - Add rows for the new instance files (active project brief, active PRD). Place them after the existing rows for their area landing pages.
  - Do not remove the existing template rows.
- Optional: create [`docs/adr/ADR-001-<topic>.md`](../docs/adr/ADR-000-template.md) from [`docs/adr/ADR-000-template.md`](../docs/adr/ADR-000-template.md) only if the user explicitly committed to a durable decision during this conversation.
  - Set `Status: Proposed`, `Date:` to the current date, and fill the context, decision drivers, options considered, decision, and consequences sections from the conversation.
  - Pick the next free `ADR-NNN` number. Use a short hyphenated topic in the filename.
  - Do not invent a decision the user did not explicitly make.

Out-of-scope updates:

- Do not modify [`docs/Architecture.md`](../docs/Architecture.md), [`docs/00-documentation-standards.md`](../docs/00-documentation-standards.md), the existing `_TEMPLATE.md` files, any `AGENTS.md`, or any file outside the list above.
- Do not create documents in canonical areas the user has not engaged with (no security-operations runbook, no delivery plan, no AI use policy from a one-line product description).

TBD discipline:

- Replace each unanswered placeholder with `[TBD: <what is unknown>]`. Keep the marker inline; do not leave the original square-bracket template hint in place.
- Bump `Last updated:` to the current date on every file you touch.
- Set `Owner:` to a role the user named or to `[TBD: owner]` when no role was given.
- Do not pre-populate fields with plausible-sounding inventions. Empty is better than wrong.

Adopter handoff:

- After generation, summarize what was created, list every `[TBD: ...]` marker grouped by file, and recommend that the user run [`language-adaptation.md`](language-adaptation.md) next.
- Recommend that any durable decision the user makes between now and language-adaptation be recorded as an ADR per the rule above.

Project bootstrap quality gate:

- Documents reflect the user's actual answers, not invented detail.
- Every file is implementation-neutral. No language, framework, runtime, or version pinning leaks into any file.
- Tech-stack proposals are framed as options, not decisions, in any file that mentions them.
- Every unfilled section uses an explicit `[TBD: ...]` marker.
- Required frontmatter (`Status`, `Owner`, `Purpose`, `Last updated`) is present on every created or updated canonical document.
- All internal links in the created documents resolve to real paths in the current tree.

Output expectations:

1. Show the final list of created and modified files.
2. List the gathered project facts that drove generation.
3. Summarize the proposed approaches that were offered and which (if any) the user confirmed.
4. List every `[TBD: ...]` marker grouped by file, so the user has a punch list.
5. State the recommended next step ([`language-adaptation.md`](language-adaptation.md)) and any decisions the user should record as ADRs first.

Response format:

- `Gathered Facts`
- `Proposed Approaches`
- `Created And Updated Files`
- `Open Decisions And TBDs`
- `Quality Gate Results`
- `Next Steps`

Non-goals:

- Do not pick a language, framework, or runtime. That happens in [`language-adaptation.md`](language-adaptation.md) or via an explicit ADR.
- Do not generate code, configuration, infrastructure, or sample data.
- Do not create docs in canonical areas the user has not engaged with.
- Do not invent facts to fill gaps; use `[TBD: ...]` markers instead.
- Do not modify the documentation control spine, governance standards, AGENTS.md files, or starter `_TEMPLATE.md` files.
