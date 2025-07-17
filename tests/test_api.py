import pytest
from api.demoblaze_api import DemoblazeAPI
from config import USERNAME, PASSWORD

class TestAPI:
    def test_api_login_with_valid_credentials(self):
        print("\n--- Running test_api_login_with_valid_credentials ---")
        api = DemoblazeAPI()
        response = api.login(USERNAME, PASSWORD)
        print(f"Login response text: {response.text}")
        assert response.status_code == 200
        assert "Auth_token" in response.text

    def test_api_login_with_invalid_credentials(self):
        api = DemoblazeAPI()
        response = api.login("invalid_user", "invalid_password")
        assert response.status_code == 200
        assert "Wrong password." in response.text

    def test_add_item_to_cart_api(self):
        print("\n--- Running test_add_item_to_cart_api ---")
        api = DemoblazeAPI()
        login_response = api.login(USERNAME, PASSWORD)
        assert login_response.status_code == 200
        auth_token = None
        if "Auth_token" in login_response.text:
            auth_token = login_response.json().get('Auth_token')
        print(f"Extracted auth_token: {auth_token}")
        add_to_cart_response = api.add_to_cart(1, auth_token)
        assert add_to_cart_response.status_code == 200
        assert "Product added." in add_to_cart_response.text

    def test_place_order_api(self):
        print("\n--- Running test_place_order_api ---")
        api = DemoblazeAPI()
        login_response = api.login(USERNAME, PASSWORD)
        assert login_response.status_code == 200
        auth_token = None
        if "Auth_token" in login_response.text:
            auth_token = login_response.json().get('Auth_token')
        print(f"Extracted auth_token for order: {auth_token}")
        api.add_to_cart(1, auth_token)
        order_response = api.place_order("API Test", "USA", "New York", "1234567890123456", "12", "2025")
        assert order_response.status_code == 200
        assert "Thank you for your purchase!" in order_response.text


