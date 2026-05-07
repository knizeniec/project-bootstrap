# AI Use Policy Template

Status: Active
Owner: [Role or team responsible for AI governance]
Purpose: provide a starter template for defining approved use, restricted use, approval workflow, and oversight for AI components in this project
Last updated: YYYY-MM-DD

## How to use this template

- Copy this file when defining the AI use baseline for a project that uses, embeds, or operates AI models.
- Keep this policy aligned with accepted ADRs and with [../00_governance/README.md](../00_governance/README.md).
- Link evaluation evidence and incident records from [../05_testing_acceptance/README.md](../05_testing_acceptance/README.md) and [../06_security_operations/README.md](../06_security_operations/README.md).

## Scope

- Systems in scope: [Components, agents, pipelines, or model-backed features covered by this policy]
- Systems out of scope: [Explicit exclusions]
- Applicable model classes: [Foundation models, fine-tuned variants, embeddings, classifiers, or rule-based fallbacks]

## Approved use cases

| ID | Use case | Owner | Notes |
| --- | --- | --- | --- |
| AI-001 | [Approved purpose, audience, and data class] | [Role or team] | [Constraints or model class] |
| AI-002 | [Approved purpose] | [Owner] | [Notes] |

## Restricted or prohibited use cases

| ID | Restriction | Reason | Notes |
| --- | --- | --- | --- |
| AI-R-001 | [Disallowed purpose, audience, or data class] | [Risk, regulatory, or contract reason] | [Notes] |
| AI-R-002 | [Restriction] | [Reason] | [Notes] |

## Data and model boundaries

- Data classes that may be sent to AI components: [Public, internal, confidential, regulated]
- Data classes that must not be sent: [Class and reason]
- Model providers and deployment surfaces: [Hosted, self-hosted, on-device]
- Retention and logging expectations: [What is logged, where, for how long]

## Approval workflow

- Triage: [Who reviews new AI use requests and how]
- Approval gates: [Risk class to approver mapping]
- Documentation: [Where approved use is recorded — typically an ADR plus an entry in this file]
- Re-review cadence: [Frequency or trigger]

## Evaluation and safety

- Pre-deployment evaluation: [Required tests, datasets, and acceptance thresholds]
- Ongoing monitoring: [Metrics, alerting, and dashboards]
- Human oversight: [Where humans review or override outputs]
- Red-team or adversarial testing: [Frequency and scope]
- Incident response: [Trigger conditions and pointer to runbook in `../06_security_operations/`]

## Compliance and external references

- Applicable frameworks or regulations: [NIST AI RMF, ISO/IEC 42001, EU AI Act, sector regulation]
- Internal standards: [Pointer to `../00-documentation-standards.md` and relevant `../00_governance/`]
- Vendor and contract obligations: [Pointer to entry in `../08_references/`]

## Owners and approvers

- Policy owner: [Role or team]
- Technical approver: [Role]
- Risk or legal approver: [Role]
- Last review: [YYYY-MM-DD]
- Next review: [YYYY-MM-DD]

## Related documents

- [../03_architecture/01_solution_design_TEMPLATE.md](../03_architecture/01_solution_design_TEMPLATE.md)
- [../05_testing_acceptance/README.md](../05_testing_acceptance/README.md)
- [../06_security_operations/README.md](../06_security_operations/README.md)
- [../adr/README.md](../adr/README.md)
