# Create a Person class which will have three properties:
# Name
# List of foods they like
# List of foods they hate
# In this class, create the method taste():
# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person's like list, add 'and loves it!' to the end.
# If it is in the person's hate list, add 'and hates it!' to the end.
# If it is in neither list, simply add an exclamation mark to the end.
# Notes
# A person can have an empty list for foods they hate and/or love.
# Examples
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
# p1.taste("cheese") ➞ "Sam eats the cheese!"
# p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

class Person(object):

    def __init__(self, person_name, love_food_name, hate_food_name):
        self.person_name = person_name
        self.love_food_name = love_food_name
        self.hate_food_name = hate_food_name

    def taste(self, food_name):
        if food_name in self.love_food_name:
            return print(self.person_name + ' eats the ' + food_name + ' and loves it!')
        if food_name in self.hate_food_name:
            print(self.person_name + ' eats the ' + food_name + ' and hates it!')
        else:
            return print(self.person_name + ' eats the ' + food_name + '!')

p1 = Person("Sam", ["ice cream", "pie", "apples"], ["carrots", "bananas", "cheese", "lettuce"])
p1.taste("ice cream")
p2 = Person("Mitchell", [], ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"])
p2.taste("ice cream")
p3 = Person("Julie", ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"], [])
p3.taste("ice cream")
