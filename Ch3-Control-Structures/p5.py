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

# Alternate version using lists

terminate2 = False
nums = []

while not terminate2:
    try:
        num = int(input('Please enter an integer number (enter any letter to finish): '))
        nums.append(num)

    except ValueError:
        posval = [x for x in nums if x >= 0]
        print('The number of positive values you entered is:', len(posval))

        negval = [x for x in nums if x < 0]
        print('The number of negative values you entered is:', len(negval))

        terminate2 = True
