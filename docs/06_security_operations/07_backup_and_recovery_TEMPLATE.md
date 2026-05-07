---
title: Backup And Recovery Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: operations-lead
capability: operations
phase: execution
cadence: monthly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Backup And Recovery Template

> **Purpose**: define what data is backed up, how often, how long it is retained, and how recovery is tested.
> **Audience**: operations teams, security teams, service owners, and managers responsible for resilience targets.
> **When to update**: update when data classes, backup tooling, retention rules, or recovery objectives change.

## How to use this template

Use this template to document resilience expectations for restore-capable services. Keep it focused on recoverability and evidence, with detailed restore steps linked from runbooks.

- Mandatory: data classes, cadence, retention, restore drills, and RPO or RTO.
- Optional: storage implementation details if those are already documented elsewhere.
- Remove backup assumptions that are not validated by restore testing.

## Data classes

List the data types or systems that require backup or reconstruction planning. Distinguish between critical records, rebuildable data, and externally sourced data.

- Example: transactional database, configuration state, audit logs, and user-uploaded files.
- Example: analytics cache may be rebuildable and therefore treated differently from source records.

## Backup cadence

State how often backups run and whether cadence varies by data class or environment. Keep the cadence tied to the recovery needs of the service.

- Example: nightly full backups with point-in-time recovery for primary transactional data.
- Example: weekly snapshot for lower-criticality configuration history.

## Retention

Define how long backups are kept and what policy or business reason supports that period. Include deletion or archival expectations if relevant.

- Example: daily backups retained 35 days, monthly backups retained 12 months.
- Example: legal or client obligations may require longer retention for specific records.

## Restore drills

Describe how often recovery is tested and what evidence must be kept. The goal is to prove recovery works, not just that backups exist.

- Example: quarterly restore drill for database and file store into isolated environment.
- Example: drill output records recovery duration, data integrity checks, and follow-up actions.

## RPO/RTO

State the recovery point objective and recovery time objective for the service or each critical component. Explain any differences between business expectation and technical capability.

- Example: RPO 15 minutes and RTO 2 hours for customer transaction data.
- Example: less critical reporting data may have longer recovery targets.

## Related documents

- [10_runbook_index_TEMPLATE.md](10_runbook_index_TEMPLATE.md) — should link to the detailed restore procedures that support this plan.
- [06_incident_response_TEMPLATE.md](06_incident_response_TEMPLATE.md) — calls on recovery procedures during major incidents.
- [08_service_acceptance_TEMPLATE.md](08_service_acceptance_TEMPLATE.md) — verifies backup and restore readiness before go-live.
- [03_operating_model_TEMPLATE.md](03_operating_model_TEMPLATE.md) — provides the live ownership for resilience activities and drills.
