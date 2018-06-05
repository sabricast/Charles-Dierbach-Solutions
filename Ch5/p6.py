# Write a Python function named getContinue that displays to the user “Do you want to continue (y/n): ”,
# and continues to prompt the user until either uppercase or lowercase 'y' or 'n' is entered,
# returning (lowercase) 'y' or 'n' as the function value.

def getContinue():
    terminate = False

    while not terminate:
        entry = input('Do you want to continue (y/n)? ')
        if entry == 'Y' or entry == 'y':
            terminate = True
            return 'y'
        elif entry == 'N' or entry == 'n':
            terminate = True
            return 'n'


hello = getContinue()
print(hello)
