# Bootstrap

The bootstrap layer turns Potencia IA from a repository into an operational Claude Code environment.

Start with:
- BOOTSTRAP.md — complete procedure and gates.
- COMPONENT-MATRIX.md — selected components and verification states.
- preflight.ps1 — Windows diagnostic.
- preflight.sh — macOS/Linux diagnostic.

The bootstrap is deliberately diagnostic plus agent-driven rather than a blind remote installer. Claude Code reads the official component instructions, detects the machine, installs what is applicable, verifies it, records evidence, and only then reports activation.

No secrets belong in this directory.
