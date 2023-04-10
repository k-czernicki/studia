import sqlite3
import hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial

# Database
with sqlite3.connect("password_manager.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
application TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

# PopUp


def pop_up(text):
    answer = simpledialog.askstring("input string", text)

    return answer


# Initiate Window
window = Tk()

window.title("Password Manager")


def hash_password(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()

    return hash


def first_screen():
    window.geometry("300x200")

    lbl = Label(window, text="Create \"Master\" password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter \"Master\" password")
    lbl1.pack()

    txt1 = Entry(window, width=20)
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()

    def save_password():
        if txt.get() == txt1.get():
            hashed_password = hash_password(txt.get().encode("utf-8"))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [hashed_password])
            db.commit()

            password_vault()
        else:
            lbl2.config(text="Password do not match!")

    btn = Button(window, text="Save", command=save_password)
    btn.pack(pady=5)


def login_screen():
    window.geometry("300x150")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

# txt = Entry(window, width=20, show="*")
    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def get_master_password():
        check_hashed_password = hash_password(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [check_hashed_password])
        return cursor.fetchall()

    def check_password():
        match = get_master_password()

        if match:
            password_vault()
        else:
            txt.delete(0, "end")
            lbl1.config(text="Password incorrect")

    btn = Button(window, text="Submit", command=check_password)
    btn.pack(pady=5)


def password_vault():
    for widget in window.winfo_children():
        widget.destroy()

    def add_entry():
        text1 = "Website or Application"
        text2 = "Username"
        text3 = "Password"

        application = pop_up(text1)
        username = pop_up(text2)
        password = pop_up(text3)

        insert_fields = """INSERT INTO vault(application,username,password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (application, username, password))
        db.commit()

        password_vault()

    def remove_entry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        password_vault()

    window.geometry("800x400")

    lbl = Label(window, text="Password Vault")
    lbl.grid(column=1)

    btn = Button(window, text="+", command=add_entry)
    btn.grid(column=1, pady=10)

    lbl = Label(window, text="Application")
    lbl.grid(row=2, column=0, padx=80)
    lbl = Label(window, text="Username")
    lbl.grid(row=2, column=1, padx=80)
    lbl = Label(window, text="Password")
    lbl.grid(row=2, column=2, padx=80)

    cursor.execute("SELECT * FROM vault")
    if cursor.fetchall() != None:
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            lbl2 = Label(window, text=(array[i][1]), font=("Times New Roman", 12))
            lbl2.grid(column=0, row=i+3)
            lbl2 = Label(window, text=(array[i][2]), font=("Times New Roman", 12))
            lbl2.grid(column=1, row=i+3)
            lbl2 = Label(window, text=(array[i][3]), font=("Times New Roman", 12))
            lbl2.grid(column=2, row=i+3)

            btn = Button(window, text="Delete", command=partial(remove_entry, array[i][0]))
            btn.grid(column=3, row=i+3, pady=10)

            i += 1

            cursor.execute("SELECT * FROM vault")
            if len(cursor.fetchall()) <= i:
                break


cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    login_screen()
else:
    first_screen()

window.mainloop()
