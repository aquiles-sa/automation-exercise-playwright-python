from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_signUp_acess_btn = self.page.get_by_role("link", name=" Signup / Login")
        
    def access_login_page(self):
        self.login_signUp_acess_btn.click()