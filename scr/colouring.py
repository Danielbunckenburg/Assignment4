#this is my solution

class Country:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        neighbors_names = [n.name for n in self.neighbors]
        return f"Country(name={self.name}, neighbors={neighbors_names})"


def create_graph(neighbour_relation):
    country_map = {}

    for c1, c2 in neighbour_relation:
        if c1 not in country_map:
            country_map[c1] = Country(c1)
        if c2 not in country_map:
            country_map[c2] = Country(c2)

        country_map[c1].add_neighbor(country_map[c2])
        country_map[c2].add_neighbor(country_map[c1])

    return list(country_map.values())


# Example usage
simple = [("da", "se"), ("no", "da"), ("se", "no"), ("de", "da")]

countries_graph = create_graph(simple)
for country in countries_graph:
    print(country)



















# Simple neighbour relation example
simple = [("da", "se"), ("no", "da"), ("se", "no"), ("de", "da")]

# Involved neighbour relation example
involved = [
    # Outer ring connections among themselves + ocean
    ("a", "b"), ("a", "d"), ("a", "ocean"), ("b", "c"), ("b", "ocean"), ("c", "d"), ("c", "ocean"), ("d", "ocean"),

    # Each outer region touches two inner regions
    ("a", "e"), ("a", "f"), ("b", "f"), ("b", "g"), ("c", "g"), ("c", "h"), ("d", "e"), ("d", "h"),

    # Inner ring connections among themselves + lake
    ("e", "f"), ("e", "h"), ("e", "lake"), ("f", "g"), ("f", "lake"), ("g", "h"), ("g", "lake"), ("h", "lake")
]

# Check if two countries are neighbours
def is_neighbour(nr, c1, c2):
    return any((c1 == p[0] and c2 == p[1]) or (c1 == p[1] and c2 == p[0]) for p in nr)

# Check if a colour can be extended with a new country
def can_extend_colour(nr, country, colour):
    return all(not is_neighbour(nr, c, country) for c in colour)

# Assign a colour to a country
def give_colour(nr, country, colouring):
    if not colouring:
        return [[country]]
    for col in colouring:
        if can_extend_colour(nr, country, col):
            return [col + [country]] + colouring
    return colouring + [[country]]

# Extract all unique countries from the neighbour relation
def countries(nr):
    return list(set([c for pair in nr for c in pair]))

# Colour the countries based on the neighbour relations
def colour_countries(nr):
    cs = countries(nr)
    colouring = []
    for c in cs:
        colouring = give_colour(nr, c, colouring)
    return colouring

# Examples
simple_colouring = colour_countries(simple)
involved_colouring = colour_countries(involved)

print("Simple Colouring:", simple_colouring)
print("Involved Colouring:", involved_colouring)
