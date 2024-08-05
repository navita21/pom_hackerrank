from playwright.sync_api import Page
 
class Locator:
    def __init__(self,page:Page):
        self.page = page
 
    def login_locator(self):
        return self.page.wait_for_selector('text="Log in"')
   
    def dev_login_locator(self):
        return self.page.locator('//*[@id="main"]/article/div/div/div/ul/li[2]/p[2]/a')
    
    def dev_login_page_title_locator(self):
        return self.page.locator('text="Access Account - HackerRank"')

 
    def email_locator(self):
        return self.page.get_by_label("Your username or email")
 
    def password_locator(self):
        return self.page.get_by_label("Your password")
 
    def user_login_locator(self):
        return self.page.locator('//*[@id="content"]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/form/div[3]/button')
    
    def main_page_locator(self):
        return self.page.locator('//*[@id="base-card-1-link"]/div/span')
 
 