import pytest

from tests.API.clients.products_api import ProductsAPI
from tests.API.clients.brands_api import BrandsAPI
from tests.API.payloads.users_payload import gerar_payload_usuario_teste
from tests.API.clients.users_api import UsersAPI


@pytest.fixture
def products_api():
    return ProductsAPI()

@pytest.fixture
def brands_api():
    return BrandsAPI()

@pytest.fixture
def dados_usuario_teste():
    return gerar_payload_usuario_teste()

@pytest.fixture
def users_api():
    return UsersAPI()

@pytest.fixture
def usuario_criado(users_api, dados_usuario_teste):
    users_api.criar_conta(dados_usuario_teste)
    yield dados_usuario_teste
    users_api.deletar_conta(dados_usuario_teste["email"], dados_usuario_teste["password"])

