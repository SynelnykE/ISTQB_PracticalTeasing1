# Create a function **check()** that takes three arguments (first dictionary, second dictionary, key) in order to:
# - Return the boolean _True_ if both dictionaries have the same values for the same keys.
# - If the dictionaries don't match, return the string _"Not the same"_, or the string _"One's empty"_ if
# only one of the dictionaries contains the given key.
# _Notes._  
# - Dictionaries are an unordered data type.
# - Double quotes may be helpful.
# - _KeyError_ can occur when trying to access a dictionary key that doesn't exist.  
# _Examples_  
# print(check(dict_first, dict_second, "horde") 
# ➞ "One's empty")
# print(check(dict_first, dict_second, "people") )
# ➞ True)
# print(check(dict_first, dict_second, "sun")
#  ➞ "Not the same")

dict_first = {"sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright"}
dict_second = {"people": 12, "sun": "star", "book": "bad"}


def check(dict1, dict2, key_ch):
    if key_ch not in dict1:
        return "One's empty"
    elif key_ch not in dict2:
        return "One's empty"
    if dict1[key_ch] != dict2[key_ch]:
        return "Not the same"
    if dict1[key_ch] == dict2[key_ch]:
        return True


print(check(dict_first, dict_second, "horde"))
