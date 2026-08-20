# Esqueleto de Projeto — Playwright + Python

Este é só o **esqueleto** do projeto: pastas criadas e arquivos com comentários
explicando o que vai em cada um. Nada de código pronto — a ideia é você
implementar aos poucos enquanto aprende.

## Estrutura

```
tests/      -> os testes em si
pages/      -> Page Objects (uma classe por tela do sistema)
utils/      -> configuração (.env) e leitura de dados (JSON/YAML)
data/       -> dados de teste separados do código
reports/    -> relatórios gerados (vazio por enquanto)
```

## Sugestão de ordem para ir implementando

1. **utils/config.py** — leia a `BASE_URL` do `.env`
2. **pages/base_page.py** — implemente `navigate`, `click`, `fill`
3. **tests/conftest.py** — crie as fixtures `browser` e `page`
4. **pages/exemplo_page.py** — crie sua primeira Page Object real (renomeie o arquivo)
5. **tests/test_exemplo.py** — escreva seu primeiro teste usando a Page Object
6. Só depois: **utils/data_loader.py** + arquivo em `data/` — para tirar dados fixos do teste

## Setup do ambiente

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
cp .env.example .env
```

## Rodando os testes (depois de implementados)

```bash
pytest
pytest --headed     # ver o navegador rodando
```
