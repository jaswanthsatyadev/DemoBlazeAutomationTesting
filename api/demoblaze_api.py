import requests
import json
from config import API_BASE_URL

class DemoblazeAPI:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()

    def login(self, username, password):
        url = f"{self.base_url}login"
        headers = {"Content-Type": "application/json"}
        payload = {"username": username, "password": password}
        response = self.session.post(url, headers=headers, data=json.dumps(payload))
        print(f"Login request to {url} with payload {payload} responded with {response.status_code} and text: {response.text}")
        return response

    def get_products(self):
        url = f"{self.base_url}entries"
        response = self.session.get(url)
        return response

    def add_to_cart(self, product_id, cookie):
        url = f"{self.base_url}addtocart"
        headers = {"Content-Type": "application/json"}
        import uuid
        payload = {
            "id": str(uuid.uuid4()), 
            "cookie": cookie, 
            "prod_id": product_id, 
            "flag": True
        }
        response = self.session.post(url, headers=headers, data=json.dumps(payload))
        print(f"Add to cart request to {url} with payload {payload} responded with {response.status_code} and text: {response.text}")
        return response

    def get_cart(self, cookie):
        url = f"{self.base_url}viewcart"
        headers = {"Content-Type": "application/json"}
        payload = {"cookie": cookie}
        response = self.session.post(url, headers=headers, data=json.dumps(payload))
        print(f"Place order request to {url} with payload {payload} responded with {response.status_code} and text: {response.text}")
        return response

    def delete_from_cart(self, product_id, cookie):
        url = f"{self.base_url}deleteitem"
        headers = {"Content-Type": "application/json"}
        payload = {"id": product_id, "cookie": cookie}
        response = self.session.post(url, headers=headers, data=json.dumps(payload))
        return response

    def place_order(self, name, country, city, credit_card, month, year):
        url = f"{self.base_url}placeorder"
        headers = {"Content-Type": "application/json"}
        payload = {
            "name": name,
            "country": country,
            "city": city,
            "card": credit_card,
            "month": month,
            "year": year
        }
        response = self.session.post(url, headers=headers, data=json.dumps(payload))
        return response


