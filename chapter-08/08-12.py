def sandwich(*items):
    print("Here is the list of all the items that you gave us:")
    for item in items:
        print(f"- {item}")
    return items


sandwich("ohayo", "sekai", "good", "morning")
# sandwich(a="ohayo", b="sekai", c="good", d="morning")
