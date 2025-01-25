def parse_card(card_data):
    """Parse card data into sets of winning and owned numbers."""
    parts = card_data.split('|')
    winning_numbers = set(parts[0].strip().split())
    owned_numbers = set(parts[1].strip().split())
    return winning_numbers, owned_numbers

def calculate_points(card_data):
    """Calculate points for a single card based on matching numbers."""
    winning_numbers, owned_numbers = parse_card(card_data)
    matched_numbers = winning_numbers & owned_numbers

    points = 0
    for _ in matched_numbers:
        points = points * 2 if points else 1
    return points

def load_cards(filename):
    """Load card data from a file and return as a list of strings."""
    with open(filename, 'r') as file:
        return [line.split(':', 1)[1].strip() for line in file]

def calculate_total_points(cards):
    """Calculate the total points for a list of cards."""
    total_points = 0
    for card in cards:
        total_points += calculate_points(card)
    return total_points

# Example usage
if __name__ == "__main__":
    filename = "data/cards.txt"  # Replace with your file's name
    cards = load_cards(filename)
    total_points = calculate_total_points(cards)
    print(f"Total points for all cards: {total_points}")



# Tests for the functional implementation
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

    # Test case 4: Mix of matching and non-matching numbers
    card = "5 6 7 | 7 5 8"
    assert calculate_points(card) == 2, "Test 4 Failed"

    # Test case 5: One matching number with duplicates in one group
    card = "4 4 4 | 4 5 6"
    assert calculate_points(card) == 1, "Test 5 Failed"

    print("All calculate_points tests passed!")

def test_calculate_total_points():
    # Create a temporary list of card data
    cards = [
        "1 2 3 | 4 5 6",  # 0 points
        "8 9 10 | 7 8 11",  # 1 point
        "12 15 20 | 15 12 18"  # 2 points
    ]
    assert calculate_total_points(cards) == 3, "Test Failed"
    print("All calculate_total_points tests passed!")

# Run tests
test_calculate_points()
test_calculate_total_points()
