def city_country(city, country, population=0):
    # return f"{city.title()}, {country.title()} {}"
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" -population {population}"
    return output_string
