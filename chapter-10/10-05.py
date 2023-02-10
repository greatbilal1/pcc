from pathlib import Path

contents = ""
while True:
    name = input('What\'s your name? \n(Enter "q" to exit)\n')
    contents += name + "\n"
    if name == "q":
        break

path = Path("guests.txt").write_text(contents)
