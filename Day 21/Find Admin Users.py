users = [
    {"name": "Amin", "age": 22, "role": "admin"},
    {"name": "Ali", "age": 17, "role": "viewer"},
    {"name": "Sara", "age": 19, "role": "editor"},
    {"name": "Hassan", "age": 30, "role": "admin"}
]

print("Admins:")
for user in users:
    if user["role"] == "admin":
        print("-", user["name"])

