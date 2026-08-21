
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = "[data-qa='login-email']"
    PASSWORD_INPUT = "[data-qa='login-password']"
    LOGIN_BUTTON  = "[data-qa='login-button']"

    def login(self, email: str, senha: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, senha)
        self.click(self.LOGIN_BUTTON)

    
