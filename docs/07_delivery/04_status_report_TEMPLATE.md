---
title: Status Report Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: project-manager
capability: execution
phase: monitoring
cadence: weekly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Status Report Template

> **Purpose**: provide the recurring management snapshot of progress, health, risks, and immediate decisions needed.
> **Audience**: delivery leads and managers who review weekly execution status and decide on actions.
> **When to update**: update on the agreed weekly cadence and before any governance forum needing current status.

## How to use this template

Use this template for the canonical weekly status view, even if detailed task tracking lives elsewhere. Keep it brief, decision-oriented, and consistent from week to week so trends are easy to read.

- Mandatory: period, RAG summary, progress, risks/issues, decisions needed, and next-period focus.
- Optional: supporting links to detailed metrics or delivery tooling.
- Remove narrative history that no longer affects the current reporting decision.

## Period

Record the reporting window, report owner, and any meeting or decision forum the update supports. A clear period marker keeps weekly reports auditable and comparable.

- Example: week ending date, board pack reference, and author role.
- Example: current stage or release wave covered by the report.

## RAG status (scope/schedule/cost/quality)

Provide the headline RAG view and a short explanation for any amber or red area. Keep the logic stable so readers can compare one report to the next without re-learning the scale.

- Example: schedule amber due to an external dependency slip.
- Example: quality red because critical defects exceed release threshold.

## Progress against plan

Summarize what moved forward during the period relative to the delivery or stage plan. Focus on completed outcomes and meaningful variance instead of listing every team activity.

- Example: build completed for workstream A and rehearsal started on plan.
- Example: milestone achieved early or delayed, with the reason noted.

## Risks and issues since last report

Highlight what changed in the control picture and what management attention is needed now. This section should pull from the live RAID register rather than maintain a competing list.

- Example: new high risk raised, issue closed, dependency escalated.
- Example: assumption invalidated and converted into a tracked issue.

## Decisions needed

List the decisions or approvals the project needs before the next reporting cycle. Make each ask explicit so the report drives action rather than passive awareness.

- Example: approve scope trade-off to protect release date.
- Example: confirm additional resourcing or accept stage tolerance breach.

## Next-period focus

State the main objectives for the next reporting period so readers know what good progress looks like next week. This also helps reviewers judge whether the plan remains realistic.

- Example: close top three readiness gaps and complete cutover rehearsal.
- Example: secure change approval and finalize client communications.

## Related documents

- [../00_governance/06_raid_register_TEMPLATE.md](../00_governance/06_raid_register_TEMPLATE.md) — provides the underlying risks, assumptions, issues, and dependencies summarized here.
- [../00_governance/07_change_control_log_TEMPLATE.md](../00_governance/07_change_control_log_TEMPLATE.md) — records formal change decisions referenced by the report.
- [06_readiness_tracker_TEMPLATE.md](06_readiness_tracker_TEMPLATE.md) — shows whether execution and release-readiness domains are trending green.
