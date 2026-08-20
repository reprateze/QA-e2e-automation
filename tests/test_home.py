import pytest

pytestmark = pytest.mark.ui


class TestHome:

    @pytest.mark.smoke
    def test_navega_para_login(home_page):
        home_page.ir_para_signup_login()
