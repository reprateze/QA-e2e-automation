from pages.base_page import BasePage

class HomePage(BasePage):

    LOGIN_BUTTON = "Signup / Login"
    LOGOUT_LINK_TEXT = "Logout"

    def ir_para_signup_login(self):
        self.page.get_by_role("link", name=self.LOGIN_BUTTON).click()

    def logout(self):
        self.page.get_by_role("link", name=self.LOGOUT_LINK_TEXT).click()