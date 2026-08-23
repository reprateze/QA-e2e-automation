import pytest

pytestmark = pytest.mark.ui


class TestHome:

    def test_navega_para_login(self, home_page):
        home_page.ir_para_signup_login()
        assert "/login" in home_page.page.url
