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


filename = "../Data/cards.txt"
cards = load_cards(filename)
total_points = calculate_total_points(cards)
print(f"Total points: {total_points}")