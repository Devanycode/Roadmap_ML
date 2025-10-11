import pyperclip
from tkinter import *
from tkinter import messagebox
import random


FONT = ("Times New Roman", 14)
SEPARATOR = "  |  "

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

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message="There are the details entered: "
        f"\nEmail: {email_user_input.get()} \nPassword: {password_input.get()}")

        if is_ok:
            with open("contraseñas.txt", mode="a") as file:
                data_format = website_input.get() + SEPARATOR + email_user_input.get() + SEPARATOR + password_input.get() + "\n"
                file.write(data_format)
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
website = Label(text="Website:", font=FONT)
website.grid(column=0, row=1)
email_user = Label(text="Email/Username:", font=FONT)
email_user.grid(column=0, row=2)
password = Label(text="Password:", font=FONT)
password.grid(column=0, row=3)

# User Inputs
website_input = Entry(width=35, justify=LEFT)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_user_input = Entry(width=35)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(index=0, string="devany.code.gg@gmail.com")    # Cuenta personal por defecto
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)
add_password = Button(text="Add", width=35, command=save_password)
add_password.grid(column=1, row=4, columnspan=2)




window.mainloop()

