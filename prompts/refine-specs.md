---
name: "Refine Active Project Documents"
description: "Use after bootstrap to close blocking gaps in the active project brief and PRD before architecture work."
argument-hint: "No required arguments. Reads the active project brief and PRD and asks only targeted clarification questions."
agent: "agent"
---

Read the active project brief and PRD.

Classify unresolved items into:

- blocking gaps for architecture
- non-blocking TBDs

Ask only targeted questions for blocking gaps.
Update the active documents in place.
Produce an `Architecture readiness` summary with:

- ready now
- ready with assumptions
- not ready
