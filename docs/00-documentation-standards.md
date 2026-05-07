# Documentation Standards

Status: Active
Owner: Documentation maintainers
Purpose: define writing, ownership, and maintenance rules for the active docs system
Last updated: 2026-05-07

## Scope

These standards apply to the control spine and the active numbered tree under `docs/`.

- Active canonical docs: `README.md`, `Architecture.md`, `00-documentation-standards.md`, `00-source-of-truth.md`, `INDEX.md`, and `00_governance/` through `08_references/`
- Durable decisions: `adr/`
- Working history only: `superpowers/`
- Evidence only: `99_archive/`

## Core rules

- Keep one active documentation system only. Current guidance belongs in the control spine or the numbered tree.
- Keep one canonical owner per concern. Use [00-source-of-truth.md](00-source-of-truth.md) to name that owner.
- Keep documents single-purpose. A document should mainly explain, instruct, reference, or record a decision.
- Prefer short headings, short paragraphs, small tables, and links over duplicated prose.
- State assumptions, unknowns, and approval conditions explicitly.
- Archive material can support a claim but cannot become the current rule by implication.
- `superpowers/` may describe how work was done, but it cannot define the active product, architecture, governance, delivery, or operations baseline.

## Structure rules

- Create new canonical content inside the numbered tree.
- Keep cross-cutting rules in the control spine instead of repeating them across area folders.
- Use folder landing pages for area-level orientation and keep detailed tree navigation in [INDEX.md](INDEX.md).
- Store durable implementation decisions in `docs/adr/`.
- Store external standards, vendor references, and framework citations in `08_references/`.
- Use named `_TEMPLATE.md` files in canonical areas for reusable bootstrap starters.

## Required metadata

Maintained Markdown documents should start with:

```text
# Title

Status: Active | Working history | Archive/evidence | Deprecated
Owner: [role or team]
Purpose: [one sentence describing the scope]
Last updated: YYYY-MM-DD
```

Active documents must not retain starter placeholders such as `[Role or team ...]`, `[TBD: ...]`, or `YYYY-MM-DD` in required metadata fields.
Starter templates may keep placeholder metadata when the file is explicitly labeled as a template.

Add `Approval state` or `Review cadence` when the document governs controls or delivery commitments.

## Update checklist

1. Update the canonical owner first.
2. Update `README.md`, `Architecture.md`, `00-source-of-truth.md`, and `INDEX.md` when the structure or ownership map changes.
3. Update `docs/adr/` when a durable implementation decision changes.
4. Keep archive and working-history readmes aligned when their handling rules change.
5. Run link validation when links change.

## External basis

Reference standards, governance frameworks, and style guides from [08_references/INDEX.md](08_references/INDEX.md).
