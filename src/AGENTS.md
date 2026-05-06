---
name: Source Coding Practices
description: Use for work under src/. Covers code quality, implementation style, and change discipline.
applyTo: "src/**"
---

# Source Coding Practices

Apply these rules when editing files under `src/`.

## Most Important Rules

- Prefer simple, explicit code over clever abstractions.
- Keep changes tightly scoped to the requested behavior.
- Fix root causes instead of layering symptom patches.
- Preserve important context in code comments and naming, but keep both concise.

## Implementation Rules

- Match existing project patterns, naming, and structure.
- Keep interfaces clear and stable unless the task explicitly changes the contract.
- Avoid unnecessary dependencies, configuration, or framework complexity.
- Do not mix unrelated responsibilities into one file or module.

## Quality Rules

- Write code that is easy to read, review, and verify.
- Prefer maintainability over micro-optimizations.
- Add or update tests with behavior changes unless explicitly told not to.
- Call out edge cases, compatibility risks, and verification gaps in the final response.
