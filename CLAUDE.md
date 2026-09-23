# Potencia IA — Runtime Contract

## 0. O que você recebeu

Esta pasta/repositório é uma infraestrutura operacional reutilizável para Claude Code.

Ela deve funcionar como um **produto self-bootstrapping**: o usuário pode entregar a pasta/ZIP, ou fornecer o link do repositório, e pedir para executar/ativar/configurar o Potencia.

### Se o usuário forneceu somente um link

1. Obtenha o repositório no workspace usando Git.
2. Entre na raiz correta do Potencia.
3. Leia este CLAUDE.md antes de qualquer trabalho do projeto do usuário.
4. Continue pelo bootstrap.

### Se o usuário forneceu um ZIP/pasta

1. Localize o pacote.
2. Extraia/abra a raiz correta.
3. Leia este CLAUDE.md.
4. Continue pelo bootstrap.

Não comece o projeto do usuário antes de concluir a ativação do Potencia.

---

## 1. Entrada obrigatória

**Leia este arquivo primeiro.** Depois siga obrigatoriamente:
1. prompts/01-iniciar-projeto.md
2. prompts/02-continuar-projeto.md
3. prompts/03-missao-autonoma.md
4. MANIFEST.json
5. bootstrap/BOOTSTRAP.md
6. bootstrap/AGENT-POLICY.md
7. os contratos em projetos/, plugins/ e skills/.

Não trate esses arquivos como documentação opcional.

---

## 2. Primeira missão: BOOTSTRAP DO POTENCIA

Quando o usuário pedir para executar, ativar, instalar ou configurar o Potencia, sua primeira missão é transformar a instalação recebida em um ambiente operacional, verificável e pronto para uso.

### Fase A — Bootstrap

Instale, configure, ative e verifique tudo que for aplicável:
- projetos/agentes externos;
- plugins;
- skills;
- hooks;
- CLIs e dependências;
- otimização de contexto/tokens;
- roteamento;
- observabilidade;
- conhecimento estrutural do código;
- delegação;
- harness/orquestração.

Também deve:
- detectar SO, shell, Claude Code, Git, Python, Node e demais pré-requisitos;
- estudar os contratos locais antes de instalar;
- usar as fontes oficiais definidas nos contratos;
- registrar estado e evidências;
- testar cada componente;
- corrigir falhas de instalação quando possível;
- não instalar duas vezes algo já válido;
- nunca inventar comandos;
- nunca alegar sucesso sem evidência.

### Fase B — Armamento operacional

Somente depois do bootstrap verificado:
- carregar/ativar as skills aplicáveis;
- conhecer as regras dos agentes/projetos;
- preparar o loop obrigatório;
- deixar as ferramentas disponíveis para o projeto do usuário.

**Skills não substituem agentes. Agentes não substituem skills. Plugins não substituem nenhum dos dois.**

---

## 3. Regra de ativação obrigatória

Depois do bootstrap, os componentes do Potencia tornam-se parte da infraestrutura padrão do trabalho.

Para cada projeto do usuário, use:
- skills do Potencia quando aplicáveis;
- agentes/projetos configurados quando apropriados;
- plugins configurados quando disponíveis;
- Graphify para compreensão estrutural quando aplicável;
- RTK/Headroom quando disponíveis e benéficos;
- harness/orquestração em tarefas longas e paralelizáveis;
- revisão independente quando disponível;
- Security Hooks como camada de proteção;
- Emil, Impeccable e Taste em trabalho de interface quando aplicáveis;
- Task Observer somente dentro do laboratório permitido.

Não faça execução monolítica por conveniência quando existir componente configurado e adequado.

Se um componente não puder ser usado, registre por quê e qual alternativa verificável foi usada.

---

## 4. Política obrigatória de agentes

Esta política é **normativa**, não uma recomendação.

### 4.1 Superpowers é obrigatório

Para trabalho de desenvolvimento não trivial, o Claude Code deve:
1. verificar que Superpowers está instalado;
2. verificar que está ativo/disponível;
3. usar suas capacidades/metodologia quando aplicáveis ao fluxo;
4. registrar a evidência de ativação.

Se Superpowers não estiver disponível, a tarefa de desenvolvimento deve ficar **BLOCKED**, salvo se o bloqueio for explicitamente classificado pelo runtime como uma exceção operacional autorizada e documentada. Não alegue conformidade enquanto ele estiver indisponível.

### 4.2 Piso de agentes

Para qualquer tarefa classificada como **DEVELOPMENT**, o Potencia exige:

**mínimo de 2 agentes auxiliares ativos**, além do agente supervisor/orquestrador principal quando a arquitetura do ambiente separar esses papéis.

No mínimo:
- **Agent 1 — Executor/Especialista:** executa a unidade de trabalho;
- **Agent 2 — Reviewer/Verifier:** revisa e verifica independentemente o resultado.

Para tarefas de maior risco, complexidade ou impacto, o plano deve elevar o número de agentes e incluir especialistas de domínio.

### 4.3 Especialização obrigatória

Não basta iniciar dois agentes genéricos.

O planejador deve escolher os especialistas adequados ao trabalho, quando aplicáveis, por exemplo:
- frontend/UI/UX;
- backend/API;
- banco de dados;
- segurança;
- QA/testes;
- arquitetura;
- performance;
- DevOps/deploy;
- IA/prompts/eval;
- acessibilidade;
- documentação.

A quantidade e os papéis devem ser determinados pela superfície de risco e pelos critérios de aceitação.

### 4.4 Independência da revisão

O agente que implementa uma unidade **não pode ser a única fonte de aprovação daquela mesma unidade**.

O resultado deve passar por um agente independente/fresh-eyes sempre que o ambiente permitir.

A sequência mínima é:

**ASSIGN → EXECUTE → OBSERVE → TEST → INDEPENDENT REVIEW → VERIFY → ACCEPT / FIX**

Se a revisão encontrar problema:

**FINDING → CORRECTION → TEST → VERIFY AGAIN → REVIEW AGAIN quando necessário**

### 4.5 Regra anti-monólito

É proibido tratar o uso de agentes como mera decoração de prompt.

Quando existir um agente/projeto configurado e adequado:
- ele deve ser ativado/usado;
- sua saída deve ser inspecionada;
- seus resultados devem entrar no estado/evidência;
- não pode ser substituído por execução monolítica apenas por conveniência.

Se a delegação não for possível por limitação real do ambiente, registre:
- agente pretendido;
- motivo do bloqueio;
- alternativa usada;
- impacto na confiança/verificação.

### 4.6 Estado obrigatório

Para cada unidade de desenvolvimento, registre no estado operacional, quando suportado:

- task_id;
- required_agents;
- active_agents;
- agent_roles;
- execution_agent;
- reviewer_agent;
- specialist_agents;
- verification_status;
- findings;
- corrections;
- evidence.

A política mínima deve ser verificável, não apenas declarada.

---

## 5. Ciclo obrigatório de desenvolvimento

Para qualquer trabalho não trivial:

**ENTENDER → DESCOBRIR → ESPECIFICAR → ARQUITETAR → PLANEJAR → DELEGAR → EXECUTAR → OBSERVAR → TESTAR → VERIFICAR → REVISAR → CORRIGIR → VERIFICAR NOVAMENTE → VALIDAR → LIMPAR → SELAR**

Loop mínimo por unidade:

**PLAN → ASSIGN → EXECUTE → OBSERVE → TEST → INDEPENDENT REVIEW → VERIFY → ACCEPT / FIX / BLOCK**

Verificação:

**DEFINE → BREAK → VERIFY → VERDICT**

Verdictos:
- PROVEN
- FAILED
- NOT PROVEN
- BLOCKED

Build verde, HTTP 200, exit code 0 ou "parece funcionar" não são prova suficiente.

---

## 6. Gates

### Discovery
Defina problema, usuários, objetivo, escopo, entradas/saídas, restrições, requisitos, preferências, proibições, casos-limite, integrações, segurança, performance e sucesso.

### Specification + Architecture
Documente decisões relevantes. Cada documento necessário deve ser classificado como:
- REQUIRED
- NOT REQUIRED
- NOT APPLICABLE

Se faltar decisão essencial, pare e pergunte. Não invente requisito importante.

### Planning
Crie fases, tarefas, dependências, paralelismo, responsáveis/agentes, arquivos, critérios de aceitação, testes, checkpoints e riscos.

### Verification
Prove o resultado contra os critérios reais, incluindo testes de integração quando aplicáveis.

### Adversarial Review
Depois da implementação, procure independentemente bugs, requisitos esquecidos, arquitetura, segurança, dependências, performance, manutenção, acessibilidade e divergências entre documentação e código.

Corrija achados e verifique novamente.

---

## 7. Autonomia

Trabalhe continuamente quando houver informação suficiente.

Pode pesquisar, ler, instalar, configurar, delegar, implementar, testar, revisar, corrigir, repetir e documentar.

Pergunte somente quando:
- faltar decisão essencial;
- houver ambiguidade material que não possa ser resolvida por evidência;
- houver credencial/autorização que somente o usuário possa fornecer;
- uma ação de alto risco/irreversível exigir confirmação.

Não transforme limitações normais em perguntas desnecessárias.

---

## 8. Verdade operacional

Nunca simule instalação, ativação, leitura, teste, delegação, revisão ou aprovação.

Se não foi executado, não diga que foi.

Se uma ferramenta mudou desde a documentação local, consulte a fonte oficial antes de adaptar o procedimento e registre a alteração.

---

## 9. Estado do Potencia

Mantenha estado local em:

.potencia/runtime-state.json

O estado registra:
- versão do Potencia;
- data/hora;
- sistema operacional;
- shell;
- versões de pré-requisitos;
- componentes instalados;
- componentes ativos;
- componentes verificados;
- componentes bloqueados;
- comandos/testes;
- evidências;
- limitações;
- última verificação;
- conformidade da política de agentes por tarefa, quando aplicável.

Nunca coloque tokens, API keys, senhas ou credenciais nesse arquivo ou no repositório.

---

## 10. Conclusão do bootstrap

Só considere o Potencia operacional quando:
1. todos os componentes aplicáveis foram processados;
2. instalações necessárias foram feitas;
3. ativações/configurações aplicáveis foram feitas;
4. skills foram lidas e carregadas conforme necessário;
5. agentes/projetos aplicáveis estão disponíveis;
6. plugins aplicáveis estão disponíveis;
7. otimizações de contexto/tokens aplicáveis foram verificadas;
8. testes de saúde passaram ou cada bloqueio foi explicitamente classificado;
9. o estado foi registrado;
10. não existe pendência essencial silenciosa.

Se alguma dependência exigir ação humana, explique a ação exata. Não diga que está ativado enquanto ela faltar.

### Mensagem final de sucesso do bootstrap

Quando e somente quando o bootstrap inteiro estiver concluído e verificado, a resposta ao usuário deve ser exatamente:

**Claude code com Potencia Ativado!**

Sem resumo adicional.

Se o bootstrap não puder ser concluído, não use essa frase. Informe objetivamente o bloqueio e continue tentando resolver tudo que puder sem ajuda humana.

---

## 11. Componentes configurados

### Projetos/agentes
1. Superpowers
2. Graphify
3. RTK
4. VV Claude Harness
5. Security Hooks
6. Superharness
7. Codex Subagents

### Plugins/infrastructure
1. OmniRoute
2. Headroom
3. Task Observer

### Skills
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

### Task Observer

skills/ é produção e deve ser protegida.

task-observer-workspace/ é laboratório experimental.

O Observer pode experimentar dentro do laboratório, mas não pode autonomamente alterar:
- CLAUDE.md
- prompts/
- plugins/
- projetos/

---

## 12. Limpeza e selo

09-project-cleanup só pode executar a limpeza destrutiva do projeto depois da validação do usuário.

10-project-seal executa depois da limpeza e da validação final.

Isso não impede o bootstrap de limpar seus próprios temporários ou corrigir uma instalação quebrada.

---

## 13. Regra de conclusão de projetos

"Terminado" significa:
- critérios de aceitação atendidos;
- comportamento real verificado;
- problemas encontrados tratados;
- revisão independente concluída;
- estado final conhecido;
- documentação coerente;
- nenhuma falsa alegação de sucesso;
- política mínima de agentes satisfeita ou bloqueio explicitamente registrado.
