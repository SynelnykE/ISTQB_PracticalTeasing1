# Given a list and a set, define a function priority_sort() that return a sorted list
# with its items in ascending order but prioritize the elements in the set over the other items in the list.
# Notes
# If the list is empty, return an empty list.
# If the set is empty there is nothing to prioritize, but the list should still be sorted.
# The set may contain values that are not in the list.
# The list may contain duplicates.
# The list and the set will only contain integer values.
# Examples
# priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]
# priority_sort([], {}) == []
# priority_sort([1, 2, 3], {}) == [1, 2, 3]
# priority_sort([1, 5, 5, 5, 5, 2, 1], {1, 5}) == [1, 1, 5, 5, 5, 5, 2]
# priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) == [-4, -3, -5, -2, -1, 0] 

def priority_sort(unsort_lst, pri_set):
    if not unsort_lst:
        return unsort_lst
    if not pri_set:
        return sorted(unsort_lst)
    pr_lst = []
    for i in pri_set:
        for x in sorted(unsort_lst):
            if i == x:
                pr_lst.append(i)
    new_lst = []
    for i in pri_set:
        new_lst.append(i)
        continue
    for x in sorted(unsort_lst):
        if x != new_lst[0] and x != new_lst[1]:
            pr_lst.append(x)
            continue
    return pr_lst

print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))
