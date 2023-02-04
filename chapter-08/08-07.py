def make_album(name="alzywelzy", title="ohayo", num_song=None):
    make_album = {
        "name": name,
        "title": title,
    }

    if num_song:
        make_album["num_song"] = num_song

    return make_album


print(make_album("a", "b", 2))
