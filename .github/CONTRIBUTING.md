# Contribuindo com o Potencia IA

Obrigado por querer contribuir.

O Potencia é uma infraestrutura open source voltada a desenvolvimento assistido por agentes de IA, harnesses, skills, verificação e automação. Contribuições devem preservar esse objetivo: tornar o trabalho dos agentes mais organizado, verificável e reutilizável.

## Antes de contribuir

1. Leia o README.
2. Leia o CLAUDE.md para entender o contrato operacional.
3. Para mudanças de bootstrap, agentes, plugins ou skills, consulte os contratos em bootstrap/, projetos/, plugins/ e skills/.
4. Não inclua API keys, tokens, senhas ou dados privados.

## Pull requests

Descreva:
- o problema que a mudança resolve;
- o que foi alterado;
- como a mudança foi testada;
- possíveis impactos em outros componentes.

Mudanças que alterem o comportamento operacional devem incluir evidência de verificação sempre que possível.

## Novos componentes

Para adicionar um agente, plugin, skill ou projeto externo, prefira:
- fonte oficial identificada;
- propósito claro;
- método de instalação/ativação documentado;
- verificação reproduzível;
- licença compatível;
- ausência de credenciais no repositório.

## Princípio

O Potencia não deve declarar uma integração como ativa ou verificada apenas porque ela foi documentada. O comportamento real precisa ser verificável.
