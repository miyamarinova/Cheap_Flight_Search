from data_manager import DataManager
from flight_search import FLightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager


notification_manager = NotificationManager()

flight_search = FLightSearch()
data_manager = DataManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_destination_data()

tomorow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()
print(sheet_data)

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorow,
        to_time=six_month_from_today
    )


    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to "
                    f"{flight.arrival_city}-{flight.arrival_airport_code} from {flight.departure_date} to {flight.return_date}."
        )