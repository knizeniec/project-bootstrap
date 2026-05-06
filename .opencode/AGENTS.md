---
name: OpenCode Workspace Assets
description: Use for work under .opencode/. Covers local OpenCode prompts, instructions, and workspace support assets.
applyTo: ".opencode/**"
---

# OpenCode Workspace Assets

This directory contains local OpenCode support files.

## Most Important Rules

- Keep prompts and instructions aligned with current repository behavior.
- Prefer minimal, high-signal instruction files.
- Avoid duplicating rules that belong in root or closer scoped `AGENTS.md` files.

## Routing

- Read `.opencode/instructions/AGENTS.md` before editing `.opencode/instructions/**`.

## Editing Guidance

- Update support files only when agent workflow, standards, or repository conventions actually change.
- Keep local tooling metadata concise and maintainable.
