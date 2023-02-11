from population_city_functions import population_city_functions


def test_city_country():
    formatted_city_country = population_city_functions("jhansi", "india").title()
    assert formatted_city_country == "Jhansi, India"
