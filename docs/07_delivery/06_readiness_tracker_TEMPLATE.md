---
title: Readiness Tracker Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: release-manager
capability: execution
phase: monitoring
cadence: weekly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Readiness Tracker Template

> **Purpose**: track whether delivery, testing, release, and operational domains are ready to pass the next gate or release decision.
> **Audience**: delivery leads, release managers, and managers reviewing go/no-go readiness.
> **When to update**: update whenever readiness evidence changes and review at least weekly near release milestones.

## How to use this template

Use this template as the canonical view of release and stage readiness across key domains. Keep statuses evidence-based, and link to the proof needed for each domain rather than replacing it with narrative.

- Mandatory: domain, status, owner, and gating evidence link.
- Optional: note required recovery actions for amber or red items.
- Remove green-by-assumption entries that do not yet have evidence.

## Per-readiness-domain register

Track readiness by domain so the team can spot weak areas early and focus action where it matters most. The listed domains should cover the whole delivery path from scope stability through operations preparedness.

- Example domains: scope, design, build, test, release, operations.
- Example statuses: green, amber, red, not started.

| Domain | Status | Owner | Gating evidence link |
| --- | --- | --- | --- |
| [Scope/Design/Build/Test/Release/Ops] | [Green/Amber/Red] | [Role or team] | [Link or reference] |

## Related documents

- [04_status_report_TEMPLATE.md](04_status_report_TEMPLATE.md) — summarizes the readiness picture in the weekly management report.
- [07_release_plan_TEMPLATE.md](07_release_plan_TEMPLATE.md) — uses readiness state to confirm release scope and sequence.
- [../00_governance/09_stage_gate_checklist_TEMPLATE.md](../00_governance/09_stage_gate_checklist_TEMPLATE.md) — checks readiness evidence before stage or release approval.
