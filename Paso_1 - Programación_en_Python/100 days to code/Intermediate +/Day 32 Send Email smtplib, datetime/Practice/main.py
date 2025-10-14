
import datetime as dt
import random
import smtplib
#
my_email = "codesamuel270@gmail.com"
password = "nwlw ygfy pjfw pebs"
friend_email = "devany.code.gg"

with open("quotes.txt", mode="r", encoding="utf-8") as data_file:
    phrases = data_file.readlines()
    phrase = random.choice(phrases).strip()

current_time = dt.datetime.now()
week_day = current_time.weekday()

if week_day == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=friend_email, 
            msg=f"Subject: Feliz día\n\n{phrase}".encode("utf-8")
        )
        phrases.remove(phrase)
    