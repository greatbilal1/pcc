def population_city_functions(city, country, population=""):
    if population:
        return f"{city}, {country} - Population {population}".title()
    else:
        return f"{city}, {country}".title()
