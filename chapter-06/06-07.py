alzywelzy = {
    "username": "alzywelzy",
    "firstName": "alzy",
    "lastName": "welzy",
    "age": 20,
    "city": "jhansi",
    "nationality": "indian",
}

welzyalzy = {
    "username": "welzyalzy",
    "firstName": "welzy",
    "lastName": "alzy",
    "age": 20,
    "city": "jhansi",
    "nationality": "indian",
}

memelordmaster = {
    "username": "memelordmaster",
    "firstName": "john",
    "lastName": "nagera",
    "age": 20,
    "city": "jhansi",
    "nationality": "indian",
}

users = [alzywelzy, welzyalzy, memelordmaster]

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")
    print("***")
