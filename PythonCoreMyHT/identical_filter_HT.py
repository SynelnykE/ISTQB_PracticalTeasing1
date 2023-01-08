# Create a function **identical_filter()** that keeps only strings with repeating identical characters 
# (in other words, it has a set size of 1).  
# _Notes._
# A string with a single character is trivially counted as a string with repeating identical characters.
# If there are no strings with repeating identical characters, return an empty array

# _Examples_```plaintext 
# identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]) ➞ ["aaaaaa", "d", "eeee"]
# identical_filter(["88", "999", "22", "545", "133"]) ➞ ["88", "999", "22"]
# identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]) ➞ []

def identical_filter(words):
    new_lst = []    
    for i in words:
        new_word = []
        for l in i:
            new_word.append(l)
        if len(set(new_word)) == 1:   
            new_lst.append(i)
    return new_lst
        
print(identical_filter(["88", "999", "22", "545", "133"]))
