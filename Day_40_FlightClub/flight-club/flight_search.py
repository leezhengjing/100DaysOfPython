import requests
from flight_data import FlightData
import os
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        data = response.json()["locations"]
        destination_code = data[0]["code"]
        return destination_code

    def get_flight_data(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_data_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_time,
            "dateTo": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "SGD",
        }
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        response = requests.get(url=flight_data_endpoint, params=params, headers=headers)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights with 1 stopover found for {destination_city_code}.")
            print("Checking to see if there are flights with 2 stopovers...")
            params["max_stopovers"] += 1
            response = requests.get(url=flight_data_endpoint, params=params, headers=headers)
            try:
                data = response.json()['data'][0]
            except IndexError:
                print(f"No flights with 2 stopovers found for {destination_city_code}.")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    destination_city=data["cityTo"],
                    destination_airport=data["flyTo"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][-1]["local_arrival"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )
                flight_data.link = data["deep_link"]
                print(f"{flight_data.destination_city}: S${flight_data.price}")
                print(flight_data.link)
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][-1]["local_arrival"].split("T")[0],
            )
            flight_data.link = data["deep_link"]
            print(f"{flight_data.destination_city}: S${flight_data.price}")
            print(flight_data.link)
            return flight_data