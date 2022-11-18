import requests
from pprint import pprint

SHEETY_API_ENDPOINT = "https://api.sheety.co/344bd9bc3fd8c2c0f2eef3e890bf385a/flightDeals/prices"
SHEETY_API_USERS_ENDPOINT = "https://api.sheety.co/344bd9bc3fd8c2c0f2eef3e890bf385a/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {"iataCode": city["iataCode"]}
            }

            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customers_emails(self):
        customers_endpoint = SHEETY_API_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data