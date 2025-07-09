from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Locators
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CREDIT_CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "#orderModal .btn-primary")
    OK_BUTTON = (By.CSS_SELECTOR, ".confirm.btn.btn-lg.btn-primary")
    PURCHASE_CONFIRMATION = (By.CSS_SELECTOR, ".sweet-alert h2")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_order_form(self, name, country, city, credit_card, month, year):
        self.enter_text(self.NAME_FIELD, name)
        self.enter_text(self.COUNTRY_FIELD, country)
        self.enter_text(self.CITY_FIELD, city)
        self.enter_text(self.CREDIT_CARD_FIELD, credit_card)
        self.enter_text(self.MONTH_FIELD, month)
        self.enter_text(self.YEAR_FIELD, year)

    def click_purchase(self):
        self.click_element(self.PURCHASE_BUTTON)

    def get_purchase_confirmation_message(self):
        return self.find_element(self.PURCHASE_CONFIRMATION).text

    def click_ok_on_confirmation(self):
        self.click_element(self.OK_BUTTON)


