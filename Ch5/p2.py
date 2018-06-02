# Write a Python function named ordered3 that is passed three integers,
# and returns true if the three integers are in order from smallest to
# largest, otherwise it returns false.

def ordered3(n1, n2, n3):
    if n1 < n2 < n3:
        return True
    else:
        return False