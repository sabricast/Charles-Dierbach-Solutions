# Write both a non-recursive and recursive function that determines how many times a given letter occurs in
# a provided string.

# Non-recursive


def countLetter(s, letter):
    """ (string, letter) -> int

    Return how many times letter appears on string.

    """
    s = s.lower()
    return s.count(letter)

# Recursive


def countLetter_r(s, letter, number=0):
    """ (string, letter) -> int

    Return how many times letter appears on string.

    """
    s = s.lower()
    if len(s) == 0:
        return number
    elif s[0] == letter:
        number += 1
    return countLetter_r(s[1:], letter, number)


#Recursive, without using the extra keyword argument.


def rcountLetter(s, letter):
    s = s.lower()
    if s == '':
        return 0
    elif s[0] == letter:
        return rcountLetter(s[1:], letter) + 1
    elif s[0] != letter:
        return rcountLetter(s[1:], letter) + 0

