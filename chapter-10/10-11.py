from pathlib import Path
import json

path = Path("favorite-number.json")

try:
    favorite_number = int(input("Enter your favorite number: "))
except Exception as e:
    print(e)
else:
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"I know that your favorite number is {favorite_number}")
