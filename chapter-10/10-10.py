from pathlib import Path

path = Path("14006.txt")
content = path.read_text().lower()

# print(content)

print(content.count("the"))
