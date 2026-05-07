---
title: Support Model Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: support-lead
capability: operations
phase: execution
cadence: monthly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Support Model Template

> **Purpose**: define how support requests are received, triaged, resolved, and handed between support tiers.
> **Audience**: support leads, operations teams, delivery teams, and managers responsible for service-support effectiveness.
> **When to update**: update when support tiers, channels, SLA targets, or handover arrangements change.

## How to use this template

Use this template to describe the ongoing support path for live users and operators. Keep it centered on who handles what, how requests arrive, and how delivery hands work over to support.

- Mandatory: support tiers, intake channels, SLA expectations, knowledge base, and handover.
- Optional: tool-specific queue settings if those are maintained elsewhere.
- Remove one-off launch-support arrangements once steady-state support begins.

## Support tiers (L1/L2/L3)

Define what each support tier owns and where escalation between tiers should occur. Keep the distinctions practical so ticket routing is predictable.

- Example: L1 handles intake and known issues, L2 handles environment and data checks, L3 handles code or deep platform defects.
- Example: product or delivery teams provide temporary L3 cover during early life support.

## Intake channels

List the approved channels for incidents, requests, and service questions. Clarify what should and should not be raised through each path.

- Example: service desk portal for standard requests, paging tool for major incidents, support email for low-severity issues.
- Example: customer success route for business-process questions that are not service faults.

## SLAs

Describe the response and resolution targets by severity or ticket type. Keep the commitments aligned with support capacity and business expectations.

- Example: critical service outage acknowledged in 15 minutes, standard request within 1 business day.
- Example: target resolution clock pauses when waiting for customer input.

## Knowledge base

Explain where repeatable support knowledge is stored and how it stays current. This should connect directly to the runbook index and user-facing help where relevant.

- Example: internal runbooks for operators and separate how-to articles for end users.
- Example: every resolved recurring issue must produce or update a knowledge article.

## Handover from delivery

Describe what delivery must provide before support can own the service confidently. Focus on knowledge transfer, readiness evidence, and unresolved risk visibility.

- Example: runbooks, known issues list, service acceptance record, and on-call contacts provided before handover.
- Example: open medium-risk items transferred with owner, target date, and mitigation notes.

## Related documents

- [03_operating_model_TEMPLATE.md](03_operating_model_TEMPLATE.md) — defines the wider live-service ownership and escalation structure for support.
- [10_runbook_index_TEMPLATE.md](10_runbook_index_TEMPLATE.md) — points to the operational procedures support teams use.
- [08_service_acceptance_TEMPLATE.md](08_service_acceptance_TEMPLATE.md) — ensures support readiness is complete before acceptance.
- [09_post_launch_review_TEMPLATE.md](09_post_launch_review_TEMPLATE.md) — reviews whether the support model worked in early life.
