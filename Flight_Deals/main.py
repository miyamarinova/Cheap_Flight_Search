#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FLightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager


notification_manager = NotificationManager()

flight_search = FLightSearch()
data_manager = DataManager()

ORIGIN_CITY_IATA = "IAD"

sheet_data = data_manager.get_destination_data()

tomorow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_code()
    sheet_data = data_manager.get_destination_data()

print(sheet_data)
print(sheet_data[0]["iataCode"])
destinations = {
    data['iataCode']: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

print(destinations)
for destination_code in destinations:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorow,
        to_time=six_month_from_today
    )
    print(flight.price)

    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customers_emails()
        emails = [row["eMail"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only $" \
                  f"{flight.price} to fly from {flight.departure_city} - {flight.arrival_city} - {flight.arrival_airport_code}, from {flight.departure_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlights has {flight.stop_overs} stop over, via {flight.via_city}."
        notification_manager.send_emails(emails, message)

    #notification_manager.send_sms(message)