from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- SEARCH DATA -------------------------------------- #
def search_website():
    WEBSITE = website_ent.get()

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="File empty", message="No data in file!")
    else:
        if WEBSITE in data:
            messagebox.showinfo(title=f"{WEBSITE}", message=f"Email: {data[WEBSITE]['email']}\nPassword: {data[WEBSITE]['password']}")
        else:
            messagebox.showwarning(title="No website found!", message="The website you're looking for is not in the file!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password = pass_letters + pass_numbers + pass_symbols

    random.shuffle(password)

    password = "".join(password)
    passwd_ent.delete(0, END)
    passwd_ent.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_data_to_file():

    WEBSITE = website_ent.get()
    EMAIL = email_ent.get()
    PASSWD = passwd_ent.get()

    new_data = {
        WEBSITE: {
            "email":EMAIL,
            "password":PASSWD
        }}

    if len(WEBSITE) == 0 or len(EMAIL) == 0 or len(PASSWD) == 0:
        messagebox.showwarning(title="Error!", message="Some of data enetered is empty")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_ent.delete(0, END)
            passwd_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)


#Labels

website = Label(text="Website:")
email = Label(text="Email/Username:")
passwd = Label(text="Password:")

website.grid(row=1, column=0)
email.grid(row=2, column=0)
passwd.grid(row=3, column=0)

#Enter
website_ent = Entry(width=20)
website_ent.grid(row=1, column=1, sticky="EW")
email_ent = Entry(width=35)
email_ent.grid(row=2, column=1, columnspan=2, sticky="EW")
email_ent.insert(0, "example@gmail.com")
passwd_ent = Entry(width=20)
passwd_ent.grid(row=3, column=1, sticky="EW")

#Buttons
search_button = Button(text="Search", command=search_website)
search_button.grid(row=1, column=2, sticky="EW")
gen_pass_butt = Button(text="Generate Password", command = generate_passwd)
gen_pass_butt.grid(row=3, column=2,)
add_butt = Button(text="Add", width=36, command=write_data_to_file)
add_butt.grid(row=4, column=1, columnspan=2, sticky="EW", )
window.mainloop()
