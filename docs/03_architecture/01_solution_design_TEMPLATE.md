# Solution Design Template

Status: Active
Owner: [Role or team responsible for architecture docs]
Purpose: provide a starter template for describing the target solution, architecture boundaries, and technical design rationale
Last updated: YYYY-MM-DD

## How to use this template

- Copy this file when a project needs a primary architecture baseline.
- Keep this document aligned with accepted ADRs.
- Use diagrams and linked interface documents where they improve clarity.

## Goals and constraints

- Goal: [Technical or system goal]
- Goal: [Technical or system goal]
- Constraint: [Platform, compliance, operational, or timeline constraint]
- Constraint: [Constraint]

## Scope and system context

- System in scope: [What this design covers]
- External systems: [Main neighboring systems or actors]
- Key boundaries: [Trust, ownership, deployment, or data boundaries]

## Solution strategy

[Describe the overall design approach and why it fits the goals and constraints.]

## Building blocks

- Component or service: [Responsibility]
- Component or service: [Responsibility]
- Shared dependency or platform element: [Responsibility]

## Data, interfaces, and integrations

- Data model or storage direction: [Summary]
- Interface or API surface: [Summary]
- External integration: [Summary]

## Runtime and deployment view

- Runtime flow: [How requests, events, or jobs move through the system]
- Deployment shape: [Where the system runs and how it is deployed]
- Operational considerations: [Monitoring, scaling, recovery, or support expectations]

## Quality attributes and risks

- Reliability: [Approach or target]
- Performance: [Approach or target]
- Security: [Approach or target]
- Main risks or technical debt: [List]

## Decision links

- ADRs: [Relevant ADR references]
- Interface docs: [Relevant ICD references]
- Delivery docs: [Relevant rollout or implementation plan references]

## Related documents

- [06_interface_control_document_TEMPLATE.md](06_interface_control_document_TEMPLATE.md)
- [../project/adr/README.md](../project/adr/README.md)
- [../07_delivery/01_delivery_plan_TEMPLATE.md](../07_delivery/01_delivery_plan_TEMPLATE.md)
