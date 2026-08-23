import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

class TestCart():

   def test_produto_aparece_no_carrinho(self, cart_page):
    produtos = cart_page.get_produtos_no_carrinho()
    assert "Blue Top" in produtos