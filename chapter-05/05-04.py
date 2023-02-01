alien_color = ["green", "yellow", "red"]

player_name = input("Enter your username: ")
player_color = input("Guess a color from yellow, green, orange or red: ")

if player_color in alien_color:
    print("You have guess correct color of alien, that was green.")
elif player_color not in alien_color:
    print(
        "You have earned 10 points for some reason even though you didn't guessed the correct answer."
    )
else:
    print("BRUH!")
