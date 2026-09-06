from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage


class homePage(BasePage):

    LOGIN_BUTTON = "Signup / Login"
    LOGOUT_LINK_TEXT = "Logout"
    PRODUCTS_LINK_TEXT = "Products"
    CART_LINK = "Cart"

    def ir_para_signup_login(self):
        self.page.get_by_role("link", name=self.LOGIN_BUTTON).click()

    def logout(self):
        self.page.get_by_role("link", name=self.LOGOUT_LINK_TEXT).click()

    def esta_logado(self) -> bool:
   
        link_logout = self.page.get_by_role("link", name=self.LOGOUT_LINK_TEXT)
    
        try:
            link_logout.wait_for(state="visible", timeout=10000)
            return True
        
        except PlaywrightTimeoutError:
            return False

    def ir_para_produtos(self):
        self.page.get_by_role("link", name=self.PRODUCTS_LINK_TEXT).click()

    def ir_para_cart(self):
        self.page.get_by_role("link", name=self.CART_LINK).click()