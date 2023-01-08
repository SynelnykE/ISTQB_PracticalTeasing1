#takes a string and returns a string with its letters in alphabetical order.

def alphabet_soup(word):
    my_sting = ''.join(sorted(word))
    return '"' + my_sting + '"'
   
print(alphabet_soup(word = list(input("Input word: "))))
