Country = str
NeighbourRelation = list[tuple[Country, Country]]
Colouring = dict[Country, int]

def is_neighbour(nr: NeighbourRelation, c1: Country, c2: Country) -> bool:
    """Check if two countries are neighbours.
    
    Args:
        nr (NeighbourRelation): List of tuples representing neighbour relations.
        c1 (Country): The first country.
        c2 (Country): The second country.
        
    Returns:
        bool: True if the countries are neighbours, False otherwise.
    """
    return (c1, c2) in nr or (c2, c1) in nr



def can_extend_colour(nr: NeighbourRelation, country: Country, colouring: Colouring, colour: int) -> bool:
    """Check if a country can be coloured with a specific colour.
    
    Args:
        nr (NeighbourRelation): List of tuples representing neighbour relations.
        country (Country): The country to be coloured.
        colouring (Colouring): Current colouring of countries.
        colour (int): The colour to be assigned.
        
    Returns:
        bool: True if the country can be coloured with the specified colour, False otherwise.
    """
    return all(not is_neighbour(nr, country, other) or colouring.get(other) != colour for other in colouring)




def colour_countries(nr: NeighbourRelation) -> Colouring:
    """Colour countries such that no two neighbouring countries have the same colour.
    
    Args:
        nr (NeighbourRelation): List of tuples representing neighbour relations.
        
    Returns:
        Colouring: A dictionary representing the colouring of each country.
    """
    countries = sorted(set().union(*nr))  # Henter unikke lande
    colouring = {}
    
    for country in countries:
        for colour in range(len(countries)):  # Maksimalt antal farver er antallet af lande
            if can_extend_colour(nr, country, colouring, colour):
                colouring[country] = colour
                break
    
    return colouring

# Example usage of colour_countries:
example_simple = [("da", "se"), ("no", "da"), ("se", "no"), ("de", "da")]
print(colour_countries(example_simple))  # Example output: {'da': 0, 'de': 1, 'no': 2, 'se': 1}