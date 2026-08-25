import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

class TestCart():

   def test_produto_aparece_no_carrinho(self, cart_page):
    produtos = cart_page.get_produtos_no_carrinho()
    assert "Blue Top" in produtos

   def test_carrinho_vazio(self, cart_page):
     cart_page.remover_todos_produtos()
     assert cart_page.get_carrinho_vazio()

   def test_totais_batem(self, cart_page):
      assert cart_page.totais_batem()


   