from pathlib import Path

path = Path("blank.txt")
contents = path.read_text()

for i in range(2):
    print(contents)

contents = contents.replace("chapter", "ehe")

path.write_text(contents)

for i in range(2):
    print(contents)
