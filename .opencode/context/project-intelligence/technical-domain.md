<!-- Context: project-intelligence/technical | Priority: critical | Version: 1.0 | Updated: 2026-05-07 -->

# Technical Domain

**Purpose**: Defines the repository's technical stack, documentation patterns, naming rules, and operating standards for agents and contributors.
**Last Updated**: 2026-05-07

## Quick Reference
This repository is a governance-first template centered on a structured documentation system plus tracked assistant-native tooling.

- Update triggers: documentation structure changes, naming rule changes, prompt workflow changes, assistant tooling changes, agent workflow changes
- Audience: developers, documentation maintainers, AI agents
- Primary surface: canonical Markdown documents under `docs/`
- Supporting surfaces: prompts, tracked assistant-native tool assets, local agent instructions, and maintainer tooling

## Primary Stack
| Layer | Technology | Notes |
| --- | --- | --- |
| Primary format | Markdown | Canonical docs and prompts are Markdown-first |
| Metadata | YAML frontmatter | Canonical docs use validated frontmatter |
| Automation | Shell scripts | Maintainer and workflow helpers |
| Agent layer | `AGENTS.md` + tracked assistant-native assets | Routing, behavior, and harness-specific integration |

## Core Patterns
Project work starts from curated documentation rather than immediate implementation.

- The active system lives in `docs/` with a control spine and numbered capability folders.
- Prompts in `prompts/` guide bootstrap, refinement, architecture, and language adaptation.
- Assistant-native assets in `.claude/`, `.copilot/`, `.codex/`, `.opencode/`, and `.agents/` are tracked when they define repo behavior or vendored harness integrations.
- Codex's repo-native runtime surface is root `AGENTS.md`, `.codex/hooks.json`, and `.agents/skills/`.
- Documentation is treated as a first-class artifact that must be curated before implementation work begins.

## Naming Conventions
| Type | Convention | Example |
| --- | --- | --- |
| Canonical docs | numbered file names | `01_lifecycle_map.md` |
| Special routing files | fixed uppercase name | `AGENTS.md` |
| Python files | `camel_case.py` | `docs_validator.py` |
| General directories | mostly kebab-case | `project-initialization` |
| Docs directories | numbered folders | `00_operating_model` |
| Assistant tooling | dot-prefixed folders plus Codex skills dir | `.opencode`, `.agents/skills` |

## Code Standards
- Keep docs canonical and avoid duplicate sources of truth.
- Use links and `INDEX.md` files to navigate documentation and references.
- Treat templates as foundations to build on, not content to copy blindly.
- Use frontmatter on canonical docs.
- Verify claims against real files before writing them down.
- Link repeated or related information across files instead of restating it.
- Follow the defined documentation specifications and rules.
- Treat documentation as one of the most important parts of the project.
- Do not drift from template guidance; sections should contain the right information.
- Update `README.md` and relevant `AGENTS.md` files when a doc change materially affects context.
- Do not start implementation plans or implementation work until documentation is complete and explicitly ready.
- When making design decisions, propose multiple options with pros, cons, and trade-offs.
- Improve canonical docs when better information emerges, but review changes carefully before replacing existing guidance.

## Security Requirements
- Never commit secrets.
- Check for dangerous patterns in the security documentation and operating guidance.
- Protect docs from unnecessary agent changes; important doc updates should be curated and reviewed.

## 📂 Codebase References
- `README.md` - repository purpose, adoption journey, and documentation-first workflow
- `docs/00-documentation-standards.md` - canonical documentation rules and update checklist
- `docs/00-source-of-truth.md` - ownership map for canonical concerns
- `docs/INDEX.md` - hand-maintained navigation across lifecycle, role, and capability
- `prompts/project-bootstrap.md` - project bootstrap prompt
- `prompts/architecture-baseline.md` - architecture decision prompt with trade-offs
- `prompts/language-adaptation.md` - stack adaptation prompt
- `.claude/README.md` - tracked Claude integration assets
- `.codex/README.md` - tracked Codex hook wiring and vendored mirror assets
- `.agents/README.md` - Codex repo-native skills surface
- `.opencode/AGENTS.md` - local guidance for tracked OpenCode assets
- `tools/` - repository-maintained validators and helper utilities
