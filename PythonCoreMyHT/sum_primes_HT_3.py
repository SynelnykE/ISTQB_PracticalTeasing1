# Create a function sum_primes() that takes a list of numbers and returns the sum of all prime numbers in the list.
# Notes
# Given numbers won't exceed 101.
# A prime number is a number which has exactly two divisors.
# Examples
# sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
# sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
# sum_primes([]) ➞ None

def sum_primes(list_numbers):
    if not list_numbers:
        return None
    lst = []
    for n in list_numbers:    
        if n <= 1:
            continue
        k = 0
        for i in range(2, n // 2+1):
            if (n % i == 0):
                k = k+1
        if (k <= 0):
            lst.append(n)
            print("Prime: ", n)
    return sum(lst)

print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
