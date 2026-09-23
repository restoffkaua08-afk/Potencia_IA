# Potencia IA

## Infraestrutura obrigatória

Esta pasta é uma infraestrutura reutilizável para agentes de desenvolvimento, especialmente Claude Code e agentes compatíveis.

**Leia este arquivo primeiro.** Depois leia, nesta ordem:
1. `prompts/01-iniciar-projeto.md`
2. `prompts/02-continuar-projeto.md`
3. `prompts/03-missao-autonoma.md`
4. `MANIFEST.json`
5. as skills, projetos/agentes e plugins necessários.

Esta infraestrutura não é documentação opcional. Quando um projeto usar Potencia IA, o agente deve seguir o ciclo e as regras definidos aqui e nos três prompts.

## Princípio fundamental

**Skills não substituem agentes.**

- Skills definem metodologia, gates, documentos, critérios e validação.
- Projetos/agentes executam pesquisa, implementação, testes, revisão, paralelismo e especializações.
- Plugins fornecem infraestrutura auxiliar.

Quando houver um projeto/agente configurado e adequado para a tarefa, ele deve ser ativado e utilizado. Não substituir automaticamente uma arquitetura multiagente por execução monolítica.

## Ciclo obrigatório

Para trabalho não trivial:

ENTENDER → DESCOBRIR → ESPECIFICAR → ARQUITETAR → PLANEJAR → DELEGAR → EXECUTAR → OBSERVAR → TESTAR → VERIFICAR → REVISAR → CORRIGIR → VERIFICAR NOVAMENTE → VALIDAR → LIMPAR → SELAR

## Gates

### Discovery
Entender problema, usuários, objetivo, escopo, entradas/saídas, restrições, requisitos obrigatórios, preferências, proibições, casos-limite, integrações, segurança, performance e definição de sucesso.

### Specification / Architecture
Documentar o que for necessário. Cada documento relevante deve ser classificado como REQUIRED, NOT REQUIRED ou NOT APPLICABLE. Se faltar decisão essencial, parar e perguntar; não inventar requisito importante.

### Planning
Transformar a especificação aprovada em fases, tarefas, dependências, paralelismo, responsáveis, arquivos, critérios de aceitação, testes, checkpoints e riscos.

### Verification
Usar:
DEFINE → BREAK → VERIFY → VERDICT

Verdictos: PROVEN, FAILED, NOT PROVEN, BLOCKED.

Não aceitar como prova apenas build verde, HTTP 200, exit code 0 ou a afirmação do agente.

### Adversarial review
Após implementação, usar revisão independente quando possível. Procurar bugs, requisitos esquecidos, arquitetura, segurança, dependências, performance, manutenção, acessibilidade e divergências entre docs e código. Corrigir e verificar novamente.

## Agentes/projetos configurados

1. Superpowers
2. Graphify
3. RTK
4. VV Claude Harness
5. Security Hooks
6. Superharness
7. Codex Subagents

## Plugins configurados

- OmniRoute
- Headroom
- Task Observer

## Skills configuradas

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

## Task Observer

`skills/` é produção e deve ser protegida.

`task-observer-workspace/` é laboratório experimental. O observer pode experimentar ali, mas não pode alterar autonomamente `CLAUDE.md`, `prompts/`, `plugins/` ou `projetos/`.

## Autonomia

Trabalhar continuamente quando houver informação suficiente. Delegar, testar, revisar, corrigir e repetir até atingir os critérios.

Perguntar somente quando faltar uma decisão essencial, houver ambiguidade material, ou uma ação irreversível/alto risco exigir confirmação.

Autonomia não permite inventar requisitos.

## Regra da verdade

Nunca simular instalação, ativação, execução, teste, revisão ou aprovação. Se algo não foi executado, declarar que não foi.

## Limpeza e selo

`09-project-cleanup` só depois da validação do usuário.

`10-project-seal` depois da limpeza e validação final.

## Regra de conclusão

"Terminado" significa que os critérios de aceitação foram atendidos, os resultados foram verificados, os problemas encontrados foram tratados e o estado final é conhecido.
