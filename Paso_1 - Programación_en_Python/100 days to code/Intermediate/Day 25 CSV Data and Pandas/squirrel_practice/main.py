"""
import pandas


data = pandas.read_csv("weather_data.csv")


# Creamos una lista de los valores numéricos de la temperatura
temp_list = data.temp.to_list()


# Cálculo de la temperatura media
sum_temp = sum(temp_list)
average_temp = sum_temp / len(temp_list)
print(int(average_temp))"""

"""
# Aunque podemos deshacernos de todo esto y usar la función integrada en Pandas
print(data["temp"].mean())  # Esto devuelve la media
print(data["temp"].max())

# Get data in column 
print(data["condition"])
print(data.temp)

# get data in row
print(data[data.day == "Monday"])   # Que busque en data, en la columna 'day', y devuelva la fila donde se encuentra el valor "Monday"

# Temperatura máxima 
print(data[data.temp == data.temp.max()])

# Búsqueda más profunda
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Celsius to Fahrenheit
convert_temp_fahr = (monday.temp * 9 / 5) + 32
print(convert_temp_fahr)


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

"""

import pandas 

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Debo crear squirrel_count.csv 
grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

dict_squirrels = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrels, black_squirrels, cinnamon_squirrels]
}

squirrels_dataframe= pandas.DataFrame(dict_squirrels)
squirrels_dataframe.to_csv("squirrel_count.csv")




