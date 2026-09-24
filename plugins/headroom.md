# Headroom

## Papel

Camada obrigatória de engenharia de contexto, compressão, recuperação e observabilidade para Claude Code e Codex.

## Fonte

https://github.com/headroomlabs-ai/headroom

## Ativação automática obrigatória

O bootstrap deve instalar e deixar o Headroom ativo antes do trabalho do usuário:

    uv tool install --python 3.13 "headroom-ai[all]"
    headroom mcp install --force
    headroom install apply --preset persistent-service --providers all --scope user --mode token
    headroom install status
    headroom mcp status

A instalação persistente configura os agentes detectados, mantém o proxy local saudável em http://127.0.0.1:8787 e reaplica/reinicia o serviço quando necessário. O usuário não precisa chamar headroom, executar wrap ou configurar MCP manualmente.

## Regra operacional

Headroom deve permanecer ligado durante toda a sessão. A compressão automática acontece pelo proxy; as ferramentas MCP ficam disponíveis para compressão, recuperação e estatísticas quando o agente precisar preservar fidelidade.

O bootstrap precisa executar um smoke test de integridade: comparar entrada original, resposta comprimida e recuperação, além de verificar que as ferramentas do agente continuam funcionando. Falha de saúde ou perda de informação é BLOCKED, não motivo para deixar Headroom instalado porém desligado.

## Host existente

Se Claude Code ou Codex já estiver aberto quando o bootstrap terminar, o agente deve aplicar a configuração persistente e recarregar/reiniciar o host quando o mecanismo disponível exigir isso. A sessão só pode ser declarada ativa depois da confirmação de que o host enxerga o Headroom.

## Credenciais

Nunca salvar chaves no Potencia. O Headroom local não deve exigir credencial nova para iniciar seu proxy.
