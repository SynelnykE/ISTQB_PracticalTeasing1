#Returns an ordered list containing the indices of all capital letters in the string

word = "hello"

def index_of_caps(word):
    char_list = []
    for i, char in enumerate(word):
        if char.isupper():
            char_list.append(i)
    return char_list
   
print(index_of_caps(word))
