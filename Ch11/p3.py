# Write both a non-recursive and recursive function that displays a provided string backwards.

# Non-recursive


def backwardString(s):
    """ (str) --> str

    Return s backwards.

    """
    backward = ''
    for k in range(len(s), 0, -1):
        backward += s[k - 1]
    return backward


# Recursive


def backwardString_r(s, backward=''):
    """ (str) --> str

    Return s backwards.

    """
    if len(s) == 0:
        return backward
    else:
        backward += s[len(s) - 1]
    return backwardString_r(s[:len(s) - 1], backward)


## Recursive answer from StackOverflow. Loved it. Helped me understand recursion a little bit more.


def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]

