from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os 
import requests
import smtplib


load_dotenv()
EMAIL = os.getenv("my_email")
PASSWORD = os.getenv("email_password")


PRODUCT_URL = "https://www.amazon.com/-/es/Interfaz-audio-generaci%C3%B3n-Scarlett-Focusrite/dp/B0C5JRTS3Y/ref=sr_1_6?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-6"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept": "text/html"
    }

response = requests.get(PRODUCT_URL, headers=HEADERS)
website_text = response.text

"""
# Hago esto para hacer el ejemplo sin hacer solicitudes en la web innecesariamente
with open("amazon_product.html", "w+", encoding="utf-8") as file:
    file.write(response.text)
    website_text = file.read()
"""
"""
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg="tu {product_name}"
    )"""

soup = BeautifulSoup(website_text, "html.parser")
product_name = soup.find(id="productTitle")
product_price = soup.select_one("span.a-offscreen")
print(product_price)
# price_without_symbol = product_price.split("$")[1]
# price_float = float(price_without_symbol)
# print(price_float)

