# Potencia IA — Codex Agent Contract

Este repositório é o Potencia IA, uma infraestrutura reutilizável para agentes de desenvolvimento em terminal. Ele é independente de Desktop.

## Bootstrap obrigatório

Quando o usuário pedir para instalar, ativar, executar, fazer bootstrap ou usar o Potencia:

1. Leia CLAUDE.md.
2. Leia MANIFEST.json, bootstrap/BOOTSTRAP.md e bootstrap/AGENT-POLICY.md.
3. Leia os contratos de todos os componentes listados em projetos/, plugins/ e skills/.
4. Detecte o ambiente e instale automaticamente todos os componentes configurados.
5. Configure e ative imediatamente todos os componentes instalados para a sessão do Codex.
6. Inicie os serviços persistentes de contexto, tokens e roteamento e verifique sua saúde.
7. Execute instalação, configuração e verificações reais; não apenas explique.
8. Registre evidências em .potencia/runtime-state.json.
9. Não declare o Potencia ativo sem o Final Gate.

O comando execute (ou executar/ativar/bootstrap/iniciar) significa iniciar o bootstrap operacional completo. Não peça ao usuário para chamar componentes individualmente depois.

## Ativação contínua

Depois do bootstrap, todos os componentes verificados permanecem disponíveis durante toda a sessão:

- skills e contratos são carregados automaticamente;
- agentes Executor e Reviewer ficam prontos para delegação;
- RTK e Headroom ficam ligados ao fluxo de ferramentas/contexto;
- OmniRoute fica ativo como gateway local com roteamento automático;
- hooks, harnesses, Graphify, Task Observer e skills de design ficam disponíveis sem comando manual.

A relevância da tarefa decide qual comportamento cada componente aplica; não decide se o componente será instalado ou ativado. Se o host não suportar alguma integração, registre BLOCKED com evidência e não finja que ela está ativa.

## Uso no projeto do usuário

Para trabalho não trivial, use a política de revisão independente e os agentes definidos em CLAUDE.md e bootstrap/AGENT-POLICY.md. O mínimo é Executor/Especialista e Reviewer/Verifier, além do agente principal quando o ambiente separar esses papéis.

## Verdade operacional

Nunca simule instalação, ativação, delegação, testes ou revisão. Se algo estiver bloqueado, registre o bloqueio e continue tudo que puder ser verificado.

## Escopo

O Potencia IA é o produto principal. Não existe dependência de Potencia Desktop para seu funcionamento.
