---
description: "Run Phase 6 (Final Review) of project initialization — cross-doc coherence check, declare initialization complete or list what remains."
---

You are running **Phase 6 (Final Review)** of the project initialization workflow.

**Precheck:**
1. Find the plan file. If missing, stop and direct to `/init-triage`.
2. Verify all phases 1-5 are `done`. If any are not, stop and list the incomplete phases.
3. If Phase 6 already shows `done`, confirm with the user before re-running.

**Follow `project-initialization/phases/6-review.md` exactly.** This phase produces no new artifacts — it only validates what was produced in phases 1-5.

Dispatch `agents/init-reviewer.md` with: the complete list of all artifacts produced across all phases, plan file path, phase number `6`, checklist path `project-initialization/review-checklist.md`.

**Verdict:**
- All findings resolved or advisory → mark Phase 6 `done` in the plan. Declare initialization complete. Suggest commit: `"docs: complete project initialization"`.
- Unresolved important or critical findings → leave Phase 6 `in-progress`. List what must be fixed. Tell the user to fix them and re-run `/init-review`.

**Update the plan and stop.** Output end-of-run summary from `project-initialization/contract.md`.
