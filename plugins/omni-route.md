# OmniRoute

## Papel

Gateway obrigatório de modelos e provedores para Claude Code, Codex e outras ferramentas. Ele fornece uma rota local automática, fallback e telemetria de uso.

## Fonte selecionada

https://github.com/crl33/omniroute

Não substitua esta fonte silenciosamente por outro fork.

## Ativação automática obrigatória

O bootstrap deve instalar, iniciar e verificar o OmniRoute sem exigir que o usuário faça configuração manual:

    npm install -g omniroute
    omniroute
    omniroute setup-claude        # quando Claude Code existir
    omniroute setup-codex         # quando Codex existir

O serviço local deve permanecer ativo em http://127.0.0.1:20128. A rota padrão é auto, usando os provedores gratuitos/sem credencial disponíveis no ambiente. O bootstrap deve testar:

- GET /v1/models;
- uma chamada mínima com o modelo auto;
- `omniroute setup-claude` e/ou `omniroute setup-codex` quando o host existir;
- MCP do OmniRoute no Claude Code;
- roteamento da sessão detectada pelo endpoint local.

A sessão não é declarada ativa só porque o processo abriu a porta: a chamada mínima precisa responder e a configuração do host precisa ser verificada.

Quando o host oferecer uma integração oficial, o Potencia deve usar o launcher/configuração oficial do OmniRoute para iniciar o agente já conectado ao gateway, sem pedir ao usuário para chamar outro comando.

## Credenciais e provedores

O baseline automático não deve exigir chave nova. Credenciais existentes do usuário podem ser preservadas para ampliar os provedores e os fallbacks, mas nunca podem ser inventadas, expostas, gravadas no repositório ou solicitadas sem necessidade.

Se nenhuma rota automática saudável estiver disponível, registrar BLOCKED com a resposta de saúde e a alternativa tentada. Não fingir que o gateway está ativo.

## Segurança

Não colocar API keys, tokens, cookies, credenciais ou URLs privadas com segredo em arquivos do Potencia ou commits.
