# Automation Exercise - Testes Automatizados

Projeto de testes end-to-end (E2E) para o site [automationexercise.com](https://www.automationexercise.com/),
usando **Playwright + Python + pytest**, seguindo o padrão **Page Object Model (POM)**.

## Stack

- [Playwright](https://playwright.dev/python/) — automação de navegador
- [pytest](https://docs.pytest.org/) — framework de testes
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente

## Estrutura do projeto

```
Automation-tests/
├── tests/
│   ├── conftest.py          # Fixtures (browser, page, home_page, signup_page, dados_cadastro, email_unico)
│   ├── test_home.py         # Testes de navegação
│   └── test_signup.py       # Testes de cadastro (signup)
│
├── pages/                    # Page Objects
│   ├── base_page.py          # Ações genéricas (goto, fill, click, select, title)
│   ├── home_page.py          # Navegação e logout
│   └── signup_page.py        # Fluxo completo de cadastro
│
├── utils/
│   └── data_loader.py        # Carrega dados de teste de arquivos JSON
│
├── data/
│   └── cadastro.json         # Dados fixos de cadastro (nome, endereço, etc.)
│
├── reports/                  # Relatórios HTML gerados após execução
├── .env                      # Variáveis de ambiente (não versionado)
├── pytest.ini
└── requirements.txt
```

## Como rodar

### 1. Preparar o ambiente

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

pip install -r requirements.txt
playwright install
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
UI_BASE_URL=https://www.automationexercise.com
API_BASE_URL=https://reqres.in/api
```

### 3. Rodar os testes

```bash
pytest -v                # roda todos os testes
pytest -v --headed       # roda com o navegador visível
pytest -v -m ui          # roda só os testes marcados como "ui"
```

Após a execução, o relatório fica disponível em `reports/report.html`.

## Cobertura de testes atual

### Navegação (`test_home.py`)
- Navegar da home até a tela de Signup/Login

### Cadastro (`test_signup.py`)
- Cadastro com sucesso (etapa 1: nome + email)
- Cadastro completo (etapa 2: dados pessoais e endereço) até a confirmação "ACCOUNT CREATED!"
- Cadastro com campos obrigatórios vazios (parametrizado: nome vazio, email vazio, ambos vazios)
- Cadastro com email já existente (cria conta → logout → tenta recriar com o mesmo email → valida mensagem de erro)

## Boas práticas adotadas

- **Page Object Model**: cada página do sistema tem sua própria classe, com seletores e ações isoladas dos testes
- **Dados de teste externos**: dados fixos (nome, endereço, etc.) ficam em `data/cadastro.json`, não hardcoded no código
- **Email dinâmico**: a fixture `email_unico` gera um e-mail único por execução (via `uuid`), evitando conflito de "e-mail já cadastrado" ao rodar os testes repetidamente
- **Isolamento entre testes**: cada teste roda em um `context` novo do Playwright (equivalente a uma janela anônima), evitando que cookies/sessão vazem entre testes

## Próximos passos

- [ ] Login com conta cadastrada
- [ ] Validação de e-mail com formato inválido
- [ ] Fluxo de produtos e carrinho
- [ ] Organizar markers (`@pytest.mark.smoke` / `regression`)
- [ ] Testes de API (`API_BASE_URL` já configurado)
