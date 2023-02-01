usernames = [
    "alzy",
    "welzy",
    "alzywelzy",
    "welzyalzy",
    "manvendra",
    "rajpoot",
    "manvendrarajpoot",
    "rajpootmanvendra",
]

# for username in usernames:
#     print(f"Welcome back, {username}")

# loginUsername = input("Enter login details: ")

# if loginUsername in usernames:
#     print(f"Welcome back, {loginUsername}")

loginUsername = input("Enter login details: ")

if loginUsername == "admin":
    print("Hello admin, would you like to see a status report?")
elif loginUsername in usernames:
    print(f"Hello {loginUsername}, thank you for logging in again.")
else:
    print("NOT IN THE USERNAMES!")
