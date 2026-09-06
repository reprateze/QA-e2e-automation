import pytest

pytestmark = pytest.mark.ui

class TestPayment:

    def test_realizar_pagamento_com_sucesso(self, payment_page):
        payment_page.preencher_dados_cartao(
        nome="Renan Teste", 
        numero="1234567891011121", 
        cvc="123", 
        mes="12", 
        ano="2030"
    )
        payment_page.confirmar_pagamento()

        assert payment_page.pagina_visivel("/payment_done/")
        assert payment_page.pedido_concluido_visivel()


    @pytest.mark.parametrize("nome, numero, cvc, mes, ano", [
    ("", "1234567891011121", "123", "12", "2030"),
    ("Renan Teste", "", "123", "12", "2030"),     
    ("Renan Teste", "1234567891011121", "", "12", "2030"), 
])
    def test_pagamento_dados_invalidos(self, payment_page, nome, numero, cvc, mes, ano):
        payment_page.preencher_dados_cartao(
        nome = nome,
        numero=numero,
        cvc=cvc,
        mes=mes,
        ano=ano
    )
        payment_page.confirmar_pagamento()

        assert not payment_page.pagina_visivel("/payment_done/")