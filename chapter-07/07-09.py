sandwiches = [
    "alzy",
    "pastrami",
    "welzy",
    "pastrami",
    "alzywelzy",
    "welzyalzy",
    "pastrami",
]
finished_sandwiches = []

while sandwiches:
    sandwich = sandwiches.pop()
    if sandwich == "pastrami":
        print("We have ran out of pastrami.")
        while "pastrami" in sandwiches:
            sandwiches.remove("pastrami")
        continue

    print(f"I made you {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been confirmed:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
