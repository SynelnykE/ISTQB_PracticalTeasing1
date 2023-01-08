# Create a function color_invert() that inverts the rgb values of a given tuple.
# Notes.
# Must return a tuple.
# 255 is the max value of a single color channel.
# Examples
# color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.
# color_invert((0, 0, 0)) ➞ (255, 255, 255)
# color_invert((165, 170, 221)) ➞ (90, 85, 34)

def color_invert(rgb):
    lst_rgb = []
    for i in rgb:
        if i == 0:
            lst_rgb.append(255)
        else:
            lst_rgb.append(255 - i)
    t_rgb = tuple(lst_rgb)
    return t_rgb

print(color_invert((165, 170, 221)))