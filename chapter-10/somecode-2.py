from pathlib import Path
import json

numbers = [1, 3, 5, 7, 9]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
