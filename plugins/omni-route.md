# OmniRoute

## Papel

Gateway/router de modelos e provedores para Claude Code, Codex e outras ferramentas.

## Fonte selecionada

Implementação selecionada para o Potencia:
https://github.com/crl33/omniroute

O nome OmniRoute possui múltiplas implementações/forks. Não substitua esta fonte silenciosamente por outra.

## Instalação

A implementação selecionada documenta instalação via npm:

npm install -g omniroute

Depois:

omniroute

A instalação deve ser verificada antes de configurar qualquer cliente.

## Ativação

O uso pode ser feito por launcher/configuração própria do OmniRoute. Nunca grave API keys no Potencia.

Antes de alterar ANTHROPIC_BASE_URL, OPENAI_BASE_URL ou configurações equivalentes:
1. verificar se o servidor está saudável;
2. confirmar o endpoint;
3. confirmar que existe pelo menos um provedor autorizado;
4. testar um modelo;
5. preservar uma forma de retornar ao endpoint direto.

## Verificação

Confirmar:
- comando omniroute disponível;
- servidor responde;
- endpoint de modelos responde;
- autenticação funciona;
- Claude Code/Codex conseguem completar uma chamada de teste quando configurados.

## Regra importante

OmniRoute é uma camada de roteamento. Ele não transforma uma cota/assinatura de um provedor em outra cota. Qualquer fallback depende dos provedores e credenciais realmente configurados.

## Segurança

Não colocar API keys, tokens, cookies, credenciais ou URLs privadas com segredo em arquivos do Potencia ou commits.

Fonte:
https://github.com/crl33/omniroute
