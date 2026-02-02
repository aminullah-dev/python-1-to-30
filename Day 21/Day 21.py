users = [
    {"name": "Amin", "age": 22,"role": "admin"},
    {"name": "Ali", "age": 17, "role": "viewer"},
    {"name": "Sara", "age": 19, "role": "editor"}
]
print(users)

for user in users:
    print("Name:", user.get("name"), "| Role:", user.get("role"))

for user in users:
    if user["age"] >=18:
        print(user["name"], "is adult")