# A city skyline can be represented as a 2-D list with 1s representing buildings. 
# In the example below, the height of the tallest building is 4 (second-most right column).
# Create a function **tallest_skyscraper()** that takes a _skyline_ (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.

# *Examples*                   
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 3

# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 4

# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 2

def tallest_skyscraper(sky_list):
     total = 0
     skyscraper = [0]*4
     for i in sky_list:
          for j in i:
               if j == 1:
                    total += 1
                    skyscraper.insert(i, total)
                    continue
          
     # Your code
     return skyscraper

print(tallest_skyscraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))