---
description: "Run Phase 0 (Triage) of project initialization — ask routing questions, select profile, build artifact roadmap, write plan file."
---

You are running **Phase 0 (Triage)** of the project initialization workflow for this repository.

**Before doing anything else:** check whether `docs/superpowers/plans/*-project-initialization.md` already exists. If it does, stop: "An initialization plan already exists. Run the next phase command, or delete the plan file and re-run `/init-triage` to start over."

**Follow `project-initialization/phases/0-triage.md` exactly.** That file defines the routing questions, profile selection matrix, fact extraction rules, mode assignment logic, and plan-file initialization instructions.

**After triage is complete:** write the plan file to `docs/superpowers/plans/YYYY-MM-DD-project-initialization.md` using today's date. Use `project-initialization/plan-template.md` as the scaffold.

**Stop after writing the plan file.** Output the end-of-run summary from `project-initialization/contract.md`. Do not begin Phase 1.

See also `project-initialization/review-checklist.md` for Phase 6 final review criteria. Later phases will dispatch `agents/init-reviewer.md` to validate work.
