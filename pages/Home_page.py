from pages.base_page import BasePage

class HomePage(BasePage):

    LOGIN_BUTTON = "Signup / Login"

    def ir_para_signup_login(self):
        self.page.get_by_role("link", name=self.LOGIN_BUTTON).click()

    