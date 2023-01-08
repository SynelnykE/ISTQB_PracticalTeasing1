# Create methods for the Calculator class that can do the following:
# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
# Notes The methods should return the result of the calculation.
# Don't worry about needing to handle division by zero errors.
# Examples
# calculator = Calculator()
# calculator.add(10, 5) ➞ 15
# calculator.subtract(10, 5) ➞ 5
# calculator.multiply(10, 5) ➞ 50
# calculator.(10, 5) ➞ 2

class Calculator(object):

    def __init__(self, number1=0, number2=1):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 // self.number2

calculator = Calculator(10, 5)
print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.divide())
