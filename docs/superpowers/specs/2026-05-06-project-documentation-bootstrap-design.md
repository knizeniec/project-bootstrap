# Project Documentation Bootstrap Design

**Goal:** Define a reusable project-management and planning bootstrap for this repository that keeps active documentation in root `docs/`, keeps ADRs in `docs/project/adr/`, and gives future projects named starter templates for governance, product, architecture, and delivery work.

## Context

The repository already has a root `docs/` control spine and numbered canonical areas, but it only provides high-level landing pages and a thin ADR template. That is enough for documentation structure, but not enough to start a real project with traceable requirements, architecture, delivery planning, and implementation planning.

Research on ADR practice and project-planning documentation showed two important constraints:

1. ADRs should stay focused on a single durable decision, with lineage and clear rationale, instead of absorbing all project-bootstrap needs.
2. Project bootstrap needs a small linked set of templates so scope, requirements, solution design, interfaces, delivery, and execution can each live in the correct canonical area.

## Design decisions

### 1. Keep the canonical docs root unchanged

Root `docs/` remains the active source-of-truth tree. The numbered areas remain the canonical home for governance, product, architecture, and delivery documentation. `docs/superpowers/` remains working history. `docs/project/adr/` remains the canonical ADR location.

### 2. Strengthen ADR governance instead of replacing ADRs

The ADR README and template should be upgraded to support:

- decision triggers
- stable naming and one-decision-per-record rules
- explicit status lifecycle
- supersession and lineage
- role clarity for author, decider, consulted, and informed parties
- planning-strength fields for impact, validation, follow-up actions, and evidence

### 3. Add a small named starter template set in canonical areas

The bootstrap should add these named templates:

- `docs/00_governance/00_project_brief_TEMPLATE.md`
- `docs/00_governance/12_requirements_traceability_matrix_TEMPLATE.md`
- `docs/02_product/01_prd_TEMPLATE.md`
- `docs/03_architecture/01_solution_design_TEMPLATE.md`
- `docs/03_architecture/06_interface_control_document_TEMPLATE.md`
- `docs/07_delivery/01_delivery_plan_TEMPLATE.md`
- `docs/07_delivery/02_implementation_plan_TEMPLATE.md`

These files are reusable starters, not project-specific content. Each one should explain how to use the template, what concern it owns, and how it links to adjacent canonical documents.

### 4. Make templates discoverable from the control spine and area landing pages

The root docs entrypoints and relevant numbered-area landing pages should point to these starter templates so a new project can begin without guessing where the first real document belongs.

## Boundaries

- Do not move active project documentation back under `docs/project/`; that area stays ADR-only.
- Do not put project-specific data into the starter templates.
- Do not turn `docs/superpowers/` into source-of-truth documentation.
- Do not add more template files than needed for the approved bootstrap.

## Expected outcome

After this change, the repository will support a coherent documentation bootstrap flow:

1. Start with a project brief.
2. Define requirements in the PRD.
3. Trace those requirements in the requirements matrix.
4. Design the solution and interfaces in architecture docs.
5. Record durable decisions in ADRs.
6. Plan delivery and implementation in the delivery area.

That flow should be visible directly from the active docs tree.
