#!/usr/bin/env python3
"""
Check that all init-* command files across .claude/, .copilot/, .codex/
contain the required contract phrases. Run from repo root.
"""

from pathlib import Path
import sys

REQUIRED_PHRASES = [
    "project-initialization/phases/",
    "project-initialization/contract.md",
    "project-initialization/review-checklist.md",
    "init-reviewer",
    "Update the plan in one batch",
]

TOOL_DIRS = [".claude", ".copilot", ".codex"]
COMMANDS = [
    "init-triage",
    "init-intent",
    "init-spec",
    "init-design",
    "init-govern",
    "init-adapt",
    "init-review",
]

# init-triage doesn't update the plan so skip that phrase for it
TRIAGE_SKIP = {"Update the plan in one batch"}

errors = []

for tool in TOOL_DIRS:
    for cmd in COMMANDS:
        path = Path(f"{tool}/commands/{cmd}.md")
        if not path.exists():
            errors.append(f"MISSING: {path}")
            continue
        content = path.read_text()
        skip = TRIAGE_SKIP if cmd == "init-triage" else set()
        for phrase in REQUIRED_PHRASES:
            if phrase in skip:
                continue
            if phrase not in content:
                errors.append(f"MISSING PHRASE in {path}: '{phrase}'")

if errors:
    print("Parity check FAILED:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)

print(f"Parity check PASSED: {len(TOOL_DIRS) * len(COMMANDS)} command files checked.")
