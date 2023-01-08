# Create a function **mineral_formation()** that determines whether 
# the input represents *"stalactites"* or *"stalagmites"*. 
# If it represents both, return *"both"*. Input will be a 2D list, 
# with 1 representing a piece of rock, and 0 representing air space.

# *Notes.*  
# In other words, if the first list has 1s, return _"stalactites"_. 
# If the last list has 1s, return _"stalagmites"_. If both have them, return _"both"_.

def mineral_formation(stones):
    a = stones[0]
    b = stones[-1]
    for i in a:
        if i == 1:
            for x in b:
                if x == 1:
                    return "both"
            else:
                return "stalactites" 
    else: 
        return "stalagmites" 

print(mineral_formation([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]))

# *Examples*
# ```plaintext
# mineral_formation([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]) ➞ "stalactites"
# mineral_formation([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]) ➞ "stalagmites"
# mineral_formation([[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]) ➞ "both"
