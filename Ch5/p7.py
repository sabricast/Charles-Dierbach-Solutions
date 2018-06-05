# Implement a Python function that is passed a list of numeric values and
# a particular threshold value, and returns the list with all values above
# the given threshold value set to 0. The list should be altered as a side
# effect to the function call, and not by function return value.


def treshold(lst, n):
    for k in range(len(lst)):
        if lst[k] > n:
            lst[k] = 0