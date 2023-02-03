cities = {
    "jhansi": {
        "population": "10_000_000",
        "majority": "hindu",
        "state": "uttar pradesh",
        "part": "central india",
    },
    "kolkata": {
        "population": "1_000_000",
        "majority": "hindu",
        "state": "west bengal",
        "part": "north east",
    },
    "madras": {
        "population": "1_000_000",
        "majority": "hindu",
        "state": "tamil nadu",
        "part": "south india",
    },
}

for key, city in cities.items():
    for k, v in cities.get(key).items():
        print(f"{k}: {v}")
    print("***")
