# Potencia Desktop Protocol

## Objetivo

O Desktop é uma interface observável e controlável do Potencia Runtime. Ele não deve inferir o estado do sistema lendo texto do terminal.

## Transporte atual

- bind: 127.0.0.1
- HTTP API: GET /health, GET /v1/state, POST /v1/commands
- eventos em tempo real: GET /v1/events usando Server-Sent Events (SSE)
- autenticação: Authorization: Bearer <runtime token>
- token: arquivo local fora do repositório
- protocolo: 1
- porta padrão: 43173

O transporte inicial é deliberadamente local. O servidor HTTP da biblioteca padrão do Python não deve ser tratado como endpoint público de produção.

## Handshake / descoberta

1. Desktop consulta /health.
2. Se houver Runtime, lê o token local.
3. Desktop solicita /v1/state.
4. Desktop abre /v1/events.
5. O primeiro evento é um snapshot completo.
6. Eventos incrementais atualizam Office, Graph e indicadores de conexão.

## Estados

declared, present, installed, configured, active, verified, failed e blocked permanecem semanticamente distintos.

## Eventos

runtime_connected, project_detected, agent_created, agent_started, agent_waiting, agent_finished, agent_failed, skill_activated, skill_deactivated, plugin_activated, plugin_deactivated, tool_started, tool_finished, task_created, task_started, task_completed, verification_started, verification_passed, verification_failed, file_modified, finding_created, correction_started, correction_completed e runtime_disconnected.

## Segurança do Desktop

O renderer deve permanecer sem Node integration, com context isolation, sandbox quando compatível e APIs de preload estreitas. IPC deve validar entradas e origem do sender.
