---
name: Instruction File Ownership
description: Use for work under .opencode/instructions/. Covers instruction documents such as industry standards.
applyTo: ".opencode/instructions/**"
---

# Instruction File Ownership

This directory holds instruction documents loaded by the local tooling.

## Most Important Rules

- Keep instruction files short, direct, and high value.
- Preserve important context, constraints, decisions, risks, and verification expectations.
- Update instructions when repository workflow, governance, or quality standards change.

## Editing Guidance

- Keep broad repo-wide rules in root `AGENTS.md`.
- Keep directory-specific rules in the closest scoped `AGENTS.md`.
- Avoid repeating the same policy in multiple instruction files unless duplication is intentional and necessary.
