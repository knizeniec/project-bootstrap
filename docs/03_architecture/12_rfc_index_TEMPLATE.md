---
title: RFC Index Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# RFC Index Template

> **Purpose**: track architecture RFCs that are under discussion before they become accepted ADRs or are closed.
> **Audience**: architects, engineers, reviewers, and decision-makers participating in technical review.
> **When to update**: update when RFCs are opened, reviewed, accepted, rejected, or superseded.

## How to use this template

- Keep this as the quick navigation layer for `rfcs/`.
- Link accepted durable outcomes to the matching ADR when one is created.
- Keep lifecycle wording consistent with the RFC README.

## RFC list

| RFC | Title | Status | Date | Outcome link |
| --- | --- | --- | --- | --- |
| RFC-001 | Example proposal | proposed | YYYY-MM-DD | ADR-001 or closure note |

## Graduation rules

- Use RFCs for open design exploration and multi-party review.
- Move durable, binding implementation decisions into `../adr/`.

## Related documents

- [rfcs/README.md](rfcs/README.md) — RFC lifecycle and review expectations.
- [rfcs/RFC-000-template.md](rfcs/RFC-000-template.md) — default RFC authoring template.
- [11_adr_index_TEMPLATE.md](11_adr_index_TEMPLATE.md) — where accepted outcomes are mirrored into the architecture view.
- [../adr/ADR-000-template.md](../adr/ADR-000-template.md) — target format for durable decisions.
