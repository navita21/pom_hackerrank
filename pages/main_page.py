from pages.locators import Locator
import time
 
class MainPage:
    def __init__(self, page):
        self.page = page
 
    def go_to_login(self):
        # Wait for and click the "Log in" button
        login_button=Locator.login_locator(self)
        login_button.click()
        if Locator.login_locator(self).is_visible():
            return True
        return False
 
    def click_developer_login(self):
        # Wait for and click the "Developer Login" link
        if Locator.dev_login_locator(self).is_visible() :
            dev_login=Locator.dev_login_locator(self)
            dev_login.click()
        
            print("developer login visible")
            return True
        return False
        
