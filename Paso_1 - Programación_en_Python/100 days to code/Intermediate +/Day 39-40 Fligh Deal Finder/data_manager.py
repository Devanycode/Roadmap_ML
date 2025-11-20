from dotenv import load_dotenv
import requests
from pprint import pprint
import os

SHEETY_PUT_ENDPOINT = "https://api.sheety.co/0788248e10a988b913a94464c37cd5b9/flightDealFinder/hoja1/[Object ID]"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_GET_ENDPOINT = "https://api.sheety.co/0788248e10a988b913a94464c37cd5b9/flightDealFinder/hoja1"
SHEETY_HEADERS = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
            }   

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init(self):
        self.destination_data = {}

    def get_destination_data(self):  
        """Sirve para obttener los datos en formato JSON de la hoja de Sheets"""
        response = requests.get(url=SHEETY_GET_ENDPOINT, headers=SHEETY_HEADERS)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["hoja1"]
        return self.destination_data

    def update_destination_codes(self):
        """Actualiza la hoja de Sheets, agregando los valores de iatacode de cada ciudad"""
        for city in self.destination_data:
            new_data = {
                "hoja1": {
                    "iataCode": city["iataCode"]
                    }
                }
            response = requests.put(url=f"{SHEETY_GET_ENDPOINT}/{city["id"]}", json=new_data, headers=SHEETY_HEADERS)
            pprint(response.text)
            
