alien_color = ["green", "yellow", "red"]

player_name = input("Enter your username: ")
player_color = input("Guess a color from yellow, green, orange or red: ")

if player_color in alien_color:
    print("You have guess correct color of alien, that was green. 5 points to you")
elif player_color not in alien_color:
    print("You have guess correct color of alien, that was yellow. 10 points to you")
elif player_color not in alien_color:
    print("You have guess correct color of alien, that was red. 15 points to you")
else:
    print("BRUH!")
