#Calculate area of triangl

base = float(input('Enter base triangl: '))
height = float(input('Enter base triangl: '))

def tri_area(base, height):     
    return base*height/2
  
print("area of triangl=", tri_area(base, height), "squaer units.")