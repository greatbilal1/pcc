bhura = {
    "race": "dog",
    "name": "bhura",
    "personality": "energetic",
    "owner": "ravi",
    "breed": "desi",
}

bhuri = {
    "race": "dog",
    "name": "bhuri",
    "personality": "lazy",
    "owner": "kamla",
    "breed": "desi",
}

neko = {
    "race": "car",
    "name": "neko",
    "personality": "introvert",
    "owner": "rajveer",
    "breed": "desi",
}

tomy = {
    "race": "tortoise",
    "name": "tomy",
    "personality": "extrovert",
    "owner": "rajdeep",
    "breed": "videshi",
}

pets = [bhura, bhuri, neko, tomy]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("***")
