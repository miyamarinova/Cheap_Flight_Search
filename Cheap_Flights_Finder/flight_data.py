# This class is responsible for structuring the FLIGHT DATA
class FlightData:

    def __init__(self, price, departure_airport_code, departure_city, arrival_airport_code, arrival_city, departure_date, return_date):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.arrival_airport_code = arrival_airport_code
        self.arrival_city = arrival_city
        self.departure_date = departure_date
        self.return_date = return_date

