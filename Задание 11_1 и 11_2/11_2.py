from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Авторизация")
root.geometry("300x150")

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

password_label = Label(root, text="Пароль:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

def login():
    conn = sqlite3.connect('userdata.sql', uri=True)
    cursor = conn.cursor()
    email = email_entry.get()
    password = password_entry.get()
    query = '''SELECT * FROM users WHERE email=? AND password=?'''
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    conn.close()

    if email == '' or password == '':
        messagebox.showinfo("Ошибка!", "Отсутствуют обязательные данные!")
    else:   
        if result:
            messagebox.showinfo("Авторизация", "Успешная авторизация")
        else:
            messagebox.showerror("Авторизация", "Данные неверны")

login_button = Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()