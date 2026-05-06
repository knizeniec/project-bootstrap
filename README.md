# Repository Template

Language-agnostic, single-project repository scaffold focused on governance, documentation, and implementation readiness.

## Purpose

- Provide a consistent starting structure for new projects.
- Establish documentation ownership and ADR-first decision flow.
- Enforce Superpowers-based brainstorming/planning before implementation.

## Repository Tree

```text
.
|-- .agents/
|   `-- rules/
|-- .github/
|   |-- CODEOWNERS
|   `-- workflows/
|       `-- ci.yml
|-- .opencode/
|-- AGENTS.md
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
|-- SECURITY.md
|-- bin/
|   `-- README.md
|-- config/
|   `-- README.md
|-- diagrams/
|   `-- README.md
|-- docs/
|   |-- README.md
|   |-- project/
|   |   |-- 00-documentation-standards.md
|   |   |-- 00-source-of-truth.md
|   |   |-- 00_governance/README.md
|   |   |-- 01_strategy/README.md
|   |   |-- 02_product/README.md
|   |   |-- 03_architecture/README.md
|   |   |-- 04_ai_governance/README.md
|   |   |-- 05_testing_acceptance/README.md
|   |   |-- 06_security_operations/README.md
|   |   |-- 07_delivery/README.md
|   |   |-- 08_references/
|   |   |   |-- INDEX.md
|   |   |   `-- README.md
|   |   |-- 99_archive/README.md
|   |   |-- Architecture.md
|   |   |-- INDEX.md
|   |   `-- adr/
|   |       |-- ADR-000-template.md
|   |       `-- README.md
|   `-- superpowers/
|       |-- README.md
|       |-- plans/README.md
|       `-- specs/README.md
|-- examples/
|   `-- README.md
|-- scripts/
|   `-- README.md
|-- src/
|   `-- README.md
`-- tests/
    `-- README.md
```

## Getting Started

1. Update `docs/project/adr/` with initial decisions.
2. Create/refresh spec in `docs/superpowers/specs/` and plan in `docs/superpowers/plans/`.
3. Implement using Superpowers `subagent-driven-development` unless a different mode is explicitly chosen.
