---
description: "Run Phase 1 (Intent) of project initialization — produce project brief and optional business case."
---

You are running **Phase 1 (Intent)** of the project initialization workflow.

**Precheck:**
1. Find `docs/superpowers/plans/*-project-initialization.md`. If missing, stop: "No initialization plan found. Run `/init-triage` first."
2. Verify Phase 0 (Triage) shows `done` in the Phase Roadmap. If not, stop.
3. If Phase 1 already shows `done`, confirm with the user before re-running.

**Follow `project-initialization/phases/1-intent.md` exactly.** Load artifact rubrics from `project-initialization/artifacts/` for each active artifact. Follow the mode (interview / confirm / extract) recorded in the Artifact Roadmap.

**Follow all cross-phase fact capture rules from `project-initialization/contract.md`.** Any statement about architecture, stack, requirements, or governance belongs in `Future-Phase Facts`, not in the current artifact.

**End-of-phase review:** dispatch the `init-reviewer` agent with: file paths produced this phase, plan file path, phase number `1`, checklist path `project-initialization/review-checklist.md`. Apply all critical and important findings before updating the plan.

**Update the plan in one batch:** Phase Roadmap (Phase 1 → done), Artifact Roadmap statuses, Project Facts, Future-Phase Facts, Files Updated This Run, Review Findings, Next Recommended Step, Resume Context.

**Stop.** Output the end-of-run summary from `project-initialization/contract.md`.
