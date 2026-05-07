---
title: AI Risk Register Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: ai-governance
capability: knowledge
phase: monitoring
cadence: monthly
last_reviewed: 2026-05-07
---

# AI Risk Register Template

> **Purpose:** maintain the live inventory of AI-specific risks, mitigations, owners, and review cadence for an AI-enabled project.
> **Audience:** AI governance, delivery, security, and management roles who need ongoing visibility into AI risk posture.
> **When to update:** update when new AI risks appear, likelihood or impact changes, mitigations change, or review outcomes change.

## How to use this template

Use this register for risks that are specific to model behavior, prompt behavior, data handling, or AI-related compliance exposure. Keep risk entries concise and operationally useful; if a risk becomes a live incident, link out to the incident and post-incident records rather than turning this file into a narrative log.

- Keep one row per distinct risk with a named owner.
- Review the register on a fixed cadence and after major AI changes.
- Remove sample rows before publishing an active register.

## AI risk register

Use the table below as the canonical AI-risk inventory. Include enough detail that a reviewer can see the risk theme, mitigation approach, ownership, and how often it is checked.

| Risk ID | Risk type | Description | Mitigation | Owner | Review cadence |
| --- | --- | --- | --- | --- | --- |
| AIR-001 | hallucination | [How incorrect confident output could cause harm] | [Control or mitigation] | [Role] | monthly |
| AIR-002 | prompt injection | [How hostile input could subvert behavior] | [Control or mitigation] | [Role] | monthly |
| AIR-003 | data leakage | [How data exposure could occur] | [Control or mitigation] | [Role] | per-release |
| AIR-004 | bias | [How unfair outcomes could arise] | [Control or mitigation] | [Role] | monthly |
| AIR-005 | compliance | [How contractual or regulatory breach could occur] | [Control or mitigation] | [Role] | monthly |

- Example additional risk types: model drift, unsafe refusal failure, tool misuse, vendor outage.
- Example mitigation patterns: human review, redaction, sandboxing, policy refusal, monitoring alert, release gate.

## Related documents

- [01_ai_use_policy_TEMPLATE.md](01_ai_use_policy_TEMPLATE.md) — the policy defines which AI uses are allowed and what boundaries should reduce these risks.
- [04_evaluation_report_TEMPLATE.md](04_evaluation_report_TEMPLATE.md) — evaluation reports provide evidence for whether key risks are improving or worsening.
- [02_model_card_TEMPLATE.md](02_model_card_TEMPLATE.md) — model limitations and caveats should feed directly into this register.
- [../06_security_operations/01_security_baseline_TEMPLATE.md](../06_security_operations/01_security_baseline_TEMPLATE.md) — broader technical controls for leakage, access, logging, and hardening live in the security baseline.
