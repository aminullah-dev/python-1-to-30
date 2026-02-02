profile = {
    "name": "Amin",
    "age": 31,
    "city": "Ottawa"
}

if "age" in profile:
    print("Age exists")


profile["age"] = 32
profile["Skill"] = "python"
del profile["city"]

print(profile)
if profile.get("age", 0) >= 18:
    print("Adult")
else:
    print("under 18")
    