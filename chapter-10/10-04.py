from pathlib import Path

#  = input("What's your name? ")
path = Path("guests.txt").write_text(
    f"""It's name is {input(f"What's your name? ")}."""
)
# path = Path("guests.txt").write_text(f"It's name is {name}.")
