import requests

AGE = "20"
GENDER = "Male"
HEIGHT = "184"
WEIGHT = "76"
LEVEL = "4"

key = "e5d1345c67mshd8c417e6e842515p1c4a89jsn7ac5b2a06f98"
endpoint = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

query_string = {
    "age": AGE,
    "gender": GENDER,
    "height": HEIGHT,
    "weight": WEIGHT,
    "activitylevel": LEVEL,
}

headers = {
    "x-rapidapi-key": key,
    "x-rapidapi-host": "fitness-calculator.p.rapidapi.com",
}

response = requests.get(url=endpoint, headers=headers, params=query_string)
response.raise_for_status()
print(response.json())