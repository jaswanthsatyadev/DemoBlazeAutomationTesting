import pytest
from api.demoblaze_api import DemoblazeAPI
from config import USERNAME, PASSWORD

class TestAPI:
    def test_api_login_with_valid_credentials(self):
        api = DemoblazeAPI()
        response = api.login(USERNAME, PASSWORD)
        assert response.status_code == 200
        assert "Auth_token: " in response.text or "token" in response.text

    def test_api_login_with_invalid_credentials(self):
        api = DemoblazeAPI()
        response = api.login("invalid_user", "invalid_password")
        assert response.status_code == 200
        assert "Wrong password." in response.text

    def test_add_item_to_cart_api(self):
        api = DemoblazeAPI()
        login_response = api.login(USERNAME, PASSWORD)
        assert login_response.status_code == 200
        auth_token = login_response.text.replace("Auth_token: ", "").strip()
        assert auth_token is not None

        # Assuming product ID for Samsung galaxy s6 is 1
        product_id = 1
        add_to_cart_response = api.add_to_cart(product_id, auth_token)
        assert add_to_cart_response.status_code == 200
        assert "Product added." in add_to_cart_response.text

    def test_place_order_api(self):
        api = DemoblazeAPI()
        login_response = api.login(USERNAME, PASSWORD)
        assert login_response.status_code == 200
        auth_token = login_response.text.replace("Auth_token: ", "").strip()
        assert auth_token is not None

        # Add item to cart first
        product_id = 1
        add_to_cart_response = api.add_to_cart(product_id, auth_token)
        assert add_to_cart_response.status_code == 200

        # Place order
        order_response = api.place_order("API Test", "USA", "New York", "1234567890123456", "12", "2025")
        assert order_response.status_code == 200
        assert "Thank you for your purchase!" in order_response.text


