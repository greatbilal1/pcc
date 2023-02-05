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
