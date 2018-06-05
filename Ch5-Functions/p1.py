# Write a Python function named zeroCheck that is given three integers,
# and returns true if any of the integers is 0, otherwise it returns false.

def zeroCheck(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return True
    else:
        return False

# Alternate version found online that I wish I had thought before:

def zeroCheck(n1, n2, n3):
    if n1 * n2 * n3 == 0:
        return True
    else:
        return False
