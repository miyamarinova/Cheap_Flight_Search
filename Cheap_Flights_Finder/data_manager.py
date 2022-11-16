import requests
from pprint import pprint

SHEETY_API_ENDPOINT = "https://api.sheety.co/b411d0b1ef11bf644de2ae20d8ea798e/flightDeals/prices"


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
            print(new_data)
            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)




