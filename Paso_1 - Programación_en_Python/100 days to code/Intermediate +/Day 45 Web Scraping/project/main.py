import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept": "text/html"
    }

"""
Lo cancelo para no llamar de forma reiterada 
response = requests.get(url, headers=headers)
response.raise_for_status()
text_html = response.text
"""
with open("website.html", encoding="utf-8") as file:
    text_html = file.read()

soup = BeautifulSoup(text_html, "html.parser")

"""
(Lo hice para escribir el documento html donde estarían los datos)

with open("website.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
"""

top_movies = soup.select(selector="span h2 strong")
list_movies = [movie.get_text().strip() for movie in top_movies]
list_movies_clean = [movie for movie in list_movies if movie[0].isdigit()]    # Para evitar incluir títulos de no comienzan con número 

with open("top_movies.txt", "w", encoding="utf-8") as file:
    for movie in list_movies_clean[::-1]:
        file.write(f"{movie}\n")




