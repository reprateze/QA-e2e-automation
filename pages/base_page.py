class BasePage:

    def __init__(self, page):
        self.page = page

    def goto(self, path: str = "/"):
        self.page.goto(path)

    def title(self) -> str:
        return self.page.title()
    
        