---
title: Policy Mappings Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: controls-maintainer
capability: references
phase: monitoring
cadence: monthly
last_reviewed: 2026-05-07
---

# Policy Mappings Template

> **Purpose**: map external policy, control, or standard expectations to the internal canonical artifacts that satisfy or evidence them.
> **Audience**: internal teams, managers, and reviewers who need traceability from external obligations to maintained documentation.
> **When to update**: update when a policy source changes, a mapped artifact moves, or control evidence is re-owned.

## How to use this template

Use this template when a project, audit, or client asks "where do we show that requirement here?" Keep the mapping focused on traceable artifacts and evidence, not on aspirational statements.

- Map each external clause, principle, or control to the smallest internal artifact set that really covers it.
- If coverage is partial, say so and note the gap or follow-up action.
- Prefer links to canonical templates over repeated control prose.

## Mapping principles

Good mappings are concrete and reviewable.

- Use stable identifiers from the external source when they exist.
- Link to the artifact that owns the control, then add the evidence artifact if it is separate.
- Separate control design from proof of execution; both may matter.

## Mapping register

Use one row per meaningful external requirement or grouped control.

| External source | Requirement or control | Internal artifact mapping | Evidence or review note | Coverage status |
| --- | --- | --- | --- | --- |
| ISO 27001 / NIST CSF | Access control and least privilege expectations | [../06_security_operations/05_access_control_TEMPLATE.md](../06_security_operations/05_access_control_TEMPLATE.md), [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md) | Review with service acceptance before go-live. | Planned |
| ISO 29119 | Test evidence and acceptance discipline | [../05_testing_acceptance/01_test_strategy_TEMPLATE.md](../05_testing_acceptance/01_test_strategy_TEMPLATE.md), [../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md](../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md), [../05_testing_acceptance/04_uat_plan_TEMPLATE.md](../05_testing_acceptance/04_uat_plan_TEMPLATE.md) | Verify evidence links are populated per release. | Planned |
| PMBOK / PRINCE2 | Change control and governance approval trail | [../00_governance/07_change_control_log_TEMPLATE.md](../00_governance/07_change_control_log_TEMPLATE.md), [../00_governance/09_stage_gate_checklist_TEMPLATE.md](../00_governance/09_stage_gate_checklist_TEMPLATE.md), [../07_delivery/04_status_report_TEMPLATE.md](../07_delivery/04_status_report_TEMPLATE.md) | Confirm tolerance breaches are explicitly escalated. | Planned |

## Coverage review guidance

Use this section to explain what "covered" means in the current context.

- **Planned**: the canonical artifact exists, but project-specific content or evidence is not yet complete.
- **Covered**: the artifact exists and current project evidence points to it.
- **Gap**: no current artifact or evidence covers the control well enough.

## Common mapping patterns

These patterns reduce duplication when building or reviewing a mapping set.

- Governance policies usually map to governance templates plus delivery reporting artifacts.
- Security frameworks usually map to security baseline, threat model, access control, incident response, and service acceptance.
- Quality frameworks usually map to test strategy, evidence index, defect management, and UAT.

## Related documents

- [01_standards_register_TEMPLATE.md](01_standards_register_TEMPLATE.md) — classifies whether the external source is adopted, adapted, or reference-only.
- [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md) — common target for security and control mappings.
- [../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md](../05_testing_acceptance/03_verification_evidence_index_TEMPLATE.md) — common evidence sink when mappings need proof, not just policy text.
- [../00_governance/12_requirements_traceability_matrix_TEMPLATE.md](../00_governance/12_requirements_traceability_matrix_TEMPLATE.md) — related traceability surface when policy obligations become project requirements.
