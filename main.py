from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters +password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please ensure all details are entered")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().strip().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            display = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{display}")
            messagebox.showinfo(title="Error", message=f"{website} not found")
        else:
            messagebox.showinfo(title="Error", message=f"{website} not found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_columnconfigure(1, weight=1)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1, columnspan=3)
canvas.grid_columnconfigure(1, weight=1)

website = Label(text="Website:")
website.grid(row=1, column=0, sticky="E")

email = Label(text="Email/Username:")
email.grid(row=2, column=0, sticky="E")

password = Label(text="Password:")
password.grid(row=3, column=0, sticky="E", padx=5, pady=5)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW", padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=21)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=5, pady=5)
email_entry.insert(0, "dellsohaib7@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW", padx=5, pady=5)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2, sticky="W", padx=5, pady=5)

add= Button(text="Add Password", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW", padx=5, pady=5)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2, sticky="W", padx=5, pady=5)
window.mainloop()