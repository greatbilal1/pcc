alzy = "AlZy"
welzy = "WeLsy"
alzywelzy = ["alzy", "welzy"]

print(alzy == "Alzy")
print(alzy == "AlZy")
print(alzy.lower() == "alzy")
print(alzy.lower() == "welzy" and welzy.lower() == "alzy")
print(alzy.lower() == "alzy" or welzy.lower() == "alzy")
print("alzy" in alzywelzy)
print("alzy" not in alzywelzy)
