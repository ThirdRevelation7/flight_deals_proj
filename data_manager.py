import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/users", headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

        

