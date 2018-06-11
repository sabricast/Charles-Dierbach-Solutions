# Write both a non-recursive and recursive function that determines if a given number is even or not.

# Non-recursive


def iseven(number):
    """ (int) -> bool

    Returns whether number is even.

    \>>> iseven(5) -> False
    \>>> iseven(4) -> True

    """
    return number % 2 == 0


# Recursive


def iseven_r(number):
    """ (int) -> bool

    Returns whether number is even.

    \>>> iseven(5) -> False
    \>>> iseven(4) -> True

    """
    if number == 2 or number == 0:
        return True
    elif number >= 2:
        number -= 2
    else:
        return False
    return iseven_r(number)


### Version found online, shorter than mine, I like it a lot.
 def isEven(number):
     if number < 2:
         return number % 2 == 0
     return isEven(number - 2)
