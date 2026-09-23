<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:071A2B,45:004B76,100:00A7E1&text=POTENCIA%20IA&fontColor=FFFFFF&fontSize=48&fontAlignY=38&animation=fadeIn&desc=INFRAESTRUTURA%20MULTIAGENTE%20PARA%20CLAUDE%20CODE&descAlignY=59&descSize=15" alt="Potencia IA"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=2800&pause=900&color=00A7E1&center=true&vCenter=true&width=900&lines=Bootstrap+autom%C3%A1tico;Multiagentes+e+especialistas;Planejamento+%E2%80%A2+Execu%C3%A7%C3%A3o+%E2%80%A2+Verifica%C3%A7%C3%A3o;Revis%C3%A3o+adversarial+e+corre%C3%A7%C3%A3o;Contexto%2C+tokens+e+harnesses" alt="Potencia IA"/>

<br>

### Infraestrutura operacional reutilizável para desenvolvimento estruturado, multiagente e verificável com Claude Code.

<br>

![Status](https://img.shields.io/badge/STATUS-SELF%20BOOTSTRAPPING-00A7E1?style=for-the-badge&labelColor=071A2B)
![Architecture](https://img.shields.io/badge/ARQUITETURA-MULTIAGENTE-19B394?style=for-the-badge&labelColor=071A2B)
![Runtime](https://img.shields.io/badge/RUNTIME-CLAUDE%20CODE-7C3AED?style=for-the-badge&labelColor=071A2B)
![Version](https://img.shields.io/badge/VERS%C3%83O-0.2.0-F7941D?style=for-the-badge&labelColor=071A2B)

<br>

[![REPOSITÓRIO](https://img.shields.io/badge/REPOSIT%C3%93RIO-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/restoffkaua08-afk/Potencia_IA)

</div>

<br>

# `> PROJECT.OVERVIEW`

## Uma camada operacional para desenvolvimento com agentes

O **Potencia IA** é uma infraestrutura self-bootstrapping para **Claude Code**.

A proposta é entregar ao agente uma estrutura que ele possa estudar, instalar, ativar, verificar e utilizar como padrão durante o desenvolvimento de projetos.

O fluxo começa com uma pasta/ZIP ou com o link deste repositório. O Claude Code lê o contrato do Potencia, detecta o ambiente, processa o bootstrap, instala e configura os componentes aplicáveis, verifica cada etapa e registra o estado operacional.

Somente depois de concluir o bootstrap, o Potencia considera o ambiente pronto.

> **Objetivo central:** reduzir execução monolítica, aumentar a cobertura de especialistas, tornar revisão e verificação obrigatórias e permitir missões longas com estado, delegação e evidência.

<br>

# `> HOW.IT.WORKS`

\`\`\`text
USUÁRIO
   │
   │  "Execute / Ative o Potencia"
   ▼
CLAUDE CODE
   │
   ├── lê CLAUDE.md
   ├── lê prompts + manifest
   ├── detecta ambiente
   ├── estuda contratos
   ▼
BOOTSTRAP
   │
   ├── instala
   ├── configura
   ├── ativa
   ├── verifica
   └── registra evidências
   ▼
POTENCIA ATIVO
   │
   ├── Superpowers
   ├── agentes especialistas
   ├── harness/orquestração
   ├── Graphify
   ├── RTK / Headroom
   ├── Security Hooks
   └── skills de engenharia
   ▼
PROJETO DO USUÁRIO
   ▼
PLAN → ASSIGN → EXECUTE → OBSERVE
   ▼
TEST → INDEPENDENT REVIEW → VERIFY
   ├── PROVEN → ACCEPT
   └── FAILED → CORRECT → VERIFY AGAIN
\`\`\`

<br>

# `> AGENT.POLICY`

## Multiagentes como regra operacional

Para cada unidade classificada como **DEVELOPMENT**:

- **mínimo de 2 agentes auxiliares ativos**;
- **1 Executor/Especialista**;
- **1 Reviewer/Verifier independente**;
- Superpowers ativo quando aplicável;
- especialistas adicionais conforme a superfície da tarefa;
- revisão independente antes de aceitar o resultado.

Exemplo:

\`\`\`text
SUPERVISOR
    │
    ├── EXECUTOR / ESPECIALISTA
    ├── SECURITY SPECIALIST
    ├── QA / TESTING
    └── REVIEWER / VERIFIER
\`\`\`

Agente apenas mencionado no plano não conta como agente ativo.

Consulte [bootstrap/AGENT-POLICY.md](./bootstrap/AGENT-POLICY.md) para a política completa.

<br>

# `> CORE.COMPONENTS`

## Projetos e agentes

| Componente | Papel |
|---|---|
| **Superpowers** | Metodologia estruturada de desenvolvimento |
| **Graphify** | Conhecimento e análise estrutural do código |
| **RTK** | Redução de saída redundante e economia de contexto |
| **VV Claude Harness** | Harness e continuidade |
| **Security Hooks** | Proteção de operações |
| **Superharness** | Coordenação e execução |
| **Codex Subagents** | Delegação complementar |

## Infraestrutura e plugins

| Componente | Papel |
|---|---|
| **OmniRoute** | Roteamento de modelos/provedores |
| **Headroom** | Engenharia de contexto |
| **Task Observer** | Observação e evolução controlada |

## Skills

1. Problem Discovery
2. Specification + Architecture Gate
3. Execution Planner
4. Verification
5. Adversarial Engineering Review
6. Emil / Design Engineering
7. Impeccable
8. Taste
9. Project Cleanup
10. Project Seal

<br>

# `> ENGINEERING.LOOP`

## Ciclo do Potencia

\`\`\`text
ENTENDER → DESCOBRIR → ESPECIFICAR → ARQUITETAR
                    ↓
PLANEJAR → DELEGAR → EXECUTAR → OBSERVAR
                    ↓
TESTAR → VERIFICAR → REVISAR → CORRIGIR
                    ↓
VERIFICAR NOVAMENTE → VALIDAR → LIMPAR → SELAR
\`\`\`

### Loop por unidade

\`\`\`text
PLAN → ASSIGN → EXECUTE → OBSERVE
     → TEST → INDEPENDENT REVIEW → VERIFY
     → ACCEPT / FIX / BLOCK
\`\`\`

### Verificação

\`\`\`text
DEFINE → BREAK → VERIFY → VERDICT
\`\`\`

Veredictos:

- `PROVEN`
- `FAILED`
- `NOT PROVEN`
- `BLOCKED`

> Build verde, HTTP 200, exit code 0 ou a afirmação de um agente não são, sozinhos, prova de conclusão.

<br>

# `> GETTING.STARTED`

## Pré-requisitos

O bootstrap detecta automaticamente:

- Claude Code;
- Git;
- Python;
- Node.js/npm;
- uv;
- pipx;
- Codex CLI quando aplicável;
- Docker quando aplicável;
- gerenciador de pacotes do sistema.

## Clonar

\`\`\`bash
git clone https://github.com/restoffkaua08-afk/Potencia_IA.git
cd Potencia_IA
\`\`\`

## Diagnóstico

### Windows / PowerShell

\`\`\`powershell
powershell -ExecutionPolicy Bypass -File .\bootstrap\preflight.ps1
\`\`\`

### macOS / Linux

\`\`\`bash
bash ./bootstrap/preflight.sh
\`\`\`

> O preflight é diagnóstico. A instalação e ativação seguem `bootstrap/BOOTSTRAP.md`.

<br>

# `> INSTALL.COMMANDS`

## Comandos padrão

### Superpowers

\`\`\`text
/plugin install superpowers@claude-plugins-official
\`\`\`

### Graphify

\`\`\`bash
uv tool install graphifyy
graphify install
\`\`\`

### RTK — Windows

\`\`\`powershell
winget install rtk-ai.rtk
rtk --version
rtk gain
\`\`\`

### VV Claude Harness

\`\`\`text
/plugin marketplace add oeftimie/vv-claude-harness
/plugin install vv-harness
\`\`\`

### Security Hooks

\`\`\`text
/plugin marketplace add atompilot/claude-code-security-hooks
/plugin install security-hooks@atompilot-security-hooks
\`\`\`

### Superharness

\`\`\`bash
pipx install superharness
shux --help
shux status
\`\`\`

### Task Observer

\`\`\`bash
npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer
\`\`\`

### Headroom

\`\`\`bash
uv tool install --python 3.13 "headroom-ai[all]"
headroom --version
headroom doctor
headroom mcp install
\`\`\`

### OmniRoute

\`\`\`bash
npm install -g omniroute
omniroute
\`\`\`

### Codex Subagents

O projeto exige Python, uv, Codex CLI e Claude Code CLI. O bootstrap usa o instalador oficial após inspeção do procedimento do repositório.

> O Potencia não inventa instaladores e não grava credenciais.

<br>

# `> ACTIVATE.WITH.CLAUDE`

## Prompt pronto para Claude Code

\`\`\`text
Quero ativar o Potencia IA neste ambiente.

Repositório:
https://github.com/restoffkaua08-afk/Potencia_IA.git

Faça o bootstrap completo antes de tocar no meu projeto.

1. Obtenha o repositório se ele ainda não estiver no workspace.
2. Leia CLAUDE.md primeiro.
3. Leia os três prompts, MANIFEST.json, bootstrap/BOOTSTRAP.md e bootstrap/AGENT-POLICY.md.
4. Estude todos os contratos de projetos, plugins e skills.
5. Detecte o ambiente e os pré-requisitos.
6. Instale, configure, ative e verifique os componentes aplicáveis.
7. Superpowers é obrigatório para desenvolvimento não trivial.
8. Para cada unidade DEVELOPMENT, use no mínimo 2 agentes auxiliares ativos:
   - Executor/Especialista;
   - Reviewer/Verifier independente.
9. Adicione especialistas conforme a tarefa exigir.
10. Não conte skills, plugins ou agentes apenas planejados como agentes ativos.
11. Não aceite "done" como prova de conclusão.
12. Registre evidências e estado em .potencia/runtime-state.json.
13. Nunca grave credenciais, tokens ou API keys no repositório.
14. Se houver falha, diagnostique e tente alternativas oficiais antes de marcar BLOCKED.
15. Não implemente meu projeto durante o bootstrap.

Quando o bootstrap estiver realmente concluído e verificado, responda exatamente:

Claude code com Potencia Ativado!

Depois disso, aguarde minha tarefa e use o Potencia como infraestrutura padrão.
\`\`\`

<br>

# `> ACTIVATE.WITH.CODEX`

## Prompt pronto para Codex

\`\`\`text
Quero preparar este ambiente usando o Potencia IA como infraestrutura de desenvolvimento multiagente.

Repositório do Potencia:
https://github.com/restoffkaua08-afk/Potencia_IA.git

Faça primeiro a preparação da infraestrutura:

1. Obtenha o repositório.
2. Leia CLAUDE.md, MANIFEST.json, os três prompts, bootstrap/BOOTSTRAP.md e bootstrap/AGENT-POLICY.md.
3. Estude os contratos de projetos, plugins e skills.
4. Detecte o ambiente e os pré-requisitos.
5. Configure o que for compatível com este ambiente.
6. Use no mínimo 2 agentes auxiliares por unidade DEVELOPMENT quando houver suporte à delegação:
   - Executor/Especialista;
   - Reviewer/Verifier independente.
7. Adicione especialistas conforme a tarefa exigir.
8. Planeje, execute, teste, revise, corrija e verifique novamente.
9. Não considere "done" como evidência suficiente.
10. Registre limitações e evidências.
11. Não exponha nem grave credenciais no repositório.

Depois de preparar a infraestrutura, trabalhe no projeto abaixo usando o Potencia como padrão:

REPOSITÓRIO DO PROJETO:
[COLE AQUI O LINK DO REPOSITÓRIO]

TAREFA:
[DESCREVA A TAREFA AQUI]

CRITÉRIOS DE ACEITAÇÃO:
[DESCREVA COMO O RESULTADO DEVE SER VALIDADO]
\`\`\`

<br>

# `> PROJECT.INPUT`

## Depois da ativação

Quando o Claude retornar:

\`\`\`text
Claude code com Potencia Ativado!
\`\`\`

o usuário pode enviar somente a tarefa:

\`\`\`text
Faça o projeto descrito abaixo usando o Potencia IA.

[DESCRIÇÃO]

REQUISITOS:
[REQUISITOS]

CRITÉRIOS DE ACEITAÇÃO:
[CRITÉRIOS]

Não pare até implementar, testar, revisar e verificar o resultado.
\`\`\`

Ou fornecer um repositório:

\`\`\`text
Projeto:
https://github.com/USUARIO/REPOSITORIO.git

Execute o projeto usando o Potencia IA.
\`\`\`

<br>

# `> PROJECT.STRUCTURE`

\`\`\`text
Potencia_IA/
├── CLAUDE.md
├── MANIFEST.json
├── prompts/
├── projetos/
├── plugins/
├── skills/
├── bootstrap/
│   ├── BOOTSTRAP.md
│   ├── AGENT-POLICY.md
│   ├── COMPONENT-MATRIX.md
│   ├── README.md
│   ├── preflight.ps1
│   └── preflight.sh
├── task-observer-workspace/
└── docs/
\`\`\`

<br>

# `> OPERATIONAL.STATE`

Estado operacional:

\`\`\`text
.potencia/runtime-state.json
\`\`\`

Registra ambiente, componentes, verificações, bloqueios, evidências e conformidade da política de agentes.

**Segredos nunca entram nesse arquivo.**

<br>

# `> SECURITY`

- credenciais ficam fora do Git;
- API keys não são armazenadas no Potencia;
- Security Hooks são tratados como camada de proteção;
- ações de alto risco respeitam os controles do ambiente;
- fontes de instalação são definidas pelos contratos;
- mudanças irreversíveis respeitam os limites de autorização.

<br>

# `> DOCUMENTATION`

- [USAGE.md](./docs/USAGE.md) — utilização;
- [INSTALLATION-PRINCIPLES.md](./docs/INSTALLATION-PRINCIPLES.md) — princípios de instalação;
- [OPERATION-MATRIX.md](./docs/OPERATION-MATRIX.md) — operação e validação;
- [COMPONENT-SOURCES.md](./docs/COMPONENT-SOURCES.md) — fontes;
- [BOOTSTRAP.md](./bootstrap/BOOTSTRAP.md) — bootstrap completo;
- [AGENT-POLICY.md](./bootstrap/AGENT-POLICY.md) — política de agentes;
- [COMPONENT-MATRIX.md](./bootstrap/COMPONENT-MATRIX.md) — matriz operacional.

<br>

# `> PROJECT.STATUS`

**Potencia IA 0.2.0 — infraestrutura self-bootstrapping em evolução.**

O repositório concentra contratos, prompts, skills, políticas, bootstrap, verificações e documentação para preparar um ambiente Claude Code com execução estruturada e multiagente.

Os componentes externos não são apresentados como se estivessem incorporados ao repositório. O Potencia mantém contratos e fontes; a instalação real ocorre no ambiente do usuário e precisa ser verificada.

<br>

# `> ENGINEERING.PRINCIPLES`

> **Planejar antes de executar. Delegar quando possível. Testar antes de aceitar. Revisar antes de concluir. Verificar antes de afirmar.**

<br>

# `> DEVELOPER`

<div align="center">

## Kauã Restoff

### Desenvolvedor de Software

[![GitHub](https://img.shields.io/badge/GitHub-restoffkaua08--afk-181717?style=for-the-badge&logo=github)](https://github.com/restoffkaua08-afk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kau%C3%A3%20Restoff-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/kau%C3%A3-restoff-2821163a0)

<br>

`BUILD • TEST • REVIEW • VERIFY • EVOLVE`

<br>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:00A7E1,50:004B76,100:071A2B&animation=fadeIn" alt="Rodapé"/>

</div>
