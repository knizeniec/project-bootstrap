# Documentation Standards

## Purpose

Define mandatory documentation quality, ownership, and lifecycle rules for this repository.

## Scope

Applies to all repository documentation under `docs/` and policy docs in repo root.

## Owner

Repository maintainers and designated code owners.

## Inputs

- ADR decisions in `docs/project/adr/`
- Approved implementation specs/plans in `docs/superpowers/`
- Code and verification outputs

## Outputs

- Current, actionable documentation aligned to implementation behavior
- Traceable links between decisions, plans, and verification

## Dependencies

- ADR records (`docs/project/adr/`)
- Repository policies (`AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`)

## Documentation Taxonomy (Diátaxis)

- Tutorials: learning-oriented walkthroughs
- How-to guides: task completion paths
- Reference: factual contracts/interfaces
- Explanation: rationale and tradeoffs

## Source-of-Truth and Ownership Rules

- ADRs are the canonical implementation decision source.
- Active ownership roots are only `docs/project/00_governance` through `docs/project/08_references`.
- `docs/project/99_archive` and `docs/superpowers` are non-owning supporting history.

## Style and Formatting

- Use concise, skimmable sections with explicit headings.
- Prefer canonical ownership + links over duplicate prose.
- Keep assumptions and constraints explicit.

## Update Policy

- Update docs in the same change when behavior, architecture, workflows, or controls change.
- Update ADRs before implementation when decisions change.
- Do not rewrite completed `docs/superpowers/specs/*` or `docs/superpowers/plans/*`; append new dated records instead.

## Traceability

- Link requirements, ADRs, plans, tests, and controls where applicable.
- Keep references in `docs/project/08_references/INDEX.md` current.

## Review Cadence

- Minimum: review documentation at each feature milestone and release boundary.
- Triggered: immediate review when critical architecture/security decisions change.

## Change Log

- 2026-05-06: Initial baseline created for language-agnostic single-project template.
