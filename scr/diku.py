
f = open('Data\diku.txt', "r")

content = f.read() 

def CountWord(text, word):
    count = 0
    start = 0
    while (index := text.find(word, start)) != -1:
        count += 1
        start = index + len(word)  # Move past the last found word
    return count


#print(CountWord(content, "DIKU"))
