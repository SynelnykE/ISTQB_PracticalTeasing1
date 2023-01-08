# Given a list of numbers, create a function show_the_love() that removes 25% from every number in the 
# list except the smallest number, and adds the total amount removed to the smallest number.
# Notes
# There will only be one smallest number in a given list.
# Examples

# show_the_love([4, 1, 4]) ➞ [3, 3, 3]
# show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
# show_the_love([2, 100]) ➞ [27, 75]


def show_the_love(share_list):
    a = min(share_list)
    index = share_list.index(min(share_list))
    new_list = []
    b = 0
    for  i in share_list:
        if i > a:
            b += i * 0.25
            new_list.insert(i, i * 0.75 )
            continue
        elif i == a:
            # b += i 
            new_list.insert(index, i + b)
            continue
        
    return new_list

print(show_the_love([100, 50, 100]))