import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_successful_login(self):
        home_page = HomePage(self.driver)
        home_page.click_login()
        login_page = LoginPage(self.driver)
        login_page.login(USERNAME, PASSWORD)
        assert f"Welcome {USERNAME}" in login_page.get_welcome_message()


