---
title: Requirements Traceability Matrix Template
status: draft
record_class: canonical
audience: [internal, manager, client]
owner: quality-manager
capability: governance
phase: monitoring
cadence: per-stage
last_reviewed: 2026-05-07
---

# Requirements Traceability Matrix Template

> **Purpose**: trace requirements from source through design, delivery, release, and verification.
> **Audience**: delivery leads, quality leads, managers, and client reviewers who need confidence that approved scope is implemented and tested.
> **When to update**: update when requirements, design references, test references, or release references change.

## How to use this template

Use this template when requirements need explicit traceability across the lifecycle. Keep one row per requirement or acceptance item, use stable IDs, and link to the most specific source available.

- Mandatory: requirement ID, source, design ref, test ref, release ref, and status.
- Optional: summary or owner columns if they help the project manage scale.
- Remove placeholder rows before the matrix is treated as live evidence.

## Traceability matrix

Use the matrix to prove that each approved requirement has a design home, a verification path, and a release destination. Keep status values simple so reviewers can spot gaps quickly during stage gates or audits.

- Example statuses: proposed, active, verified, deferred, retired.
- Example references: PRD section, architecture section, test case ID, release milestone.

| Requirement ID | Source | Design ref | Test ref | Release ref | Status |
| --- | --- | --- | --- | --- | --- |
| R-001 | [PRD section, brief, or contract reference] | [Design section or ADR] | [Test case, evidence ID, or UAT scenario] | [Release or milestone] | [Status] |
| R-002 | [Source reference] | [Design reference] | [Test reference] | [Release reference] | [Status] |

## Related documents

- [00_project_brief_TEMPLATE.md](00_project_brief_TEMPLATE.md) — provides the initial scope and success frame that requirements should support.
- [09_stage_gate_checklist_TEMPLATE.md](09_stage_gate_checklist_TEMPLATE.md) — uses traceability evidence during stage reviews.
- [../07_delivery/02_implementation_plan_TEMPLATE.md](../07_delivery/02_implementation_plan_TEMPLATE.md) — maps traced requirements into executable work and validation gates.
