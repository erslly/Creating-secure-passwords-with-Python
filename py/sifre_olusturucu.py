import tkinter as tk
import random
import string

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def update_password():
    new_password = generate_secure_password(16)
    password_label.config(text=new_password)

root = tk.Tk()
root.title("Güvenli Şifre Oluşturucu")
root.geometry("400x200")

title_label = tk.Label(root, text="Oluşturulan Güvenli Şifre:", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

password_label = tk.Label(root, text=generate_secure_password(16), font=("Helvetica", 12))
password_label.pack(pady=20)

restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12, "bold"), command=update_password)
restart_button.pack(pady=10)

root.mainloop()
