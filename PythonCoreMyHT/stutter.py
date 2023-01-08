#a word as if someone is struggling to read it

word = input("Input word for readding: ")

def stutter(word):
    stut = ((word[:2]) + "... ")*2 + word + "?"
    return stut

print(stutter(word))
