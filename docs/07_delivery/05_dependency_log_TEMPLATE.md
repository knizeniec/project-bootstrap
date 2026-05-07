---
title: Dependency Log Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: delivery-manager
capability: execution
phase: monitoring
cadence: weekly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Dependency Log Template

> **Purpose**: maintain the live list of dependencies that affect delivery sequencing, confidence, or readiness.
> **Audience**: delivery leads and managers coordinating cross-team or external dependencies.
> **When to update**: update whenever dependency status changes and review at least weekly.

## How to use this template

Use this template when the project needs more detailed dependency tracking than a plan summary can provide. Keep one row per dependency and make blocking status obvious so teams can act early.

- Mandatory: ID, type, owner, target date, status, and blocking flag.
- Optional: impact note or recovery action if it helps decision-making.
- Remove closed dependencies only after they are no longer relevant to reporting or audit trail.

## Per-dependency register

Capture dependencies in a simple table so the team can see ownership and timing at a glance. Separate incoming and outgoing dependencies clearly to avoid disputes about who must act next.

- Example types: in, out, external, internal.
- Example statuses: on track, at risk, blocked, complete.

| Dependency ID | Type | Owner | Target date | Status | Blocking? |
| --- | --- | --- | --- | --- | --- |
| DEP-001 | [In/Out] | [Role or team] | [YYYY-MM-DD] | [Status] | [Yes/No] |

## Related documents

- [01_delivery_plan_TEMPLATE.md](01_delivery_plan_TEMPLATE.md) — summarizes the critical-path dependencies at baseline level.
- [03_stage_plan_TEMPLATE.md](03_stage_plan_TEMPLATE.md) — uses dependency status to manage stage exceptions.
- [../00_governance/06_raid_register_TEMPLATE.md](../00_governance/06_raid_register_TEMPLATE.md) — provides the governance-facing view of dependency risk and escalation.
