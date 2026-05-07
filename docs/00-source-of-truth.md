# Source-of-Truth Map

Status: Active
Owner: Documentation maintainers
Purpose: name the canonical owner for each active documentation concern
Last updated: 2026-05-06

Use this file to find the one document or landing page that owns a topic. Supporting documents may explain or evidence that topic, but they do not override the owner named here.

| Concern | Canonical file | Notes |
|---|---|---|
| Docs entrypoint | [README.md](README.md) | Start here for the active documentation system. |
| Docs structure | [Architecture.md](Architecture.md) | Defines the shape of the active docs system. |
| Docs standards | [00-documentation-standards.md](00-documentation-standards.md) | Writing, ownership, and update rules. |
| Docs navigation | [INDEX.md](INDEX.md) | Compact navigation map for the active tree. |
| Governance | [00_governance/README.md](00_governance/README.md) | Owns governance, controls, and traceability documents. |
| Project brief template | [00_governance/00_project_brief_TEMPLATE.md](00_governance/00_project_brief_TEMPLATE.md) | Starter for project framing, stakeholders, constraints, and success measures. |
| Requirements traceability template | [00_governance/12_requirements_traceability_matrix_TEMPLATE.md](00_governance/12_requirements_traceability_matrix_TEMPLATE.md) | Starter for requirement-to-design-to-verification linking. |
| Strategy | [01_strategy/README.md](01_strategy/README.md) | Owns strategic framing, priorities, and direction. |
| Product | [02_product/README.md](02_product/README.md) | Owns scope, requirements, journeys, and acceptance framing. |
| PRD template | [02_product/01_prd_TEMPLATE.md](02_product/01_prd_TEMPLATE.md) | Starter for product problem, scope, requirements, and acceptance. |
| Architecture | [03_architecture/README.md](03_architecture/README.md) | Owns system design, integration boundaries, and technical patterns. |
| Solution design template | [03_architecture/01_solution_design_TEMPLATE.md](03_architecture/01_solution_design_TEMPLATE.md) | Starter for architecture baseline, boundaries, and quality concerns. |
| Interface control template | [03_architecture/06_interface_control_document_TEMPLATE.md](03_architecture/06_interface_control_document_TEMPLATE.md) | Starter for contracts, interfaces, and integration boundaries. |
| AI governance | [04_ai_governance/README.md](04_ai_governance/README.md) | Owns model-use policy, approvals, evaluation, and oversight. |
| Testing and acceptance | [05_testing_acceptance/README.md](05_testing_acceptance/README.md) | Owns verification, acceptance, and quality evidence structure. |
| Security and operations | [06_security_operations/README.md](06_security_operations/README.md) | Owns security controls, runbooks, and incident handling. |
| Delivery | [07_delivery/README.md](07_delivery/README.md) | Owns roadmap, release, rollout, and handoff planning. |
| Delivery plan template | [07_delivery/01_delivery_plan_TEMPLATE.md](07_delivery/01_delivery_plan_TEMPLATE.md) | Starter for milestones, dependencies, risks, and rollout planning. |
| Implementation plan template | [07_delivery/02_implementation_plan_TEMPLATE.md](07_delivery/02_implementation_plan_TEMPLATE.md) | Starter for workstreams, sequencing, and validation gates. |
| References | [08_references/README.md](08_references/README.md) | Owns external references and standards inputs. |
| Architecture decisions | [adr/README.md](adr/README.md) | Owns durable implementation decisions and ADR authoring rules. |
| Working-history policy | [superpowers/README.md](superpowers/README.md) | Owns rules for specs, plans, and tracked work records. |
| Archive policy | [99_archive/README.md](99_archive/README.md) | Owns rules for historical evidence and retired material. |

## Rule

Keep one active owner per concern. If a rule, requirement, or decision still matters, move it into the active root docs tree or the relevant ADR instead of duplicating it elsewhere.
