#Calculates amount of fuel per distance

distance = float(input("Enter the distance of traveling: "))

def calculate_fuel(distance):   
  if distance == 0:
    return print("Invalid distance, can not be less than 1")
  elif distance*10 < 100:
    return 100
  elif distance > 0:
    return distance*10
  else:
    return distance
      
print("You need: ", calculate_fuel(distance), "fuel points!")  
