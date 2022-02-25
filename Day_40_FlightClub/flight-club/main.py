# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users = data_manager.get_user_emails()

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
            message = f"Low price alert! Only S${flight.price} to fly from {flight.origin_city}" \
                    f"-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}," \
                    f" from {flight.out_date} to {flight.return_date}. Link: {flight.link}"

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)

            notification_manager.send_sms(message)
            for user_email in users:
                notification_manager.send_emails(address=user_email, message=message)



    except AttributeError:
        continue
