# Write a Python function named printAsterisks that is passed
# a positive integer value n, and prints out a line of n
# asterisks. If n is greater than 75, then only 75 asterisks
# should be displayed.

def printAsterisks(n):
    if n >= 75:
        print(format('*','*<75'))
    elif n < 75 and n >= 0:
        for k in range(n):
            print('*', end='')
        print()  # just so all of the options end in \n. To keep it consistent
    elif n < 0:
        print('Only positive integers')

# simpler version after seeing examples online

def printAsterisks(n):
    if n >= 75:
        n = 75
    elif n < 0:
        print('Only positive integers')
    for k in range(n):
        print('*', end='')
        print()
