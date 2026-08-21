import os
import uuid

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from utils.data_loader import carregar_json
from pages.home_page import HomePage
from pages.signup_page import SignupPage


load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL")
API_BASE_URL = os.getenv("API_BASE_URL")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(base_url=UI_BASE_URL)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def home_page(page):
    home = HomePage(page)
    home.goto("/")
    return home

@pytest.fixture
def signup_page(page):
    signup = SignupPage(page)
    signup.goto("/login")
    return signup

@pytest.fixture
def dados_cadastro():
    return carregar_json("cadastro.json")

@pytest.fixture
def email_unico():
    email = f"renan.teste.{uuid.uuid4().hex[:8]}@example.com"
    return email
    

