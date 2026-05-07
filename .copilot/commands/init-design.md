---
description: "Run Phase 3 (Design) of project initialization — produce solution design, ADRs, and optional C4 views."
---

You are running **Phase 3 (Design)** of the project initialization workflow.

**Precheck:**
1. Find the plan file. If missing, stop and direct to `/init-triage`.
2. Verify Phase 2 (Specification) is `done`. If not, stop.
3. If Phase 3 already shows `done`, confirm with the user before re-running.

**Follow `project-initialization/phases/3-design.md` exactly.** This phase invokes `superpowers:brainstorming` before writing the solution design and creates ADRs on demand as decisions arise.

**End-of-phase review:** dispatch `agents/init-reviewer.md` with all files produced this phase (solution design, ADRs, C4 files if any, updated ADR INDEX), plan file path, phase number `3`, checklist path `project-initialization/review-checklist.md`.

**Update the plan in one batch and stop.** Output end-of-run summary from `project-initialization/contract.md`.
