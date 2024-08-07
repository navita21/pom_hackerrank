from pages.locators import Locator
from playwright.sync_api import Page
import os, time
from dotenv import load_dotenv

load_dotenv()      # Load environment variables from .env file

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
 
    def fill_credentials(self, email: str = None, password: str = None):
        try:
            # Fill in the email and password fields
            #email = os.getenv('EMAIL')
            #password = os.getenv('PASSWORD')
            # Locate and fill in the email and password fields
            Locator.email_locator(self).fill(email)
            Locator.password_locator(self).fill(password)
            if Locator.user_login_locator(self):
                return True
            return False
        except Exception as e:
            print(f"An error occurred while filling credentials: {e}")
            return False
 
   
    def submit_login(self):
        try:
            # Click the login button
            u_locator = Locator.user_login_locator(self)
            if u_locator.is_visible():
                u_locator.click()
                self.page.wait_for_load_state('networkidle')
                if Locator.main_page_locator(self).is_visible():
                    return True
            return False
        except Exception:
            return False
