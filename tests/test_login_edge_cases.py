import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

@pytest.mark.usefixtures("setup_teardown")
class TestLoginEdgeCases:
    

        
    def test_login_with_empty_username(self):
        """Test login with empty username but valid password"""
        home_page = HomePage(self.driver)
        home_page.click_login()
        login_page = LoginPage(self.driver)
        login_page.login("", PASSWORD)
        
    def test_login_with_empty_password(self):
        """Test login with valid username but empty password"""
        home_page = HomePage(self.driver)
        home_page.click_login()
        login_page = LoginPage(self.driver)
        login_page.login(USERNAME, "")
        
    def test_login_with_invalid_credentials(self):
        """Test login with completely invalid credentials"""
        home_page = HomePage(self.driver)
        home_page.click_login()
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "invalid_pass")
        

