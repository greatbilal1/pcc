favorite_places = {
    "mavendra": {
        "first": "manvendra",
        "last": "rajpoot",
        "username": "alzywelzy",
        "favorite_place": "kyoto",
    },
    "amit": {
        "first": "amit",
        "last": "rajpoot",
        "username": "gamingwarrior",
        "favorite_place": "manali",
    },
    "meghansh": {
        "first": "meghansh",
        "last": "rajpoot",
        "username": "meghansh",
        "favorite_place": "kashmir",
    },
}

for place in favorite_places.keys():
    for k, v in favorite_places.get(place).items():
        print(f"{k}: {v}")
    print("***")
