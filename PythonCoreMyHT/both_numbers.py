number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))

def both(number1, number2):
    if (number1 > 0) and (number2 > 0):
        return True
    elif (number1 < 0) and (number2 < 0):
        return True
    elif (number1 == 0) and (number2 == 0):
        return True
    else:
        return False

print (both(number1, number2))
