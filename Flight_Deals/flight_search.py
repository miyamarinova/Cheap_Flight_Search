#This class is responsible for talking to the Flight Search API.
import requests
from flight_data import FlightData
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)

FLIGHT_SEARCH_API_KEY = "fM4IyxXu7WK7x-k1dKEGxcPVWY_qD7Oe"
FLIGHT_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com"

class FLightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{FLIGHT_SEARCH_API_ENDPOINT}/locations/query"
        headers = {"apikey": FLIGHT_SEARCH_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flight(self, departure_city_code, arrival_city_code, from_time, to_time):
        headers = {"apikey": FLIGHT_SEARCH_API_KEY}

        query = {
            "fly_from": departure_city_code,
            "fly_to": arrival_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "USD",
        }
        response = requests.get(url=f"{FLIGHT_SEARCH_API_ENDPOINT}/v2/search", headers=headers, params=query)

        data = response.json()["data"][0]
        print(data)


        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport_code=data["route"][0]["flyFrom"],
            arrival_city=data["cityTo"],
            arrival_airport_code=data["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs=1,
            via_city=data["route"][0]["cityTo"])

        print(f"{flight_data.arrival_city}: ${flight_data.price}")
        return flight_data
print(FlightData)


