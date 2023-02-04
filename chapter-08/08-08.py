def make_album(name="alzywelzy", title="ohayo", num_song=None):
    make_album = {
        "name": name,
        "title": title,
    }

    if num_song:
        make_album["num_song"] = int(num_song)

    return make_album


while True:
    print("Enter q to exit")
    name = input("Enter the name of the artist: ")
    if name == "q":
        break

    title = input("Enter the title of the album: ")
    if title == "q":
        break

    songs = input("Enter the number of songs, leave empty if none: ")
    if songs == "q":
        break

    if songs != "":
        print(make_album(name, title, songs))
        continue

    print(make_album(name, title))
