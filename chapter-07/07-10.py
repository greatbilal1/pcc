polls = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to spend the rest of your life? ")

    polls[name] = response

    repeat = input("Would you like to let other person respond? (yes/no) ")

    if repeat == "no":
        active = False

print("\n--- Poll Results ---")
for name, response in polls.items():
    print(f"{name} would love to spend the rest of her life in {response}.")
