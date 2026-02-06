from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_name_input = self.page.get_by_role("textbox", name="Name")
        self.signup_email_input = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        
    def enter_signup_name_and_email(self, name, email):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_email_input.press("Enter")
