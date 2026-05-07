---
title: Glossary Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: references-maintainer
capability: references
phase: n/a
cadence: monthly
last_reviewed: 2026-05-07
---

# Glossary Template

> **Purpose**: maintain the canonical definitions for key terms, abbreviations, and overloaded phrases used across the documentation system.
> **Audience**: internal teams and managers who need consistent language across governance, product, architecture, testing, operations, and delivery artifacts.
> **When to update**: update when a shared term is introduced, redefined, or linked to a new canonical source.

## How to use this template

Use this glossary for terms that appear in multiple folders or carry a meaning that could be misunderstood without context. Keep definitions short, plain-language, and linked to the artifact that owns the term operationally.

- Add terms only when they help multiple readers or reduce ambiguity across folders.
- Prefer one canonical term over near-duplicates; use notes to call out discouraged synonyms.
- Link each term to the source artifact that gives it operational meaning.

## What belongs here

Include terms that affect project control, requirements, design, testing, security, delivery, or end-user support. Do not turn this file into a general encyclopedia.

- Good examples: stage gate, acceptance catalog, ADR, runbook, service acceptance, tolerance.
- Usually out of scope: one-off product names, temporary code names, or tool commands that belong in user docs.

## Glossary register

Use one row per canonical term.

| Term | Definition | Examples or notes | Canonical source link |
| --- | --- | --- | --- |
| Stage gate | Formal decision point used to confirm entry or exit criteria before work advances. | Example: planning baseline approval before execution authorization. | [../00_governance/09_stage_gate_checklist_TEMPLATE.md](../00_governance/09_stage_gate_checklist_TEMPLATE.md) |
| ADR | Architecture decision record capturing a material technical decision and its rationale. | Example: select an integration pattern, deployment boundary, or data ownership rule. | [../adr/ADR-000-template.md](../adr/ADR-000-template.md) |
| Service acceptance | Formal operational sign-off that confirms a service is supportable, secure, and ready for live ownership. | Example: runbooks, backups, access control, and support handoff reviewed before go-live. | [../06_security_operations/08_service_acceptance_TEMPLATE.md](../06_security_operations/08_service_acceptance_TEMPLATE.md) |

## Term-writing guidance

Keep terms scannable and operational.

- Start with what the term means in this repo, not its textbook definition.
- Use examples only when they reduce ambiguity.
- If a term changes meaning by audience, call out the difference explicitly.

## Review and governance rules

Glossary changes should be lightweight but deliberate. Review additions that could change approvals, traceability, or reporting language with the owning artifact maintainer.

- Check governance-heavy terms against [../00_governance/README.md](../00_governance/README.md).
- Check architecture-heavy terms against [../03_architecture/README.md](../03_architecture/README.md) and [../adr/README.md](../adr/README.md).
- Check operations-heavy terms against [../06_security_operations/README.md](../06_security_operations/README.md).

## Related documents

- [01_standards_register_TEMPLATE.md](01_standards_register_TEMPLATE.md) — explains the external frameworks behind many glossary terms.
- [03_decision_rights_matrix_TEMPLATE.md](03_decision_rights_matrix_TEMPLATE.md) — uses role and decision terminology that should stay consistent with this glossary.
- [../00_governance/12_requirements_traceability_matrix_TEMPLATE.md](../00_governance/12_requirements_traceability_matrix_TEMPLATE.md) — depends on consistent term use for requirement and evidence references.
- [../03_architecture/01_solution_design_TEMPLATE.md](../03_architecture/01_solution_design_TEMPLATE.md) — often introduces technical terms that should link back here when reused broadly.
