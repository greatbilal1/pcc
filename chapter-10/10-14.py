from pathlib import Path
import json

# def get_stored_favnum(path):
#     """Get stored favorite number if available."""
#     if path.exists():
#         contents = path.read_text()
#         try:
#             favnum = json.loads(contents)
#             return favnum
#         except json.decoder.JSONDecodeError as e:
#             print(f"An error occurred while reading the file: {e}")
#             return None
#     else:
#         return None


def allNames(path):
    pass


def get_stored_favnum(path):
    """Get stored favorite number if available."""
    if path.exists():
        contents = path.read_text()
        if contents == "":
            return None
        favnum = json.loads(contents)
        print(favnum)
        return favnum
    else:
        return None


def get_new_favnum(path, username):
    """Prompt for a new username."""
    favnum = {}
    # username = input("What's your username: ")
    favnum["name"] = username
    favnum["num"] = input("What's your favorite number? ")
    contents = json.dumps(favnum)
    path.write_text(contents)
    return favnum


def favnum():
    """Display the favorite number."""
    username = input("Enter your username: ")
    path = Path("favnum.json")
    favnum = get_stored_favnum(path)

    if favnum and favnum.get("name") == username:
        print(f"Dear {favnum.get('name')},Your favorite number is {favnum.get('num')}.")
    else:
        favnum = get_new_favnum(path, username)
        print(f"Dear {favnum.get('name')},Your favorite number is {favnum.get('num')}.")


favnum()
