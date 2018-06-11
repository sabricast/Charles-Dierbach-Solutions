# Write both a non-recursive and recursive function that determines how many times a given letter occurs in
# a provided string.

# Non-recursive


def countLetter(s, letter):
    """ (string, letter) -> int

    Return how many times letter appears on string.

    """

    return s.count(letter)

# Recursive


def countLetter_r(s, letter, number=0):
    """ (string, letter) -> int

    Return how many times letter appears on string.

    """
    if len(s) == 0:
        return number
    elif s[0] == letter:
        number += 1
    return countLetter_r(s[1:], letter, number)

# --- main


print(countLetter('Hello', 'l'))
print(countLetter_r('Hello', 'l'))

print(countLetter('Sabrina', 'a'))
print(countLetter_r('Sabrina', 'a'))
