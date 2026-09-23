# Potencia IA — Agent Policy

## Status

**NORMATIVE / REQUIRED**

Este documento define o piso operacional de agentes do Potencia. Ele não é uma recomendação.

## 1. Superpowers

Para desenvolvimento não trivial:
- Superpowers deve estar instalado;
- Superpowers deve estar ativo/disponível;
- o fluxo deve usar suas capacidades/metodologia aplicáveis;
- a ativação deve ter evidência.

Sem isso, a tarefa não pode ser apresentada como plenamente conforme ao Potencia.

## 2. Piso mínimo

Para cada unidade classificada como **DEVELOPMENT**:

**required_agents = 2**

Esses agentes são auxiliares do supervisor/orquestrador:

### Agent A — Executor/Especialista
Responsável por executar a unidade de trabalho dentro do escopo.

### Agent B — Reviewer/Verifier
Responsável por revisar e verificar o resultado com fresh eyes.

O executor não pode aprovar sozinho o próprio trabalho.

## 3. Especialistas

O planejador deve selecionar especialistas conforme a tarefa. Exemplos:

| Superfície | Especialista |
|---|---|
| Frontend | frontend/UI/UX |
| Backend | backend/API |
| Dados | database/data |
| Segurança | security |
| Qualidade | QA/testing |
| Arquitetura | architecture |
| Performance | performance |
| Infra | DevOps/deployment |
| IA | AI/prompt/evaluation |
| Acessibilidade | accessibility |
| Documentação | technical writing |

Esses papéis podem ser combinados quando a unidade for pequena, mas a função de revisão independente continua obrigatória.

## 4. Escalonamento

Use mais de 2 agentes quando a tarefa exigir múltiplas especialidades, alto risco, grande paralelismo ou validações independentes.

Exemplo:

**Supervisor + Executor + Security + QA + Reviewer**

O número não deve ser aumentado artificialmente. O objetivo é cobertura e independência, não criar agentes por criar.

## 5. O que conta como agente ativo

Conta como ativo quando o agente:
1. foi realmente iniciado/disponibilizado;
2. recebeu objetivo e escopo;
3. recebeu contexto suficiente;
4. tem critérios de aceitação/validação;
5. produziu ou está incumbido de produzir evidência verificável.

Não conta:
- agente apenas mencionado no prompt;
- agente apenas listado no plano;
- skill;
- plugin;
- documento;
- ferramenta sem tarefa delegada.

## 6. Ordem mínima

**PLAN → ASSIGN → EXECUTE → OBSERVE → TEST → INDEPENDENT REVIEW → VERIFY**

Se houver falha:

**FINDING → CORRECTION → TEST → VERIFY AGAIN**

## 7. Delegação

Toda delegação deve conter:
- task_id;
- objetivo;
- contexto;
- escopo;
- arquivos/referências;
- restrições;
- critérios de aceitação;
- testes/validação;
- dependências;
- risco.

## 8. Independência

Sempre que o ambiente permitir, o reviewer deve usar contexto/abordagem independente da implementação.

Preferências:
1. agente especializado diferente;
2. agente com contexto mínimo suficiente para revisão;
3. implementação/CLI diferente quando disponível.

Nunca trate a frase "done" de um executor como evidência de aceitação.

## 9. Verificação da política

Antes de ACCEPT, verifique:
- [ ] Superpowers ativo quando aplicável;
- [ ] required_agents >= 2;
- [ ] active_agents >= required_agents;
- [ ] executor identificado;
- [ ] reviewer identificado;
- [ ] reviewer realmente executou revisão;
- [ ] testes aplicáveis executados;
- [ ] findings tratados;
- [ ] verificação pós-correção executada.

Se qualquer item essencial falhar:

**BLOCKED / NOT PROVEN**

Não declare conformidade.

## 10. Exceções

Uma exceção só pode existir quando uma limitação real do ambiente impede a política.

Ela deve registrar:
- regra afetada;
- causa objetiva;
- evidência;
- alternativa;
- impacto;
- ação necessária para normalizar.

Não use "foi mais rápido" ou "não precisava" como justificativa.
