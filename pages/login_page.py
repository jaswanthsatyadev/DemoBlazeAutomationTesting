from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal .btn-primary")
    WELCOME_USER = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_welcome_message(self):
        return self.find_element(self.WELCOME_USER).text


