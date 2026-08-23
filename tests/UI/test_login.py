import pytest
from pages.home_page import homePage
pytestmark = pytest.mark.ui

from utils.config import FIXED_USER_EMAIL, FIXED_USER_PASSWORD

class TestLogin:
   def test_login_com_sucesso(self, login_page):
    login_page.login(FIXED_USER_EMAIL, FIXED_USER_PASSWORD)

    home = homePage(login_page.page)
    assert home.esta_logado()

    @pytest.mark.parametrize("email, senha", [
        ("", "algumasenha"),
        ("algum@email.com", ""),
        ("", ""),
    ])
    def test_login_campos_vazios(self, login_page, email, senha):
        login_page.login(email, senha)
        home = homePage(login_page.page)
        assert not home.esta_logado()