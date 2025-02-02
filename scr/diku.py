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

    if not grid:
        return 0

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
        In the function "Search" it takes in the starting position as a x,y starting point and an direction from 1 out of the 8 direction 
        eg. (-1,0). Then it seperate it from these inputs, after that it make a list of position from the starting point and in the 
        direction that is given and to the lengh of the word that is giving. 
        So it create a list of the exact location of each letter in the word like [(2, 3), (3, 4), (4, 5), (5, 6)], for the word word = "DIKU". 
        
        Then in the next part it uses "return all()" function that only returns True if all parts is true.  The first statement "is_valid" 
        "is using the privously function to make sure that the word is within the boundary. grid[x][y] == word[i]: Ensures that the letter at each position 
        matches the corresponding letter in the word.

        The nested loops iterate over all possible grid positions (x, y).The first check (if grid[x][y] == word[0]) ensures that we only start searching 
        from positions where the first letter of the word matches.The second loop iterates over all directions, calling
        the search function to check if the word can be formed starting from the position (x, y) and moving in the direction (dx, dy).
        

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
print(f"From file DIKU.txt the number of times DIKU is in it is  {count_diku}")  # Should print 18




def test_find_word():
    grid = [
        ['D', 'I', 'K', 'U'],
        ['', 'I', '', ''],
        ['', '', 'K', ''],
        ['', '', '', 'U']
    ]
    
    # Test case 1: Search for "DIKU" in the grid
    count = find_word(grid, "DIKU")
    if count == 2:
        print("test_find_word passed for 'DIKU'.")
    else:
        print(f"test_find_word failed for 'DIKU'. Expected 18, got {count}.")
        
    # Test case 2: Search for a word not in the grid (e.g., "HELLO")
    count = find_word(grid, "HELLO")
    if count == 0:
        print("test_find_word passed for 'HELLO' (not found).")
    else:
        print(f"test_find_word failed for 'HELLO'. Expected 0, got {count}.")
        
    # Test case 3: Search for a word in reverse direction (e.g., "UKID")
    count = find_word(grid, "UKID")
    if count == 2:
        print("test_find_word passed for 'UKID'.")
    else:
        print(f"test_find_word failed for 'UKID'. Expected 18, got {count}.")
        
    # Test case 4: Search for a single character word (e.g., "I")
    count = find_word(grid, "I")
    if count == 2:
        print("test_find_word passed for 'I'.")
    else:
        print(f"test_find_word failed for 'I'. Expected 2, got {count}.")
        
    # Test case 5: Test with an empty grid
    grid = []
    count = find_word(grid, "DIKU")
    if count == 0:
        print("test_find_word passed for empty grid.")
    else:
        print(f"test_find_word failed for empty grid. Expected 0, got {count}.")


# Run the tests manually
test_find_word()


