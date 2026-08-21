# pages/signup_page.py
from pages.base_page import BasePage


class SignupPage(BasePage):
    USERNAME_INPUT = "[data-qa='signup-name']"
    EMAIL_INPUT = "[data-qa='signup-email']"
    BUTTON_INPUT = "[data-qa='signup-button']"
    GENDER_BUTTON = "#id_gender1"
    PASSWORD_INPUT = "#password"
    DAY_SELECTOR = "#days"
    MONTH_SELECTOR = "#months"
    YEAR_SELECTOR = "#years"
    NEWSLETTER_INPUT = "#newsletter"
    PARTNERS_INPUT = "#optin"
    FIRSTNAME_INPUT = "#first_name"
    LASTNAME_INPUT = "#last_name"
    ADRESS_INPUT = "#address1"
    COUNTRY_SELECTOR = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIP_INPUT = "#zipcode"
    MOBILE_INPUT = "#mobile_number"
    CREATE_ACCOUNT_BUTTON = "[data-qa='create-account']"

    def registro(self, username: str, email: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.BUTTON_INPUT)

    def esta_na_segunda_etapa(self) -> bool:
        return self.page.get_by_text("ENTER ACCOUNT INFORMATION").is_visible()

    def preencher_cadastro_completo(self, dados: dict):
        self.click(self.GENDER_BUTTON)
        self.fill(self.PASSWORD_INPUT, dados["senha"])
        self.select(self.DAY_SELECTOR, dados["dia_nascimento"])
        self.select(self.MONTH_SELECTOR, dados["mes_nascimento"])
        self.select(self.YEAR_SELECTOR, dados["ano_nascimento"])
        self.click(self.NEWSLETTER_INPUT)
        self.click(self.PARTNERS_INPUT)
        self.fill(self.FIRSTNAME_INPUT, dados["nome"])
        self.fill(self.LASTNAME_INPUT, dados["sobrenome"])
        self.fill(self.ADRESS_INPUT, dados["endereco"])
        self.select(self.COUNTRY_SELECTOR, dados["pais"])
        self.fill(self.STATE_INPUT, dados["estado"])
        self.fill(self.CITY_INPUT, dados["cidade"])
        self.fill(self.ZIP_INPUT, dados["cep"])
        self.fill(self.MOBILE_INPUT, dados["telefone"])
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def cadastro_realizado_com_sucesso(self) -> bool:
        return self.page.get_by_text("ACCOUNT CREATED").is_visible()
