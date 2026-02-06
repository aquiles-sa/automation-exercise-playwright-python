from playwright.sync_api import Page, expect
import re

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_info_text = self.page.get_by_text("Enter Account Information")
        self.content_info_box = self.page.locator("div").filter(has_text="Enter Account Information").nth(2)
        self.create_account_btn = self.page.get_by_role("button", name="Create Account")
        
    def required_field_name(self, field_name: str):
        return self.content_info_box.locator("label", has_text=re.compile(rf"^{field_name}\s*\*"))
