---
title: ADR Directory
status: active
record_class: supporting
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: monthly
last_reviewed: 2026-05-07
---

# ADR Directory

> **Purpose**: define `docs/adr/` as the canonical home for durable implementation and architecture decisions.
> **Audience**: architects, engineers, reviewers, and delivery leads who need binding decision records.
> **When to update**: update when ADR policy, lifecycle, or relationship to RFCs changes.

## How to use this template

- Create an ADR when a decision will materially shape implementation, architecture, operations, security, or delivery constraints.
- Keep one ADR focused on one durable decision.
- Treat ADRs here as the primary source of truth when other documents summarize the same decision.

## When to write an ADR

Create an ADR when a decision materially affects one or more of these areas:

- system structure or major component boundaries
- interfaces, contracts, or integration patterns
- data model or storage direction
- security, privacy, compliance, or operational controls
- delivery constraints, rollout strategy, or major implementation tradeoffs
- non-functional requirements such as reliability, performance, scalability, or maintainability

## Status lifecycle

- Proposed — under review and not yet binding.
- Accepted — approved and binding for active work until superseded.
- Superseded — replaced by a later ADR.
- Archived — retained for history without active authority.

## Relationship to RFCs

- Use RFCs in `../03_architecture/rfcs/` for open proposal review.
- Create or update an ADR when the outcome becomes a durable implementation decision.
- RFCs may inform ADRs, but ADRs are the binding record once accepted.

## Authority rules

- `docs/adr/` is the primary source of truth for durable implementation decisions.
- Update ADRs before implementation when a decision changes.
- Other docs may reference ADRs but must not override them.

## Related documents

- [ADR-000-template.md](ADR-000-template.md) — default starting point for new ADRs.
- [INDEX.md](INDEX.md) — canonical ADR listing with status tracking.
- [../03_architecture/README.md](../03_architecture/README.md) — active architecture document set.
- [../03_architecture/rfcs/README.md](../03_architecture/rfcs/README.md) — proposal-stage review before ADR graduation.
