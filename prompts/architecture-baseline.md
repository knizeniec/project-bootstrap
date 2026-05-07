---
name: "Author The Architecture Baseline"
description: "Use after the project brief and PRD are solid to decide the language stack and technical approach, then produce the canonical architecture baseline (solution design and ADRs) that language-adaptation reads from."
argument-hint: "No required arguments. The prompt reads the project brief and PRD. Optionally provide a preferred language, framework, or deployment constraint to skip that part of the conversation."
agent: "agent"
---

Author the canonical architecture baseline for a project whose intent and requirements are already captured in the canonical docs.

Run this prompt after [`project-bootstrap.md`](project-bootstrap.md) and after the project brief and PRD have been iterated to a solid state. This prompt produces [`docs/03_architecture/01_solution_design.md`](../docs/03_architecture/01_solution_design_TEMPLATE.md) and the corresponding ADRs, which [`language-adaptation.md`](language-adaptation.md) reads as its primary source of truth. It does not generate implementation code or lock dependency versions.

Canonical input documents (read before doing anything else):

- [`docs/00_governance/00_project_brief.md`](../docs/00_governance/00_project_brief_TEMPLATE.md) — project name, problem, goals, scope, stakeholders, constraints, risks.
- [`docs/02_product/01_prd.md`](../docs/02_product/01_prd_TEMPLATE.md) — product scope, users, functional and non-functional requirements, user journeys, acceptance criteria.
- [`docs/adr/`](../docs/adr/) — any ADRs already accepted from the bootstrap phase.

Preflight gate (halt before asking anything if any of the following hold):

- [`docs/00_governance/00_project_brief.md`](../docs/00_governance/00_project_brief_TEMPLATE.md) or [`docs/02_product/01_prd.md`](../docs/02_product/01_prd_TEMPLATE.md) does not exist as an active instance file.
- Either file still contains template placeholder text `[Technical or system goal]`, `[TBD: ...]`, or other unfilled markers in the problem statement, goals, scope, or requirements sections.
- The project name, problem statement, or primary goals cannot be read from the files.

If any halt condition holds, list the missing or incomplete inputs precisely (file path, section, what is missing), point to [`project-bootstrap.md`](project-bootstrap.md) if the bootstrap docs are the problem, and stop. Do not infer missing facts.

Context extraction (before asking questions):
Read the input documents and summarise what you already know:

- Project name and one-sentence problem statement.
- Primary goals and success measures.
- Hard constraints from the project brief (compliance, performance, vendor, timeline, platform).
- Project type inferred from the PRD (service, web app, CLI, library, data pipeline, mobile, infrastructure, or hybrid).
- Scale expectations from the PRD non-functional requirements.
- Key integration points named in the PRD.
- Decisions already locked in accepted ADRs.

Present this summary to the user before asking any questions. Correct any misreads before proceeding.

Mandatory clarification gate:

- Block architecture generation until all required decisions below are explicit.
- Never invent answers; ask one targeted question per gap if the user's input is vague.
- Do not ask about information already captured clearly in the canonical docs.
- Required questions (ask only if not already resolved by the canonical docs or user arguments):
  - What language or languages will this project use?
  - What primary framework, runtime, or platform will be used per language?
  - What is the data storage approach? (relational, document, key-value, in-memory, flat files, no persistent storage, or a combination)
- Recommended follow-up questions (ask only the ones still unclear after required answers and context extraction):
  - What is the deployment target? (cloud provider and service type, containerised, serverless, bare metal, edge, local-only)
  - Is this a monolith, a set of separate services, or a hybrid? What is the rationale given the scale and team size?
  - Are there external systems this project must integrate with beyond what the PRD names?
  - Are there security or compliance requirements that constrain the stack or deployment shape?
  - What is the expected team size and operational ownership model at launch?
- Keep the conversation focused on durable structural decisions. Do not ask about library versions, internal module names, or implementation details.

Architecture approach proposal:

- After gathering required answers, propose two or three architecture approaches that fit the project requirements, chosen stack, and constraints.
- Each proposal must include:
  - a one-sentence summary of the approach,
  - the primary trade-off it favors (for example: operational simplicity vs. scalability, tight coupling vs. independent deployability, build-it vs. buy-it),
  - the structural shape it implies (number and nature of major components, data flow, deployment units),
  - at least one concrete risk or drawback.
- Ask the user to confirm or modify a direction before generating any documents.
- If the user's required answers already imply a single clear approach, present it as the proposed direction and ask for confirmation rather than forcing unnecessary alternatives.

Primary objective:

- Produce a complete, implementation-neutral architecture baseline that records the chosen stack, structural approach, and key technical decisions.
- Ensure the solution design is traceable to the project brief and PRD requirements.
- Record every durable technical decision made during this conversation as an ADR.
- Make the output ready to hand directly to [`language-adaptation.md`](language-adaptation.md) without further manual editing.

Document creation rules:

- Create [`docs/03_architecture/01_solution_design.md`](../docs/03_architecture/01_solution_design_TEMPLATE.md) from [`docs/03_architecture/01_solution_design_TEMPLATE.md`](../docs/03_architecture/01_solution_design_TEMPLATE.md). Fill every section:
  - **Goals and constraints**: derive from the project brief and PRD. Add technical goals and constraints the brief does not capture but that are implied by the chosen approach.
  - **Scope and system context**: derive from the PRD scope. Add the external systems and trust boundaries that the architectural choice introduces.
  - **Solution strategy**: explain the chosen approach in two to four sentences. State why it fits the goals and constraints extracted from the canonical docs.
  - **Building blocks**: name the major structural components or services and their single responsibility. Derive these from the PRD functional areas and the chosen architectural approach. Do not name internal modules or classes.
  - **Data, interfaces, and integrations**: summarise the data storage choice and rationale, any significant API or interface surfaces, and external integrations named in the PRD or conversation.
  - **Runtime and deployment view**: describe how work flows through the system at runtime, where the system runs, and the basic operational shape.
  - **Quality attributes and risks**: map NFRs from the PRD to the chosen approach. List risks introduced by the architecture and how they will be mitigated or accepted.
  - **Decision links**: list the ADRs created in this session.
- Create ADRs under [`docs/adr/`](../docs/adr/) from [`docs/adr/ADR-000-template.md`](../docs/adr/ADR-000-template.md) for every durable decision made during this conversation. Typical decisions that warrant an ADR:
  - language or runtime choice
  - primary framework choice
  - data storage approach
  - monolith vs. services vs. hybrid
  - deployment target or platform
  - significant security or compliance approach
  - any other structural choice that would be costly to reverse
  - Set `Status: Accepted`, `Date:` to the current date, and fill every section from the conversation.
  - Pick the next free `ADR-NNN` number. Use a short hyphenated topic in the filename.
  - Do not create an ADR for a decision the user did not explicitly make or confirm.
- Update [`docs/03_architecture/README.md`](../docs/03_architecture/README.md):
  - Add a `## Project documents` subsection listing the new solution design instance file, alongside any existing `## Starter templates` list.
- Update [`docs/INDEX.md`](../docs/INDEX.md):
  - Add the new solution design and any new ADRs under the Active tree. Use the same row format already in the file.
- Update [`docs/00-source-of-truth.md`](../docs/00-source-of-truth.md):
  - Add a row for the active solution design file after the existing solution design template row.
  - Add rows for new ADRs after the existing architecture decisions row.

Out-of-scope updates:

- Do not modify [`docs/Architecture.md`](../docs/Architecture.md), [`docs/00-documentation-standards.md`](../docs/00-documentation-standards.md), the existing `_TEMPLATE.md` files, any `AGENTS.md`, the project brief, the PRD, or any file outside the list above.
- Do not generate implementation code, configuration files, directory structure, or dependency specifications.
- Do not create documents in canonical areas the user has not engaged with (no delivery plan, no security runbook, no AI use policy).

TBD discipline:

- Replace each unanswered placeholder with `[TBD: <what is unknown>]`. Do not leave original template hints in place.
- Bump `Last updated:` to the current date on every file you touch.
- Set `Owner:` to a role the user named or to `[TBD: owner]` when no role was given.
- Do not pre-populate fields with plausible-sounding inventions. Empty is better than wrong.

Architecture baseline quality gate:

- The solution design is traceable: every goal, constraint, and requirement named in the solution design has a source in the project brief, PRD, or an accepted ADR.
- Every durable decision made during the conversation has a corresponding ADR.
- The solution design names the language(s), primary framework(s), data storage approach, and deployment shape explicitly — these are the fields [`language-adaptation.md`](language-adaptation.md) requires.
- No template placeholder text remains in the solution design.
- All internal links in created documents resolve to real paths in the current tree.
- No implementation code, version pins, or framework-specific configuration has been generated.

Output expectations:

1. Show the context summary extracted from the canonical docs and confirm it is correct before proceeding.
2. Show the final list of created and modified files.
3. List the architectural decisions made, each linked to its ADR.
4. List every `[TBD: ...]` marker grouped by file.
5. State that the repository is ready for [`language-adaptation.md`](language-adaptation.md) and list any open decisions the user should resolve first.

Response format:

- `Context Extracted`
- `Approach Proposed And Confirmed`
- `Created And Updated Files`
- `Decisions And ADRs`
- `Open TBDs`
- `Quality Gate Results`
- `Next Steps`

Non-goals:

- Do not choose implementation details, library versions, module names, or internal code structure.
- Do not generate code, configuration, directory structure, or sample data.
- Do not modify the documentation control spine, governance standards, or AGENTS.md files.
- Do not re-ask for information clearly captured in the project brief or PRD.
- Do not invent facts to fill gaps; use `[TBD: ...]` markers instead.
