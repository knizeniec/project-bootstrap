---
title: C4 Context Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# C4 Context Template

> **Purpose**: capture the system context view: people, external systems, system boundary, and key interactions.
> **Audience**: architects, engineers, product stakeholders, and reviewers aligning on scope.
> **When to update**: update when system boundaries, actors, or major integrations change.

## How to use this template

- Use one context view per system or major solution boundary.
- Keep names aligned with the solution design and ADR terminology.
- Include a diagram placeholder plus short text that explains the critical interactions.

## System context overview

Describe what the system is, why it exists, and what sits outside the boundary.

- Link the parent design in [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md).

## People

List the human actors, roles, or operational personas that interact with the system.

- Example: end user, support analyst, partner operator.

## External systems

List the systems outside the boundary that exchange data, events, or control signals.

- Note owner, trust level, and interaction purpose.

## System in scope

Name the system being designed and summarize its primary responsibilities.

- Keep the wording consistent with the solution design and container view.

## Key interactions

Summarize the most important inbound and outbound interactions.

- Example: user submits request through the web app.
- Example: system publishes domain events to an external platform.

## Diagram placeholder

Add a PlantUML or Mermaid context diagram and keep the text version readable without it.

```text
[Person] -> [System in Scope] -> [External System]
```

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — explains goals, scope, and architectural strategy.
- [03_c4_container_TEMPLATE.md](03_c4_container_TEMPLATE.md) — expands the system into deployable containers.
- [../adr/INDEX.md](../adr/INDEX.md) — links context-shaping decisions to accepted ADRs.
