# Headroom

## Papel

Camada de engenharia de contexto/token. Pode comprimir conteúdo, fornecer ferramentas MCP e envolver Claude Code/Codex através de um proxy local.

## Fonte

https://github.com/headroomlabs-ai/headroom

## Instalação

Para a CLI:

uv tool install --python 3.13 "headroom-ai[all]"

ou, em um ambiente Python:

pip install "headroom-ai[all]"

Verificar:

headroom --version
headroom doctor

## Modos

Headroom oferece proxy local, wrap de Claude Code/Codex, MCP, compressão e observabilidade.

Para registrar MCP no Claude Code:

headroom mcp install

Para um proxy local:

headroom proxy --port 8787

Para iniciar Claude através dele:

headroom wrap claude

## Regra do Potencia

Não assumir que Headroom sempre reduz custo/contexto em qualquer cenário.

Antes de torná-lo parte obrigatória do caminho:
1. executar smoke test;
2. verificar integridade das respostas;
3. comparar contexto/saída antes e depois;
4. verificar latência;
5. confirmar que ferramentas continuam funcionando.

Se o wrapper/proxy aumentar overhead ou quebrar uma integração, manter o componente instalado, mas não forçar o caminho otimizado.

## Credenciais

Nunca salvar chaves no Potencia.

Fonte:
https://github.com/headroomlabs-ai/headroom
