def calculate_points(card):
    """Calculate the points for a single card."""
    # Split the card into winning numbers and numbers you have
    parts = card.split('|')
    vindernummer = parts[0].strip().split()
    egnenummer = parts[1].strip().split()

    # Convert to sets for fast lookups
    vindernummer = set(vindernummer)
    egnenummer = set(egnenummer)

    # Find matching numbers
    matchedenummer = vindernummer & egnenummer

    # Calculate points based on the rules
    point = 0
    for i, _ in enumerate(matchedenummer):
        if i == 0:
            point += 1  # First match gives 1 point
        else:
            point *= 2  # Subsequent matches double the points

    return point

def total_points_from_file(filename):
    """Calculate the total points from cards in a file."""
    total = 0

    with open(filename, 'r') as file:
        for line in file:

            card_data = line.split(':', 1)[1].strip()
            total += calculate_points(card_data)

    return total

filename = "data/cards.txt"  # Replace with your file's name
total = total_points_from_file(filename)
#print(f"Total points for all cards: {total}")

# Tests for calculate_points function
def test_calculate_points():
    # Test case 1: No matching numbers
    card = "1 2 3 | 4 5 6"
    assert calculate_points(card) == 0, "Test 1 Failed"
    
    # Test case 2: One matching number
    card = "8 9 10 | 7 8 11"
    assert calculate_points(card) == 1, "Test 2 Failed"
    
    # Test case 3: Two matching numbers
    card = "12 15 20 | 15 12 18"
    assert calculate_points(card) == 2, "Test 3 Failed"
    

    # Test case 5: Mix of matching and non-matching numbers
    card = "5 6 7 | 7 5 8"
    assert calculate_points(card) == 2, "Test 4 Failed"
    
    # Test case 6: One matching number with duplicates in one group
    card = "4 4 4 | 4 5 6"
    assert calculate_points(card) == 1, "Test 5 Failed"
    


    print("All tests passed!")

# Run tests
test_calculate_points()
