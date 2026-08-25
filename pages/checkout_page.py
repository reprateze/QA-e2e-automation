from pages.base_page import BasePage

class CheckoutPage(BasePage):

    DETALHES_ENDERECO = "#address_delivery"
    PLACE_ORDER = "a.check_out"
    CAMPO_MENSAGEM = "textarea[name='message']"
    BUTTON_PAGAMENTO  = '.check_out'

    def get_dados_endereco(self) -> list [str]:
        self.page.locator(self.DETALHES_ENDERECO).first.wait_for(state="visible")
        return  self.page.locator (self.DETALHES_ENDERECO).all_text_contents()

    def add_comentario(self, mensagem: str):
        self.fill(self.CAMPO_MENSAGEM, mensagem)

    def finalizar_checkout(self):
        self.click(self.BUTTON_PAGAMENTO)