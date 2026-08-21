import pytest

pytestmark = pytest.mark.ui

class TestSignup:


    def test_registro_com_sucesso(self, signup_page):
        signup_page.registro("Renan Teste", "renan.teste@example.com")
        assert signup_page.esta_na_segunda_etapa()

    def test_completar_formulario_cadastro(self, signup_page, dados_cadastro):
        signup_page.registro("Renan Teste", "renan.teste2@example.com")
        assert signup_page.esta_na_segunda_etapa()

        signup_page.preencher_cadastro_completo(dados_cadastro)

        assert "/account_created" in signup_page.page.url
        assert signup_page.cadastro_realizado_com_sucesso()
        
    