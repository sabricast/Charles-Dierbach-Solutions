# Implement a set of functions called getData, extractValues, and calcRatios. Function getData
# should prompt the user to enter pairs of integers, two per line, with each pair read as a
# single string. These strings should be passed one at a time as they are being read to function
# extractValue, which is designed to return the string as a tuple of two integer values.
# Finally, each of these tuples is passed to function calcRatios one at a time to calculate and
# return the ratio of the two values.
# Implement a complete program that displays a list of ratios for an entered series of integer
# value pairs. Make sure to include docstring specification for each of the functions.


def getData():
    """ Returns a list composed of integer pairs separated by a space. """

    lst = []
    terminate = False
    while not terminate:
        s = input('Enter integer pair (hit Enter to quit): ')
        if s != '':
            lst.append(s)
        else:
            terminate = True

    return lst


def extractValue(pair):
    """
    (str) -> (int, int)

    From pair returns a tuple of two integers.

    \>>> extractValue('121 432') -> (121, 432)

    """
    n1, n2 = pair.split(' ')
    return int(n1), int(n2)


def calcRatios(n1, n2):
    """
    (int, int) -> float

    Returns the ratio between n1 and n2.

    \>>> calcRatios(20, 10) -> 2.0

    """

    return n1/n2


# --- main


lst = getData()
print(lst)

for k in range(len(lst)):
    string = lst[k]
    n1, n2 = extractValue(string)
    ratio = calcRatios(n1, n2)
    print(ratio)
