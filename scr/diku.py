def find_word(grid, word):
    """
    Searches for all instances of a word in a 2D grid, considering all possible directions.
    
    Args:
    - grid (list of list of str): The 2D grid containing characters.
    - word (str): The word to search for in the grid.

    Returns:
    - tuple: A tuple containing:
        - An integer representing the number of times the word is found in the grid.
        - A list of tuples where each tuple contains the starting position (x, y) and the direction (dx, dy) of the word in the grid.
    """
    if not grid or not grid[0]:  # Check if grid is empty or has no rows
        return 0, []

    if not word:  # Check if the word is empty
        return 0, []

    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_valid(x, y):
        """
        Checks if a position (x, y) is within the bounds of the grid.
        
        Args:
        - x (int): The x-coordinate of the position.
        - y (int): The y-coordinate of the position.

        Returns:
        - bool: True if the position is within the grid, False otherwise.
        """
        return 0 <= x < rows and 0 <= y < cols

    def search(start, direction):
        """
        Searches for the word starting from a given position in a specified direction.
        
        Args:
        - start (tuple): A tuple (x, y) representing the starting position.
        - direction (tuple): A tuple (dx, dy) representing the direction to move in.

        Returns:
        - bool: True if the word is found starting from the given position and direction, False otherwise.
        """
        x, y = start
        dx, dy = direction
        positions = [(x + i * dx, y + i * dy) for i in range(len(word))]
        return all(
            is_valid(nx, ny) and grid[nx][ny] == char
            for (nx, ny), char in zip(positions, word)
        )

    starts = [
        (x, y)
        for x in range(rows)
        for y in range(cols)
        if grid[x][y] == word[0]
    ]

    found_positions = list(
        filter(
            lambda pos: any(search(pos, direction) for direction in directions),
            starts,
        )
    )

    return len(found_positions), found_positions


def test_find_word():
    """
    Runs a series of tests to check the behavior of the find_word function under various edge cases.
    """
    # Test 1: Empty Grid
    grid_empty = []
    word_empty_grid = "TEST"
    count_empty_grid, _ = find_word(grid_empty, word_empty_grid)
    print(f"Empty grid result: {count_empty_grid}")  # Expected: 0

    # Test 2: Empty Word
    grid_normal = [
        [".", ".", "D", ".", ".", "."],
        [".", "U", "K", "I", "D", "."],
        [".", "K", ".", ".", "K", "."],
        ["D", "I", "K", "U", ".", "U"],
        [".", "D", ".", ".", ".", "."]
    ]
    word_empty = ""
    count_empty_word, _ = find_word(grid_normal, word_empty)
    print(f"Empty word result: {count_empty_word}")  # Expected: 0

    # Test 3: Grid with Only One Letter
    grid_one_letter = [
        ["A", "A", "A"],
        ["A", "A", "A"],
        ["A", "A", "A"]
    ]
    word_not_found = "DIKU"
    count_not_found, _ = find_word(grid_one_letter, word_not_found)
    print(f"Grid with one letter (not found): {count_not_found}")  # Expected: 0

    # Test 4: Word Larger than Grid Dimensions
    grid_small = [
        ["D", "I", "K"],
        ["U", "K", "U"]
    ]
    word_large = "DIKUTEST"
    count_large_word, _ = find_word(grid_small, word_large)
    print(f"Word larger than grid dimensions: {count_large_word}")  # Expected: 0

    # Test 5: Word Present Only Partially in Some Directions
    grid_partial_word = [
        ["D", ".", ".", ".", "."],
        [".", "I", ".", ".", "."],
        [".", ".", "K", ".", "."],
        [".", ".", ".", "U", "."]
    ]
    word_partial = "DIKU"
    count_partial, _ = find_word(grid_partial_word, word_partial)
    print(f"Partial word match: {count_partial}")  # Expected: 0 (incomplete matches)

    # Test 6: Word at the Edge of the Grid
    grid_edge = [
        ["D", "I", "K"],
        ["U", ".", "."],
        [".", ".", "."]
    ]
    word_edge = "DIK"
    count_edge, _ = find_word(grid_edge, word_edge)
    print(f"Word at the edge: {count_edge}")  # Expected: 1 (from the top-left corner)

    # Test 7: Invalid Characters in Grid
    grid_invalid_chars = [
        ["@", "#", "$"],
        ["%", "&", "*"],
        ["!", "(", ")"]
    ]
    word_with_symbols = "DIKU"
    count_invalid_chars, _ = find_word(grid_invalid_chars, word_with_symbols)
    print(f"Invalid characters grid: {count_invalid_chars}")  # Expected: 0

    # Test 8: Word Found in Multiple Directions
    grid_multiple_directions = [
        ["D", "I", "K", "U"],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]
    word_multiple = "DIKU"
    count_multiple_directions, _ = find_word(grid_multiple_directions, word_multiple)
    print(f"Word in multiple directions: {count_multiple_directions}")  # Expected: 2 (horizontal, diagonal)


# Run the test function
test_find_word()
