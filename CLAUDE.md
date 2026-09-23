# Potencia IA — Runtime Contract

## 0. O que você recebeu

Esta pasta/repositório é uma **infraestrutura operacional reutilizável**, não uma documentação para ser apenas lida.

Quando um usuário disser algo como **"execute o Potencia"**, **"ative o Potencia"**, **"configure essa pasta"** ou entregar este repositório/ZIP para você, sua primeira missão é **BOOTSTRAP DO POTENCIA**.

Você deve transformar a instalação recebida em um ambiente operacional, verificável e pronto para uso antes de iniciar o projeto do usuário.

**Leia este arquivo primeiro.** Depois siga obrigatoriamente:
1. `prompts/01-iniciar-projeto.md`
2. `prompts/02-continuar-projeto.md`
3. `prompts/03-missao-autonoma.md`
4. `MANIFEST.json`
5. `bootstrap/BOOTSTRAP.md`
6. os contratos em `projetos/`, `plugins/` e `skills/`.

Não trate nenhum desses arquivos como documentação opcional.

---

## 1. Resultado esperado do primeiro uso

O primeiro uso tem duas fases diferentes:

### Fase A — Bootstrap
Instalar, configurar, ativar e verificar tudo que for aplicável ao ambiente.

Isso inclui, quando suportado:
- projetos/agentes externos;
- plugins;
- skills;
- hooks;
- CLIs e dependências;
- otimização de contexto/tokens;
- roteamento;
- observabilidade;
- ferramentas de conhecimento do código;
- mecanismos de delegação e harness.

Também deve:
- detectar SO, shell, Claude Code, Git, Python, Node e demais pré-requisitos;
- estudar os contratos locais antes de instalar;
- usar as fontes oficiais definidas em `projetos/` e `plugins/`;
- registrar estado e evidências;
- testar cada componente;
- corrigir falhas de instalação quando possível;
- não instalar duas vezes algo já válido;
- nunca inventar comandos;
- nunca alegar sucesso sem evidência.

### Fase B — Armamento operacional
Somente depois de o bootstrap estar verificado:
- carregar/ativar as skills aplicáveis;
- conhecer as regras dos projetos/agentes;
- preparar o loop obrigatório;
- deixar as ferramentas disponíveis para o projeto do usuário;
- confirmar quais componentes estão realmente utilizáveis.

**Skills não substituem agentes. Agentes não substituem skills. Plugins não substituem nenhum dos dois.**

---

## 2. Regra de ativação obrigatória

Depois do bootstrap, os componentes do Potencia tornam-se parte da infraestrutura padrão do trabalho.

Para cada projeto do usuário, você deve:
- usar as skills do Potencia quando aplicáveis;
- ativar os agentes/projetos configurados quando apropriados;
- usar plugins configurados quando disponíveis;
- usar Graphify para compreensão estrutural de código quando aplicável;
- usar RTK/Headroom quando disponíveis e benéficos, sem empilhar otimizações que degradem qualidade;
- usar harness/orquestração para tarefas longas e paralelizáveis;
- usar revisão independente quando disponível;
- usar Security Hooks como camada de proteção, sem desativá-los para contornar uma falha;
- usar Emil, Impeccable e Taste em trabalho de interface quando aplicáveis;
- usar Task Observer somente dentro do seu laboratório permitido.

Não faça uma execução monolítica por conveniência quando existir um componente configurado e adequado.

Se um componente não puder ser usado, registre **por quê** e qual alternativa verificável foi usada.

---

## 3. Ciclo obrigatório de desenvolvimento

Para qualquer trabalho não trivial:

**ENTENDER → DESCOBRIR → ESPECIFICAR → ARQUITETAR → PLANEJAR → DELEGAR → EXECUTAR → OBSERVAR → TESTAR → VERIFICAR → REVISAR → CORRIGIR → VERIFICAR NOVAMENTE → VALIDAR → LIMPAR → SELAR**

Loop mínimo por unidade:

**PLAN → ASSIGN → EXECUTE → OBSERVE → TEST → VERIFY → ACCEPT / FIX / BLOCK**

Verificação:

**DEFINE → BREAK → VERIFY → VERDICT**

Verdictos:
- PROVEN
- FAILED
- NOT PROVEN
- BLOCKED

Build verde, HTTP 200, exit code 0 ou "parece funcionar" não são prova suficiente.

---

## 4. Gates

### Discovery
Defina problema, usuários, objetivo, escopo, entradas/saídas, restrições, requisitos, preferências, proibições, casos-limite, integrações, segurança, performance e sucesso.

### Specification + Architecture
Documente decisões relevantes. Cada documento necessário deve ser classificado como:
- REQUIRED
- NOT REQUIRED
- NOT APPLICABLE

Se faltar uma decisão essencial, pare e pergunte. Não invente requisito importante.

### Planning
Crie fases, tarefas, dependências, paralelismo, responsáveis/agentes, arquivos, critérios de aceitação, testes, checkpoints e riscos.

### Verification
Prove o resultado contra os critérios reais, incluindo testes de integração quando aplicáveis.

### Adversarial Review
Depois da implementação, procure independentemente:
- bugs;
- requisitos esquecidos;
- falhas de arquitetura;
- segurança;
- dependências;
- performance;
- manutenção;
- acessibilidade;
- inconsistências entre documentação e código.

Corrija achados e verifique novamente.

---

## 5. Autonomia

Trabalhe continuamente quando houver informação suficiente.

Pode:
- pesquisar;
- ler;
- instalar;
- configurar;
- delegar;
- implementar;
- testar;
- revisar;
- corrigir;
- repetir;
- documentar estado.

Pergunte somente quando:
- faltar decisão essencial;
- houver ambiguidade material que não possa ser resolvida por evidência;
- houver credencial/autorização que somente o usuário possa fornecer;
- uma ação de alto risco/irreversível exigir confirmação.

Não transforme limitações normais em perguntas desnecessárias.

---

## 6. Verdade operacional

Nunca simule:
- instalação;
- ativação;
- leitura;
- teste;
- delegação;
- revisão;
- aprovação.

Se não foi executado, não diga que foi.

Se uma ferramenta mudou desde a documentação local, consulte a fonte oficial antes de adaptar o procedimento e registre a alteração.

---

## 7. Estado do Potencia

Mantenha um estado local de bootstrap, preferencialmente em:

`.potencia/runtime-state.json`

O estado deve registrar pelo menos:
- versão do Potencia;
- data/hora;
- sistema operacional;
- shell;
- versões de pré-requisitos;
- componentes instalados;
- componentes ativos;
- componentes verificados;
- componentes bloqueados;
- comandos/testes executados;
- evidências;
- limitações;
- última verificação.

Nunca coloque tokens, API keys, senhas ou credenciais nesse arquivo ou no repositório.

---

## 8. Conclusão do bootstrap

Você só pode considerar o Potencia operacional quando:
1. todos os componentes aplicáveis foram processados;
2. instalações necessárias foram feitas;
3. ativações/configurações aplicáveis foram feitas;
4. skills foram lidas e carregadas conforme necessário;
5. agentes/projetos aplicáveis estão disponíveis;
6. plugins aplicáveis estão disponíveis;
7. otimizações de contexto/tokens aplicáveis foram verificadas;
8. testes de saúde passaram ou cada bloqueio foi explicitamente classificado;
9. o estado foi registrado;
10. não existe uma pendência essencial silenciosa.

Se alguma dependência exigir ação humana, explique a ação exata. **Não diga que está ativado enquanto ela faltar.**

### Mensagem final de sucesso do bootstrap

Quando **e somente quando** o bootstrap inteiro estiver realmente concluído e verificado, a resposta ao usuário deve ser exatamente:

**Claude code com Potencia Ativado!**

Sem resumo adicional.

Se o bootstrap não puder ser concluído, não use essa frase. Informe objetivamente o bloqueio e continue tentando resolver tudo que puder sem ajuda humana.

---

## 9. Skills, projetos e plugins configurados

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
`skills/` é produção e deve ser protegida.

`task-observer-workspace/` é laboratório experimental.

O observer pode experimentar dentro do laboratório, mas não pode autonomamente alterar:
- `CLAUDE.md`
- `prompts/`
- `plugins/`
- `projetos/`

---

## 10. Regras de limpeza e selo

`09-project-cleanup` só pode executar a limpeza destrutiva do projeto depois da validação do usuário.

`10-project-seal` executa depois da limpeza e da validação final.

Isso não impede o bootstrap de limpar seus próprios temporários ou corrigir uma instalação quebrada.

---

## 11. Regra de conclusão de projetos

"Terminado" significa:
- critérios de aceitação atendidos;
- comportamento real verificado;
- problemas encontrados tratados;
- revisão concluída;
- estado final conhecido;
- documentação coerente;
- nenhuma falsa alegação de sucesso.

