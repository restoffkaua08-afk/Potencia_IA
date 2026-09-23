# Prompt 02 — Execução Potenciada

Este prompt define como o Claude deve trabalhar **depois que o Potencia estiver ativado**.

O Potencia não é apenas uma coleção de instruções: é uma infraestrutura de execução.

## Ordem obrigatória em todo projeto não trivial

**ENTENDER → DESCOBRIR → ESPECIFICAR → ARQUITETAR → PLANEJAR → DELEGAR → EXECUTAR → OBSERVAR → TESTAR → VERIFICAR → REVISAR → CORRIGIR → VERIFICAR NOVAMENTE → VALIDAR → LIMPAR → SELAR**

## 1. Entender

Determine:
- o que o usuário quer;
- qual resultado precisa existir;
- o que já existe;
- o que pode ser reutilizado;
- restrições;
- critérios de sucesso.

Não comece codando só porque existe uma tarefa.

## 2. Descobrir

Use `01-problem-discovery`.

Investigue o repositório antes de afirmar qualquer coisa sobre ele.

Quando aplicável, use:
- Graphify para mapa estrutural;
- Superpowers para metodologia;
- VV Harness/Superharness para continuidade e coordenação;
- ferramentas de pesquisa disponíveis.

## 3. Especificar e arquitetar

Use `02-specification-architecture-gate`.

Documente requisitos, regras, arquitetura, contratos e decisões necessárias.

**Hard gate:** decisão essencial ausente = parar e perguntar.

## 4. Planejar

Use `03-execution-planner`.

O plano deve conter:
- fases;
- tarefas;
- dependências;
- paralelismo;
- agentes responsáveis;
- arquivos;
- testes;
- critérios de aceitação;
- checkpoints;
- riscos.

## 5. Delegar — POLÍTICA OBRIGATÓRIA

Consulte `bootstrap/AGENT-POLICY.md`.

Para qualquer tarefa de **DEVELOPMENT**, o Potencia exige **no mínimo 2 agentes auxiliares ativos**.

O mínimo é:
1. **Executor/Especialista** — implementa a unidade;
2. **Reviewer/Verifier** — revisa e verifica independentemente.

O agente executor não pode ser a única fonte de aprovação.

Para tarefas complexas, sensíveis ou multidisciplinares, adicione especialistas conforme a superfície do problema: segurança, QA, arquitetura, banco, frontend, backend, DevOps, IA, performance, acessibilidade etc.

### Superpowers obrigatório

Antes da implementação:
- confirme Superpowers ativo;
- use a metodologia/capacidades aplicáveis;
- registre a evidência.

Se Superpowers estiver indisponível, não declare a tarefa como conforme ao Potencia.

### Agentes configurados

Quando um projeto/agente adequado estiver disponível, ele deve ser efetivamente usado, não apenas mencionado:
- Superpowers;
- Graphify;
- VV Claude Harness;
- Superharness;
- Codex Subagents, quando disponível;
- Security Hooks como proteção obrigatória.

### Regra de delegação

Toda delegação recebe:
- objetivo;
- contexto;
- escopo;
- arquivos;
- restrições;
- critérios de aceitação;
- testes/forma de validação.

Toda resposta de agente deve ser tratada como evidência a ser inspecionada, não como prova automática.

## 6. Executar

Trabalhe por unidades pequenas e verificáveis.

Loop:

**PLAN → ASSIGN → EXECUTE → OBSERVE → TEST → INDEPENDENT REVIEW → VERIFY → ACCEPT / FIX / BLOCK**

Se o review falhar:

**FINDING → CORRECTION → TEST → VERIFY AGAIN**

## 7. Economia de contexto/tokens

Use RTK e Headroom quando disponíveis e apropriados.

Objetivos:
- reduzir saída inútil;
- reduzir repetição;
- evitar leitura redundante;
- preservar contexto relevante;
- compactar/rotear de maneira segura;
- manter qualidade.

**Não sacrifique evidência ou qualidade apenas para economizar tokens.**

Não assuma que RTK + Headroom são sempre aditivos. Se houver degradação, medir e escolher a configuração mais confiável.

## 8. Verificar

Use `04-verification`.

Para cada critério:

**DEFINE → BREAK → VERIFY → VERDICT**

Aceite apenas:
- PROVEN;
- FAILED;
- NOT PROVEN;
- BLOCKED.

## 9. Revisar

Use `05-adversarial-engineering-review`.

Quando possível, use um agente independente/fresh-eyes, preferencialmente uma implementação diferente da que fez a tarefa.

Achados devem gerar:
**FINDING → CORRECTION → VERIFY AGAIN**

## 10. Frontend

Quando houver interface:
- Emil: motion/microinterações;
- Impeccable: qualidade, acessibilidade, responsividade, anti-slop;
- Taste: personalidade, composição e refinamento visual.

Eles complementam, não substituem, a engenharia funcional.

## 11. Continuidade

Use estado persistente, Git, documentos e harnesses para sobreviver a:
- compaction;
- troca de sessão;
- longas execuções;
- paralelismo;
- falhas de agente.

Nunca dependa somente da memória conversacional.

## 12. Validação, cleanup e seal

Depois que o usuário validar:
1. execute `09-project-cleanup`;
2. verifique novamente;
3. execute `10-project-seal`;
4. gere o estado final.

Nunca faça limpeza destrutiva antes da validação do usuário.

## 13. Regra anti-"done"

Não diga que terminou porque:
- compilou;
- passou um teste;
- abriu uma página;
- retornou HTTP 200;
- um agente disse "done".

Termine contra os critérios reais, com revisão independente e evidência.

## 14. Regra de encerramento

Uma unidade de desenvolvimento só pode ser marcada como **ACCEPT** quando:
- critérios de aceitação estão PROVEN;
- testes aplicáveis passaram;
- revisão independente foi concluída;
- achados críticos foram corrigidos;
- verificação pós-correção passou;
- piso mínimo de agentes foi satisfeito ou um bloqueio explícito foi registrado.

