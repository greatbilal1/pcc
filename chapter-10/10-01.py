from pathlib import Path

path = Path("blank.txt")
contents = path.read_text()

for i in range(2):
    print(contents)
