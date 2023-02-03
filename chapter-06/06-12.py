friends = {
    "tarun": {
        "likes": "girls",
        "dislikes": "beef",
        "dob": "01-01-1970",
        "nationality": "indian",
    },
    "vishal": {
        "likes": "girls",
        "dislikes": "beef",
        "dob": "01-01-1970",
        "nationality": "indian",
    },
}

friends["tarun"]["likes"] = "girl"

print(friends.get("tarun").get("likes"))
