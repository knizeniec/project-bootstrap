---
title: Observability Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: execution
cadence: monthly
last_reviewed: 2026-05-07
---

# Observability Template

> **Purpose**: define the logging, metrics, traces, alerts, and dashboards needed to operate the solution.
> **Audience**: engineers, SRE or operations teams, and reviewers validating operational readiness.
> **When to update**: update when telemetry coverage, SLOs, retention, or alerting strategy changes.

## How to use this template

- Capture only the telemetry design that needs shared agreement.
- Link implementation-specific dashboards or queries rather than pasting large exports.
- Keep signals mapped to important user journeys and failure modes.

## Logs

Define log structure, severity levels, redaction rules, and retention expectations.

- Example: JSON logs with request ID, actor ID, and outcome code.

## Metrics

List the golden signals, business metrics, and service-level indicators that matter.

- Include target SLOs where they exist.

## Traces

Describe trace boundaries, span naming expectations, and cross-service correlation rules.

- Note where end-to-end tracing is mandatory.

## Alerts

Explain the conditions that should page, warn, or create tickets.

- Keep alert ownership and escalation paths explicit.

## Dashboards

List the minimum dashboard views needed for release, incident response, and routine operation.

- Example: service health, dependency health, business throughput.

## Related documents

- [07_deployment_TEMPLATE.md](07_deployment_TEMPLATE.md) — runtime topology and environment placement.
- [09_resilience_TEMPLATE.md](09_resilience_TEMPLATE.md) — failure modes that drive monitoring priorities.
- [../06_security_operations/10_runbook_index_TEMPLATE.md](../06_security_operations/10_runbook_index_TEMPLATE.md) — operational procedures used when alerts fire.
