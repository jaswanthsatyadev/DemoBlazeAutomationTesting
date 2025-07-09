from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    # Locators
    CONTACT_EMAIL_FIELD = (By.ID, "recipient-email")
    CONTACT_NAME_FIELD = (By.ID, "recipient-name")
    MESSAGE_FIELD = (By.ID, "message-text")
    SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, "#exampleModal .btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_contact_form(self, email, name, message):
        self.enter_text(self.CONTACT_EMAIL_FIELD, email)
        self.enter_text(self.CONTACT_NAME_FIELD, name)
        self.enter_text(self.MESSAGE_FIELD, message)

    def click_send_message(self, email, name, message):
        self.fill_contact_form(email, name, message)
        self.click_element(self.SEND_MESSAGE_BUTTON)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text


