# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "SIN"


check_updated = True
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        check_updated = False

if not check_updated:
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.now().date()
date_from = today.strftime("%d/%m/%Y")
date_to = today + timedelta(days=6 * 30)
date_to = date_to.strftime("%d/%m/%Y")

for row in sheet_data:
    flight = flight_search.get_flight_data(
        ORIGIN_CITY_IATA,
        row["iataCode"],
        from_time=date_from,
        to_time=date_to,
    )
    try:
        if row["lowestPrice"] > flight.price:
            notification_manager.send_sms(
                message=f"Low price alert! Only S${flight.price} to fly from {flight.origin_city}-"
                        f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport},"
                        f" from {flight.out_date} to {flight.return_date}. Link: {flight.link}")
    except AttributeError:
        pass

# for data in sheet_data:
#     if not data["iataCode"]:
#         search_flight = FlightSearch(data["city"])
#         result = search_flight.get_destination_code()
#         data["iataCode"] = result
#         edit_data = {
#             "price": data
#         }
#         data_manager = DataManager(edit_data)
#         data_manager.get_destination_data()
