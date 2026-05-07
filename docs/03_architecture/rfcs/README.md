---
title: RFC Directory
status: active
record_class: supporting
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: monthly
last_reviewed: 2026-05-07
---

# RFC Directory

> **Purpose**: define when to write an RFC, how RFC review works, and how accepted proposals graduate into ADRs.
> **Audience**: architects, engineers, and reviewers collaborating on non-final technical proposals.
> **When to update**: update when RFC lifecycle, review expectations, or ADR handoff rules change.

## How to use this template

- Create an RFC when a design is important enough to need structured review but is not yet a binding ADR.
- Keep one RFC focused on one proposal or tightly related set of options.
- Once the proposal becomes durable policy or implementation direction, create or update an ADR.

## When to write an RFC

- The team needs written review of multiple architecture options.
- The change crosses team boundaries, interfaces, or operating responsibilities.
- The design may become an ADR after review.

## Lifecycle

- Draft: being shaped by the author.
- Proposed: ready for formal review.
- Accepted: proposal approved; usually graduates to an ADR if it becomes durable.
- Rejected: not adopted; keep the record for traceability.
- Superseded: replaced by a later RFC or by an ADR.

## Review cadence

- Define review window, reviewer set, and decision owner at the start of the RFC.
- Keep unresolved questions explicit so reviewers know where input is needed.

## Graduation to ADR

- Create or update an ADR when the outcome becomes binding implementation direction.
- Link the RFC to the resulting ADR and close the RFC with the outcome.

## Related documents

- [RFC-000-template.md](RFC-000-template.md) — default RFC authoring template.
- [../12_rfc_index_TEMPLATE.md](../12_rfc_index_TEMPLATE.md) — architecture-side RFC index.
- [../../adr/ADR-000-template.md](../../adr/ADR-000-template.md) — destination format for durable accepted decisions.
- [../../adr/README.md](../../adr/README.md) — ADR policy and authority rules.
