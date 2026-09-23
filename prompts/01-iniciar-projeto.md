# Prompt 01 — Bootstrap / Iniciar Potencia

> **TRIGGER OPERACIONAL:** se o usuário entregar o link/pasta do Potencia_IA e disser **execute**, **executar**, **ativar**, **bootstrap** ou equivalente, este prompt deve ser executado automaticamente. Não responder pedindo a próxima missão.

## Missão

Este prompt é um **runbook executável**, não uma explicação conceitual. O resultado esperado é uma instalação realmente operacional.

### Regra do gatilho `execute`

Ao detectar o gatilho, o Claude deve entrar em `BOOTSTRAPPING` e continuar pelas etapas abaixo sem esperar uma segunda ordem.

**Não permitido antes do Final Gate:**
- perguntar "qual é a missão?";
- dizer que o Potencia foi ativado só porque os arquivos foram lidos;
- encerrar após carregar skills;
- iniciar o projeto do usuário;
- retornar "estou pronto" como conclusão.

**Permitido:** perguntar somente quando uma ação humana indispensável e não automatizável bloquear uma etapa. Mesmo nesse caso, continue todas as etapas independentes e registre o bloqueio.


Este prompt é o **procedimento de ativação inicial** do Potencia IA.

Quando o usuário entregar a pasta/repositório e pedir para executar/ativar/configurar o Potencia, **não comece o projeto do usuário**.

Primeiro transforme o Potencia em uma infraestrutura operacional.

## Ordem obrigatória

### 1. Ler a própria infraestrutura

**Não pare depois desta etapa. Ler é apenas o começo do bootstrap.**
Leia:
1. `CLAUDE.md`
2. este prompt
3. `prompts/02-continuar-projeto.md`
4. `prompts/03-missao-autonoma.md`
5. `MANIFEST.json`
6. `bootstrap/BOOTSTRAP.md`

Depois faça um inventário das pastas e arquivos.

### 2. Estudar os componentes

Para cada item de `projetos/`, `plugins/` e `skills/`:
- leia o contrato local;
- identifique finalidade;
- identifique dependências;
- identifique instalação;
- identifique ativação;
- identifique como verificar;
- identifique conflitos/limitações;
- identifique se exige credencial ou ação humana.

Não presuma que um arquivo `.md` instalado localmente significa que o projeto externo está instalado.

### 3. Detectar o ambiente

Descubra, sem pedir ao usuário informações que possam ser obtidas por ferramentas:
- SO;
- arquitetura;
- shell;
- Claude Code;
- Git;
- Python;
- Node/npm;
- uv/pipx;
- Codex CLI, se disponível;
- outras dependências exigidas.

Registre versões.

### 4. Instalar

Use primeiro o procedimento oficial do componente.

Prioridade:
1. instalação nativa/oficial;
2. instalação via CLI oficial;
3. instalação por repositório oficial;
4. fallback documentado no contrato local.

Nunca invente um instalador.

Não execute código remoto obscuro sem primeiro verificar a fonte e o conteúdo quando isso for possível.

### 5. Ativar

Ative/configure:
- plugins;
- skills;
- hooks;
- comandos;
- integrações;
- roteadores;
- otimizações;
- harnesses;
- subagentes.

Quando uma ativação só puder ocorrer dentro da interface do Claude Code, execute o procedimento suportado pelo ambiente; se a plataforma não permitir automação completa, registre o bloqueio em vez de fingir.

### 6. Verificar

Cada componente deve terminar em um estado:

- INSTALLED
- CONFIGURED
- ACTIVE
- VERIFIED
- BLOCKED
- NOT APPLICABLE
- FAILED

Sempre registre evidência.

### 7. Corrigir

Se falhar:
1. leia o erro;
2. diagnostique;
3. tente correção segura;
4. repita o teste;
5. tente alternativa oficial;
6. marque BLOCKED somente depois de esgotar alternativas razoáveis.

Não repita cegamente o mesmo comando.

### 8. Registrar estado

Crie/atualize:

`.potencia/runtime-state.json`

Nunca inclua segredos.

### 9. Teste de integração

Depois dos testes individuais, confirme:
- skills carregáveis;
- agentes/projetos acessíveis;
- plugins ativos;
- Graphify operacional quando aplicável;
- otimização de contexto/token operacional quando aplicável;
- hooks funcionando;
- harness/orquestração disponível;
- delegação disponível quando configurada.

### 10. Fechamento

Antes de fechar, faça uma checagem explícita de que nenhuma fase anterior foi apenas lida ou declarada sem execução real.

Se o usuário entrou pelo gatilho `execute`, o bootstrap só pode terminar no **Final Gate**. Não existe retorno intermediário de "Potencia pronto".


Só conclua quando a matriz estiver processada.

Se tudo aplicável estiver operacional, retorne **exatamente**:

**Claude code com Potencia Ativado!**

Não implemente o projeto do usuário nessa etapa.

Se existir bloqueio essencial, não use a frase de sucesso.
