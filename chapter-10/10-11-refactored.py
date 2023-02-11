from pathlib import Path
import json


def get_stored_favnum(path):
    """Get stored favorite number if available."""
    if path.exists():
        contents = path.read_text()
        favnum = json.loads(contents)
        return favnum
    else:
        return None


def get_new_favnum(path):
    """Prompt for a new username."""
    favnum = str(input("What's your favorite number? "))
    contents = json.dumps(favnum)
    path.write_text(contents)
    return favnum


def favnum():
    """Display the favorite number."""
    path = Path("favnum.json")
    favnum = get_stored_favnum(path)
    if favnum:
        print(f"Your favorite number is {favnum}.")
    else:
        favnum = get_new_favnum(path)
        print(f"Your favorite number is {favnum}.")


favnum()
