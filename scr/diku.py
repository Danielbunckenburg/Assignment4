def read_grid_from_file(filename):
    """
    Reads a grid from a text file and returns it as a 2D list of characters.
    
    Args:
        filename (str): The path to the file containing the grid.

    Returns:
        list[list[str]]: A 2D list where each inner list represents a row of the grid.

    Behavior:
        - Reads the file line by line.
        - Strips whitespace and ignores empty lines.
        - Converts each line into a list of characters.

    """
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]


def find_word(grid, word):
    """
    Finds all occurrences of a word in a 2D grid considering all possible directions.

    Args:
        grid (list[list[str]]): The 2D grid of characters.
        word (str): The word to search for.

    Returns:
        int: The total number of occurrences of the word in the grid.

    Behavior:
        - Searches for the word in 8 possible directions:
            1. Left to right
            2. Right to left
            3. Top to bottom
            4. Bottom to top
            5. Diagonal (top-left to bottom-right)
            6. Diagonal (bottom-right to top-left)
            7. Diagonal (top-right to bottom-left)
            8. Diagonal (bottom-left to top-right)
        - Counts overlapping occurrences of the word.
        - Ensures words are counted even if they cross boundaries.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_valid(x, y):
        """
        Checks if a given position (x, y) is within the bounds of the grid.

        Args:
            x (int): Row index.
            y (int): Column index.

        Returns:
            bool: True if the position is within the grid, False otherwise.
        """
        return 0 <= x < rows and 0 <= y < cols

    def search(start_x, start_y, dx, dy):
        """
        Searches for the word starting from a given position in a specified direction.

        Args:
            start_x (int): Starting row index.
            start_y (int): Starting column index.
            dx (int): Row movement direction.
            dy (int): Column movement direction.

        Returns:
            int: 1 if the word is found starting at (start_x, start_y) in (dx, dy) direction, otherwise 0.
        """
        positions = [(start_x + i * dx, start_y + i * dy) for i in range(len(word))]
        if all(is_valid(x, y) and grid[x][y] == word[i] for i, (x, y) in enumerate(positions)):
            return 1  # Found one occurrence
        return 0  # No occurrence

    found_count = 0


    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:  # Only check positions where the word could start
                for dx, dy in directions:
                    found_count += search(x, y, dx, dy)

    return found_count


# Read grid from file
grid = read_grid_from_file("../Data/diku.txt")

# Search for "DIKU"
count_diku = find_word(grid, "DIKU")
print(count_diku)  # Should print 18
