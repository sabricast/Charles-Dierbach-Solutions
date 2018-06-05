# Implement the Python function described in question P7 so that the altered
# list is returned as a function value, rather than by side effect.


def threshold(lst, n):
    new_lst = list(lst)
    for k in range(len(lst)):
        if lst[k] > n:
            new_lst[k] = 0
    return new_lst
