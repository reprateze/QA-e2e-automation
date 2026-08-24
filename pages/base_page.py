from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class BasePage:

    def __init__(self, page):
        self.page = page

    def goto(self, path: str = "/"):
        self.page.goto(path)

    def title(self) -> str:
        return self.page.title()

    def fill(self, selector: str, texto: str):
        self.page.fill(selector, texto)

    def select(self, seletor: str, texto: str):
        self.page.select_option(seletor, texto)

    def click(self, seletor: str):
        self.page.click(seletor)

    def pagina_visivel(self, padrao_url: str) -> bool:
        try:
            self.page.wait_for_url(f"**{padrao_url}**", timeout=5000)
            return True
        except PlaywrightTimeoutError:
            return False
        