---
title: Defect Management Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: qa-lead
capability: quality
phase: monitoring
cadence: weekly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Defect Management Template

> **Purpose**: define the canonical process for triaging, prioritizing, tracking, and reviewing defects.
> **Audience**: QA leads, engineers, product owners, support teams, and managers responsible for defect decisions and response times.
> **When to update**: update when severity rules, SLA targets, reporting cadence, or review responsibilities change.

## How to use this template

Use this template to document the common defect workflow used across testing, UAT, and early-live support. Keep it policy-oriented and link to tool dashboards for live defect lists.

- Mandatory: triage flow, severity scale, SLA expectations, reporting cadence, and escaped-defect review.
- Optional: team-specific queue views if the canonical workflow is already clear here.
- Remove duplicate status definitions if they already exist in the defect tool configuration.

## Triage process

Describe how defects are logged, reviewed, assigned, and moved through decision states. Make the ownership and escalation path explicit so work does not stall between teams.

- Example: QA validates reproducibility, product confirms business impact, engineering estimates fix path.
- Example: unresolved ownership after 24 hours escalates to delivery lead.

## Severity scale

Define the severity levels used to classify impact and urgency. Keep the scale short and aligned with release and support decision-making.

- Example: Sev-1 blocks core service or creates regulatory risk; Sev-2 degrades a major workflow with workaround limits.
- Example: Sev-3 has acceptable workaround; Sev-4 is minor or cosmetic.

## SLAs

State the expected response and resolution targets by severity or workflow stage. Clarify whether the targets are internal goals or formal commitments.

- Example: Sev-1 acknowledged within 30 minutes and workaround or fix plan within 4 hours.
- Example: Sev-3 reviewed in weekly triage and scheduled into the next planned release.

## Reporting cadence

Describe when defect status is summarized and who receives the report. Keep this section tied to governance and release decisions rather than duplicating ticket-level detail.

- Example: daily release-war-room updates during cutover week and weekly portfolio summary otherwise.
- Example: trend chart shared with managers showing opened, closed, and escaped defects.

## Escape-defect review

Explain how defects found after release or outside planned verification are reviewed for root cause and preventive action. This should connect directly to learning and post-launch improvement.

- Example: escaped defects reviewed within 5 working days with root cause, missed signal, and improvement action.
- Example: repeated category of misses triggers strategy or automation updates.

## Related documents

- [01_test_strategy_TEMPLATE.md](01_test_strategy_TEMPLATE.md) — references this defect workflow as part of exit and acceptance control.
- [04_uat_plan_TEMPLATE.md](04_uat_plan_TEMPLATE.md) — relies on severity and closure rules during business acceptance.
- [../06_security_operations/09_post_launch_review_TEMPLATE.md](../06_security_operations/09_post_launch_review_TEMPLATE.md) — uses escaped-defect information to assess early-live outcomes.
- [../07_delivery/04_status_report_TEMPLATE.md](../07_delivery/04_status_report_TEMPLATE.md) — summarizes defect trends for delivery governance.
