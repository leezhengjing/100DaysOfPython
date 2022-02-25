import requests
import os

SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=bearer_headers)
        self.destination_data = response.json()["prices"]
        print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers,
            )
            print(response.text)

