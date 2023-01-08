#Calculates sum of even nums in range

start = int(input("Enter start number of a range:  "))
stop = int(input("Enter finish number of a range: "))

def sum_even_nums_in_range(start, stop):  
    sum = 0
    while start <= stop:
        if (start % 2 == 0):
            sum += start
            start += 1
    return sum

print(sum_even_nums_in_range(start, stop))
