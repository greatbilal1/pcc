users = ["alzy", "welzy", "welzyalzy", "alzywelzy"]
favorite_languages = {
    "alzy": "python",
    "welzy": "javascript",
}

for user in users:
    if user in favorite_languages.keys():
        print(f"Thanks for taking part in the poll, {user.title()}")
    else:
        print(f"Dear {user}, Please take part in the poll.")
