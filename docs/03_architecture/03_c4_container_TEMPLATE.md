---
title: C4 Container Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# C4 Container Template

> **Purpose**: describe the deployable applications, services, data stores, and their communication paths.
> **Audience**: architects, engineers, operators, and reviewers validating runtime structure.
> **When to update**: update when containers, technologies, or container communication paths change.

## How to use this template

- Use this view after the context view is stable.
- Keep one row or subsection per container with responsibility, technology, and dependencies.
- Link deep internal detail to the component view rather than overloading this document.

## Containers

List each application, service, worker, gateway, or data store in scope.

- Example: web application, background worker, relational database, cache.

## Technology choices

Record the primary technologies or platforms for each container.

- Explain why the choice matters only when it affects architecture or operation.

## Responsibilities

State what each container owns and what it must not own.

- Keep boundaries clear enough that later ADRs and components can refine them without contradiction.

## Communication paths

Describe how the containers communicate.

- Note protocol, direction, sync or async behavior, and notable failure handling.
- Link contract-heavy paths to [06_interface_control_document_TEMPLATE.md](06_interface_control_document_TEMPLATE.md).

## Diagram placeholder

Add a PlantUML or Mermaid container diagram.

```text
[User] -> [Web App] -> [API Service] -> [Database]
```

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — parent architecture baseline.
- [04_c4_component_TEMPLATE.md](04_c4_component_TEMPLATE.md) — internal structure of critical containers.
- [06_interface_control_document_TEMPLATE.md](06_interface_control_document_TEMPLATE.md) — detailed interface contracts.
- [../adr/INDEX.md](../adr/INDEX.md) — decisions that explain major technology or boundary choices.
