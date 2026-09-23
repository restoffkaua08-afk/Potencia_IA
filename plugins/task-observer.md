# Task Observer

## Papel

Meta-skill de observação e evolução das skills.

Fonte selecionada:
https://github.com/rebelytics/one-skill-to-rule-them-all

## Instalação

A forma documentada para Claude Code é:

npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer

Preserve a estrutura exigida pela skill, incluindo referências/scripts quando fornecidos.

## Ativação

A descrição da skill sozinha não é considerada suficiente.

O Potencia fornece uma ativação estrutural em CLAUDE.md:
- iniciar observação em sessões de trabalho;
- registrar observações;
- manter laboratório isolado;
- revisar antes de promover mudanças.

## Isolamento obrigatório

Produção:
skills/

Laboratório:
task-observer-workspace/

O Observer pode experimentar apenas no laboratório.

Não pode alterar autonomamente:
- CLAUDE.md;
- prompts/;
- plugins/;
- projetos/.

## Verificação

Confirmar que:
- a skill está disponível;
- o gatilho estrutural existe;
- o workspace de observação pode ser criado;
- observações não escrevem diretamente na produção.

Fonte:
https://github.com/rebelytics/one-skill-to-rule-them-all
