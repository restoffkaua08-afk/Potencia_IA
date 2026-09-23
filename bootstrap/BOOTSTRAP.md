# Potencia IA — Bootstrap Specification

## Purpose

This is the operational specification for turning a fresh Potencia IA checkout or ZIP into a usable Claude Code environment.

The bootstrap is idempotent: detect first, install only what is missing, configure only what is necessary, verify after every change, and record state.

## Automatic execution trigger

Quando o usuário fornece o repositório/pasta do Potencia IA e usa **execute**, **executar**, **ativar**, **bootstrap** ou equivalente, isso inicia automaticamente este documento como uma missão operacional.

**Não é necessário um segundo prompt para autorizar o bootstrap.**

O agente deve continuar pelas fases 0–8 sem voltar ao usuário para perguntar qual é a missão. O projeto do usuário só entra em execução depois do Final Gate.

Se o ambiente permitir executar uma ação automaticamente, execute-a. Não substitua execução por explicação.

## Golden rule

Do not confuse:

- READ = Claude inspected the component documentation.
- INSTALLED = files/package/plugin exist.
- CONFIGURED = settings/hooks/integration are wired.
- ACTIVE = Claude Code can invoke/use it.
- VERIFIED = a concrete health check passed.

The final activation message is allowed only after the required state is verified.

## Phase 0 — Discover the environment

Run the local preflight helper when supported:

- Windows PowerShell: bootstrap/preflight.ps1
- macOS/Linux: bootstrap/preflight.sh

Then independently verify the output when needed.

Collect OS, architecture, shell, Claude Code version, Git, Python, Node/npm, uv, pipx, Codex CLI, Docker when needed, and available package managers.

Do not ask the user for information that can be detected.

## Phase 1 — Read Potencia itself

Read in order:

1. CLAUDE.md
2. prompts/01-iniciar-projeto.md
3. prompts/02-continuar-projeto.md
4. prompts/03-missao-autonoma.md
5. MANIFEST.json
6. this file
7. bootstrap/COMPONENT-MATRIX.md
8. all applicable component contracts.

Read enough of external project documentation to understand the current installation and verification procedure before executing it.

## Phase 2 — Install core projects

### Superpowers

Official Claude Code installation:

/plugin install superpowers@claude-plugins-official

Verify that Superpowers commands/skills are visible after restart or reload.

Source: https://github.com/obra/superpowers

### Graphify

Prerequisite: Python 3.10+ and uv or pipx.

Recommended:

uv tool install graphifyy

Then:

graphify install

For strict Claude Code project behavior, when appropriate:

graphify install --project --strict

Verify with graphify --help and a small graph/query smoke test when a target project exists.

Source: https://github.com/Graphify-Labs/graphify

### RTK — Rust Token Killer

Do not install the unrelated Rust Type Kit named rtk.

Windows:

winget install rtk-ai.rtk

Linux/macOS: use the official RTK installer or Homebrew as documented by the project.

Verify:

rtk --version
rtk gain

Then initialize the Claude Code integration according to current official instructions. Prefer non-interactive/auto-patch mode only when global configuration is authorized.

Source: https://github.com/rtk-ai/rtk

### VV Claude Harness

Native Claude Code plugin:

/plugin marketplace add oeftimie/vv-claude-harness
/plugin install vv-harness

Verify plugin discovery and use /harness-doctor when available.

Source: https://github.com/oeftimie/vv-claude-harness

### Security Hooks

Preferred native plugin path:

/plugin marketplace add atompilot/claude-code-security-hooks
/plugin install security-hooks@atompilot-security-hooks

Restart/reload Claude Code and verify hooks are registered.

Do not disable security hooks just to make another component work.

Source: https://github.com/atompilot/claude-code-security-hooks

### Superharness

Install with:

pipx install superharness

Verify:

shux --help
shux status

Do not enable dangerous autonomous modes merely because they exist. Respect project approval and sandbox controls.

Source: https://github.com/artificemachine/superharness

### Codex Subagents

Secondary delegation layer. Requires Python 3, uv, Codex CLI, and Claude Code CLI.

Use the official repository install.sh after inspecting it.

Source: https://github.com/mgoulart/codex-subagents

Verify MCP registration and command availability.

## Phase 3 — Plugins

### OmniRoute

The selected implementation is pinned in plugins/omni-route.md.

Do not silently substitute a similarly named fork.

Because OmniRoute can alter model endpoints and provider routing, treat provider credentials and routing policy as a separate configuration step.

Verify health before wiring Claude Code to it.

Never put API keys in Potencia files or Git.

### Headroom

The selected implementation is pinned in plugins/headroom.md.

Headroom is a context-management layer. Measure it before and after enabling it.

Do not assume it improves every workload. If it increases context/tool overhead or harms reliability, keep it installed but do not force it into the active path.

### Task Observer

Install the selected Task Observer skill into the supported Claude Code skills location.

Activation must be structural, not merely assumed from a skill description.

Its experimental changes belong only in task-observer-workspace/.

It must never autonomously rewrite Potencia production contracts.

## Phase 4 — Design skills

For frontend work, Potencia includes contracts for Emil, Impeccable, and Taste.

The bootstrap must make actual skill implementations available when the source/install method is defined in their contract.

Do not claim that a local SKILL.md contract is the complete upstream implementation.

When the selected skill is external, read its current upstream license and installation instructions before installing.

## Phase 5 — Persistent state

Create:

.potencia/runtime-state.json

Minimum schema:

{
  "potencia_version": "0.2.0",
  "status": "BOOTSTRAPPING",
  "environment": {},
  "components": {},
  "checks": [],
  "blockers": [],
  "updated_at": ""
}

Never store API keys, OAuth tokens, passwords, cookies, private keys, or secrets.

## Phase 6 — Verification

Every component needs installation evidence, configuration evidence, activation evidence, a health check, and a practical smoke test when possible.

Installed but not active is not ACTIVE.

Active without a successful health check is not VERIFIED.

## Phase 7 — Integration test

Before success, run a small controlled task that exercises the infrastructure without modifying the user's real project unnecessarily.

Where applicable demonstrate:
- a Potencia skill loads;
- an external agent/project is available;
- Graphify can inspect code;
- RTK can process a supported command;
- the harness can report status;
- security hooks are active;
- Codex delegation works when configured;
- context optimization does not corrupt tool results;
- Task Observer can create/read workspace state.

## Phase 8 — Final gate

Antes do Final Gate, faça uma checagem anti-falso-positivo:

- o repositório foi apenas lido? Então NÃO está ativado;
- as skills foram apenas carregadas? Então NÃO está ativado;
- um componente foi instalado mas não testado? Então NÃO está VERIFIED;
- um plugin foi instalado mas não está disponível? Então NÃO está ACTIVE;
- os agentes foram apenas mencionados? Então NÃO estão ativos;
- o runtime-state não foi escrito? Então NÃO há conclusão do bootstrap.

O agente não deve encerrar o bootstrap para perguntar pela missão do usuário. O único encerramento normal após `execute` é o sucesso do Final Gate ou um bloqueio real que exija ação humana.


Bootstrap succeeds only when all required components are VERIFIED, optional components are explicitly VERIFIED/NOT_APPLICABLE/BLOCKED with a reason, no essential human action is pending, runtime state is written, and Claude Code can continue into user work without another setup phase.

Then, and only then, output exactly:

Claude code com Potencia Ativado!

No additional text.
