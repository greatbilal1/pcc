from city_functions import city_functions


def test_city_country():
    formatted_city_country = city_functions("jhansi", "india").title()
    assert formatted_city_country == "Jhansi, India"
