# The effect of a water balloon popping can be modeled using a list. 
# Create a function **pops()** that takes a list which takes the pre-pop state and returns the state after the balloon is popped.
# The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.
# *Notes.*  
# - Length of input list is always odd.
# - The input list will always be the exact length it takes for there to be exactly one border zero.
# - If the input list consists only of zeroes, return the same list.

def pops(pop_list):
    new_pop = [0]
    for number in pop_list:
        if number != 0:
            i = 0
            while i < number:
                i += 1
                new_pop.append(i)
            while i > 0:
                i -= 1
                new_pop.append(i)
    return new_pop

print(pops([0, 0, 0, 3, 0, 0, 0]))
# *Examples*
# ```plaintext
# pops([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
# pops([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
# pops([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
# pops([0]) ➞ [0]