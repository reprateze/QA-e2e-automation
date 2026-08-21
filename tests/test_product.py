import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

class TestProduct():

    def test_pagina_visivel(self, products_page):
        assert products_page.pagina_visivel()

    def test_adicionar_produto_ao_carrinho(self, products_page):
        products_page.adicionar_produto_ao_carrinho("Blue Top")
        assert products_page.produto_adicionado_sucesso()
