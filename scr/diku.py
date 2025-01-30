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
            is_valid(nx1, ny1) and grid[nx1][ny1] == char
            for (nx1, ny1), char in zip(positions, word)
        )

    starts = [
        (x, y)
        for x in range(rows)
        for y in range(cols)
        if grid[x][y] == word[0]
    ]


    found_count = sum( 1 for pos in starts if any(search(pos, direction) for direction in directions)
)
    return found_count


grid_normal = [
        [".", ".", "D", ".", ".", "."],
        [".", "U", "K", "I", "D", "."],
        [".", "K", ".", ".", "K", "."],
        ["D", "I", "K", "U", ".", "U"],
        [".", "D", ".", ".", ".", "."]
    ]
count_empty_word = find_word(grid_normal, "DIKU")
print(count_empty_word)
