---
title: Resilience Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: execution
cadence: per-stage
last_reviewed: 2026-05-07
---

# Resilience Template

> **Purpose**: capture the expected failure modes, redundancy model, degradation policy, and validation approach for resilience.
> **Audience**: architects, engineers, operators, and reviewers focused on continuity and recovery.
> **When to update**: update when failure assumptions, redundancy patterns, or recovery expectations change.

## How to use this template

- Focus on the failures that materially affect users or operations.
- Describe what the system should do under stress, dependency loss, or partial outage.
- Link detailed procedures to runbooks instead of duplicating them here.

## Failure modes

List the most important component, dependency, data, and human-process failures.

- Example: database unavailable, queue backlog growth, third-party timeout, bad deployment.

## Redundancy

Describe the redundancy model for critical compute, data, and connectivity paths.

- Note single points of failure that are accepted or still unresolved.

## Failover

Explain automated and manual failover expectations.

- Include triggers, owner, and recovery target where relevant.

## Degradation policy

State what features may degrade, what must remain available, and what must fail closed.

- Example: read-only mode during write-path recovery.

## Chaos testing approach

Describe how resilience assumptions are tested.

- Example: game days, fault injection, dependency throttling, restore drills.

## Related documents

- [07_deployment_TEMPLATE.md](07_deployment_TEMPLATE.md) — topology and environment dependencies.
- [08_observability_TEMPLATE.md](08_observability_TEMPLATE.md) — telemetry used to detect and confirm resilience behavior.
- [../06_security_operations/10_runbook_index_TEMPLATE.md](../06_security_operations/10_runbook_index_TEMPLATE.md) — operational response procedures.
