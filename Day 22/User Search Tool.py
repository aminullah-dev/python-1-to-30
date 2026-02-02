users = [
    {"name": "Amin", "age": 22, "role": "admin"},
    {"name": "Ali", "age": 17, "role": "viewer"},
    {"name": "Sara", "age": 19, "role": "editor"},
    {"name": "Hassan", "age": 30, "role": "admin"}
]

search_name = "Sara"
for user in users:
    if user["name"] == search_name:
        print("Found:", user)

for user in users:
    if user["age"] >= 18 and user["role"] == "admin":
        print(user["name"])
    
serch_name = input("enter name: ")

found = False

for user in users:
    if user["name"] .lower() == serch_name.lower():
        print("user found:")
        print("Name:", user["name"])
        print("Age:", user["age"])
        print("Role:", user["role"])
        found = True
if not found:
    print("User not found")

