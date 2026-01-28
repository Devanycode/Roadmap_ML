from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, "html.parser")

# Lista de todos los títulos 
title = soup.select(selector="td.title .titleline a")
title_list = [x.get_text() for x in title]
# Lista de todas las puntuaciones
points = soup.select(selector="td.subtext .subline .score")
points_list = [int(x.get_text().split()[0]) for x in points]    # el -7 es para eliminar el término ' points' y sólo dejar el número de la puntuación


for article in range(len(points_list)):
    article_text = title_list[article]
    article_link = title[article].get("href")
    article_upvote = points_list[article]
    print(f"{article + 1}. {article_text}\n{article_link}\n{article_upvote}\n")

best_upvotes = int(points_list.index(max(points_list))) + 1
print(best_upvotes)























"""
with open("website.html", "r") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.body.li.string)
# print(soup.prettify())
all_paragraph_tags = soup.find_all(name="a")
# print(all_paragraph_tags)
# for tag in all_paragraph_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find_all (name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector= "p a")
print(company_url)
"""