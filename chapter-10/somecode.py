from pathlib import Path

path = Path("blank.txt")

with path.open(mode="a") as file:
    file.write("This is a new line of text.\n")
