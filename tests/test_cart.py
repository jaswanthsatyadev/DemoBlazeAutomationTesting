import pytest
import time
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_teardown")
class TestCart:

    def test_add_item_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.click_product("Samsung galaxy s6")
        product_page = ProductPage(self.driver)
        alert_text = product_page.add_product_to_cart()
        print(f"Alert text: {alert_text}")
        assert "Product added" in alert_text
        home_page.click_element(home_page.CART_LINK)
        cart_page = CartPage(self.driver)
        time.sleep(2)
        cart_page.click_place_order()


