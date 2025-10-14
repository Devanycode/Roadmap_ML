##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas 
import random
import smtplib

my_email = "codesamuel270@gmail.com"
password = "nwlw ygfy pjfw pebs"

letter_paths = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# Datos de fecha actuales
current_time = dt.datetime.now()
current_month = current_time.month
current_day = current_time.day
date_now = (current_month, current_day)

# Datos de mis amigos
friends_data = pandas.read_csv("birthdays.csv")
dict_friends = friends_data.to_dict(orient="records")

for friend in dict_friends:
    month = friend["month"]
    day = friend["day"]
    date_friend = (month, day)

    if date_friend == date_now:
        # Abrimos una Carta Aleatoria e incluimos el Nombre de la persona
        with open(random.choice(letter_paths), mode="r") as data_file:
            letter = data_file.read()
            letter = letter.replace("[NAME]", friend["name"]).replace("Angela", "Devany")    # Mi nombre

        # Enviamos el correo a la persona 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=friend["email"],
                msg=f"Subject: Happy Birthday! \n\n{letter}".encode("utf-8"))


