
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

#test
def test_CountWord():
    # Test 1: Basic occurrence
    
    assert CountWord("COMPUTERSCINCE computerscince", "computerscince") == 1, "Test 1 Failed"  
    
    assert CountWord("Computerscince ", "Daniel") == 0, "Test 2 Failed"
    
    assert CountWord("hello Daniel", "hello") == 1, "Test 3 Failed"
    
    assert CountWord("COMPUTERSCINCE computerscince", "computerscince") == 1, "Test 4 Failed"  
    
    assert CountWord("Computerscince Computerscince", "Computerscince") == 2, "Test 5 Failed"
    
    assert CountWord("", "Computerscince") == 0, "Test 6 Failed"
    
    assert CountWord("COMPUTERSCINCE computerscince", "computerscince") == 1, "Test 7 Failed"  
    
    print("All tests passed!")

# Run tests
test_CountWord()

