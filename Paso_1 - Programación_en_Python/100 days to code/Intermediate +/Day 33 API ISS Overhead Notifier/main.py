
from datetime import datetime
import requests 
import smtplib
import time


# LONG --> LAT ORDER
MY_LONGITUDE = -75.57151
MY_LATITUDE = 6.245
ISS_PROXIMITY_RANGE = 5
UTC_COL = -5

# Mail Data
my_email = "codesamuel270@gmail.com"
password = "nwlw ygfy pjfw pebs"

# Funciones 
def iss_near_position():
    return (
        (iss_latitude <= MY_LATITUDE + ISS_PROXIMITY_RANGE or iss_latitude >= MY_LATITUDE - ISS_PROXIMITY_RANGE)
        and
        (iss_longitude <= MY_LONGITUDE + ISS_PROXIMITY_RANGE or iss_longitude >= MY_LONGITUDE - ISS_PROXIMITY_RANGE)
    )

def is_dark():
    return (
        (current_hour >= sunrise_hour and current_min >= sunset_min)
        or
        (current_hour <= sunrise_hour and current_min <= sunrise_min)
    )

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg="Subject: Mira el cielo!\n\nEl ISS está pasando.")


# ISS DATA
response = requests.get(url="http://api.open-notify.org/iss-now.json#")
response.raise_for_status()
data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])


# SUNRISE AND SUNSET DATA
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# Llamamos a la hora y modificamos el formato para poder compararlo con datetime 
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + UTC_COL    # Modificamos la salida al horario local 
sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + UTC_COL
sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1])


# CURRENT TIME DATA
time_now = datetime.now()
current_hour = time_now.hour
current_min = time_now.minute

# BLOQUE PRINCIPAL
while True:
    if iss_near_position() and is_dark():
        send_email()
        time.sleep(60)
    else:
        time.sleep(60)
        continue
   
            

