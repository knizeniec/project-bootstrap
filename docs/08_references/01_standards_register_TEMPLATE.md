---
title: Standards Register Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: references-maintainer
capability: references
phase: n/a
cadence: monthly
last_reviewed: 2026-05-07
---

# Standards Register Template

> **Purpose**: record which external standards and frameworks are adopted, adapted, or reference-only in this documentation system, and where they show up downstream.
> **Audience**: internal teams, managers, and reviewers who need a traceable standards posture before tailoring or audit work.
> **When to update**: update when a standard is added, reclassified, materially reinterpreted, or linked target areas change.

## How to use this template

Use this register when you need one canonical answer to "why do we use this framework here?" Record only standards that materially influence repository structure, control design, architecture shape, testing posture, operations, or end-user documentation.

- Keep the rationale close to the wording already ratified in the redesign plan.
- Add downstream target paths so readers can see where each standard actually affects artifacts.
- If a standard is informative only, say so clearly and state the boundary to prevent accidental over-adoption.

## Classification rules

Use exactly one disposition per standard in this register.

- **Adopted** means the framework materially shapes the canonical artifact set or structure as-is.
- **Adapted** means selected concepts are used, but the repository deliberately narrows, reshapes, or scopes the method.
- **Reference-only** means the standard is informative, not mandatory, unless a project adds stricter requirements elsewhere.

## Adopted standards

These are the standards and frameworks treated as active structural inputs to the repository.

| Standard | Scope and rationale | Surface | Version | Last reviewed | Current target areas |
| --- | --- | --- | --- | --- | --- |
| ISO 21502 | Neutral external baseline for project-management coverage. | manager | Project-specific | 2026-05-07 | [../00_governance/README.md](../00_governance/README.md), [../07_delivery/README.md](../07_delivery/README.md) |
| arc42 | Structure the architecture domain so constraints, context, quality, deployment, and rationale stay complete. | engineering | Current arc42 guidance | 2026-05-07 | [../03_architecture/README.md](../03_architecture/README.md), [../03_architecture/01_solution_design_TEMPLATE.md](../03_architecture/01_solution_design_TEMPLATE.md) |
| C4 | Context, container, component, code views as the canonical visual model for diagrams; complements arc42's narrative. | engineering | Current C4 guidance | 2026-05-07 | [../03_architecture/02_c4_context_TEMPLATE.md](../03_architecture/02_c4_context_TEMPLATE.md), [../03_architecture/03_c4_container_TEMPLATE.md](../03_architecture/03_c4_container_TEMPLATE.md), [../03_architecture/04_c4_component_TEMPLATE.md](../03_architecture/04_c4_component_TEMPLATE.md) |
| MADR | Keep architecture decisions structured, lightweight, and durable. | engineering | Current MADR guidance | 2026-05-07 | [../adr/README.md](../adr/README.md), [../adr/ADR-000-template.md](../adr/ADR-000-template.md), [../03_architecture/11_adr_index_TEMPLATE.md](../03_architecture/11_adr_index_TEMPLATE.md) |
| ISO 31000 | Risk identification, treatment, and monitoring discipline. | manager | Concepts adopted | 2026-05-07 | [../00_governance/06_raid_register_TEMPLATE.md](../00_governance/06_raid_register_TEMPLATE.md), [../07_delivery/05_dependency_log_TEMPLATE.md](../07_delivery/05_dependency_log_TEMPLATE.md) |
| ISO 29148 | Requirements quality and traceability. | manager | Concepts adopted | 2026-05-07 | [../02_product/02_requirements_catalog_TEMPLATE.md](../02_product/02_requirements_catalog_TEMPLATE.md), [../00_governance/12_requirements_traceability_matrix_TEMPLATE.md](../00_governance/12_requirements_traceability_matrix_TEMPLATE.md) |
| ISO 29119 | Test strategy, evidence, and acceptance discipline. | manager | Concepts adopted | 2026-05-07 | [../05_testing_acceptance/01_test_strategy_TEMPLATE.md](../05_testing_acceptance/01_test_strategy_TEMPLATE.md), [../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md](../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md), [../05_testing_acceptance/04_uat_plan_TEMPLATE.md](../05_testing_acceptance/04_uat_plan_TEMPLATE.md) |

## Adapted standards

These are mandatory influences, but only in the bounded form described below.

| Standard | Adaptation notes | Surface | Version | Last reviewed | Current or future target areas |
| --- | --- | --- | --- | --- | --- |
| PMBOK | Full lifecycle control domains and planning coverage; supplies the vocabulary sponsors and clients expect. Adapted to a Markdown-first repository, with planning domains represented by linked artifacts rather than a monolithic plan document. | manager / sponsor / client | Project-specific | 2026-05-07 | [../00_governance/README.md](../00_governance/README.md), [../07_delivery/README.md](../07_delivery/README.md), [../01_strategy/README.md](../01_strategy/README.md) |
| PRINCE2 | Stage gates, tolerances, escalation, business justification, and role clarity. Adapted as a governance overlay, not as a full method rollout; only gate logic, tolerances, roles, and justification controls are mandatory. | manager / sponsor / client | Principles adapted | 2026-05-07 | [../00_governance/09_stage_gate_checklist_TEMPLATE.md](../00_governance/09_stage_gate_checklist_TEMPLATE.md), [../00_governance/03_board_terms_of_reference_TEMPLATE.md](../00_governance/03_board_terms_of_reference_TEMPLATE.md), [../07_delivery/04_status_report_TEMPLATE.md](../07_delivery/04_status_report_TEMPLATE.md) |
| Diataxis | Tutorial, how-to, reference, and explanation as the four canonical modes for `09_user_documentation/`. Adopted in scope for `09_user_documentation/` only; internal governance, project-management, and engineering artifacts are not forced into Diataxis modes. | end-user | Current Diataxis guidance | 2026-05-07 | [../09_user_documentation/README.md](../09_user_documentation/README.md), [../09_user_documentation/tutorials/README.md](../09_user_documentation/tutorials/README.md), [../09_user_documentation/how-to/README.md](../09_user_documentation/how-to/README.md) |
| ITIL | Service transition concepts are adapted for release readiness, cutover, support handoff, and early-life support rather than a full ITSM implementation. | operations | Service-transition concepts adapted | 2026-05-07 | [../06_security_operations/08_service_acceptance_TEMPLATE.md](../06_security_operations/08_service_acceptance_TEMPLATE.md), [../06_security_operations/04_support_model_TEMPLATE.md](../06_security_operations/04_support_model_TEMPLATE.md), [../07_delivery/08_cutover_and_rollback_TEMPLATE.md](../07_delivery/08_cutover_and_rollback_TEMPLATE.md) |

## Reference-only standards

These are useful comparison points or optional baselines, but they are not mandatory operating rules for every project in this repo.

| Standard | Boundary | Surface | Version | Last reviewed | Typical target areas |
| --- | --- | --- | --- | --- | --- |
| BABOK | Useful for deeper analysis practice, but not required for every project. | manager / analyst | Reference only | 2026-05-07 | [../02_product/01_prd_TEMPLATE.md](../02_product/01_prd_TEMPLATE.md), [../02_product/03_user_journeys_TEMPLATE.md](../02_product/03_user_journeys_TEMPLATE.md) |
| NIST CSF | Reference baseline for security operating controls; does not imply certification unless separately declared. | security / operations | Reference only | 2026-05-07 | [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md), [../06_security_operations/02_threat_model_TEMPLATE.md](../06_security_operations/02_threat_model_TEMPLATE.md) |
| ISO 27001 | Reference baseline for security operating controls; does not imply certification unless separately declared. | security / operations | Reference only | 2026-05-07 | [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md), [../06_security_operations/05_access_control_TEMPLATE.md](../06_security_operations/05_access_control_TEMPLATE.md), [../04_ai_governance/01_ai_use_policy_TEMPLATE.md](../04_ai_governance/01_ai_use_policy_TEMPLATE.md) |

## Capability-area map

Use this map to show where standards influence the current documentation tree. It helps reviewers jump from a standard to the canonical area that operationalizes it.

- Governance and strategy: [../00_governance/README.md](../00_governance/README.md), [../01_strategy/README.md](../01_strategy/README.md)
- Product and architecture: [../02_product/README.md](../02_product/README.md), [../03_architecture/README.md](../03_architecture/README.md)
- AI governance and quality: [../04_ai_governance/README.md](../04_ai_governance/README.md), [../05_testing_acceptance/README.md](../05_testing_acceptance/README.md)
- Operations and delivery: [../06_security_operations/README.md](../06_security_operations/README.md), [../07_delivery/README.md](../07_delivery/README.md)
- End-user documentation area: [../09_user_documentation/README.md](../09_user_documentation/README.md)

## Review prompts

Use these prompts when updating the register.

- Has any standard become reference-only because the repo no longer operationalizes it?
- Has any template started using a framework without the register explaining why?
- Has a future target area become current and therefore earned a real cross-link?

## Related documents

- [02_glossary_TEMPLATE.md](02_glossary_TEMPLATE.md) — defines the shared terminology used in standards rationale.
- [04_policy_mappings_TEMPLATE.md](04_policy_mappings_TEMPLATE.md) — turns standard posture into control-to-artifact mappings.
- [../03_architecture/README.md](../03_architecture/README.md) — primary home for arc42, C4, and ADR-linked architecture artifacts.
- [../06_security_operations/README.md](../06_security_operations/README.md) — primary home for security and ITIL-aligned operational controls.
