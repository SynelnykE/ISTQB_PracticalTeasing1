

a = 
k = 0
lst = []

for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    lst.append(a)
    print("Число простое")
else:
    print("Число не является простым")
    


        

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
