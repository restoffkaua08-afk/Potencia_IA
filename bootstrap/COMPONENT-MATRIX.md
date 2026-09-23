# Potencia IA — Component Matrix

| Component | Source | Install/activation | Health check | Required |
|---|---|---|---|---|
| Superpowers | obra/superpowers | Claude Code official marketplace | commands/skills visible | YES |
| Graphify | Graphify-Labs/graphify | uv tool install graphifyy + graphify install | help + graph smoke test | YES |
| RTK | rtk-ai/rtk | OS package/install + rtk init | rtk --version + rtk gain | YES |
| VV Harness | oefimie/vv-claude-harness | native Claude plugin | harness doctor / plugin discovery | YES |
| Security Hooks | atompilot/claude-code-security-hooks | native Claude plugin | hook registration + controlled test | YES |
| Superharness | artificemachine/superharness | pipx install superharness | shux status | YES |
| Codex Subagents | mgoulart/codex-subagents | official install.sh after inspection | MCP + command discovery | CONDITIONAL |
| OmniRoute | see plugin contract | selected implementation + provider configuration | local health/API check | CONDITIONAL |
| Headroom | see plugin contract | selected implementation | context/tool integrity benchmark | CONDITIONAL |
| Task Observer | see plugin contract | Claude skill + structural trigger | observation workspace activity | YES |
| Emil | emilkowalski/skills | current upstream skill install | skill discovery | CONDITIONAL |
| Impeccable | pbakaus/impeccable | current upstream skill install | skill discovery | CONDITIONAL |
| Taste | selected source in skill contract | current upstream skill install | skill discovery | CONDITIONAL |

## Required vs conditional

YES means the bootstrap must attempt installation/activation.

CONDITIONAL means the bootstrap must inspect whether the component applies to the current environment/workflow. It must not be silently ignored.

Examples:
- Codex Subagents is conditional if Codex CLI is unavailable.
- frontend design skills are conditional for non-frontend projects.
- OmniRoute/Headroom are conditional if the user is not using their routing/context path.

Conditional does not mean skip reading. The agent must understand the component before deciding.

## Evidence levels

READ
INSTALLED
CONFIGURED
ACTIVE
VERIFIED
BLOCKED
NOT_APPLICABLE

Never collapse these states.
