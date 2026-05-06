# ADR-000: ADR Template and Decision Governance

- Status: Accepted
- Date: 2026-05-06
- Deciders: Repository Maintainers
- Technical Story: Establish baseline decision governance

## Context

This repository uses a language-agnostic template scaffold and requires consistent decision authority and implementation planning discipline.

## Decision

1. `docs/project/adr/` is the primary source of truth for implementation decisions.
2. ADRs must be updated before implementation starts when decisions change.
3. ADR decisions are not modified during implementation except for approved factual corrections.
4. ADRs must include enough context and constraints to execute implementation safely.
5. `docs/superpowers/specs/` and `docs/superpowers/plans/` are implementation planning artifacts for historical reference after completion.
6. Superpowers plugin usage is mandatory for all changes, with `subagent-driven-development` as default execution mode unless explicitly overridden.

## Consequences

- Decision drift is reduced through explicit ADR-first updates.
- Implementation planning remains traceable to governing decisions.
- Historical planning records remain auditable and stable.

## Alternatives Considered

- Treat all docs equally authoritative: rejected due to conflict risk.
- Allow mutable historical plans: rejected due to auditability loss.
