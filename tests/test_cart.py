import pytest
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
        assert "Product added." in alert_text
        home_page.click_element(home_page.CART_LINK)
        cart_page = CartPage(self.driver)
        products_in_cart = cart_page.get_products_in_cart()
        assert "Samsung galaxy s6" in products_in_cart


