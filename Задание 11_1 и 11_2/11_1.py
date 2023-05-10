import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Регистрация")
root.geometry("320x400")

conn = sqlite3.connect("userdata.sql", uri=True)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (name TEXT, email TEXT, phone TEXT, gender TEXT, country TEXT, password TEXT)""")
conn.commit()

name_label = Label(root, text="Имя ->")
name_label.grid(column=0, row=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(column=1, row=0, padx=10, pady=10)
 
email_label = Label(root, text="Email ->")
email_label.grid(column=0, row=1, padx=10, pady=10)
email_entry = Entry(root)
email_entry.grid(column=1, row=1, padx=10, pady=10)

phone_label = Label(root, text="Телефон ->")
phone_label.grid(column=0, row=2, padx=10, pady=10)
phone_entry = Entry(root)
phone_entry.grid(column=1, row=2, padx=10, pady=10)

gender_label = Label(root, text="Пол ->")
gender_label.grid(column=0, row=3, padx=10, pady=10)
gender_var = StringVar()
gender_var.set("Мужской")
male_rb = Radiobutton(root, text="Мужской", variable=gender_var, value="Мужской")
male_rb.grid(column=1, row=3, padx=10, pady=10)
female_rb = Radiobutton(root, text="Женский", variable=gender_var, value="Женский")
female_rb.grid(column=1, row=4, padx=10, pady=10)

country_label = Label(root, text="Страна ->")
country_label.grid(column=0, row=5, padx=10, pady=10)
country_combo = ttk.Combobox(root, values=[line.strip() for line in open("countries.txt", "r")])
country_combo.grid(column=1, row=5, padx=10, pady=10)

password_label = Label(root, text="Пароль ->")
password_label.grid(column=0, row=6, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(column=1, row=6, padx=10, pady=10)

confirm_password_label = Label(root, text="Подтвердите пароль ->")
confirm_password_label.grid(column=0, row=7, padx=10, pady=10)
confirm_password_entry = Entry(root, show="*")
confirm_password_entry.grid(column=1, row=7, padx=10, pady=10)

def save_user():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    country = country_combo.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    if name == '' or email == '' or phone == '' or country == '' or password == '':
        messagebox.showinfo("Ошибка!", "Отсутствуют обязательные данные!")
    else:
        if password == confirm_password:
            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, gender, country, password))
            conn.commit()
            messagebox.showinfo("Сохранение", "Запись сохранена")
        else:
            messagebox.showerror("Ошибка!", "Пароли не совпадают!")
    
save_btn = Button(root, text="Зарегистрироваться", command=save_user)
save_btn.grid(column=1, row=8, padx=10, pady=10)

root.mainloop()