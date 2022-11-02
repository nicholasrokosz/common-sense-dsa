from string import ascii_lowercase

def find_missing_letter(sentence):
    letters = list(ascii_lowercase)
    chars = {}
    
    for char in sentence.lower():
        chars[char] = True

    for letter in letters:
        if letter not in chars:
            return letter



print(find_missing_letter("The quick brown box jumps over the lazy dog."))
