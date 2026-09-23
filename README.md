# Potencia IA

**Potencia IA é uma infraestrutura self-bootstrapping para Claude Code.**

A ideia do produto é simples:

1. entregue a pasta/ZIP ou o repositório ao Claude Code;
2. diga para executar/ativar o Potencia;
3. Claude lê a infraestrutura;
4. detecta o ambiente;
5. instala e configura os componentes aplicáveis;
6. ativa skills, agentes, plugins, hooks e otimizações;
7. verifica tudo;
8. registra o estado;
9. só então responde:

**Claude code com Potencia Ativado!**

Depois disso, o usuário pode simplesmente descrever o projeto.

## O que existe

- 10 skills de metodologia, verificação e qualidade.
- 7 projetos/agentes externos especializados.
- 3 camadas de infraestrutura/plugins.
- Bootstrap e preflight.
- Matriz de componentes e estados.
- Loop obrigatório de descoberta → especificação → planejamento → execução → verificação → revisão → correção.
- Economia de contexto/tokens com RTK/Headroom quando apropriado.
- Delegação e coordenação multiagente.
- Revisão adversarial.
- Task Observer com laboratório isolado.
- Cleanup e Project Seal no final do projeto.

## Importante

O repositório não finge que arquivos de contrato são os projetos externos.

Os contratos dizem ao Claude onde está a fonte oficial, como instalar, como ativar e como verificar.

A instalação real acontece no ambiente do usuário e deve ser comprovada.

## Regra de segurança

Nunca coloque credenciais, API keys, tokens ou senhas no Potencia IA.

## Entrada

Comece por CLAUDE.md.

Em seguida, o Claude segue o bootstrap e os três prompts.
