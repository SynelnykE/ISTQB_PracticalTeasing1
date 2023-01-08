#Calculates sum of square even nums in range

num = int(input("Enter value of num: "))
start = 1
stop = num+1

def sum_even_nums_in_range(start, stop):
    sum = 0
    for i in range(start, stop):
        sum += (i*i)
    return sum

print(sum_even_nums_in_range(start, stop))