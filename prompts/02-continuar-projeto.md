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
- agente responsável;
- arquivos;
- testes;
- critérios de aceitação;
- checkpoints;
- riscos.

## 5. Delegar

**É obrigatório usar agentes/projetos configurados quando forem adequados.**

Não substitua automaticamente:
- revisão por auto-revisão;
- paralelismo por trabalho sequencial;
- harness por memória informal;
- Graphify por grep quando a análise estrutural for necessária;
- Codex Subagents por um único agente quando houver unidades independentes;
- Superharness por execução monolítica em tarefas que exigem coordenação.

Toda delegação deve receber:
- objetivo;
- contexto;
- escopo;
- arquivos;
- restrições;
- critérios;
- forma de validação.

## 6. Executar

Trabalhe por unidades pequenas e verificáveis.

Loop:

**PLAN → ASSIGN → EXECUTE → OBSERVE → TEST → VERIFY → ACCEPT / FIX / BLOCK**

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

Termine contra os critérios reais e com evidência.

