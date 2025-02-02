def parse_card(card_data):
    """
    Parses a string containing card data into two sets of numbers: 
    winning numbers and owned numbers.

    Parameters:
    card_data (str): A string formatted as "winning_numbers | owned_numbers", 
                     where each part is a space-separated list of numbers.

    Returns:
    tuple: A tuple containing two sets:
        - winning_numbers (set): A set of numbers from the first part of card_data.
        - owned_numbers (set): A set of numbers from the second part of card_data.

    Raises:
    ValueError: If the card_data format is invalid (does not contain exactly one '|').
    """
    parts = card_data.split('|')
    
    # Check if the card data has exactly two parts separated by '|'
    if len(parts) != 2:
        raise ValueError("Invalid card format. Expected 'winning_numbers | owned_numbers'.")
    
    winning_numbers = set(parts[0].strip().split())
    owned_numbers = set(parts[1].strip().split())
    
    return winning_numbers, owned_numbers

def calculate_points(card_data):
    """
    Calculates the total points for a single card based on the match between 
    the winning numbers and the owned numbers. Points are calculated with 
    exponential growth: the first match earns 1 point, and each subsequent match 
    doubles the points.

    Parameters:
    card_data (str): A string formatted as "winning_numbers | owned_numbers", 
                     representing the card's data.

    Returns:
    int: The total points for the card based on the matched numbers.

    Raises:
    ValueError: If the card_data format is invalid, it will propagate the exception 
                raised by `parse_card`.
    """
    winning_numbers, owned_numbers = parse_card(card_data)
    matched_numbers = winning_numbers & owned_numbers

    points = 0
    for _ in matched_numbers:
        points = points * 2 if points else 1
    return points

def load_cards(filename):
    """
    Loads card data from a file where each line contains a card in the format 
    'Card_Name: card_data'. It returns a list of card data strings.

    Parameters:
    filename (str): The path to the file containing card data.

    Returns:
    list of str: A list of card data strings, where each string is the data part 
                 (after the colon) from each line in the file.

    Raises:
    FileNotFoundError: If the file is not found.
    IOError: If there is an issue reading the file.
    """
    with open(filename, 'r') as file:
        return [line.split(':', 1)[1].strip() for line in file]

def calculate_total_points(cards):
    """
    Calculates the total points from a list of cards. It calls `calculate_points` 
    to sum the points for each card.

    Parameters:
    cards (list of str): A list of strings representing the card data, 
                         each in the format "winning_numbers | owned_numbers".

    Returns:
    int: The total points from all the cards.

    Raises:
    ValueError: If any card data format is invalid, it will propagate the exception 
                raised by `calculate_points`.
    """
    total_points = 0
    for card in cards:
        total_points += calculate_points(card)
    return total_points


cards = load_cards( "../Data/cards.txt")
total_points = calculate_total_points(cards)
print(f"Total points: {total_points}")


def test_parse_card():
    # Valid test cases
    result = parse_card("1 2 3 | 4 5")
    assert result == ({'1', '2', '3'}, {'4', '5'}), f"Expected ({'1', '2', '3'}, {'4', '5'}), but got {result}"

    result = parse_card("1 | 2")
    assert result == ({'1'}, {'2'}), f"Expected ({'1'}, {'2'}), but got {result}"

    # Invalid test cases
    try:
        parse_card("1 2 3 4")
        print("Failed: No error raised for missing '|'")
    except ValueError:
        pass  # Expected error, do nothing

    try:
        parse_card("1 2 3 | 4 | 5")
        print("Failed: No error raised for extra '|'")
    except ValueError:
        pass  # Expected error, do nothing

    print("test_parse_card passed")

def test_points():
    # Valid test cases
    result = calculate_points("34 8 54 | 84 17 3")
    assert result == 0, f"Expected 0, but got {result}"

    result = calculate_points("34 8 54  | 54 8")
    assert result == 2, f"Expected 2, but got {result}"


    result = calculate_points("34 8 54  | ")
    assert result == 0, f"Expected 0, but got {result}"

    print("test_points passed")

def test_load_cards():
    # Creating a temporary test file
    with open('test_file.txt', 'w') as f:
        f.write("Card1: 1 2 3 | 3 4\nCard2: 4 5 6 | 1 2")

    result = load_cards('test_file.txt')
    assert result == ['1 2 3 | 3 4', '4 5 6 | 1 2'], f"Expected ['1 2 3 | 3 4', '4 5 6 | 1 2], but got {result}"

    print("test_load_cards passed")

def test_calculate_total_points():
    # Test cases
    cards = ['1 2 3 | 3 4', '4 5 6 | 1 2']
    result = calculate_total_points(cards)
    assert result == 1, f"Expected 1, but got {result}"

    cards = []
    result = calculate_total_points(cards)
    assert result == 0, f"Expected 0, but got {result}"

    print("test_calculate_total_points passed")


# Run all tests
test_parse_card()
test_points()
test_load_cards()
test_calculate_total_points()

print("All tests passed!")
