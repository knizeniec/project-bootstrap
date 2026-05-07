---
title: Reference Templates
status: draft
record_class: canonical
audience: [internal, manager]
owner: references-maintainer
capability: references
phase: n/a
cadence: monthly
last_reviewed: 2026-05-07
---

# Reference Templates

> **Purpose**: orient readers to the canonical reference artifacts that define standards, shared language, policy traceability, and reusable lessons.
> **Audience**: internal teams and managers who need one place for standards posture, glossary terms, decision rights, and reference mappings.
> **When to update**: update when the reference set, reading order, or cross-area ownership guidance changes.

## How to use this template

Use this landing page to pick the smallest reference artifact that solves the current question, then follow its linked downstream documents instead of duplicating guidance in delivery or governance records.

- Start with the standards register when you need to justify why a framework or standard is adopted, adapted, or reference-only.
- Use the glossary to normalize terms before writing governance, product, architecture, or operations records.
- Use the policy mappings and lessons-learned index when reviews need traceability from external expectations to internal artifacts and follow-up actions.

## Folder purpose

This folder is the shared reference layer for the numbered documentation tree. It does not replace governance, architecture, delivery, testing, or operations records; it helps those areas stay consistent by defining the external frames of reference and internal shared vocabulary they rely on.

- Typical use: show why arc42, C4, MADR, PMBOK, or ISO-derived practices appear elsewhere in the repo.
- Typical use: point auditors or managers to a single policy-to-artifact map instead of repeating control mappings in multiple folders.
- Typical use: keep lessons visible after a release without turning post-launch reviews into the only place reusable learning lives.

## Reading order

Read the standards register first so readers know which external frameworks are mandatory, adapted, or informative only. Then use the glossary and decision-rights matrix to align language and authority before moving into policy mappings and lessons.

1. [01_standards_register_TEMPLATE.md](01_standards_register_TEMPLATE.md)
2. [02_glossary_TEMPLATE.md](02_glossary_TEMPLATE.md)
3. [03_decision_rights_matrix_TEMPLATE.md](03_decision_rights_matrix_TEMPLATE.md)
4. [04_policy_mappings_TEMPLATE.md](04_policy_mappings_TEMPLATE.md)
5. [05_lessons_learned_index_TEMPLATE.md](05_lessons_learned_index_TEMPLATE.md)
6. [INDEX.md](INDEX.md)

## Artifact index

Use the list below as the quick chooser for this folder.

- [01_standards_register_TEMPLATE.md](01_standards_register_TEMPLATE.md) — adopted, adapted, and reference-only standards with rationale, boundaries, and downstream target areas.
- [02_glossary_TEMPLATE.md](02_glossary_TEMPLATE.md) — canonical term register with definitions, examples, and source links.
- [03_decision_rights_matrix_TEMPLATE.md](03_decision_rights_matrix_TEMPLATE.md) — project-ready RACI or DACI matrix for governance and change decisions.
- [04_policy_mappings_TEMPLATE.md](04_policy_mappings_TEMPLATE.md) — external policy or control expectations mapped to internal canonical artifacts.
- [05_lessons_learned_index_TEMPLATE.md](05_lessons_learned_index_TEMPLATE.md) — reusable learning log linked to releases, reviews, and action status.
- [INDEX.md](INDEX.md) — compact folder index shaped for future frontmatter-driven generation.

## Related documents

- [INDEX.md](INDEX.md) — compact navigation for this folder and a pointer back to the root index.
- [../README.md](../README.md) — root documentation entrypoint for the full canonical tree.
- [../INDEX.md](../INDEX.md) — root navigation map this folder should align with.
- [../00_operating_model/04_frontmatter_schema.md](../00_operating_model/04_frontmatter_schema.md) — frontmatter contract this folder must satisfy.
