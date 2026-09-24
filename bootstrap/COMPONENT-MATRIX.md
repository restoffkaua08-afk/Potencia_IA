# Potencia IA — Component Matrix

| Component | Source | Install/activation | Health check | Required |
|---|---|---|---|---|
| Superpowers | obra/superpowers | native plugin for Claude Code/Codex | skills and session hook visible | YES |
| Graphify | Graphify-Labs/graphify | uv tool install graphifyy + graphify install | help + graph smoke test | YES |
| RTK | rtk-ai/rtk | official OS install + global auto-patch | rtk --version + rtk gain + hook check | YES |
| VV Harness | oefimie/vv-claude-harness | native Claude plugin | plugin discovery + harness doctor | YES |
| Security Hooks | atompilot/claude-code-security-hooks | native Claude plugin | hook registration + controlled test | YES |
| Superharness | artificemachine/superharness | pipx install + onboarding/guardian | shux status | YES |
| Codex Subagents | mgoulart/codex-subagents | official install + MCP registration | command and MCP discovery | YES |
| OmniRoute | crl33/omniroute | global install + persistent local auto gateway | health + automatic route smoke test | YES |
| Headroom | headroomlabs-ai/headroom | persistent service + MCP wiring for detected agents | health + response-integrity smoke test | YES |
| Task Observer | rebelytics/one-skill-to-rule-them-all | skill install + structural trigger | isolated observation workspace | YES |
| Emil | emilkowalski/skills | upstream skill install | skill discovery | YES |
| Impeccable | pbakaus/impeccable | upstream skill install | skill discovery | YES |
| Taste | source declared by skill contract | upstream skill install | skill discovery | YES |

## Activation rule

All listed components are installed, configured, activated and verified during Potencia bootstrap. The user does not need to call or configure components individually.

“Required” means the bootstrap must perform the work and record evidence. If the host lacks a capability, the result is BLOCKED with the exact reason and attempted alternative; it is never silently treated as optional.

Task relevance controls which component behavior is applied to a task. It does not disable the component, remove it from the session, or defer activation until the user asks for it.

## Evidence levels

READ → INSTALLED → CONFIGURED → ACTIVE → VERIFIED

Never collapse these states and never claim activation from documentation alone.
