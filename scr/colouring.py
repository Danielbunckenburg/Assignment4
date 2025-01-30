Country = str
NeighbourRelation = list[tuple[Country, Country]]
Colouring = dict[Country, int]

def is_neighbour(nr, c1, c2):
    return (c1, c2) in nr or (c2, c1) in nr



# Example usage of is_neighbour:
example_nr = [("a", "b"), ("b", "c"), ("c", "d")]
print(is_neighbour(example_nr, "a", "b"))  # True
print(is_neighbour(example_nr, "a", "c"))  # False

