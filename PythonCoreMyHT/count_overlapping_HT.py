# Create a function count_overlapping() that takes in a list of intervals and returns how many intervals overlap with a given point.
# An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary.
# For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).
# Notes.
# Each interval is represented as a list with a start point and an endpoint.
# Intervals count as intersecting even if they only intersect at one point, i.e. [2, 3] and [3, 4] both intersect at point 3.
# If it's helpful, you can draw these intervals on a line on a piece of paper.
# Examples
# count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0
# count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2
# count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2
# count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2)

def count_overlapping(list_intervals, point):
    k = 0
    for i in list_intervals:
        if i[0] <= point <= i[-1]:
            k += 1
            continue
    return k

print(count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2))