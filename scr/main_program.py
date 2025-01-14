#This is the start of the program.

#os.chdir("")

#Question 3


# Replace 'file.txt' with your file's path
with open('Data\diku.txt', 'r') as file:
    content = file.read()  # Reads the entire file as a string

#print(content)

#with open('Data\diku.txt', 'r') as file:
   # content = file.read().strip()  # Removes leading and trailing whitespaces/newlines

def count_word_no_spaces(text, word):
    """
    Counts the number of times a word appears in a string, even if there are no spaces.

    Args:
        text (str): The string to search in.
        word (str): The word to count.

    Returns:
        int: The number of occurrences of the word in the string.
    """
    count = 0
    start = 0
    while (index := text.find(word, start)) != -1:
        count += 1
        start = index + len(word)  # Move past the last found word
    return count


print(count_word_no_spaces(content, "DIKU"))