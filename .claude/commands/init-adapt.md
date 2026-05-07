---
description: "Run Phase 5 (Adapt) of project initialization — language adaptation and repository sync."
---

You are running **Phase 5 (Adapt)** of the project initialization workflow.

**Precheck:**
1. Find the plan file. If missing, stop and direct to `/init-triage`.
2. Verify Phase 4 (Govern & Operate) is `done`. If not, stop.
3. If Phase 5 already shows `done`, confirm with the user before re-running.

**Follow `project-initialization/phases/5-adapt.md` exactly.** Read all accepted ADRs before beginning. Do not add feature code, stubs, or version pins beyond what ADRs explicitly require.

**End-of-phase review:** dispatch `agents/init-reviewer.md` with all adapted files, plan file path, phase number `5`, checklist path `project-initialization/review-checklist.md`.

**Update the plan in one batch and stop.** Output end-of-run summary from `project-initialization/contract.md`.
