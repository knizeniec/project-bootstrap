---
title: Source-of-Truth Map
status: active
record_class: canonical
audience: [internal, manager]
owner: Documentation maintainers
capability: operating_model
phase: n/a
cadence: monthly
last_reviewed: 2026-05-07
---

# Source-of-Truth Map

> **Purpose**: name the active owner for each documentation concern.
> **Audience**: contributors and reviewers deciding where current guidance belongs.
> **When to update**: update when canonical ownership, folder structure, or starter-template coverage changes.

Use this file to find the one active document or landing page that owns a topic. Supporting documents may explain or evidence that topic, but they do not override the owner named here.

## Terms

- `template`: a reusable `_TEMPLATE.md` starter file
- `active document`: a project-specific document that governs current work
- `historical record`: a non-canonical planning or archive document

## Ownership map

| Concern | Canonical file | Notes |
| --- | --- | --- |
| Docs entrypoint | [README.md](README.md) | Start here for the active documentation system. |
| Docs structure | [Architecture.md](Architecture.md) | Defines the shape of the active docs system. |
| Docs standards | [00-documentation-standards.md](00-documentation-standards.md) | Writing, ownership, and update rules. |
| Docs navigation | [INDEX.md](INDEX.md) | Hand-maintained navigation map for the active tree. |
| Operating model | [00_operating_model/README.md](00_operating_model/README.md) | Owns lifecycle, audience, schema, naming, and tailoring orientation. |
| Lifecycle map | [00_operating_model/01_lifecycle_map.md](00_operating_model/01_lifecycle_map.md) | Defines lifecycle phases and expected evidence. |
| Role and audience map | [00_operating_model/02_role_audience_map.md](00_operating_model/02_role_audience_map.md) | Defines role-based reading paths and audience tags. |
| Frontmatter schema | [00_operating_model/04_frontmatter_schema.md](00_operating_model/04_frontmatter_schema.md) | Defines valid frontmatter keys, enums, and validation behavior. |
| Governance | [00_governance/README.md](00_governance/README.md) | Owns governance, controls, and traceability documents. |
| Project brief template | [00_governance/00_project_brief_TEMPLATE.md](00_governance/00_project_brief_TEMPLATE.md) | Starter template for project framing, stakeholders, constraints, and success measures. |
| Requirements traceability template | [00_governance/12_requirements_traceability_matrix_TEMPLATE.md](00_governance/12_requirements_traceability_matrix_TEMPLATE.md) | Starter template for requirement-to-design-to-verification linking. |
| Strategy | [01_strategy/README.md](01_strategy/README.md) | Owns strategic framing, priorities, and direction. |
| Product | [02_product/README.md](02_product/README.md) | Owns scope, requirements, journeys, and acceptance framing. |
| PRD template | [02_product/01_prd_TEMPLATE.md](02_product/01_prd_TEMPLATE.md) | Starter template for product problem, scope, requirements, and acceptance. |
| Architecture | [03_architecture/README.md](03_architecture/README.md) | Owns system design, integration boundaries, and technical patterns. |
| Solution design template | [03_architecture/01_solution_design_TEMPLATE.md](03_architecture/01_solution_design_TEMPLATE.md) | Starter template for architecture baseline, boundaries, and quality concerns. |
| Interface control template | [03_architecture/06_interface_control_document_TEMPLATE.md](03_architecture/06_interface_control_document_TEMPLATE.md) | Starter template for contracts, interfaces, and integration boundaries. |
| AI governance | [04_ai_governance/README.md](04_ai_governance/README.md) | Owns model-use policy, approvals, evaluation, and oversight. |
| AI use policy template | [04_ai_governance/01_ai_use_policy_TEMPLATE.md](04_ai_governance/01_ai_use_policy_TEMPLATE.md) | Starter template for AI approved use, restrictions, approval workflow, and oversight. |
| Testing and acceptance | [05_testing_acceptance/README.md](05_testing_acceptance/README.md) | Owns verification, acceptance, and quality evidence structure. |
| Security and operations | [06_security_operations/README.md](06_security_operations/README.md) | Owns security controls, runbooks, and incident handling. |
| Delivery | [07_delivery/README.md](07_delivery/README.md) | Owns roadmap, release, rollout, and handoff planning. |
| Delivery plan template | [07_delivery/01_delivery_plan_TEMPLATE.md](07_delivery/01_delivery_plan_TEMPLATE.md) | Starter template for milestones, dependencies, risks, and rollout planning. |
| Implementation plan template | [07_delivery/02_implementation_plan_TEMPLATE.md](07_delivery/02_implementation_plan_TEMPLATE.md) | Starter template for workstreams, sequencing, and validation gates. |
| References | [08_references/README.md](08_references/README.md) | Owns external references and standards inputs. |
| User documentation | [09_user_documentation/README.md](09_user_documentation/README.md) | Owns end-user tutorials, how-to guides, reference, explanation, changelog, and release notes. |
| Architecture decisions | [adr/README.md](adr/README.md) | Owns durable implementation decisions and ADR authoring rules. |
| Working-history policy | [superpowers/README.md](superpowers/README.md) | Owns historical records for specs, plans, and tracked work. |
| Archive policy | [99_archive/README.md](99_archive/README.md) | Owns rules for historical evidence and retired material. |
| Adoption prompts | [../prompts/README.md](../prompts/README.md) | Owns adoption-time prompts that adapt this template to a chosen language stack. |
| Architecture baseline prompt | [../prompts/architecture-baseline.md](../prompts/architecture-baseline.md) | Guides the stack decision conversation and generates the solution design and ADRs. |

## Rule

Keep one active owner per concern. If a rule, requirement, or decision still matters, move it into the active root docs tree or the relevant ADR instead of duplicating it elsewhere.

## Related documents

- [README.md](README.md) — root orientation for new contributors.
- [Architecture.md](Architecture.md) — shows how the owned surfaces fit together.
- [00-documentation-standards.md](00-documentation-standards.md) — defines how owned docs should be written and maintained.
- [00_operating_model/03_source_of_truth_map.md](00_operating_model/03_source_of_truth_map.md) — operating-model guidance for tool boundaries and mirroring.
- [INDEX.md](INDEX.md) — navigates the currently active tree.
