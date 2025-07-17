from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "#tbodyid tr .success td:nth-child(2)")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, ".btn-success")
    TOTAL_PRICE = (By.ID, "totalp")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demoblaze.com/cart.html")

    def get_products_in_cart(self):
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_IN_CART))
        products = self.driver.find_elements(*self.PRODUCT_IN_CART)
        return [product.text for product in products]

    def click_place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)

    def get_total_price(self):
        return self.find_element(self.TOTAL_PRICE).text


