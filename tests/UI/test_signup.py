import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

class TestSignup:


    def test_registro_com_sucesso(self, signup_page, email_unico, dados_cadastro):
        signup_page.registro(dados_cadastro["nome"], email_unico)
        assert signup_page.esta_na_segunda_etapa()

    def test_completar_formulario_cadastro(self, signup_page, dados_cadastro, email_unico):
        signup_page.registro(dados_cadastro["nome"], email_unico)
        assert signup_page.esta_na_segunda_etapa()

        signup_page.preencher_cadastro_completo(dados_cadastro)

        assert "/account_created" in signup_page.page.url
        assert signup_page.cadastro_realizado_com_sucesso()

    # usar_email e um sinalizador para indicar ao teste se usar o email ou nao, foi a unica forma que achei para conseguir testar pois
    # como o parametrize rodam antes da fixture - ai precisei usar o email fixo quer foi gerado no teste da funcao abaixo
    @pytest.mark.parametrize("nome, usar_email", [
        ("", True),           
        ("Renan Teste", False),  
        ("", False),           
        ])
    
    def test_registro_com_campos_vazios(self, signup_page, email_unico, nome, usar_email):
        email = email_unico if usar_email else ""
        signup_page.registro(nome, email)
        assert not signup_page.esta_na_segunda_etapa()

    def test_email_repetido(self, signup_page, email_unico, dados_cadastro):
        signup_page.registro(dados_cadastro["nome"], email_unico)
        assert signup_page.esta_na_segunda_etapa()

        signup_page.preencher_cadastro_completo(dados_cadastro)
        assert "/account_created" in signup_page.page.url
        assert signup_page.cadastro_realizado_com_sucesso() 

        signup_page.continuar()

        home = homePage(signup_page.page)
        home.logout()
    
        signup_page.goto("/login")
        signup_page.registro(dados_cadastro["nome"],email_unico)
        assert signup_page.email_ja_cadastrado_visivel()
        
    