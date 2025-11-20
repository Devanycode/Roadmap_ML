from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint



ORIGIN_CITY_IATA = "MDE"
TRAVEL_DATE = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
RETURN_DATE = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")



data = DataManager()
sheet_data = data.get_destination_data()
search = FlightSearch()
cheapest_flight = search.search_prices(
    origin_city=ORIGIN_CITY_IATA, 
    sheet_data=sheet_data,
    travel_date=TRAVEL_DATE, 
    return_date=RETURN_DATE
    )
print(type(cheapest_flight))
print(cheapest_flight)
"""
sms = NotificationManager()
if cheapest_flight:
    for city, message in cheapest_flight.items():
        sms.send_sms(message=message)
"""

if sheet_data[0]["iataCode"] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data.destination_data = sheet_data
    data.update_destination_codes()

