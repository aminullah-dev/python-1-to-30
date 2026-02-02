profile = {
    "name": "Amin",
    "age": 31
}

print("checking user...")

if "age" in profile:
    if profile["age"] >= 18:
        print("Access denied")
    else:
        print("Access denied")
else:
    print("No age info")