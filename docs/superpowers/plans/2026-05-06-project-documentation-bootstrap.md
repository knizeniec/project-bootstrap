# Project Documentation Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the repository documentation scaffold so it includes a robust ADR standard and a named starter template set for project governance, product, architecture, and delivery planning.

**Architecture:** Keep root `docs/` as the canonical documentation system, keep `docs/project/adr/` as the ADR authority surface, and add a small set of reusable `_TEMPLATE.md` files directly inside the numbered canonical areas. Update the control spine and area landing pages so the bootstrap flow is visible and navigable.

**Tech Stack:** Markdown documentation, repository routing rules, grep-based verification

---

### Task 1: Strengthen ADR Governance

**Files:**
- Modify: `docs/project/adr/README.md`
- Modify: `docs/project/adr/ADR-000-template.md`

- [ ] **Step 1: Add governance rules to the ADR README**

Add sections covering when ADRs are required, record rules, status lifecycle, roles, and supersession triggers.

- [ ] **Step 2: Expand the ADR template for planning readiness**

Add metadata and sections for consulted and informed parties, scope, tags, decision lineage, decision drivers, options considered, rationale, implementation impact, follow-up actions, and evidence.

- [ ] **Step 3: Verify ADR governance language is present**

Run: `rg -n "When to write an ADR|Status lifecycle|Supersedes|Implementation impact|Evidence and references" docs/project/adr`
Expected: matches in both ADR files.

### Task 2: Add Canonical Bootstrap Templates

**Files:**
- Create: `docs/00_governance/00_project_brief_TEMPLATE.md`
- Create: `docs/00_governance/12_requirements_traceability_matrix_TEMPLATE.md`
- Create: `docs/02_product/01_prd_TEMPLATE.md`
- Create: `docs/03_architecture/01_solution_design_TEMPLATE.md`
- Create: `docs/03_architecture/06_interface_control_document_TEMPLATE.md`
- Create: `docs/07_delivery/01_delivery_plan_TEMPLATE.md`
- Create: `docs/07_delivery/02_implementation_plan_TEMPLATE.md`

- [ ] **Step 1: Add governance starter templates**

Create the project brief and requirements traceability matrix templates in `docs/00_governance/`.

- [ ] **Step 2: Add product and architecture starter templates**

Create the PRD, solution design, and interface control document templates in their canonical directories.

- [ ] **Step 3: Add delivery starter templates**

Create the delivery plan and implementation plan templates in `docs/07_delivery/`.

- [ ] **Step 4: Verify template files exist**

Run: `test -f docs/00_governance/00_project_brief_TEMPLATE.md && test -f docs/00_governance/12_requirements_traceability_matrix_TEMPLATE.md && test -f docs/02_product/01_prd_TEMPLATE.md && test -f docs/03_architecture/01_solution_design_TEMPLATE.md && test -f docs/03_architecture/06_interface_control_document_TEMPLATE.md && test -f docs/07_delivery/01_delivery_plan_TEMPLATE.md && test -f docs/07_delivery/02_implementation_plan_TEMPLATE.md`
Expected: command exits successfully.

### Task 3: Update Navigation And Ownership Surfaces

**Files:**
- Modify: `docs/README.md`
- Modify: `docs/Architecture.md`
- Modify: `docs/INDEX.md`
- Modify: `docs/00-source-of-truth.md`
- Modify: `docs/00_governance/README.md`
- Modify: `docs/02_product/README.md`
- Modify: `docs/03_architecture/README.md`
- Modify: `docs/07_delivery/README.md`
- Modify: `docs/00-documentation-standards.md`

- [ ] **Step 1: Add bootstrap-template discovery to root docs entrypoints**

Update the control spine so users can find the new starter templates from the root docs surfaces.

- [ ] **Step 2: Add template references to area landing pages**

Update the governance, product, architecture, and delivery landing pages so each area points to its starter templates.

- [ ] **Step 3: Update ownership and standards text**

Update the source-of-truth map and documentation standards so the new starter templates are reflected in ownership and structure guidance.

- [ ] **Step 4: Verify discovery paths are wired**

Run: `rg -n "_TEMPLATE.md|starter template|bootstrap" docs/README.md docs/Architecture.md docs/INDEX.md docs/00-source-of-truth.md docs/00_governance/README.md docs/02_product/README.md docs/03_architecture/README.md docs/07_delivery/README.md docs/00-documentation-standards.md`
Expected: matches across the updated navigation and area files.

### Task 4: Record The Change In Working History And Validate Usability

**Files:**
- Create: `docs/superpowers/specs/2026-05-06-project-documentation-bootstrap-design.md`
- Create: `docs/superpowers/plans/2026-05-06-project-documentation-bootstrap.md`
- Modify: `REPOSTORY_MAP.md`

- [ ] **Step 1: Save the approved design record**

Create the bootstrap design record in `docs/superpowers/specs/`.

- [ ] **Step 2: Save the implementation plan record**

Create the bootstrap implementation plan in `docs/superpowers/plans/`.

- [ ] **Step 3: Update the repository map**

Add the new docs files to `REPOSTORY_MAP.md` so the scaffold remains discoverable.

- [ ] **Step 4: Validate there are no stale references to the old bootstrap shape**

Run: `rg -n "docs/project/(00_|01_|02_|03_|04_|05_|06_|07_|08_|99_archive|Architecture\.md|INDEX\.md|00-source-of-truth\.md)" .`
Expected: no matches.

- [ ] **Step 5: Manually walk the docs flow**

Read, in order: `docs/README.md`, `docs/INDEX.md`, `docs/00_governance/00_project_brief_TEMPLATE.md`, `docs/02_product/01_prd_TEMPLATE.md`, `docs/03_architecture/01_solution_design_TEMPLATE.md`, `docs/project/adr/ADR-000-template.md`, and `docs/07_delivery/02_implementation_plan_TEMPLATE.md`.
Expected: the bootstrap flow is understandable from entrypoint to execution planning.
