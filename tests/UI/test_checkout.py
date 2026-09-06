import pytest

pytestmark = pytest.mark.ui

class TestCheckout:

    def test_pagina_visivel(self, checkout_page):
        assert checkout_page.pagina_visivel("/checkout")

    def test_endereco_checkout(self, checkout_page, dados_cadastro):
       
        textos_lista = checkout_page.get_dados_endereco()
        texto_completo = " ".join(textos_lista)

       
        assert dados_cadastro["cidade"] in texto_completo
        assert dados_cadastro["cep"] in texto_completo
        assert dados_cadastro["telefone"] in texto_completo

    def test_totais_batem_no_checkout(self, checkout_page):
        assert checkout_page.totais_batem()

    def test_add_comentario(self, checkout_page, dados_cadastro):
        texto_da_mensagem = dados_cadastro["mensagem_pedido"] 
        
        checkout_page.add_comentario(texto_da_mensagem)


    def test_finalizar_checkout(self, checkout_page):
      
        checkout_page.finalizar_checkout()

    
        assert checkout_page.pagina_visivel("/payment")
 

    