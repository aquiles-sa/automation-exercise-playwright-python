from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def find_text_in_page(self, target_text):
        return self.page.get_by_text(target_text)
    
    def visualize_button(self, name_btn: str):
        target_button = self.page.get_by_role("button", name=name_btn)
        expect(target_button).to_be_visible()