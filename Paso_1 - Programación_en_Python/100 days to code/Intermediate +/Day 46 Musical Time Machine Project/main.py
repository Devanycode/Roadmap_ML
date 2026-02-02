from bs4 import BeautifulSoup
import requests

"""

url = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2014"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept": "text/html"
    }

# Aquí hago la solicitud 
response = requests.get(url, headers=headers)
response.raise_for_status()
text_html = response.text

# Aquí escribo el archivo con el texto html
with open("website.html", "w", encoding="utf-8") as file:
    file.write(text_html)
"""
with open("website.html", encoding="utf-8") as file:
    text_html = file.read()

soup = BeautifulSoup(text_html, "html.parser")

songs = soup.select(selector="tbody tr td a")
list_songs = [song.get_text() for song in songs if song.get_text().isdigit() is False]

name_songs = list_songs[::2]
name_artist = list_songs[1::2]

print(f"Names:{name_songs}\n\nArtist:{name_artist}")
