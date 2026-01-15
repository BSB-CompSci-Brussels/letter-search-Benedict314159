
def countLetters(anyText:str,anyLetter:str)->int:
    counter = 0
    for letter in anyText:
        if letter == anyLetter:
            counter += 1
    return counter

print(countLetters("hello world", "o"))  # Output: 2
