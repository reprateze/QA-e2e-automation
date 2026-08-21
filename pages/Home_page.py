from pages.base_page import BasePage

class homePage(BasePage):

    LOGIN_BUTTON = "Signup / Login"
    LOGOUT_LINK_TEXT = "Logout"
    PRODUCTS_LINK_TEXT = "Products"

    def ir_para_signup_login(self):
        self.page.get_by_role("link", name=self.LOGIN_BUTTON).click()

    def logout(self):
        self.page.get_by_role("link", name=self.LOGOUT_LINK_TEXT).click()

    def esta_logado(self) -> bool:
        return self.page.get_by_role("link", name=self.LOGOUT_LINK_TEXT).is_visible()

    def ir_para_produtos(self):
        self.page.get_by_role("link", name=self.PRODUCTS_LINK_TEXT).click()