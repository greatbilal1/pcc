from pathlib import Path

catPath = Path("cats.txt")
dogPath = Path("dogs.txt")


try:
    catContent = catPath.read_text()
    dogContent = dogPath.read_text()
except FileNotFoundError as e:
    # print(e)
    pass
else:
    print(catContent)
    print(dogContent)
