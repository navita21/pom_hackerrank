import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.login_page import LoginPage

 
@pytest.fixture(scope="class")
def setup_and_teardown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.hackerrank.com/")
        yield page
        browser.close()

@pytest.fixture(scope="class")
def initial(setup_and_teardown):
    page = setup_and_teardown
    main_page = MainPage(page)
    login_page = LoginPage(page)
    return page, main_page, login_page