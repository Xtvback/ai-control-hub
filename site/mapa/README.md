# Mapa das Ligações ChatGPT

Página: `site/mapa/index.html`. Site previsto: `https://xtvback.github.io/ai-control-hub/mapa/` (depende de GitHub Pages estar ativo).

## Funcionalidades
- Árvore navegável (expandir/recolher, pesquisa, zoom, painel de detalhes e ligações cruzadas).
- PIN visual de 4 dígitos validado por hash SHA-256. Não é autenticação real: ficheiros públicos são inspecionáveis.
- Catálogo gerado a partir de ferramentas expostas na sessão em 2026-11-17, com notas de configuração histórica. Estados verificados apenas para GitHub, SentinelX e Remote Desktop Commander.
- Sem chaves, tokens, IPs, identificadores do computador, emails ou dados de repositórios privados.

## Segurança e atualização
**Nunca** inserir credenciais ou infraestrutura sensível no código de GitHub Pages. Para acesso privado efetivo, configurar autenticação à frente do site, por exemplo Cloudflare Access, com utilizadores autorizados e regras de sessão, ou servir o mapa a partir de um backend protegido. O PIN de 4 dígitos não é adequado para segurança.

O catálogo fica congelado na data indicada e **não mostra saúde em tempo real**. Atualizar a página após novas verificações, ajustando o campo `asOf` e as notas de estado. As ramificações de PC/IA local baseiam-se em histórico reportado e precisam de novo teste.

## Sem impacto
Adicionada apenas a pasta `site/mapa/`; a homepage e os outros projetos não foram alterados.
