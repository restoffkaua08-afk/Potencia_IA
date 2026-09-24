# Potencia Bootstrap

Execute o bootstrap operacional real do Potencia na raiz do projeto do usuário.

1. Leia CLAUDE.md, MANIFEST.json e os contratos em bootstrap/, projetos/, plugins/ e .claude/.
2. Execute python -m potencia_runtime bootstrap --workspace . (ou potencia bootstrap --workspace . se o pacote estiver instalado).
3. Deixe o processo instalar, configurar, iniciar e verificar todos os componentes.
4. Leia .potencia/runtime-state.json e confira o Final Gate.
5. Se houver BLOCKED, execute no host a ação exata registrada em components[*].evidence, quando ela exigir interação do Claude/Codex, e rode o bootstrap novamente.
6. Só termine quando o estado for VERIFIED; caso contrário, informe o bloqueio objetivo e não alegue ativação.

O bootstrap é obrigatório. Nenhum componente configurado pode ser pulado silenciosamente.
