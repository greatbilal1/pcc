favorite_fruits = ["apple", "banana", "mango"]

playerFruit = None

while playerFruit != "n":
    playerFruit = input("Enter a fruit name to check or type n to exit: ")
    if playerFruit in favorite_fruits:
        print(f"You really like {playerFruit}")
    else:
        print(f"You don't really like {playerFruit}")
