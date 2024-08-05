import pytest
from playwright.sync_api import sync_playwright, Page
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLogin:
    # Test navigating to the login page from the main page
    def test_login(self,initial):
        page, main_page, login_page = initial  
        assert main_page.go_to_login(), "Failed to navigate to the login page"

    # Test clicking on the developer login link
    def test_developer_login(self,initial): 
        page, main_page, login_page= initial  
        assert main_page.click_developer_login(), "Failed to click the developer login link"

    # Test filling in the login credentials                      
    def test_fill_credential(self,initial):
        page, main_page, login_page = initial
        assert login_page.fill_credentials(), "Failed to fill in login credentials"

    # Test submitting the login form and verifying successful login   
    def test_submit_login(self, initial):
        page, main_page, login_page = initial
        assert login_page.submit_login(), "Failed to submit the login form and verify login"

   
 
 