from random import choices

stuff = (
    "1",
    "2",
    "3",
    "4",
    "1",
    "4",
    "5",
    "1",
    "2",
    "1",
    "a",
    "x",
    "y",
    "b",
)

lottery = "".join(choices(stuff, k=4))

print(f"Any ticket matching these digits wins the prize: {lottery}.")

my_ticket = "xx12"

i = 1

while my_ticket != lottery:
    i += 1
    lottery = "".join(choices(stuff, k=4))
    print(f"Any ticket matching these digits wins the prize: {lottery}.")


print(f"It took you {i} tries.")
