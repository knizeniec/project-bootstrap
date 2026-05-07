---
title: RAID Register Template
status: draft
record_class: canonical
audience: [internal, manager, client]
owner: project-manager
capability: governance
phase: monitoring
cadence: weekly
last_reviewed: 2026-05-07
---

# RAID Register Template

> **Purpose**: maintain a live record of risks, assumptions, issues, and dependencies that could affect project outcomes.
> **Audience**: delivery leads, managers, sponsors, and client stakeholders who need current project control information.
> **When to update**: update whenever RAID items change and review at least on the project reporting cadence.

## How to use this template

Use this register as the live control log for RAID management throughout the project. Keep items specific, named, and action-oriented so the register supports decisions rather than becoming a backlog of vague concerns.

- Mandatory: owner, status, next action, and due date for every live item.
- Optional: separate tabs or sections by workstream if the project is large.
- Remove or archive closed items only after decision history is preserved.

## Risks

Record uncertain events that may affect scope, schedule, cost, quality, or benefits. Include a practical mitigation and owner so each risk can be discussed in governance forums without extra preparation.

- Example fields: ID, description, probability, impact, score, mitigation, owner, target review date.
- Example risks: vendor delay, data-quality uncertainty, adoption shortfall, staffing gap.

## Assumptions

Capture statements the plan currently depends on but has not yet proven. Review them regularly because invalid assumptions are a common source of hidden risk.

- Example fields: assumption, validity date, owner, validation method.
- Example assumptions: environment access by a milestone, policy sign-off before pilot, stable API contract.

## Issues

Track current problems that already require action rather than future uncertainty. Keep issue wording factual and outcome-focused so owners can move them to resolution quickly.

- Example fields: issue, status, owner, due date, impact, resolution action.
- Example issues: failed dependency handoff, unresolved defect cluster, missed approval.

## Dependencies

List upstream, downstream, or external dependencies that could block progress or readiness. Note whether each dependency is incoming or outgoing and how it is being managed.

- Example fields: dependency, type, owner, target date, status, blocking flag.
- Example dependencies: vendor contract, architecture decision, data feed, service acceptance sign-off.

## Related documents

- [07_change_control_log_TEMPLATE.md](07_change_control_log_TEMPLATE.md) — captures formal change decisions triggered by RAID items.
- [09_stage_gate_checklist_TEMPLATE.md](09_stage_gate_checklist_TEMPLATE.md) — uses RAID evidence to decide whether a stage can progress.
- [../07_delivery/04_status_report_TEMPLATE.md](../07_delivery/04_status_report_TEMPLATE.md) — summarizes the most important RAID changes each reporting period.
