import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import ttk
from random import choice

from screen.admin_screen import open_admin_page
from screen.employee_form import open_employee_page

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("رساله")
app.geometry("1080x720")
app.iconbitmap('Resala-logo.ico')
# window size
app.minsize(960, 540)

# screen atribute

# window atribute
app.attributes('-alpha', 1)

# security event

# app.attributes('-fullscreen',True)

# titlebar
# app.overrideredirect(True)
grip = ttk.Sizegrip(app)
grip.place(relx=1.0, rely=1.0, anchor='se')

# midle screen window
width = 1400
hight = 600
display_width = app.winfo_screenwidth()
display_hight = app.winfo_screenheight()

left = int(display_width / 2 - width / 2)
top = int(display_hight / 2 - hight / 2)
app.geometry(f'{width}x{hight}+{left}+{top}')


def login():
    username = "resala"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        if menu_var.get() == "Admin":
            # Close the login window
            app.withdraw()
            # Navigate to admin page
            open_admin_page()
        elif menu_var.get() == "Employee":
            # Close the login window
            app.withdraw()
            # Navigate to employee page
            open_employee_page()
        else:
            tkmb.showinfo(title="Invalid Option", message="Please select a valid mode: Admin or Employee")
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username or password")




def show_login_page():
    app.destroy()
    app.deiconify()



frame = ctk.CTkFrame(master=app)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = ctk.CTkLabel(master=frame, text='Log In', width=200, font=("Arial bold", 25))
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=200)
user_entry.pack(pady=12, padx=10)
user_entry.bind("<Return>", login)  # Bind <Return> event to the login function

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=200)
user_pass.pack(pady=12, padx=10)
user_pass.bind("<Return>", login)  # Bind <Return> event to the login function

menu_var = tk.StringVar()
menu_button = ttk.OptionMenu(frame, menu_var, "Select Option", "Admin", "Employee")
menu_button.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login, width=200)
button.pack(pady=12, padx=10)


# checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
# checkbox.pack(pady=12, padx=10)

app.mainloop()
