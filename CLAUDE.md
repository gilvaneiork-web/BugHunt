# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projeto

Laboratório didático (Unidade V) em Python puro, sem dependências externas. O objetivo **não** é corrigir rápido, e sim demonstrar um processo verificável: compreender a base → investigar o sintoma → formular hipóteses → corrigir em pequeno escopo → criar teste de regressão → revisar o diff. Mantenha as mudanças mínimas e rastreáveis a esse fluxo.

## Comandos

Executar sempre a partir da raiz do repositório (os testes importam `src.catalogo` como pacote):

```powershell
# Todos os testes
python -m unittest discover -s tests -v

# Um único teste
python -m unittest tests.test_catalogo.TestCatalogo.test_buscar_categoria_administrativo -v
```

Não há build nem linter configurados.

## Arquitetura

- `src/catalogo.py` contém tudo: os dados em memória (`SERVICOS`, lista de dicts com `id`, `nome`, `categoria`, `ativo`) e as funções de consulta (`listar_ativos`, `buscar_por_categoria`). Não há persistência.
- `tests/test_catalogo.py` usa `unittest` e testa diretamente contra `SERVICOS`; mudar os dados altera as contagens esperadas nos testes.
- `docs/regras.md` é a fonte de verdade do comportamento esperado. Qualquer mudança em `catalogo.py` deve ser checada contra elas.

## Regras de negócio que restringem correções (docs/regras.md)

- **RN01 / RN05:** serviços inativos permanecem em `SERVICOS` para preservar histórico. Nunca "corrija" uma consulta removendo ou alterando dados — o filtro é que deve excluí-los.
- **RN02 / RN03:** `listar_ativos()` e consultas por categoria retornam somente serviços ativos.
- **RN04:** a categoria é comparada de forma exata (sem normalizar caixa ou acentos) nesta versão.
