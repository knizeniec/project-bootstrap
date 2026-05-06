# Source of Truth

## Decision Authority

- Primary implementation decision authority: `docs/project/adr/`.
- ADR updates are required before implementation when decisions change.
- ADR decisions are not changed during active implementation except approved factual corrections.

## Ownership Model

- Active ownership roots: `docs/project/00_governance` through `docs/project/08_references`.
- Supporting/historical only: `docs/project/99_archive` and `docs/superpowers`.

## Superpowers Execution Protocol

- Superpowers plugin usage is mandatory for every change.
- Brainstorming/planning must use ADR context first.
- Specs/plans are created under `docs/superpowers/specs` and `docs/superpowers/plans`.
- Completed specs/plans are historical records and must not be rewritten.
- Default implementation execution mode is `subagent-driven-development` unless explicitly overridden.
