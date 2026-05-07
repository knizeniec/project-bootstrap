---
title: RFC-000 Template
status: draft
record_class: canonical
audience: [internal]
owner: architecture-maintainer
capability: architecture
phase: planning
cadence: per-stage
last_reviewed: 2026-05-07
---

# RFC-000 Template

> **Purpose**: provide the default template for a review-stage architecture proposal.
> **Audience**: authors, reviewers, and decision-makers evaluating a proposed change.
> **When to update**: update when RFC authoring or review expectations change.

## How to use this template

- Use one RFC for one proposal or tightly scoped set of alternatives.
- Keep frontmatter `status` schema-valid for the repo; record any RFC-specific outcome wording in the body.
- If the proposal becomes a durable implementation decision, create or update the matching ADR using [../../adr/ADR-000-template.md](../../adr/ADR-000-template.md).

## Title

State the proposal in one short sentence.

## Status

Record the RFC lifecycle clearly in the body.

- Typical RFC states: draft, proposed, accepted, rejected, superseded.
- For validator compatibility, keep frontmatter `status` within the repo schema and explain any rejected outcome here.

## Context

Describe the problem, scope, forces, and why review is needed now.

## Proposal

State the proposed approach in clear, testable terms.

- Include boundaries, responsibilities, and rollout assumptions.

## Alternatives considered

List the realistic alternatives and why they were not selected.

- Keep trade-offs explicit.

## Drawbacks

Call out costs, risks, complexity, or lock-in introduced by the proposal.

## Unresolved questions

List the open issues that reviewers must help answer.

## Security and privacy implications

Note trust boundaries, data sensitivity, access concerns, and audit needs.

## Prior art

Reference comparable systems, prior internal patterns, or external guidance.

## References

- Link related solution design, C4 views, tickets, experiments, and ADRs.
- If accepted as a durable decision, link the resulting ADR.

## Related documents

- [README.md](README.md) — RFC lifecycle and graduation rules.
- [../12_rfc_index_TEMPLATE.md](../12_rfc_index_TEMPLATE.md) — tracking index for open and closed RFCs.
- [../01_solution_design_TEMPLATE.md](../01_solution_design_TEMPLATE.md) — parent architecture baseline.
- [../../adr/ADR-000-template.md](../../adr/ADR-000-template.md) — target template for durable accepted decisions.
