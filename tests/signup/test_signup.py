from playwright.sync_api import expect
import pytest
import time

@pytest.mark.login
def test_ct01_access_login_page(home_page, login_page):
    home_page.access_login_page()
    login_page.enter_signup_name_and_email()
    
@pytest.mark.sign_up
def test_ct02_signup_new_user(home_page, login_page, base_page):
    home_page.access_login_page()
    login_page.enter_signup_name_and_email("Fake User", "fakeUser@example.com")
    base_page.find_text_in_page("Enter account information")

@pytest.mark.sign_up
def test_ct03_assert_required_fields_exist(home_page, login_page, signup_page):
    home_page.access_login_page()
    login_page.enter_signup_name_and_email("Fake User", "fakeUser@example.com")
    
    required_fields = [
                            "Name", "Email", "Password", 
                            "First name", "Last name", 
                            "Address", "Country", "State", 
                            "City", "Zipcode", "Mobile Number"
                        ]
    
    for field in required_fields:
        expect(signup_page.required_field_name(field)).to_be_visible()
    
@pytest.mark.sign_up
def test_ct04_assert_create_account_button_exists(home_page, login_page, base_page):
    home_page.access_login_page()
    login_page.enter_signup_name_and_email("Fake User", "fakeUser@example.com")
    base_page.visualize_button("Create Account")

