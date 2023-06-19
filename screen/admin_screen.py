import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import ttk
from random import choice

def open_admin_page():
    # Functions
    def item_select(_):
        print(table.selection())
        for i in table.selection():
            print(table.item(i)['values'])
        # table.item(table.selection())

    def delete_select(_):
        for i in table.selection():
            table.delete(i)

    # Data
    table_data = []
    Names = ['Bob Smith', 'Maria Brown', 'Alex Wilson', 'James Thomson', 'Susan Cook', 'Henry Taylor', 'Lisa Walker',
             'Anna Clark', 'Lisa king']
    Email = ['john.doe@example.com', 'mary.smith@example.com', 'david.jones@example.com', 'emily.wilson@example.com',
             'alexander.brown@example.com', 'olivia.johnson@example.com', 'william.davis@example.com']
    Phone = ['010035051', '012502315', '0120615610', '131530352', '2568564641532']

    # Populate table_data with initial data
    for i in range(100):
        name = choice(Names)
        phone = choice(Phone)
        email = choice(Email)
        data = (name, phone, email)
        table_data.append(data)

    # ...

    def search():
        search_input = search_entry.get()
        search_type = search_var.get()

        # Clear the table
        table.delete(*table.get_children())

        # Perform the search based on the selected search type
        if search_type == "Name":
            # Search by name logic
            searched_items = [item for item in table_data if search_input.lower() in item[0].lower()]
        elif search_type == "Phone":
            # Search by phone logic
            searched_items = [item for item in table_data if search_input.lower() in item[1].lower()]
        elif search_type == "Email":
            # Search by email logic
            searched_items = [item for item in table_data if search_input.lower() in item[2].lower()]
        else:
            searched_items = []

        # Insert the searched items into the table
        for item in searched_items:
            table.insert(parent='', index='end', values=item)

        # Clear the search input
        search_entry.delete(0, tk.END)

    # Window
    window = tk.Tk()
    window.title("Admin")
    window.geometry("1080x720")
    window.iconbitmap('Resala-logo.ico')
    window.minsize(960, 540)

    width = 1400
    height = 600
    display_width = window.winfo_screenwidth()
    display_height = window.winfo_screenheight()
    left = int(display_width / 2 - width / 2)
    top = int(display_height / 2 - height / 2)
    window.geometry(f'{width}x{height}+{left}+{top}')

    grip = ttk.Sizegrip(window)
    grip.place(relx=1.0, rely=1.0, anchor='se')

    # Grid
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=5)

    # Create the search bar components
    search_entry = tk.Entry(window, width=30)
    search_entry.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

    search_var = tk.StringVar(window)
    search_var.set("Name")  # Default search type

    search_type_menu = tk.OptionMenu(window, search_var, "Name", "Phone", "Email")
    search_type_menu.grid(row=0, column=1, padx=(5, 2), pady=10)  # Adjusted padx value

    search_button = tk.Button(window, text="Search", command=search)
    search_button.grid(row=0, column=2, padx=(2, 5), pady=10)  # Adjusted padx value

    # Treeview
    # Menu
    menu = tk.Menu(window)

    file_menu = tk.Menu(menu, tearoff=False)
    file_menu.add_command(label='New', command=lambda: print('New File'))
    file_menu.add_command(label='Open', command=lambda: print('Open File'))
    menu.add_cascade(label='File', menu=file_menu)

    help_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Help', menu=help_menu)

    window.configure(menu=menu)

    table = ttk.Treeview(window, columns=('Name', 'Phone', 'Email'), show='headings')
    table.heading('Name', text='Name')
    table.heading('Phone', text='Phone')
    table.heading('Email', text='Email')
    table.grid(row=1, column=0, sticky='nsew')

    # Insert data into the table
    for i in range(100):
        name = choice(Names)
        phone = choice(Phone)
        email = choice(Email)
        data = (name, phone, email)
        table.insert(parent='', index=0, values=data)

    # Events
    table.bind('<<TreeviewSelect>>', item_select)
    table.bind('<Delete>', delete_select)

    # Run
    window.mainloop()

    # Close the admin page and show the login page again when admin page is closed
    window.protocol("WM_DELETE_WINDOW", show_login_page)

