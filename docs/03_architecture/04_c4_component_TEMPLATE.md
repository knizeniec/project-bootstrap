---
title: C4 Component Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# C4 Component Template

> **Purpose**: describe the internal components inside a key container and how they collaborate.
> **Audience**: engineers and reviewers working inside a specific container boundary.
> **When to update**: update when a container's internal structure or responsibilities materially change.

## How to use this template

- Create one component view per important container.
- Keep components responsibility-based, not file-list-based.
- Link durable design rules to ADRs instead of duplicating rationale here.

## Container in scope

Name the parent container and link back to the container view.

- Example: API service, web application, ingestion worker.

## Components

List the main components inside the container.

- Example: API layer, domain service, repository, adapter, scheduler.

## Responsibilities

State what each component owns and the boundary between components.

- Prefer clear verbs and nouns over implementation detail.

## Collaborators

Describe the main dependencies between components and any external collaborators.

- Note direction, protocol, and important invariants.

## Technology

Record the key frameworks, libraries, or runtime patterns that matter for the component view.

- Example: framework layer, ORM boundary, event bus adapter.

## Diagram placeholder

Add a PlantUML or Mermaid component diagram.

```text
[API Layer] -> [Domain Service] -> [Repository]
```

## Related documents

- [03_c4_container_TEMPLATE.md](03_c4_container_TEMPLATE.md) — parent container structure.
- [06_interface_control_document_TEMPLATE.md](06_interface_control_document_TEMPLATE.md) — external or cross-boundary contracts.
- [../adr/INDEX.md](../adr/INDEX.md) — decisions that constrain internal decomposition.
