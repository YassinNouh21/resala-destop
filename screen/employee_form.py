import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

def open_employee_page():


    # the appearance mode of the system
    ctk.set_appearance_mode("System")

    ctk.set_default_color_theme("green")

    # Dimensions of the window


    # Function to generate the text for display
    def create_text(name, address, state, birth_date, phone, mobile_number, national_id, education_year, school_name,
                    level, faculty, college, graduation_year, job, workplace, email, blood_type, skills, club_member,
                    club_name,
                    has_car, car_participation):
        text = f"Name: {name}\n"
        text += f"Address: {address}\n"
        text += f"State: {state}\n"
        text += f"Birth Date: {birth_date}\n"
        text += f"Phone: {phone}\n"
        text += f"Mobile Number: {mobile_number}\n"
        text += f"National ID: {national_id}\n"
        text += f"Education Year: {education_year}\n"
        text += f"School Name: {school_name}\n"
        text += f"Level: {level}\n"
        text += f"Faculty: {faculty}\n"
        text += f"College: {college}\n"
        text += f"Year of Graduation: {graduation_year}\n"
        text += f"Job: {job}\n"
        text += f"Workplace: {workplace}\n"
        text += f"Email: {email}\n"
        text += f"Blood Type: {blood_type}\n"
        text += f"Skills: {skills}\n"
        text += f"Club Member: {'Yes' if club_member else 'No'}\n"
        text += f"Club Name: {club_name}\n" if club_member else ""
        text += f"Has Car: {'Yes' if has_car else 'No'}\n"
        text += f"Car Participation: {car_participation}\n" if has_car else ""
        return text

    # Function to generate results and display them
    def generate_results():
        display_box.delete("0.0", "end")
        name = name_entry.get()
        address = address_entry.get()
        state = state_entry.get()
        birth_date = birth_date_entry.get()
        phone = phone_entry.get()
        mobile_number = mobile_number_entry.get()
        national_id = national_id_entry.get()
        education_year = education_year_entry.get()
        school_name = school_name_entry.get()
        level = level_entry.get()
        faculty = faculty_entry.get()
        college = college_entry.get()
        graduation_year = graduation_year_entry.get()
        job = job_entry.get()
        workplace = workplace_entry.get()
        email = email_entry.get()
        blood_type = blood_type_entry.get()
        skills = skills_entry.get()
        club_member = club_member_var.get()
        club_name = club_name_entry.get()
        has_car = has_car_var.get()
        car_participation = car_participation_entry.get()

        text = create_text(name, address, state, birth_date, phone, mobile_number, national_id, education_year,
                           school_name,
                           level, faculty, college, graduation_year, job, workplace, email, blood_type, skills,
                           club_member,
                           club_name, has_car, car_participation)
        display_box.insert("0.0", text)

    # Create the main window
    window = ctk.CTk()

    # Window
    window.title("Form Application")
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

    # Name Label
    name_label = ctk.CTkLabel(window, text="Name")
    name_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Name Entry Field
    name_entry = ctk.CTkEntry(window, placeholder_text="Name")
    name_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

    # Address Label
    address_label = ctk.CTkLabel(window, text="Address")
    address_label.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

    # Address Entry Field
    address_entry = ctk.CTkEntry(window, placeholder_text="Address")
    address_entry.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

    # State Label
    state_label = ctk.CTkLabel(window, text="State")
    state_label.grid(row=0, column=4, padx=20, pady=10, sticky="ew")

    # State Entry Field
    state_entry = ctk.CTkEntry(window, placeholder_text="State")
    state_entry.grid(row=0, column=5, padx=5, pady=10, sticky="ew")

    # Birth Date Label
    birth_date_label = ctk.CTkLabel(window, text="Birth Date")
    birth_date_label.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    # Birth Date Entry Field
    birth_date_entry = ctk.CTkEntry(window, placeholder_text="Birth Date")
    birth_date_entry.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

    # Phone Label
    phone_label = ctk.CTkLabel(window, text="Phone")
    phone_label.grid(row=1, column=2, padx=20, pady=10, sticky="ew")

    # Phone Entry Field
    phone_entry = ctk.CTkEntry(window, placeholder_text="Phone")
    phone_entry.grid(row=1, column=3, padx=5, pady=10, sticky="ew")

    # Mobile Number Label
    mobile_number_label = ctk.CTkLabel(window, text="Mobile Number")
    mobile_number_label.grid(row=1, column=4, padx=20, pady=10, sticky="ew")

    # Mobile Number Entry Field
    mobile_number_entry = ctk.CTkEntry(window, placeholder_text="Mobile Number")
    mobile_number_entry.grid(row=1, column=5, padx=5, pady=10, sticky="ew")

    # National ID Label
    national_id_label = ctk.CTkLabel(window, text="National ID")
    national_id_label.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    # National ID Entry Field
    national_id_entry = ctk.CTkEntry(window, placeholder_text="National ID")
    national_id_entry.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

    # Education Year Label
    education_year_label = ctk.CTkLabel(window, text="Education Year")
    education_year_label.grid(row=2, column=2, padx=20, pady=10, sticky="ew")

    # Education Year Entry Field
    education_year_entry = ctk.CTkEntry(window, placeholder_text="Education Year")
    education_year_entry.grid(row=2, column=3, padx=5, pady=10, sticky="ew")

    # School Name Label
    school_name_label = ctk.CTkLabel(window, text="School Name")
    school_name_label.grid(row=2, column=4, padx=20, pady=10, sticky="ew")

    # School Name Entry Field
    school_name_entry = ctk.CTkEntry(window, placeholder_text="School Name")
    school_name_entry.grid(row=2, column=5, padx=5, pady=10, sticky="ew")

    # Level Label
    level_label = ctk.CTkLabel(window, text="Level")
    level_label.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    # Level Entry Field
    level_entry = ctk.CTkEntry(window, placeholder_text="Level")
    level_entry.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

    # Faculty Label
    faculty_label = ctk.CTkLabel(window, text="Faculty")
    faculty_label.grid(row=3, column=2, padx=20, pady=10, sticky="ew")

    # Faculty Entry Field
    faculty_entry = ctk.CTkEntry(window, placeholder_text="Faculty")
    faculty_entry.grid(row=3, column=3, padx=5, pady=10, sticky="ew")

    # College Label
    college_label = ctk.CTkLabel(window, text="College")
    college_label.grid(row=3, column=4, padx=20, pady=10, sticky="ew")

    # College Entry Field
    college_entry = ctk.CTkEntry(window, placeholder_text="College")
    college_entry.grid(row=3, column=5, padx=5, pady=10, sticky="ew")

    # Graduation Year Label
    graduation_year_label = ctk.CTkLabel(window, text="Graduation Year")
    graduation_year_label.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    # Graduation Year Entry Field
    graduation_year_entry = ctk.CTkEntry(window, placeholder_text="Graduation Year")
    graduation_year_entry.grid(row=4, column=1, padx=5, pady=10, sticky="ew")

    # Job Label
    job_label = ctk.CTkLabel(window, text="Job")
    job_label.grid(row=4, column=2, padx=20, pady=10, sticky="ew")

    # Job Entry Field
    job_entry = ctk.CTkEntry(window, placeholder_text="Job")
    job_entry.grid(row=4, column=3, padx=5, pady=10, sticky="ew")

    # Workplace Label
    workplace_label = ctk.CTkLabel(window, text="Workplace")
    workplace_label.grid(row=4, column=4, padx=20, pady=10, sticky="ew")

    # Workplace Entry Field
    workplace_entry = ctk.CTkEntry(window, placeholder_text="Workplace")
    workplace_entry.grid(row=4, column=5, padx=5, pady=10, sticky="ew")

    # Email Label
    email_label = ctk.CTkLabel(window, text="Email")
    email_label.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

    # Email Entry Field
    email_entry = ctk.CTkEntry(window, placeholder_text="Email")
    email_entry.grid(row=5, column=1, padx=5, pady=10, sticky="ew")

    # Blood Type Label
    blood_type_label = ctk.CTkLabel(window, text="Blood Type")
    blood_type_label.grid(row=5, column=2, padx=20, pady=10, sticky="ew")

    # Blood Type Entry Field
    blood_type_entry = ctk.CTkEntry(window, placeholder_text="Blood Type")
    blood_type_entry.grid(row=5, column=3, padx=5, pady=10, sticky="ew")

    # Skills Label
    skills_label = ctk.CTkLabel(window, text="Skills")
    skills_label.grid(row=5, column=4, padx=20, pady=10, sticky="ew")

    # Skills Entry Field
    skills_entry = ctk.CTkEntry(window, placeholder_text="Skills")
    skills_entry.grid(row=5, column=5, padx=5, pady=10, sticky="ew")

    # Club Member Label
    club_member_label = ctk.CTkLabel(window, text="Club Member")
    club_member_label.grid(row=18, column=0, padx=20, pady=10, sticky="ew")

    # Club Member Checkbox
    club_member_var = tk.BooleanVar()
    club_member_checkbox = ctk.CTkCheckBox(window, text="Yes", variable=club_member_var)
    club_member_checkbox.grid(row=18, column=1, padx=20, pady=10, sticky="ew")

    # Club Name Label
    club_name_label = ctk.CTkLabel(window, text="Club Name")
    club_name_label.grid(row=19, column=0, padx=20, pady=10, sticky="ew")

    # Club Name Entry Field
    club_name_entry = ctk.CTkEntry(window, placeholder_text="Club Name")
    club_name_entry.grid(row=19, column=1, columnspan=3, padx=20, pady=10, sticky="ew")

    # Has Car Label
    has_car_label = ctk.CTkLabel(window, text="Has Car")
    has_car_label.grid(row=20, column=0, padx=20, pady=10, sticky="ew")

    # Has Car Checkbox
    has_car_var = tk.BooleanVar()
    has_car_checkbox = ctk.CTkCheckBox(window, text="Yes", variable=has_car_var)
    has_car_checkbox.grid(row=20, column=1, padx=20, pady=10, sticky="ew")

    # Car Participation Label
    car_participation_label = ctk.CTkLabel(window, text="Car Participation")
    car_participation_label.grid(row=21, column=0, padx=20, pady=10, sticky="ew")

    # Car Participation Entry Field
    car_participation_entry = ctk.CTkEntry(window, placeholder_text="Car Participation")
    car_participation_entry.grid(row=21, column=1, columnspan=3, padx=20, pady=10, sticky="ew")

    # Generate Results Button
    generate_button = ctk.CTkButton(window, text="Generate Results", command=generate_results)
    generate_button.grid(row=22, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

    # Display Box
    display_box = ctk.CTkTextbox(window)
    display_box.grid(row=23, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

    # Run the application
    window.mainloop()