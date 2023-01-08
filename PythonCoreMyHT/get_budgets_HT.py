# Create the function **get_budgets()** that takes a list of dictionaries and returns the sum of people's budgets.
# _Examples_
# ```plaintext
# get_budgets([{ "name": "John", "age": 21, "budget": 23000 }, { "name": "Steve",  "age": 32, "budget": 40000 }, 
# { "name": "Martin",  "age": 16, "budget": 2700 }]) ➞ 65700

def get_budgets(lst_budgets):
    return sum(key.get('budget') for key in lst_budgets)    

print(get_budgets([{ "name": "John",  "age": 21, "budget": 29000 }, { "name": "Steve",  "age": 32, "budget": 32000 }, { "name": "Martin",  "age": 16, "budget": 1600 }]) )
