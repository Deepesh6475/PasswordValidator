from tkinter import *
import bcrypt


def validate(password):
    hashed_password = b'$2b$12$KKx55zdRTGxnx3Js2Yb5cOIMndqk9o0qkbqQGSXdzUsJ2ycgB7QI6'
    password = bytes(password, encoding="utf-8")
    if bcrypt.checkpw(password, hashed_password):
        print("Logged in!")
    else:
        print("Invalid Password!")


root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate",
                command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()
