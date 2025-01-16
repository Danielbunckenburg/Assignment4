def calculate_points(card):
    """Calculate the points for a single card."""
    # Split the card into winning numbers and numbers you have
    parts = card.split('|')
    winning_numbers = parts[0].strip().split()
    numbers_you_have = parts[1].strip().split()

    # Convert to sets for fast lookups
    winning_numbers_set = set(winning_numbers)
    numbers_you_have_set = set(numbers_you_have)

    # Find matching numbers
    matching_numbers = winning_numbers_set & numbers_you_have_set

    # Calculate points based on the rules
    points = 0
    for i, _ in enumerate(matching_numbers):
        if i == 0:
            points += 1  # First match gives 1 point
        else:
            points *= 2  # Subsequent matches double the points

    return points

def total_points_from_file(filename):
    """Calculate the total points from cards in a file."""
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            # Extract the part after 'Card   X:'
            card_data = line.split(':', 1)[1].strip()
            total += calculate_points(card_data)

    return total

filename = "data/cards.txt"  # Replace with your file's name
total = total_points_from_file(filename)
#print(f"Total points for all cards: {total}")
