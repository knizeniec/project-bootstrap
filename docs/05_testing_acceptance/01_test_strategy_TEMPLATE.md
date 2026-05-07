---
title: Test Strategy Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: quality-lead
capability: quality
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Test Strategy Template

> **Purpose**: define what will be tested, at which levels, in which environments, and what must be true before testing starts and ends.
> **Audience**: quality leads, engineers, product owners, and managers approving test scope and risk coverage.
> **When to update**: update when scope, risk posture, environments, tools, or acceptance expectations change.

## How to use this template

Use this template to set the verification baseline before detailed test design begins. Keep it focused on scope, levels, controls, and interfaces to product acceptance and defect handling.

- Mandatory: scope, test levels, environments, tools, and entry or exit criteria.
- Optional: tool-specific workflows if they already live in a team runbook.
- Remove assumptions that are no longer true once environments and ownership are confirmed.

## Scope

State the system, release, or change set covered by this strategy and note any explicit exclusions. Keep the wording decision-ready so reviewers can tell what the strategy governs.

- Example: release 2.1 customer messaging workflows, related APIs, and admin moderation paths.
- Example: out of scope are legacy exports scheduled for later retirement.

## Testing scope (functional/NFR/security/AI eval)

Describe the coverage split across functional behavior, non-functional requirements, security concerns, and any AI-specific evaluation work. Use this section to show risk-based emphasis rather than listing every test case.

- Example: functional coverage for core journeys, role permissions, and failure handling.
- Example: NFR and security coverage for latency, audit logging, rate limits, and prompt-safety evaluation.

## Levels (unit/integration/E2E/UAT)

Summarize which test levels are in scope and what each level is expected to prove. Make ownership boundaries clear so gaps between engineering, QA, and business acceptance are visible.

- Example: unit tests prove domain rules, integration tests prove service boundaries, E2E tests prove critical journeys.
- Example: UAT confirms real user workflows and business acceptance, not technical regression depth.

## Environments

List the environments used for each verification level and any environmental constraints that affect confidence. Call out data, access, or parity limitations early.

- Example: CI for unit and integration, staging for E2E rehearsal, UAT tenant for business validation.
- Example: masked production-like data required for performance and security checks.

## Tools

Name the core tools, dashboards, or repositories used to execute tests and store evidence. Keep it to the systems needed for traceability and review.

- Example: pytest suite, browser automation, API collection runner, vulnerability scanner.
- Example: evidence stored in CI artifacts, test management export, and linked screenshots.

## Entry/exit criteria

Define what must be true before testing begins and what evidence is required before the scope is considered complete. Use measurable statements so readiness reviews can apply the criteria consistently.

- Example: entry requires approved acceptance criteria, stable environment, and seeded test data.
- Example: exit requires critical scenarios passed, no open Sev-1 defects, and evidence logged in the verification index.

## Defect-management cross-link

Point readers to the canonical defect workflow and explain how defect status affects test completion and acceptance. This section should prevent teams from inventing separate triage rules inside the strategy.

- Example: use the defect management template for severity, SLA, and escalation rules.
- Example: unresolved high-severity defects block exit unless formally accepted as conditional risk.

## Related documents

- [03_verification_evidence_index_TEMPLATE.md](03_verification_evidence_index_TEMPLATE.md) — records the evidence that proves this strategy was executed.
- [../02_product/05_acceptance_catalog_TEMPLATE.md](../02_product/05_acceptance_catalog_TEMPLATE.md) — supplies the acceptance scenarios this strategy must verify.
- [05_defect_management_TEMPLATE.md](05_defect_management_TEMPLATE.md) — defines the canonical triage and defect closure rules referenced here.
- [04_uat_plan_TEMPLATE.md](04_uat_plan_TEMPLATE.md) — details business-led acceptance activity that sits on top of this strategy.
