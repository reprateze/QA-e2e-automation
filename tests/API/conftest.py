import pytest

from tests.API.clients.products_api import ProductsAPI
from tests.API.clients.brands_api import BrandsAPI


@pytest.fixture
def products_api():
    return ProductsAPI()

@pytest.fixture
def brands_api():
    return BrandsAPI()