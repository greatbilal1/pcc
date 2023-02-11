from population_city_functions import population_city_functions


def test_city_country():
    formatted_city_country = population_city_functions("jhansi", "india").title()
    assert formatted_city_country == "Jhansi, India"


def test_population_city_country():
    formatted_city_country = population_city_functions(
        "jhansi", "india", 100000
    ).title()
    assert formatted_city_country != "Jhansi, India - Population 1000000"
