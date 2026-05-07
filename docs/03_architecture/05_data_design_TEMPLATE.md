---
title: Data Design Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# Data Design Template

> **Purpose**: capture the domain model, storage choices, lifecycle rules, and migration approach for solution data.
> **Audience**: architects, engineers, DBAs, and reviewers responsible for data integrity and evolution.
> **When to update**: update when core entities, storage direction, retention policy, or migration strategy changes.

## How to use this template

- Use this document for solution-level data structure, not low-level schema dumps.
- Keep domain concepts and lifecycle rules readable before listing storage specifics.
- Link storage-affecting decisions to ADRs.

## Domain model

Describe the main business concepts and how they relate.

- Example: account, order, policy, event, audit record.

## Entities and relationships

List the most important entities, keys, and relationship patterns.

- Call out ownership, cardinality, and referential rules.

## Storage choices

Explain which stores are used and why.

- Example: relational store for transactional integrity, object storage for large artifacts.

## Data lifecycle

Define creation, retention, archival, deletion, and recovery expectations.

- Include privacy, legal hold, and restoration considerations where relevant.

## Migration strategy

Summarize how data structure changes are introduced safely.

- Example: additive change first, dual-read period, backfill, then cleanup.

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — parent architecture baseline.
- [07_deployment_TEMPLATE.md](07_deployment_TEMPLATE.md) — environment and infrastructure implications.
- [../adr/INDEX.md](../adr/INDEX.md) — durable decisions affecting data structure and storage.
