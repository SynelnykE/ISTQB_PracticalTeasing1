number = float(input("Enter number: ")) 
lower_bound = int(input("Enter lower_bound: "))
upper_bound = int(input("Enter upper_bound: "))

def int_within_bounds(number, lower_bound, upper_bound):
  if float(number)/int(number)==1.0 and (number > lower_bound) and (number < upper_bound):
    return True
  else:
    return False 
