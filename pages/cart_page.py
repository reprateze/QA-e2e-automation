from pages.base_page import BasePage

class CartPage(BasePage):

    CART_PRODUCT_NAMES = ".cart_description h4"
    REMOVER_BUTTON = ".cart_quantity_delete"
    CARRINHO_VAZIO = "#empty_cart"
    CART_PRECO = ".cart_price"
    CART_QUANTIDADE = ".cart_quantity button"
    CART_TOTAL = ".cart_total"

    def get_produtos_no_carrinho(self) -> list[str]:
        return self.page.locator(self.CART_PRODUCT_NAMES).all_text_contents()
    
    def remover_todos_produtos(self):
        while self.page.locator(self.REMOVER_BUTTON).count() > 0:
            quantidade_antes = self.page.locator(self.REMOVER_BUTTON).count()
            self.page.locator(self.REMOVER_BUTTON).first.click()
            self.page.wait_for_function(
                f"document.querySelectorAll('{self.REMOVER_BUTTON}').length < {quantidade_antes}"
            )

    def get_carrinho_vazio(self) -> bool:
        return self.page.locator(self.CARRINHO_VAZIO).is_visible()

    def _extrair_valor(self, texto: str) -> int:
        numero = texto.replace("Rs. ", "")
        return int(numero)

    def totais_batem(self) -> bool:
        linhas = self.page.locator("#cart_info_table tbody tr")
    
        for i in range(linhas.count()):
            linha = linhas.nth(i)
        
            preco_texto = linha.locator(self.CART_PRECO).inner_text()
            quantidade_texto = linha.locator(self.CART_QUANTIDADE).inner_text()
            total_texto = linha.locator(self.CART_TOTAL).inner_text()

            preco = self._extrair_valor(preco_texto)
            quantidade = int(quantidade_texto)
            total_exibido = self._extrair_valor(total_texto)

            if preco * quantidade != total_exibido:
                return False


        return True