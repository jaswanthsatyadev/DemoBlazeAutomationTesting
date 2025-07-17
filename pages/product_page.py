from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-success")
    PRODUCT_NAME = (By.CLASS_NAME, "name")
    PRODUCT_PRICE = (By.CLASS_NAME, "price-container")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        return self.find_element(self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find_element(self.PRODUCT_PRICE).text

    def add_product_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert text from product page: {alert_text}")
            alert.accept()
            return alert_text
        except Exception as e:
            print(f"An exception occurred: {e}")
            return ""


