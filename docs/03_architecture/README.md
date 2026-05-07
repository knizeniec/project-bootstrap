---
title: Architecture Documentation
status: active
record_class: supporting
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: monthly
last_reviewed: 2026-05-07
---

# Architecture Documentation

> **Purpose**: provide the landing page for solution design, C4 views, deployment and operability architecture, ADR links, and RFC intake.
> **Audience**: architects, engineers, reviewers, and delivery leads aligning implementation to the approved design.
> **When to update**: update when the architecture document set, reading order, or decision flow changes.

## How to use this template

- Use this page as the entry point into the architecture doc set.
- Start with the solution design, then move into the matching C4 view, ADRs, and supporting templates.
- Keep durable decisions in `../adr/`; keep proposal-stage discussion in `rfcs/`.

## Reading order

1. [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — arc42-style primary architecture baseline.
2. [02_c4_context_TEMPLATE.md](02_c4_context_TEMPLATE.md) — system boundary and external actors.
3. [03_c4_container_TEMPLATE.md](03_c4_container_TEMPLATE.md) — deployable/runtime building blocks.
4. [04_c4_component_TEMPLATE.md](04_c4_component_TEMPLATE.md) — internal structure of key containers.
5. [11_adr_index_TEMPLATE.md](11_adr_index_TEMPLATE.md) and [../adr/INDEX.md](../adr/INDEX.md) — accepted and in-flight decisions.
6. [12_rfc_index_TEMPLATE.md](12_rfc_index_TEMPLATE.md) and [rfcs/README.md](rfcs/README.md) — proposal flow before ADR graduation.

## Template set

- Core design: solution design, C4 context, C4 container, C4 component.
- Detailed reference: data design, interface control, deployment, observability, resilience, configuration baseline.
- Decision support: ADR index, RFC index, RFC template, ADR template.

## Decision flow

- Use an RFC when the team still needs structured review of a change or option.
- Promote accepted durable implementation decisions into `../adr/`.
- Link each solution design to the relevant C4 views and ADRs so readers can move from overview to binding decision quickly.

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md) — primary architecture baseline.
- [11_adr_index_TEMPLATE.md](11_adr_index_TEMPLATE.md) — architecture-side ADR tracking view.
- [../adr/README.md](../adr/README.md) — ADR policy and authority rules.
- [rfcs/README.md](rfcs/README.md) — RFC lifecycle and review process.
