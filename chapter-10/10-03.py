from pathlib import Path

path = Path("blank.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line
    print(line)

print(pi_string)
