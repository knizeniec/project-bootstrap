---
title: ADR Index Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# ADR Index Template

> **Purpose**: provide the project-facing index of architecture decisions relevant to the current solution design.
> **Audience**: architects, engineers, and reviewers who need a quick decision map from design to ADR.
> **When to update**: update when ADRs are created, accepted, superseded, or newly linked to the solution design.

## How to use this template

- Use this file as the local architecture-side listing for ADRs that matter to a specific solution or program.
- Keep the canonical ADR records in `../adr/`.
- Include only enough metadata to help readers find the binding decision quickly.

## ADR list

Use a simple table with one row per ADR.

| ADR | Title | Status | Date | Notes |
| --- | --- | --- | --- | --- |
| ADR-001 | Example decision | accepted | YYYY-MM-DD | Link from the solution design section it affects |

## Linkage rules

- Every entry should link to the canonical file in `../adr/`.
- Note whether the ADR shapes context, container, component, data, deployment, or operations design.

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — references the ADR set from the architecture baseline.
- [02_c4_context_TEMPLATE.md](02_c4_context_TEMPLATE.md) — context-shaping decisions often appear here first.
- [03_c4_container_TEMPLATE.md](03_c4_container_TEMPLATE.md) — major technology and boundary decisions.
- [../adr/INDEX.md](../adr/INDEX.md) — canonical ADR source of truth.
