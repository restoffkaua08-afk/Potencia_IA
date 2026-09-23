# Potencia + Claude Code

Esta pasta contém a camada nativa de projeto do Claude Code.

O contrato operacional principal continua em CLAUDE.md. Os arquivos daqui existem para aproximar o Potencia dos mecanismos nativos de projeto do Claude Code sem duplicar toda a documentação operacional.

## Estrutura

- agents/ — papéis especializados reutilizáveis.
- commands/ — comandos slash específicos do Potencia.
- skills/ — skills nativas que fazem ponte com o contrato do Potencia.

As configurações locais do usuário devem ficar em .claude/settings.local.json e não devem ser commitadas.
