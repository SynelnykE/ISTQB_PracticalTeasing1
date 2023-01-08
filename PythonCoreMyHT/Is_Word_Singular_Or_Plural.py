#Is word plural form?

word = input("Enter word what would you like to check on plural form ")

def is_plural(word):
    return word.endswith('s')

print("Word ", word, " is ", is_plural(word), "plural form") 