# Same as p1 but using elif statements

terminate = False

while not terminate:
    letter = input('Choose your fruit! Enter A, B, or C (-1 to finish): ')
    if letter == 'A':
        print('Apple!')
    elif letter == 'B':
        print('Banana!')
    elif letter == 'C':
        print('Coconut!')
    elif letter == '-1':
        print('Thanks for playing!')
        terminate = True
    else:
        print('Invalid input! Please try again.')
