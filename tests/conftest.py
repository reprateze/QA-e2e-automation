import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.Home_page import HomePage


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

    

