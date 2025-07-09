from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    CONTACT_LINK = (By.LINK_TEXT, "Contact")
    ABOUT_US_LINK = (By.LINK_TEXT, "About us")
    CART_LINK = (By.ID, "cartur")
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    PRODUCT_TITLE = (By.CLASS_NAME, "card-title")
    PRODUCT_PRICE = (By.CLASS_NAME, "card-price")
    NEXT_BUTTON = (By.ID, "next2")
    PREVIOUS_BUTTON = (By.ID, "prev2")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".card-title a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demoblaze.com/")

    def click_login(self):
        self.click_element(self.LOGIN_LINK)

    def get_product_titles(self):
        products = self.driver.find_elements(*self.PRODUCT_TITLE)
        return [product.text for product in products]

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [price.text for price in prices]

    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    def click_previous(self):
        self.click_element(self.PREVIOUS_BUTTON)

    def click_product(self, product_name):
        product_link = (By.LINK_TEXT, product_name)
        self.click_element(product_link)


