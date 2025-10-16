
from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client


load_dotenv()
# Weather API personal data
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
lat = os.getenv("LATITUDE")
long = os.getenv("LONGITUDE")
limit_result = 4

# Twilio personal data 
# acount_sid = os.getenv("TWILIO_SID")
# auth_token = os.getenv("AUTH_TOKEN")


parameters = {
    "lat": lat,
    "lon": long,
    "appid":api_key,
    "lang": "sp, es",
    "cnt": limit_result
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

for _ in range(limit_result):
    condition_code = response.json()["list"][_]["weather"][0]["id"]
    date = response.json()["list"][_]["dt_txt"]

    if int(condition_code) < 600:
        client = Client(acount_sid, auth_token)

        message = client.messages.create(
            body="Hoy va a llover. No olvides llevar una sombrilla.☂️",
            from_="+13612668748",
            to="+573023660773",
        ) 

        print(message.body)
        
        break

