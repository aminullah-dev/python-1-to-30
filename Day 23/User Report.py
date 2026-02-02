users = [
    {"name": "Amin", "age": 22, "role": "admin"},
    {"name": "Ali", "age": 17, "role": "viewer"},
    {"name": "Sara", "age": 19, "role": "editor"},
    {"name": "Hassan", "age": 30, "role": "admin"}
]

total_users = 0
total_age = 0
admins = 0

for user in users:
    total_users += 1
    total_age += user["age"]

    if user["role"] == "admin":
        admins += 1

average_age = total_age / total_users

print("User Report")
print("-----------")
print("Total users:", total_users)
print("Admins:", admins)
print("Average age:", average_age)
