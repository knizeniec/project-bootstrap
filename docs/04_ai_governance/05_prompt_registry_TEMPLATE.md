---
title: Prompt Registry Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: ai-governance
capability: ai_governance
phase: execution
cadence: monthly
last_reviewed: 2026-05-07
---

# Prompt Registry Template

> **Purpose:** maintain a controlled inventory of prompts, versions, owners, and evaluation links for AI-enabled features.
> **Audience:** AI governance, engineering, QA, and operators who need prompt-level traceability and change awareness.
> **When to update:** update when prompts are added, revised, retired, re-evaluated, or reassigned.

## How to use this template

Use this registry when prompts materially affect product behavior, safety, or compliance. Keep one row per managed prompt version, and link to the source location rather than pasting long prompt text unless policy requires it.

- Store stable IDs so evaluation reports and incidents can reference the same prompt lineage.
- Record the prompt text location, not just the friendly name.
- Remove sample rows before publishing an active registry.

## Prompt registry

Use the table below as the canonical inventory for governed prompts. Each row should make it easy to answer what the prompt does, which model it targets, who owns it, and when it was last evaluated.

| ID | Version | Purpose | Model target | Prompt text reference | Owner | Last-eval date | Change history pointer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | v1 | [Purpose] | [Model/version] | [Repo path or registry link] | [Role] | 2026-05-07 | [ADR, changelog, or issue link] |
| PR-002 | v2 | [Purpose] | [Model/version] | [Reference] | [Role] | 2026-05-07 | [Pointer] |

- Example `purpose` values: summarization, extraction, safety guard, classification.
- Example `change history pointer` values: ADR, release note, pull request, experiment log.

## Related documents

- [04_evaluation_report_TEMPLATE.md](04_evaluation_report_TEMPLATE.md) — prompt changes should be backed by evaluation reports when behavior changes materially.
- [01_ai_use_policy_TEMPLATE.md](01_ai_use_policy_TEMPLATE.md) — prompt behavior must remain inside approved-use and data-boundary rules.
- [06_ai_risk_register_TEMPLATE.md](06_ai_risk_register_TEMPLATE.md) — prompt injection, jailbreak, and leakage risks should be tracked alongside governed prompts.
- [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md) — the security baseline provides control requirements for prompt handling, logging, and secrets exposure.
