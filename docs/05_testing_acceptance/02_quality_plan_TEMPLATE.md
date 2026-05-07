---
title: Quality Plan Template
status: draft
record_class: canonical
audience: [internal, manager]
owner: quality-manager
capability: quality
phase: planning
cadence: monthly
last_reviewed: 2026-05-07
source_of_truth: repo
---

# Quality Plan Template

> **Purpose**: define how the team will measure, review, and gate quality across the delivery lifecycle.
> **Audience**: quality managers, delivery leads, and managers responsible for approving quality thresholds and assurance activity.
> **When to update**: update when quality objectives, metrics, review methods, or gate expectations change.

## How to use this template

Use this template to describe the control system around testing, reviews, and assurance. Keep the plan metric-driven and phase-aware rather than turning it into a detailed execution log.

- Mandatory: objectives, metrics, review activities, audits, and phase gates.
- Optional: team-local dashboards if the canonical thresholds are already stated here.
- Remove vanity measures that do not change decisions or trigger actions.

## Quality objectives

State the few quality outcomes that matter most for this work. Objectives should describe the intended level of reliability, usability, security, or compliance rather than vague aspirations.

- Example: critical user journeys complete reliably under expected load.
- Example: release decisions use documented evidence instead of informal confidence.

## Metrics (coverage, defect density, escaped defects)

List the metrics that will be reviewed, what they mean, and what action thresholds apply. Use only measures the team can collect consistently and interpret correctly.

- Example: automated coverage threshold for critical modules, defect density trend by release, escaped defects in the first 14 days.
- Example: open critical defect count and mean time to close high-severity issues.

## Reviews

Describe the planned review activities that improve quality before formal testing or release. Include design, code, test, content, or readiness reviews as relevant.

- Example: requirement review before test design and peer review before merge.
- Example: release-readiness review using the evidence index and readiness tracker.

## Audits

Explain what independent or semi-independent checks are expected and what they will inspect. Keep the focus on assurance evidence, policy conformance, and traceability.

- Example: audit of requirement-to-test traceability for regulated workflows.
- Example: spot check of evidence links, sign-off records, and security verification outputs.

## Quality gates per phase

Define the minimum quality conditions for initiation, planning, execution, monitoring, and release or closure as applicable. Make each gate observable so it can be used in stage reviews.

- Example: planning gate requires approved strategy and acceptance catalog alignment.
- Example: execution gate requires evidence current, defect backlog within threshold, and UAT pass criteria met.

## Related documents

- [01_test_strategy_TEMPLATE.md](01_test_strategy_TEMPLATE.md) — provides the testing structure this quality plan governs.
- [03_verification_evidence_index_TEMPLATE.md](03_verification_evidence_index_TEMPLATE.md) — holds the proof used to measure gate completion.
- [../07_delivery/06_readiness_tracker_TEMPLATE.md](../07_delivery/06_readiness_tracker_TEMPLATE.md) — captures whether the defined quality gates are satisfied.
- [../02_product/05_acceptance_catalog_TEMPLATE.md](../02_product/05_acceptance_catalog_TEMPLATE.md) — anchors quality checks to accepted product outcomes.
