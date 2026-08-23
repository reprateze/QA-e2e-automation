from pages.base_page import BasePage

class CartPage(BasePage):

   CART_PRODUCT_NAMES = ".cart_description h4"
   REMOVER_BUTTON = ".cart_quantity_delete"

   def get_produtos_no_carrinho(self) -> list[str]:
    return self.page.locator(self.CART_PRODUCT_NAMES).all_text_contents()
    
   def remover_todos_produtos(self):
        while self.page.locator(self.REMOVER_BUTTON).count() > 0:
            quantidade_antes = self.page.locator(self.REMOVER_BUTTON).count()
            self.page.locator(self.REMOVER_BUTTON).first.click()
            self.page.wait_for_function(
            f"document.querySelectorAll('{self.REMOVER_BUTTON}').length < {quantidade_antes}"
        )

        