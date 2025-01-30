
Country = str
NeighbourRelation = list[tuple[Country, Country]]
Colouring = dict[Country, int]

def is_neighbour(nr, c1, c2):
    return (c1, c2) in nr or (c2, c1) in nr

def can_extend_colour(nr, country, colouring, colour):
    return all(not is_neighbour(nr, country, other) or colouring.get(other) != colour for other in colouring)


def colour_countries(nr):
    countries = countries = sorted(set().union(*nr))  # Henter unikke lande
    colouring = {}
    
    for country in countries:
        for colour in range(len(countries)):  # Maksimalt antal farver er antallet af lande
            if can_extend_colour(nr, country, colouring, colour):
                colouring[country] = colour
                break
    
    return colouring


# Example usage of colour_countries:
example_simple = [("da", "se"), ("no", "da"), ("se", "no"), ("de", "da")]
print(colour_countries(example_simple))  # Example output: [('da', 0), ('de', 1), ('no', 2), ('se', 1)]
