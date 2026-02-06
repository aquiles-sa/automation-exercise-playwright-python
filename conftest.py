from playwright.sync_api import sync_playwright

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.base_page import BasePage

import pytest

base_url = "https://automationexercise.com"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def base_page(page):
    return BasePage(page)