# Automation Exercise - Testes Automatizados

Projeto de testes automatizados (UI + API) para o site [automationexercise.com](https://www.automationexercise.com/),
usando **Playwright + Python + pytest** para UI (padrão **Page Object Model**) e **requests + Pydantic** para API
(validação de contrato/schema das respostas).

## Contribuições e uso de IA

Durante o desenvolvimento deste projeto, ferramentas de Inteligência Artificial foram utilizadas como apoio para análise, investigação e resolução de bugs, além de auxiliar na revisão e melhoria do código.

A IA foi utilizada como ferramenta de suporte, enquanto a implementação, validação e decisões finais sobre o código foram realizadas pelo autor.

Um dos exemplos foi a utilização de IA para auxiliar na investigação e resolução de um bug encontrado durante o desenvolvimento dos testes automatizados.

## Stack

- [Playwright](https://playwright.dev/python/) — automação de navegador
- [pytest](https://docs.pytest.org/) — framework de testes
- [requests](https://requests.readthedocs.io/) — cliente HTTP para os testes de API
- [Pydantic](https://docs.pydantic.dev/) — validação de schema/contrato das respostas de API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente
- [ruff](https://docs.astral.sh/ruff/) — lint

## Estrutura do projeto

```
QA-e2e-automation/
├── pages/                          # Page Objects (UI)
│   ├── base_page.py                # Ações genéricas (goto, fill, click, select, title)
│   ├── home_page.py
│   ├── signup_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── payment_page.py
│
├── tests/
│   ├── UI/                         # Testes de interface (Playwright)
│   │   ├── conftest.py             # Fixtures (browser, page, home_page, login_page, cart_page, ...)
│   │   ├── test_home.py
│   │   ├── test_signup.py
│   │   ├── test_login.py
│   │   ├── test_product.py
│   │   ├── test_cart.py
│   │   ├── test_checkout.py
│   │   └── test_payment.py
│   │
│   └── API/                        # Testes de API (requests)
│       ├── conftest.py             # Fixtures (users_api, products_api, brands_api, ...)
│       ├── clients/                # Um client por recurso da API (createAccount, productsList, ...)
│       ├── payloads/                # Geração de payloads de teste
│       ├── schemas/                 # Contratos das respostas, validados com Pydantic
│       └── test_cases/
│
├── utils/
│   ├── config.py                    # Variáveis de ambiente e configuração
│   └── data_loader.py               # Carrega dados de teste de arquivos JSON
│
├── data/
│   └── cadastro.json                 # Dados fixos de cadastro (nome, endereço, etc.)
│
├── reports/                          # Relatórios HTML gerados após execução
├── .env                               # Variáveis de ambiente (não versionado)
├── pyproject.toml                    # Configuração do ruff
├── pytest.ini
└── requirements.txt
```

## Como rodar

### 1. Preparar o ambiente

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

pip install -r requirements.txt
playwright install
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
UI_BASE_URL=https://www.automationexercise.com
API_BASE_URL=https://automationexercise.com/api
FIXED_USER_EMAIL=<conta fixa usada nos testes de login/carrinho>
FIXED_USER_PASSWORD=<senha dessa conta>
```

### 3. Rodar os testes

```bash
pytest -v                # roda todos os testes
pytest -v --headed       # roda com o navegador visível
pytest -v -m ui          # só testes de UI
pytest -v -m api         # só testes de API
pytest -v -m smoke       # subconjunto rápido de testes críticos (UI + API)
pytest -v -m regression  # cobertura ampla, casos de borda e negativos
```

Após a execução, o relatório fica disponível em `reports/report.html`.

## Cobertura de testes atual

### UI (`tests/UI/`)
- **Navegação** (`test_home.py`): navegar da home até Signup/Login
- **Cadastro** (`test_signup.py`): sucesso, campos obrigatórios vazios (parametrizado), e-mail já existente
- **Login** (`test_login.py`): login válido, login inválido (parametrizado)
- **Produtos** (`test_product.py`): detalhes do produto, adicionar ao carrinho, review, busca
- **Carrinho** (`test_cart.py`): totais, remoção de produtos
- **Checkout** (`test_checkout.py`): fluxo de finalização de pedido
- **Pagamento** (`test_payment.py`): confirmação de pagamento (parametrizado)

### API (`tests/API/`)
- **Brands** (`test_brands_api.py`): listagem de marcas, método não suportado
- **Products** (`test_products_api.py`): listagem, busca (parametrizado com casos de borda), parâmetro ausente
- **Users** (`test_users_api.py`): criar conta, login válido/inválido, atualizar conta, buscar por e-mail, deletar conta
- Todas as respostas de API são validadas contra um **schema Pydantic** (`tests/API/schemas/`), garantindo que a API não mude formato/tipos sem que o teste perceba

## Boas práticas adotadas

- **Page Object Model**: cada página do sistema tem sua própria classe, com seletores e ações isoladas dos testes
- **Clients de API por recurso**: cada endpoint tem um método dedicado em `tests/API/clients/`, isolando os testes de detalhes de request
- **Validação de contrato (schema)**: além de checar valores específicos, os testes de API validam o **formato** da resposta inteira com Pydantic — pega mudanças de tipo/campo que passariam despercebidas em um `assert` pontual
- **Dados de teste externos**: dados fixos (nome, endereço, etc.) ficam em `data/cadastro.json`, não hardcoded no código
- **Email dinâmico**: fixtures geram e-mail único por execução (via `uuid`/timestamp), evitando conflito de "e-mail já cadastrado"
- **Isolamento entre testes**: cada teste de UI roda em um `context` novo do Playwright (equivalente a uma janela anônima)
- **Markers organizados**: `smoke` (fluxo crítico, execução rápida) e `regression` (cobertura ampla, edge cases e negativos) em UI e API

## Próximos passos

- [ ] CI (GitHub Actions) rodando lint + testes de API a cada push/PR
- [ ] `.env.example` documentando as variáveis esperadas
- [ ] Evidência visual em falhas de UI (tracing/screenshot do Playwright)
- [ ] Ampliar schemas de API para os cenários de erro de `products`/`brands`
