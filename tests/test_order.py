import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

@pytest.mark.usefixtures("setup_teardown")
class TestOrder:
    def test_place_order(self):
        home_page = HomePage(self.driver)
        home_page.click_product("Samsung galaxy s6")
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()
        home_page.click_element(home_page.CART_LINK)
        cart_page = CartPage(self.driver)
        cart_page.click_place_order()
        order_page = OrderPage(self.driver)
        order_page.fill_order_form("Test Name", "Test Country", "Test City", "1234567890123456", "10", "2025")
        order_page.click_purchase()
        assert "Thank you for your purchase!" in order_page.get_purchase_confirmation_message()
        order_page.click_ok_on_confirmation()


