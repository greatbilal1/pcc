from pathlib import Path

path = Path("blank.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    print(line)
    pi_string += line.strip()

print(pi_string)


print(repr(pi_string))
