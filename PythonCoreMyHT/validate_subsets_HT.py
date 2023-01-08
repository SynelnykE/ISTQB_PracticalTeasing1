# Write a function validate_subsets() that returns True if all subsets in a list belong to a given set.
# Notes. The empty set and the set itself are both valid subsets of a set 
# (we are not talking about proper subsets here). The set and the subset will each have unique elements.
# Examples
# validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True
# validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True
# validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False
# validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False

def validate_subsets(subsets, one_set):
    return set(sum(subsets, [])).issubset(set(one_set))

print(validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]))