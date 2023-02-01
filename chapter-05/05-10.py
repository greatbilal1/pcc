current_users = [
    "alzy",
    "welzy",
    "alzywelzy",
    "welzyalzy",
    "alzy_welzy",
]

new_users = [
    "alzywelzy",
    "welzyalzy",
    "manvendrarajpoot",
    "rajpootmanvendra",
    "manraj",
    "AlzyWelzy",
]

for new_user in new_users:
    if new_user in current_users:
        print("This person will need to enter a new username for you to use.")
    else:
        print(f"{new_user} is available for you.")
