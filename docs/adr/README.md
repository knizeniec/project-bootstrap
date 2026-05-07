# ADR Directory

Status: Active
Owner: Architecture decision maintainers
Purpose: define `docs/adr/` as the home for durable implementation and architecture decisions
Last updated: 2026-05-06

This directory contains Architecture Decision Records (ADRs).

## When to write an ADR

Create an ADR when a decision materially affects one or more of these areas:

- system structure or major component boundaries
- interfaces, contracts, or integration patterns
- data model or storage direction
- security, privacy, compliance, or operational controls
- delivery constraints, rollout strategy, or major implementation tradeoffs
- non-functional requirements such as reliability, performance, scalability, or maintainability

Do not create an ADR for routine implementation details, local refactors with no durable tradeoff, or transient planning notes that belong in working-history docs.

## Record rules

- One ADR should capture one significant decision.
- Use stable file names in the form `ADR-XXX-short-title.md`.
- Keep accepted ADRs immutable except for approved factual corrections.
- Replace old decisions by creating a new ADR that explicitly supersedes the prior one.
- Link ADRs to related product, architecture, delivery, and verification documents when those links exist.

## Status lifecycle

- `Proposed` - under review and not yet binding.
- `Accepted` - approved and binding for active work.
- `Superseded` - replaced by a newer accepted ADR.
- `Deprecated` - no longer preferred, but not replaced by a direct successor.

## Authority rules

- ADRs are the primary source of truth for durable implementation decisions.
- Update ADRs before implementation begins when a decision changes.
- Do not change an accepted ADR during implementation except for approved factual corrections.
- Other docs may reference ADRs but must not override them.

## Roles and review

- Author: the person or team proposing the decision.
- Deciders: the role or group with authority to accept or reject the decision.
- Consulted: roles or teams that provide material input.
- Informed: roles or teams that need visibility after the decision is made.

If a project needs stricter approval rules, define them in the relevant governance and delivery documents and reference them from the ADR.

## Review and supersession triggers

Revisit an accepted ADR when one or more of these conditions occurs:

- assumptions or constraints have materially changed
- a new requirement conflicts with the accepted decision
- incidents, benchmarks, or delivery experience invalidate the original tradeoffs
- a dependent system or interface changes in a way that affects the decision
- the project adopts a new architecture direction that replaces the prior choice

## Related documents

- [../03_architecture/README.md](../03_architecture/README.md) for active architecture ownership.
- [../00-source-of-truth.md](../00-source-of-truth.md) for canonical ownership.
- [ADR-000-template.md](ADR-000-template.md) for the default ADR format.
