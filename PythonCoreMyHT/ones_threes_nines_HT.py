# Given an int, figure out how many ones, threes and nines you could fit into the number.
# You must create a class OnesThreesNines. You will make variables (self.ones, self.threes, self.nines) to do this.
# Examples
# n1 = OnesThreesNines(5)
# n1.nines ➞ 0
# n1.ones ➞ 5
# n1.threes ➞ 1

class OnesThreesNines:

    def __init__(self, number):
        self.number = number

    def nines(self):
        return self.number // 9

    def ones(self):
        return self.number // 1

    def threes(self):
        return self.number // 3

n1 = OnesThreesNines(5)
print(n1.nines())
print(n1.ones())   
print(n1.threes())
