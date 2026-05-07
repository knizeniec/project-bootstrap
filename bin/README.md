# bin

Purpose: Entry-point scripts or binaries after implementation starts.

This directory is a slot. The [`prompts/language-adaptation.md`](../prompts/language-adaptation.md) adoption prompt may rename, populate, or remove it depending on the chosen stack — many languages use a different convention (Go uses `cmd/`, Rust uses `src/bin/`, Python typically has no top-level `bin/`).

Template default:
- Keep this folder as documentation-only until runtime artifacts are explicitly requested.
- Prefer thin wrappers that delegate real logic to `src/`.
- Remove this folder if your chosen stack does not need it.
