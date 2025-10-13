import json
import pyperclip
from tkinter import *
from tkinter import messagebox
import random


FONT = ("Times New Roman", 14)

# ---------------------------- SEARCH DATA -------------------------------------- #

# title: Website. Email: Password: 

def search():
    website = website_input.get().title()
    try:
        with open("contraseñas.json", mode="r") as data_file:
            data_website = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="Error", message="Please enter a website to search.")
        else:
            try:
                email = data_website[website]["email"]
                password = data_website[website]["password"]
            except KeyError:
                messagebox.showinfo(title="Ooops", message= f"The website: {website} you request is not registered.\n"
                                                            "Check if you wrote correctly, or if you have already registered that site.")
            else:    # Significa que el sitio web se encuentra en el archivo json
                messagebox.showinfo(title=website, message= f"Email: {email}\nPassword: {password}")    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
        'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password_input.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random_password = password_letters + password_numbers + password_symbols

    random.shuffle(random_password)
    random_password = "".join(random_password)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)    # Esto copiará en el portapapeles la contraseña cuando se genere

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get().title()
    password = password_input.get()
    email = email_user_input.get() 

    # DICT FOR JSON FILE 
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")
    
    else:
        try:
            with open("contraseñas.json", mode="r") as data_file:
                # Leer el archivo viejo
                data = json.load(data_file)
        except:
            with open("contraseñas.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Actualizamos el archivo viejo con datos nuevos
            data.update(new_data)

            with open("contraseñas.json", mode="w") as data_file:
                # Guardamos los datos actualizados 
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #

# Ventana
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:", font=FONT)
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

# User Inputs
website_input = Entry(width=25, justify=LEFT)
website_input.grid(column=1, row=1)
website_input.focus()
email_user_input = Entry(width=43)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(index=0, string="devany.code.gg@gmail.com")    # Cuenta personal por defecto
password_input = Entry(width=25)
password_input.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)
add_password = Button(text="Add", width=35, command=save_password)
add_password.grid(column=1, row=4, columnspan=2)
search_data = Button(text="Search", width= 14, command=search)
search_data.grid(column=2, row=1)




window.mainloop()