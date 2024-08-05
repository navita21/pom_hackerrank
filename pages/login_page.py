from pages.locators import Locator
from playwright.sync_api import Page
import os
from dotenv import load_dotenv

load_dotenv()      # Load environment variables from .env file

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
 
    def fill_credentials(self, email: str = None, password: str = None):
        # Fill in the email and password fields
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        # Locate and fill in the email and password fields
        Locator.email_locator(self).fill(email)
        Locator.password_locator(self).fill(password)
        if Locator.user_login_locator(self):
            return True
        return False
        
 
    def submit_login(self):
        # Click the login button
        if Locator.user_login_locator(self).is_visible():
            u_locator=Locator.user_login_locator(self)
            u_locator.click()
            self.page.wait_for_load_state('networkidle')
            return True
        return False
   
   
 