#Given an unsorted list, create a function nth_smallest() that returns the 
#nth smallest integer (the smallest integer is the first smallest, 
#the second smallest integer is the second smallest, etc).

def nth_smallest(list_numbers, ind_num):
    list_numbers.sort()
    if ind_num > len(list_numbers):
        return None
    else:
        return(list_numbers[ind_num - 1])
        
print(nth_smallest([5, 3, 2, 1, 10], 1))
# assert nth_smallest([5, 3, 2, 1, 10], 2) == 2
# assert nth_smallest([5, 3, 2, 1, 10], 1) == 1