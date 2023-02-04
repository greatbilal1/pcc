sandwiches = ["alzy", "welzy", "alzywelzy", "welzyalzy"]
finished_sandwiches = []

while sandwiches:
    sandwich = sandwiches.pop()
    print(f"I made you {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been confirmed:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
