# Potencia Bootstrap

Execute o bootstrap operacional completo do Potencia.

1. Leia CLAUDE.md, MANIFEST.json e todos os contratos do Potencia.
2. Detecte o ambiente.
3. Instale automaticamente todos os projetos, plugins, skills, hooks, CLIs e dependências configurados.
4. Configure e ative todos eles para a sessão atual e para as próximas sessões.
5. Inicie Headroom e OmniRoute em modo persistente com roteamento automático.
6. Registre o estado em .potencia/runtime-state.json.
7. Execute o Final Gate com evidências reais.

Não trate nenhum componente configurado como opcional e não peça ao usuário para ativá-lo manualmente. Se uma integração for tecnicamente impossível no host, registre BLOCKED com o motivo exato; não declare sucesso parcial.
