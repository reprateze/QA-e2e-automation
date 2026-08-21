from pages.base_page import BasePage

class ProductPage(BasePage):

    def pagina_visivel(self) -> bool:
        return self.page.url.endswith("/products")
      
    def adicionar_produto_ao_carrinho(self, nome_produto: str):
        produto = self.page.locator(".productinfo").filter(has_text=nome_produto)
        produto.hover()
        produto.locator(".add-to-cart").click()

    def produto_adicionado_sucesso(self) -> bool:
        locator = self.page.get_by_text("Your product has been added to cart.")
        locator.wait_for(state="visible", timeout=5000)
        return locator.is_visible()