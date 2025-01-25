def count_word(text, word):
    """
    Counts the occurrences of a word in a text using a purely functional approach.

    Parameters:
    text (str): The text to search within.
    word (str): The word to count.

    Returns:
    int: The number of occurrences of the word in the text.
    """
    def count_occurrences(text, word):
        index = text.find(word)
        if index == -1:
            return 0  # Base case: no more occurrences
        # Add 1 for the current match and recurse with the remaining text
        return 1 + count_occurrences(text[index + len(word):], word)
    
    return count_occurrences(text, word)

# Example usage:
with open('Data/diku.txt', 'r') as f:  # File I/O is external to the functional part
    content = f.read()

# Count occurrences of a specific word
result = count_word(content, "DIKU")
print(result)
