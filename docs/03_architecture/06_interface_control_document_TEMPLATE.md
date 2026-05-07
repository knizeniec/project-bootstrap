# Interface Control Document Template

Status: Active
Owner: Architecture maintainers
Purpose: provide a starter template for documenting an interface, contract, or integration boundary
Last updated: 2026-05-06

## How to use this template

- Copy this file when a system boundary needs a durable contract document.
- Keep it specific to one interface or integration.
- Link to the parent solution design and any governing ADRs.

## Interface summary

- Interface name: [Name]
- Owner: [Role or team]
- Consumers: [Systems, teams, or user groups]
- Purpose: [Why this interface exists]

## Contract definition

- Inputs: [Requests, messages, files, or events received]
- Outputs: [Responses, messages, files, or state changes produced]
- Protocol or transport: [HTTP, queue, file exchange, internal API, and so on]
- Data contract: [Schema, payload, or field expectations]

## Operational behavior

- Authentication and authorization: [Rules]
- Error handling and retries: [Behavior]
- Timeout, latency, or throughput expectations: [Constraints]
- Observability: [Logs, metrics, traces, alerts]

## Dependencies and failure modes

- Upstream dependencies: [List]
- Downstream dependencies: [List]
- Failure mode 1: [What can fail and what happens]
- Failure mode 2: [What can fail and what happens]

## Change control

- Versioning approach: [How contract changes are managed]
- Compatibility expectations: [Backward compatibility or migration rules]
- Governing ADRs: [ADR references]

## Related documents

- [01_solution_design_TEMPLATE.md](01_solution_design_TEMPLATE.md)
- [../adr/README.md](../adr/README.md)
