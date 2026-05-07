---
title: User Journeys Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: product-management
capability: product
phase: planning
cadence: per-release
last_reviewed: 2026-05-07
---

# User Journeys Template

> **Purpose:** capture the key user journeys that explain how personas move through the product, where friction occurs, and what success looks like.
> **Audience:** product, design, engineering, and QA roles who need behavior-centered context for requirements and acceptance.
> **When to update:** update when personas, workflow steps, pain points, or success measures change.

## How to use this template

Use this template when a requirement list alone does not explain the real user flow. Keep journeys focused on high-value outcomes, and use them to expose edge cases, handoffs, and experience risks before design or implementation deepens.

- Create one subsection or table row per meaningful journey.
- Link journey IDs back to PRD stories, requirements, and acceptance scenarios.
- Remove low-value narrative detail that does not change product or test decisions.

## User journeys

Describe each journey in enough detail that a reader can understand the user goal, the main steps, and the points most likely to fail. A simple table is often enough if the flow is linear; use bullets under the table for exceptions or edge cases.

| Journey ID | Persona | Goal | Steps | Pain points | Opportunities | Success measure |
| --- | --- | --- | --- | --- | --- | --- |
| J-001 | [Persona] | [Outcome the user wants] | [Key steps] | [Current friction] | [Improvement idea] | [Observable measure] |
| J-002 | [Persona] | [Outcome] | [Key steps] | [Current friction] | [Improvement idea] | [Observable measure] |

- Example pain points: duplicate entry, unclear status, delayed response, inaccessible control.
- Example success measures: completion rate, task time, error rate, support contact reduction.

## Related documents

- [01_prd_TEMPLATE.md](01_prd_TEMPLATE.md) — the PRD explains which users and outcomes matter most.
- [02_requirements_catalog_TEMPLATE.md](02_requirements_catalog_TEMPLATE.md) — journeys often reveal missing requirements or clarify ambiguous ones.
- [05_acceptance_catalog_TEMPLATE.md](05_acceptance_catalog_TEMPLATE.md) — critical journey paths should become explicit acceptance scenarios.
- [../05_testing_acceptance/04_uat_plan_TEMPLATE.md](../05_testing_acceptance/04_uat_plan_TEMPLATE.md) — UAT scenarios should exercise the most important journeys end to end.
