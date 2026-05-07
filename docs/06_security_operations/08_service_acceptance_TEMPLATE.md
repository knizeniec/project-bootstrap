---
title: Service Acceptance Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: service-owner
capability: operations
phase: execution
cadence: per-release
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Service Acceptance Template

> **Purpose**: define the operational, security, support, and readiness checks required before a service or release is accepted.
> **Audience**: service owners, operations teams, release managers, and managers making go or no-go decisions.
> **When to update**: update when readiness criteria, sign-off roles, conditional acceptance rules, or release dependencies change.

## How to use this template

Use this template at the point where delivery hands work over to live-service ownership or where a release needs formal operational acceptance. Keep it check-based, evidence-linked, and decision-ready.

- Mandatory: criteria, checks, sign-off roles, and conditional acceptance rules.
- Optional: links to detailed execution evidence if the summary here is sufficient for decision forums.
- Remove checks that are no longer relevant to the service boundary or support model.

## Acceptance criteria

State the high-level conditions that must be true before the service can be accepted. These criteria should summarize operational readiness, not reproduce every lower-level task.

- Example: service has named owners, tested support path, approved security posture, and monitored release plan.
- Example: open risks above agreed threshold must be resolved or explicitly accepted.

## Checks (security/operability/observability/runbooks/training)

List the required checks and where the supporting evidence lives. Keep the checks grouped so reviewers can quickly see if a readiness area is incomplete.

- Example: security baseline met, alerts tested, dashboards reviewed, runbooks published, support training completed.
- Example: backup drill evidence, access review completed, and incident contacts confirmed.

## Sign-off roles

Define who recommends acceptance, who approves it, and who records the final state. Separate delivery, operations, security, and business responsibilities when needed.

- Example: release manager recommends, service owner and operations lead approve, PM records the decision.
- Example: security lead signs off only the security control subset.

## Conditional acceptance

Explain how temporary exceptions are handled when the service can launch with bounded residual risk. Conditional acceptance should always include owner, expiry, and follow-up action.

- Example: low-risk documentation gap accepted for 7 days with named owner and completion date.
- Example: performance tuning accepted only for limited pilot traffic, not full-scale rollout.

## Related documents

- [10_runbook_index_TEMPLATE.md](10_runbook_index_TEMPLATE.md) — provides the runbook set that must exist before acceptance.
- [../07_delivery/07_release_plan_TEMPLATE.md](../07_delivery/07_release_plan_TEMPLATE.md) — uses this acceptance outcome during final release approval.
- [03_operating_model_TEMPLATE.md](03_operating_model_TEMPLATE.md) — defines who will own and operate the accepted service.
- [01_security_baseline_TEMPLATE.md](01_security_baseline_TEMPLATE.md) — provides the baseline control expectations checked here.
