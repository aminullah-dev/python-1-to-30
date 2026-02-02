import tkinter as tk
from tkinter import messagebox

users = []

def add_user():
    name = name_var.get().strip()
    age_text = age_var.get().strip()
    role = role_var.get().strip().lower()

    if not name:
        messagebox.showerror("Error", "Name is required.")
        return

    if not age_text.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return

    age = int(age_text)

    if role not in ["admin", "editor", "viewer"]:
        messagebox.showerror("Error", "Role must be: admin / editor / viewer")
        return

    users.append({"name": name, "age": age, "role": role})
    user_list.insert(tk.END, f"{name} | {age} | {role}")

    name_var.set("")
    age_var.set("")
    role_var.set("viewer")

def show_report():
    if len(users) == 0:
        messagebox.showinfo("Report", "No users saved yet.")
        return

    total_users = len(users)
    total_age = 0
    admins = 0

    for user in users:
        total_age += user["age"]
        if user["role"] == "admin":
            admins += 1

    avg_age = total_age / total_users

    report = (
        f"Total users: {total_users}\n"
        f"Admins: {admins}\n"
        f"Average age: {avg_age:.2f}"
    )
    messagebox.showinfo("User Report", report)

def clear_all():
    users.clear()
    user_list.delete(0, tk.END)
    messagebox.showinfo("Done", "All users cleared.")

root = tk.Tk()
root.title("User Report App - Day 23 GUI")
root.geometry("520x420")

title = tk.Label(root, text="User Report App", font=("Arial", 18, "bold"))
title.pack(pady=10)

form = tk.Frame(root)
form.pack(pady=5)

name_var = tk.StringVar()
age_var = tk.StringVar()
role_var = tk.StringVar(value="viewer")

tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
tk.Entry(form, textvariable=name_var, width=28).grid(row=0, column=1, padx=6, pady=6)

tk.Label(form, text="Age:").grid(row=1, column=0, sticky="e", padx=6, pady=6)
tk.Entry(form, textvariable=age_var, width=28).grid(row=1, column=1, padx=6, pady=6)

tk.Label(form, text="Role:").grid(row=2, column=0, sticky="e", padx=6, pady=6)
role_menu = tk.OptionMenu(form, role_var, "admin", "editor", "viewer")
role_menu.config(width=25)
role_menu.grid(row=2, column=1, padx=6, pady=6)

buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Add User", width=12, command=add_user).grid(row=0, column=0, padx=6)
tk.Button(buttons, text="Show Report", width=12, command=show_report).grid(row=0, column=1, padx=6)
tk.Button(buttons, text="Clear All", width=12, command=clear_all).grid(row=0, column=2, padx=6)

tk.Label(root, text="Users:").pack(anchor="w", padx=12)

user_list = tk.Listbox(root, height=10, width=60)
user_list.pack(padx=12, pady=6, fill="both", expand=True)

root.mainloop()
