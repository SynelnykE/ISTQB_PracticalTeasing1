#Calculates square sum in a range

n = int(input("Enter value of range: "))

def squares_sum(n):   
    sum = 0
    for i in range(1, n+1):
      sum = sum + (i*i)
    return sum

print(squares_sum(n))
