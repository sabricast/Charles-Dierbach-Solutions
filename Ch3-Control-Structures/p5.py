# User enters any number of integer values, program tells you how many negatives and how many positives

terminate = False
numpos = 0
numneg = 0

while not terminate:
    try:
        num = int(input('Please enter an integer number (enter any letter to finish): '))

        if num >= 0:
            numpos = numpos + 1
        elif num < 0:
            numneg = numneg + 1
    except ValueError:
        print('The number of positives you entered was %s, and the number of negatives was %s.' % (numpos, numneg))
        terminate = True
