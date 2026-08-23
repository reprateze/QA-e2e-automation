import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

class TestProduct():

    def test_pagina_visivel(self, products_page):
        assert products_page.pagina_visivel()

    def test_adicionar_produto_ao_carrinho(self, products_page):
        products_page.adicionar_produto_ao_carrinho("Blue Top")
        assert products_page.produto_adicionado_sucesso()

    def test_filtro_de_pesquisa(self, products_page):
        products_page.pesquisar("Blue Top")

        produtos = products_page.get_produtos_nome()
        print(produtos)  # temporário, só pra debug

        assert produtos
        assert all("Blue Top" in produto for produto in produtos)

    def test_acessar_detalhes_produto(self, products_page):
        assert products_page.pagina_visivel()

        products_page.acessar_detalhes_produto(1)

        assert products_page.pagina_detalhes_visivel()


    @pytest.mark.parametrize("quantidade", [1, 2, 10, 50, 100])
    def test_quantidades_validas(self, product_details_page, quantidade):
        product_details_page.altera_quantidade_produtos(quantidade)
        assert product_details_page.obter_quantidade() == str(quantidade)

    def test_quantidade_exorbitante_impede_adicionar_ao_carrinho(self, product_details_page):
        quantidade_exorbitante = 10 ** 20
        product_details_page.altera_quantidade_produtos(quantidade_exorbitante)
        product_details_page.pagina_detalhes_adicionar_produto()
        assert not product_details_page.produto_adicionado_sucesso()

    def test_realizar_review(self, product_details_page):
        product_details_page.preencher_review("Renan Teste", "renan@teste.com", "Ótimo produto!")
        assert product_details_page.review_enviada_com_sucesso()


    @pytest.mark.parametrize("nome, email, texto", [
        ("","email@teste.com", "texto"),
        ("Nome", "", "texto"),
        ("Nome", "email@teste.com", "")
    ])
    def test_review_vazio(self, product_details_page, nome, email, texto):
        product_details_page.preencher_review(nome, email, texto)
        assert not product_details_page.produto_adicionado_sucesso()