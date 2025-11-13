import requests
import datetime

USERNAME = "devanycode"
TOKEN = "XFVT9(+vocNRV8"

date = datetime.datetime.today()
date_today = f"{date.year}{date.month}{date.day}"

pixela_endpoint = "https://pixe.la/v1/users"

# USER 
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes", 
}

# GRAPHS
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# GRAPH 1
graph1_endpoint = f"{graph_endpoint}/graph1"

graph1_post = {
    "date": date_today,
    "quantity": input("¿Cuántas páginas  leí hoy?"),
}

response = requests.post(url=graph1_endpoint, json=graph1_post, headers=headers)
response.raise_for_status()
print(response.text)
