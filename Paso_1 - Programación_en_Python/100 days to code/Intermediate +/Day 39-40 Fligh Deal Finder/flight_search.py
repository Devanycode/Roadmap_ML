from dotenv import load_dotenv
from pprint import pprint
import requests
import os 

load_dotenv()
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()["access_token"]

    def _get_new_token(self):

        headers = {
            "content-type": "application/x-www-form-urlencoded"
            }
        params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=token_endpoint, data=params, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        return token_data        


    def get_destination_code(self, city_name):
        """Esta función devuelve el código iata asignado para una ciudad que entregue el usuario"""
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {"keyword": city_name}
        response = requests.get(url=endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]


    def search_prices(self, origin_city, sheet_data, travel_date, return_date):
        """Esta función busca el precio total de ida y vuelta a cada ciudad que tengas en tu hoja sheet, 
        tomando en cuenta tu ciudad de origen y el lugar al que viajarás, y también 
        la fecha en la que viajarás y la fecha de regreso"""
        endpoint =  "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {self._token}"}

        prices = {}   # Diccionario donde se guardará el precio total por ciudad
        for row in sheet_data:
            params = {
                "originLocationCode": origin_city,
                "destinationLocationCode": row["iataCode"],
                "departureDate": travel_date,
                "returnDate": return_date,
                "adults": 4,
                "currencyCode": "COP",
                "nonStop": "true",
                "max": 1
            }
            response = requests.get(url=endpoint, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()["data"]
            if data:
                total_price = data[0]["price"]["total"]
                print(f"Precio total de viaje a {row["city"]}: ${total_price}.")
                if float(total_price) < row["lowestPrice"]:

                    body_message = (
                        f"¡Alerta de precio bajo!\n"
                        f"Por solo £{float(total_price)} puedes viajar "
                        f"de {origin_city} a {row["city"]}, del {travel_date} al {return_date}."
                    )
                    prices[f"{row["city"]}"] = body_message
            else:
                print(f"No se encontraron resultados de vuelos para {row["city"]}.")
        return prices
             
