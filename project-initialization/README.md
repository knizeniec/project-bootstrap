---
title: Project Initialization
status: active
record_class: supporting
audience: [internal]
owner: Template maintainers
capability: knowledge
phase: n/a
cadence: ad-hoc
last_reviewed: 2026-05-07
---

# Project Initialization

> **Purpose**: serve as the entrypoint and contract summary for the tool-neutral project initialization workflow.
> **Audience**: contributors maintaining the initialization workflow; AI agents reading phase content.
> **When to update**: update when the phase catalog, artifact list, or shared contract rules change.

## How initialization works

A fresh clone of this template is unspecialized. To initialize it for a specific project, run the tool-native commands in your AI tool's command surface:

- Claude: `.claude/commands/init-triage.md` (invoke as `/init-triage`)
- Copilot: `.copilot/commands/init-triage.md`
- Codex: `.codex/commands/init-triage.md`

Each tool exposes seven phase commands. They must be run in order. State is tracked in `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md`.

## Phases

| Phase | Command | Purpose |
| --- | --- | --- |
| 0. Triage | `/init-triage` | Routing questions, profile selection, artifact roadmap |
| 1. Intent | `/init-intent` | Project brief, optional business case |
| 2. Specification | `/init-spec` | PRD, requirements catalog, user journeys, acceptance catalog |
| 3. Design | `/init-design` | Solution design, ADRs, optional C4 views |
| 4. Govern & Operate | `/init-govern` | AI policy, test strategy, security baseline, delivery plan |
| 5. Adapt | `/init-adapt` | Language adaptation, repository sync |
| 6. Final review | `/init-review` | Cross-doc coherence, entry-doc parity, standards pass |

## This directory

| Path | Responsibility |
| --- | --- |
| `contract.md` | Stop rules, concern framing, output format — all commands follow this |
| `plan-template.md` | Scaffold for the plan file created by triage |
| `review-checklist.md` | Standards + coherence rubric used by `init-reviewer` |
| `phases/` | Per-phase orchestration files |
| `artifacts/` | Per-artifact question rubrics, gating criteria, review hooks |
| `profiles/` | Default artifact activations per project type |
