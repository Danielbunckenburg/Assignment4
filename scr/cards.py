def parse_card(card_data): 
    """Parse card data into sets of winning and owned numbers."""
    parts = card_data.split('|')
    
    # Check if the card data has exactly two parts separated by '|'
    if len(parts) != 2:
        raise ValueError("Invalid card format. Expected 'winning_numbers | owned_numbers'.")
    
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






# Test 1: Empty card data
card_data_1 = "|"
try:
    print(f"Points for empty card data: {calculate_points(card_data_1)}")
except ValueError as e:
    print(f"Error: {e}")

# Test 2: Non-numeric input in card data
card_data_2 = "1 2 3 | a b c"
try:
    print(f"Points for non-numeric input: {calculate_points(card_data_2)}")
except ValueError as e:
    print(f"Error: {e}")

# Test 3: Invalid card format (no '|')
card_data_3 = "1 2 3 4 5"
try:
    print(f"Points for invalid format: {calculate_points(card_data_3)}")
except ValueError as e:
    print(f"Error: {e}")

# Test 4: Extra whitespace in card data
card_data_4 = " 1  2  3  | 4  5  6 "
try:
    print(f"Points for extra whitespace: {calculate_points(card_data_4)}")
except ValueError as e:
    print(f"Error: {e}")

# Test 5: Malformed card data in file
# Assuming a file with the following content:
# card1 | 1 2 3 | 4 5 6
# card2 | 7 8 9 | 10 11 12
filename = "data/cards.txt"  # File should contain malformed data

# Test 6: File does not exist
try:
    cards = load_cards("invalid_file.txt")
except Exception as e:
    print(f"Error loading cards: {e}")

# Test 7: Card data with only one number in each set
card_data_5 = "1 | 1"
try:
    print(f"Points for single number match: {calculate_points(card_data_5)}")
except ValueError as e:
    print(f"Error: {e}")
